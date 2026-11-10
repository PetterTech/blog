#!/usr/bin/env bash
# Headless browser checks: theme toggle (same localStorage key as pettertech.com), CSP, images, fonts, highlighting.
#   hugo --minify && bash tools/test/run-browser-tests.sh
# Serves public/ as /blog/ (plus theme-test.html at the root) on 127.0.0.1:$PORT and loads the test page in
# headless Chrome with a dark colour-scheme preference. Set CHROME to your Chrome/Chromium binary if needed.
set -euo pipefail
cd "$(dirname "$0")/../.."
PORT="${PORT:-8765}"
if [ -z "${CHROME:-}" ]; then
  for c in "$HOME"/.cache/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell; do
    if [ -x "$c" ]; then CHROME="$c"; fi   # newest Playwright headless shell, if any
  done
  CHROME="${CHROME:-$(command -v chromium || command -v google-chrome || echo chromium)}"
fi
[ -f public/index.html ] || { echo "Build the site first: hugo --minify"; exit 1; }

SERVE=tools/test/.serve   # gitignored server root: blog -> public/, theme-test.html
mkdir -p "$SERVE"
ln -sfn ../../../public "$SERVE/blog"
ln -sfn ../theme-test.html "$SERVE/theme-test.html"
python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$SERVE" >/dev/null 2>&1 &
SERVER=$!
trap 'kill "$SERVER"' EXIT
sleep 1

if ! "$CHROME" --headless --no-sandbox --disable-gpu --force-dark-mode --blink-settings=preferredColorScheme=0 \
  --enable-logging=stderr --v=0 --virtual-time-budget=30000 \
  --dump-dom "http://127.0.0.1:$PORT/theme-test.html" >"$SERVE/dom.html" 2>"$SERVE/chrome.log"; then
  echo "RESULT FAIL  Chrome did not complete successfully"
  cat "$SERVE/chrome.log" >&2
  exit 1
fi
sed 's/<pre id="out">//' "$SERVE/dom.html" | grep -E '^RESULT (PASS|FAIL)|^DONE$' >"$SERVE/results.log" || true
cat "$SERVE/results.log"
status=0
if ! grep -qx 'DONE' "$SERVE/results.log"; then
  echo "RESULT FAIL  browser tests did not finish"
  status=1
fi
if grep -q '^RESULT FAIL' "$SERVE/results.log"; then status=1; fi

# CSP violations show up as console messages in Chrome's log
if grep -q 'Content Security Policy' "$SERVE/chrome.log"; then
  echo "RESULT FAIL  CSP violation(s):"
  grep -m 5 'Content Security Policy' "$SERVE/chrome.log"
  status=1
else
  echo "RESULT PASS  no CSP violations in the browser log"
fi
exit "$status"
