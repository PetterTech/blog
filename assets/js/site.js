// PetterTech · Ye Olde Blogge – theme toggle. Same behaviour and localStorage key ("theme") as the
// pettertech.com splash page, so the choice carries over between the two (same origin). No cookies.
(() => {
  const root = document.documentElement;
  const mq = matchMedia('(prefers-color-scheme: light)');
  const btn = document.getElementById('theme-toggle');
  const metaColor = document.querySelector('meta[name="theme-color"]');
  const systemTheme = () => (mq.matches ? 'light' : 'dark');
  const stored = () => {
    try { const t = localStorage.getItem('theme'); return t === 'light' || t === 'dark' ? t : null; } catch { return null; }
  };
  const store = (value) => {
    try { value ? localStorage.setItem('theme', value) : localStorage.removeItem('theme'); } catch { /* private mode */ }
  };
  function apply(theme) {
    root.dataset.theme = theme;
    if (metaColor) metaColor.content = theme === 'light' ? '#f2f2f2' : '#232323';
    if (btn) {
      const next = theme === 'dark' ? 'light' : 'dark';
      btn.setAttribute('aria-label', `Switch to ${next} mode`);
      btn.title = `Switch to ${next} mode`;
    }
  }
  apply(stored() || systemTheme());
  btn?.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    // Picking the same as the OS means "follow the OS again".
    store(next === systemTheme() ? null : next);
    apply(next);
  });
  mq.addEventListener('change', () => { if (!stored()) apply(systemTheme()); });
})();
