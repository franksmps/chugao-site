# CHUGAO Power - GitHub Pages site

CHUGAO is a Zhongshan-based LED switching power supply factory. This is the static B2B website.

## Stack

- Plain HTML + CSS + JS
- 11 languages via in-page data-i18n + `main.js` T object
- No build step

## Files

- `index.html` — single page with anchor links
- `style.css` — all styles
- `main.js` — language switcher, form handler, FAQ accordion, fade-up animation
- `images/` — product photos and factory shots
- `logo.png`, `whatsapp.png` — assets

## Local dev

```bash
node -e "var http=require('http'),fs=require('fs'),path=require('path');http.createServer((q,r)=>{var p=path.join(__dirname,q.url==='/'?'/index.html':q.url);fs.readFile(p,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.end(d);});}).listen(9000)"
# open http://localhost:9000
```

## Add a language

1. In `main.js` KEYS array, add the 2-letter code.
2. Add `T.<code> = { ... }` block with all keys.
3. Add a flag/option in `index.html` header `lang-dropdown`.
4. Add a mobile option in `index.html` mobile menu.
5. Add to `SUPPORTED` array in `main.js`.

## Deployment

Pushes to `main` are served at <https://franksmps.github.io/chugao-site/>.
For chugaopower.com, configure custom domain in repo Settings → Pages.
