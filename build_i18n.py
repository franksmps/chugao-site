#!/usr/bin/env python3
# build_i18n.py  -- CHUGAO multilingual static build
# Reads src/*.html, translates via main.js T dictionary, emits per-language
# subdirectory pages (/zh/, /es/ ...) with hreflang + absolute asset paths.
import os, re, json, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n_subpages import apply_translations

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO, 'src')
NODE = r"C:/Users/Admin/.workbuddy/binaries/node/versions/22.22.2/node.exe"
EXTRACT = os.path.join(REPO, 'extract_i18n.cjs')
MAIN_JS = os.path.join(REPO, 'main.js')
I18N_JSON = os.path.join(REPO, 'i18n.json')
DOMAIN = 'https://www.chugaopower.com'

BCP = {'en':'en','zh':'zh-CN','es':'es','fr':'fr','de':'de','pt':'pt','ru':'ru','ja':'ja','ko':'ko','ar':'ar','it':'it'}

# (code, ISO letters for flag, native name)
LANGS_META = [
  ('en','EN','English'),
  ('zh','CN','简体中文'),
  ('es','ES','Español'),
  ('fr','FR','Français'),
  ('de','DE','Deutsch'),
  ('pt','PT','Português'),
  ('ru','RU','Русский'),
  ('ja','JP','日本語'),
  ('ko','KR','한국어'),
  ('ar','SA','العربية'),
  ('it','IT','Italiano'),
]
LANGS = [c for c,_,_ in LANGS_META]

# Source pages that fan out to ALL languages (full localization available).
# Content is English-only until T keys are translated, but fanning out keeps the
# language switcher links valid (no 404) across the whole site.
LOCALIZED = {'index', 'about', 'certs', 'faq',
             'products/adapters', 'products/indoor', 'products/ip65', 'products/ip67'}

def flag(letters):
    base = 0x1F1E6
    return ''.join(chr(base + ord(c) - ord('A')) for c in letters)

# ---------- URL helpers ----------
def abs_url(u):
    if not u:
        return u
    if u.startswith(('http://','https://','//','/','#','?','mailto:','tel:','data:','javascript:')):
        return u
    if u.startswith('./'):
        u = u[2:]
    if u.startswith('../'):
        u = u[3:]
    return '/' + u.lstrip('/')

def abs_srcset(v):
    out = []
    for part in v.split(','):
        part = part.strip()
        toks = part.split()
        if toks:
            toks[0] = abs_url(toks[0])
        out.append(' '.join(toks))
    return ', '.join(out)

# ---------- transforms ----------
def translate(html, T, lang):
    t = T.get(lang, T['en'])
    def repl(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        km = re.search(r'data-i18n="([^"]+)"', attrs)
        if not km:
            return m.group(0)
        key = km.group(1)
        val = t.get(key)
        if val is None:
            val = T['en'].get(key, inner)
        return f'<{tag}{attrs}>{val}</{tag}>'
    return re.sub(r'<([a-zA-Z0-9]+)([^>]*?data-i18n="[^"]*"[^>]*)>(.*?)</\1>', repl, html, flags=re.S)

RTL_LANGS = {"ar", "fa", "he", "ur", "yi", "dv"}

def set_html_lang(html, bcp):
    lang_code = bcp.split("-")[0].lower()
    dir_attr = ' dir="rtl"' if lang_code in RTL_LANGS else ""
    return re.sub(r'<html[^>]*>', f'<html lang="{bcp}"{dir_attr}>', html, count=1)

def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')

def set_title_desc(html, META, lang):
    meta = META.get(lang, META.get('en', {}))
    if meta.get('title'):
        title = meta['title']
        html = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', html, count=1)
        html = re.sub(r'<meta property="og:title" content="[^"]*"',
                      f'<meta property="og:title" content="{esc_attr(title)}"', html, count=1)
        html = re.sub(r'<meta name="twitter:title" content="[^"]*"',
                      f'<meta name="twitter:title" content="{esc_attr(title)}"', html, count=1)
    if meta.get('desc'):
        d = meta['desc']
        html = re.sub(r'<meta name="description" content="[^"]*"',
                      f'<meta name="description" content="{esc_attr(d)}"', html, count=1)
        html = re.sub(r'<meta property="og:description" content="[^"]*"',
                      f'<meta property="og:description" content="{esc_attr(d)}"', html, count=1)
        html = re.sub(r'<meta name="twitter:description" content="[^"]*"',
                      f'<meta name="twitter:description" content="{esc_attr(d)}"', html, count=1)
    return html

def set_jsonld_lang(html, bcp):
    return html.replace('"inLanguage":"en"', f'"inLanguage":"{bcp}"')

def strip_old_hreflang(html):
    html = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>\n?', '', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"\s*/?>\n?', '', html)
    return html

def inject_hreflang(html, page_url, langs):
    links = []
    for l in langs:
        href = DOMAIN + (page_url if l == 'en' else '/' + l + page_url)
        links.append(f'  <link rel="alternate" hreflang="{l}" href="{href}" />')
    links.append(f'  <link rel="alternate" hreflang="x-default" href="{DOMAIN + page_url}" />')
    return re.sub(r'(</title>)', r'\1\n' + '\n'.join(links), html, count=1)

def inject_canonical(html, page_url, lang):
    url = page_url if lang == 'en' else '/' + lang + page_url
    canon = f'  <link rel="canonical" href="{DOMAIN + url}" />'
    return re.sub(r'(</title>)', r'\1\n' + canon, html, count=1)

def inject_og_locale(html, bcp):
    loc = bcp.replace('-', '_')
    cur = bcp.split('-')[0] if '-' in bcp else bcp
    tags = [f'  <meta property="og:locale" content="{loc}" />']
    for l in LANGS:
        if l == cur:
            continue
        tags.append(f'  <meta property="og:locale:alternate" content="{BCP[l].replace("-", "_")}" />')
    return re.sub(r'(</title>)', r'\1\n' + '\n'.join(tags), html, count=1)

def rewrite_urls(html):
    def fix(m):
        attr, q, val = m.group(1), m.group(2), m.group(3)
        return f'{attr}{q}{abs_url(val)}{q}'
    html = re.sub(r'(\b(?:src|href|poster|data-src)=)("|\')([^"\']*)\2', fix, html)
    def fixss(m):
        attr, q, val = m.group(1), m.group(2), m.group(3)
        return f'{attr}{q}{abs_srcset(val)}{q}'
    html = re.sub(r'(\bsrcset=)("|\')([^"\']*)\2', fixss, html)
    return html

def inject_switcher(html, lang, page_url='/'):
    # Anchor fallback: each language item carries a real href so navigation works
    # even if main.min.js fails to execute. goLang() still enhances (preserves hash).
    def href_for(l):
        return page_url if l == 'en' else '/' + l + page_url
    dd = ''.join(
        f'<a class="lang-item{" active" if l==lang else ""}" id="lang-{l}" '
        f'href="{href_for(l)}" onclick="goLang(\'{l}\')">'
        f'<span class="lang-flag">{flag(letters)}</span>'
        f'<span class="lang-name">{native}</span></a>'
        for (l, letters, native) in LANGS_META)
    mob = ''.join(
        f'<a href="{href_for(l)}" onclick="goLang(\'{l}\');closeMobileMenu()" id="ml-{l}"'
        f'{" class=\"active\"" if l==lang else ""}>{l.upper()}</a>'
        for (l, letters, native) in LANGS_META)
    html = html.replace('<!--LANG_DROPDOWN-->', dd)
    html = html.replace('<!--LANG_MOBILE-->', mob)
    html = re.sub(r'<span id="current-lang">[^<]*</span>',
                  f'<span id="current-lang">{lang.upper()}</span>', html)
    return html

def out_path(page_base, lang):
    if page_base == '/':
        return 'index.html' if lang == 'en' else f'{lang}/index.html'
    base = page_base[1:]
    if lang == 'en':
        return os.path.join(base, 'index.html')
    return os.path.join(lang, base, 'index.html')

def build_page(rel_html, T, META):
    name = rel_html[:-5]                 # strip .html
    url = '/' if name == 'index' else '/' + name
    page_url = url if url.endswith('/') else url + '/'
    src_path = os.path.join(SRC, rel_html)
    with open(src_path, encoding='utf-8') as f:
        raw = f.read()
    name = rel_html[:-5]
    fan_out = name in LOCALIZED
    target_langs = LANGS if fan_out else ['en']
    alts = {}
    for lang in target_langs:
        html = translate(raw, T, lang)
        html = apply_translations(html, lang)
        html = set_html_lang(html, BCP[lang])
        if name == 'index':
            html = set_title_desc(html, META, lang)
        html = set_jsonld_lang(html, BCP[lang])
        html = strip_old_hreflang(html)
        html = inject_hreflang(html, page_url, target_langs)
        html = inject_canonical(html, page_url, lang)
        html = inject_og_locale(html, BCP[lang])
        html = rewrite_urls(html)
        html = inject_switcher(html, lang, page_url)
        out_rel = out_path(url, lang)
        out_abs = os.path.join(REPO, out_rel)
        os.makedirs(os.path.dirname(out_abs), exist_ok=True)
        with open(out_abs, 'w', encoding='utf-8') as f:
            f.write(html)
        alts[lang] = DOMAIN + (page_url if lang == 'en' else '/' + lang + page_url)
    return {'canonical': DOMAIN + page_url, 'alts': alts, 'page': page_url, 'fan_out': fan_out}

def build_sitemap(entries):
    out = []
    out.append('<?xml version="1.0" encoding="UTF-8"?>')
    out.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    for e in entries:
        if e['fan_out']:
            # Emit one <url> per language, each carrying the full hreflang set.
            for l in LANGS:
                if l not in e['alts']:
                    continue
                out.append('  <url>')
                out.append(f'    <loc>{e["alts"][l]}</loc>')
                for la in LANGS:
                    if la in e['alts']:
                        out.append(f'    <xhtml:link rel="alternate" hreflang="{la}" href="{e["alts"][la]}" />')
                out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{e["alts"]["en"]}" />')
                out.append('  </url>')
        else:
            out.append('  <url>')
            out.append(f'    <loc>{e["canonical"]}</loc>')
            out.append('  </url>')
    # static blog pages (English only)
    for b in ['blog-1','blog-2','blog-3','blog-4','blog-5','blog']:
        out.append('  <url>')
        out.append(f'    <loc>{DOMAIN}/{b}.html</loc>')
        out.append('  </url>')
    out.append('</urlset>')
    with open(os.path.join(REPO, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')

def main():
    if not os.path.exists(I18N_JSON):
        r = subprocess.run([NODE, EXTRACT, MAIN_JS, I18N_JSON], capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr); sys.exit(1)
    with open(I18N_JSON, encoding='utf-8') as f:
        data = json.load(f)
    T, META = data['T'], data['META']

    entries = []
    for root, _, files in os.walk(SRC):
        for fn in sorted(files):
            if not fn.endswith('.html'):
                continue
            rel = os.path.relpath(os.path.join(root, fn), SRC).replace('\\', '/')
            print('building', rel)
            entries.append(build_page(rel, T, META))
    build_sitemap(entries)
    print(f'Done. {len(entries)} page templates -> {sum(len(e["alts"]) for e in entries)} URLs in sitemap.xml')

if __name__ == '__main__':
    main()
