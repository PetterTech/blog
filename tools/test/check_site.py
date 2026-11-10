#!/usr/bin/env python3
"""Static checks for the built site (stdlib only).

    hugo --minify && python3 tools/test/check_site.py public [--old OLD_PUBLIC]

- every internal href/src/srcset (pages, CSS, JS, fonts, images, favicon) and CSS url() resolves to a file
- CSP meta on every page; each inline <script> matches a 'sha256-…' in script-src; no inline style
  attributes, <style> elements or on* handlers (they would be blocked by the CSP)
- no third-party resources (img/script/stylesheet/font from another host)
- index.xml and sitemap.xml are well-formed XML; RSS links resolve
- report every remaining "cloud.kemta.net" in the output
- with --old: the set of post/About page paths is identical to the old build (URL parity)
Exit code 1 if anything is broken.
"""
import argparse, base64, hashlib, html, html.parser, pathlib, re, sys, urllib.parse
import xml.etree.ElementTree as ET

BASE = urllib.parse.urlsplit('https://pettertech.com/blog/')

ap = argparse.ArgumentParser()
ap.add_argument('public', type=pathlib.Path)
ap.add_argument('--old', type=pathlib.Path, help='old build to compare post/About URLs with')
args = ap.parse_args()
pub = args.public.resolve()
problems = []


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs, self.scripts, self.csp, self.inline_styles, self.handlers = [], [], None, 0, []
        self._in_script = False
        self._buf = []
        self.style_elems = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k, v in attrs:
            if k.startswith('on'):
                self.handlers.append(f'{tag}[{k}]')
        if 'style' in a:
            self.inline_styles += 1
        if tag == 'meta' and (a.get('http-equiv') or '').lower() == 'content-security-policy':
            self.csp = a.get('content', '')
        if tag == 'style':
            self.style_elems += 1
        for k in ('href', 'src'):
            if a.get(k):
                self.refs.append((tag, k, a[k], a.get('rel', '')))
        if a.get('srcset'):
            for cand in (a.get('srcset') or '').split(','):
                if cand.strip():
                    self.refs.append((tag, 'srcset', cand.split()[0], ''))
        if tag == 'script' and not a.get('src'):
            self._in_script, self._buf = True, []

    def handle_endtag(self, tag):
        if tag == 'script' and self._in_script:
            self.scripts.append(''.join(self._buf))
            self._in_script = False

    def handle_data(self, data):
        if self._in_script:
            self._buf.append(data)


def target(url, page_url):
    """Return the local file for an internal URL, None for external/ignored ones."""
    if url.startswith(('mailto:', 'data:', 'javascript:', '#')):
        return None
    u = urllib.parse.urlsplit(urllib.parse.urljoin(page_url, url))
    if u.scheme not in ('http', 'https') or u.netloc != BASE.netloc:
        return None
    path = urllib.parse.unquote(u.path)
    if not path.startswith(BASE.path):
        return ('outside', path)
    rel = path[len(BASE.path):]
    f = pub / rel
    if path.endswith('/'):
        f = f / 'index.html'
    elif not f.exists() and (pub / rel / 'index.html').exists():
        f = pub / rel / 'index.html'
    return f


def page_url_for(f):
    rel = f.relative_to(pub).as_posix()
    return urllib.parse.urlunsplit((BASE.scheme, BASE.netloc, BASE.path + rel, '', ''))


html_files = sorted(pub.rglob('*.html'))
checked = external_links = 0
external_res = set()
for f in html_files:
    p = Page()
    p.feed(f.read_text('utf-8'))
    url = page_url_for(f)
    name = f.relative_to(pub).as_posix()
    if p.csp is None:
        problems.append(f'{name}: no CSP meta')
    else:
        allowed = set(re.findall(r"'(sha256-[A-Za-z0-9+/=]+)'", p.csp))
        for s in p.scripts:
            h = 'sha256-' + base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()
            if h not in allowed:
                problems.append(f'{name}: inline script hash {h} not in CSP')
    if p.inline_styles or p.style_elems:
        problems.append(f'{name}: {p.inline_styles} style attributes, {p.style_elems} <style> elements')
    if p.handlers:
        problems.append(f'{name}: inline event handlers {p.handlers}')
    for tag, attr, ref, rel in p.refs:
        t = target(ref, url)
        is_resource = attr in ('src', 'srcset') or (tag == 'link' and rel not in ('canonical', 'alternate'))
        if t is None:
            host = urllib.parse.urlsplit(urllib.parse.urljoin(url, ref)).netloc
            if host and host != BASE.netloc:
                if is_resource:
                    external_res.add(f'{name}: <{tag} {attr}={ref}>')
                else:
                    external_links += 1
            continue
        checked += 1
        if isinstance(t, tuple):
            # same host, outside /blog/: only the splash page itself is expected
            if t[1] != '/':
                problems.append(f'{name}: {attr}={ref} points outside {BASE.path}')
            continue
        if not t.exists():
            problems.append(f'{name}: broken {tag}[{attr}] -> {ref}')

for css in sorted(pub.rglob('*.css')):
    css_url = page_url_for(css)
    for ref in re.findall(r'url\(\s*[\'"]?([^\'")]+)', css.read_text('utf-8')):
        t = target(ref, css_url)
        checked += 1
        if t is None or isinstance(t, tuple) or not t.exists():
            problems.append(f'{css.relative_to(pub)}: broken url({ref})')

for xml_name in ('index.xml', 'sitemap.xml'):
    x = pub / xml_name
    if not x.exists():
        problems.append(f'{xml_name} missing')
        continue
    try:
        tree = ET.parse(x)
    except ET.ParseError as e:
        problems.append(f'{xml_name}: not well-formed: {e}')
        continue
    locs = [e.text for e in tree.iter() if e.tag.split('}')[-1] in ('link', 'loc') and e.text]
    for loc in locs:
        t = target(loc, BASE.geturl())
        checked += 1
        if t is None or isinstance(t, tuple) or not t.exists():
            problems.append(f'{xml_name}: {loc} does not resolve')
    if xml_name == 'index.xml':
        print(f'RSS: {len(tree.findall("./channel/item"))} items')

kemta = []
for f in sorted(pub.rglob('*')):
    if f.suffix in ('.html', '.xml', '.css', '.js', '.txt') and f.is_file():
        text = f.read_text('utf-8', errors='replace')
        if f.suffix in ('.html', '.xml'):   # text as shown (highlighted code is split into <span>s; RSS is escaped)
            for _ in range(2):
                text = html.unescape(re.sub(r'<[^>]+>', '', text))
        for line in text.splitlines():
            for m in re.finditer(r'.{0,60}cloud\.kemta\.net.{0,40}', line):
                kemta.append(f'{f.relative_to(pub)}: …{m.group(0)}…')

posts = sorted(p.parent.relative_to(pub).as_posix() for p in pub.glob('index.php/**/index.html'))
print(f'HTML files: {len(html_files)}, post pages: {len(posts)}, internal refs checked: {checked}, '
      f'external links (not followed): {external_links}')
print(f'third-party resources: {len(external_res)}')
for r in sorted(external_res):
    print('  ', r)
    problems.append(f'third-party resource {r}')
print(f'cloud.kemta.net mentions: {len(kemta)}')
for k in kemta:
    print('  ', k)

if args.old:
    old = args.old.resolve()
    def page_set(root):
        s = {p.parent.relative_to(root).as_posix() + '/' for p in root.glob('index.php/**/index.html')}
        s |= {p.parent.relative_to(root).as_posix() + '/' for p in root.glob('about-2/index.html')}
        return s
    a, b = page_set(old), page_set(pub)
    print(f'URL parity: old {len(a)} post/About pages, new {len(b)}; missing in new: {len(a - b)}, extra in new: {len(b - a)}')
    for x in sorted(a - b):
        problems.append(f'URL missing in new build: /blog/{x}')
    for x in sorted(b - a):
        print(f'   extra: /blog/{x}')

print(f'PROBLEMS: {len(problems)}')
for pr in problems:
    print('  ', pr)
sys.exit(1 if problems else 0)
