#!/usr/bin/env python3
# avif_wrap.py -- add AVIF to every raster <img>/<picture> on the site.
#  - bare <img>  -> wrapped in <picture> with an AVIF <source> + original fallback
#  - existing <picture> with a webp source -> an AVIF <source> prepended
# Idempotent: skips when an AVIF source already exists or no .avif is on disk.
import os, re, glob

REPO = os.path.dirname(os.path.abspath(__file__))

def avif_of(url):
    if not url or url.startswith(('http://', 'https://', '//', 'data:')):
        return None
    base, ext = os.path.splitext(url)
    if ext.lower() not in ('.webp', '.jpg', '.jpeg', '.png'):
        return None
    av = base + '.avif'
    if os.path.exists(av.lstrip('/')):
        return av
    return None

def avif_srcset(ss):
    parts = []
    for part in ss.split(','):
        part = part.strip()
        toks = part.split()
        if toks:
            a = avif_of(toks[0])
            if a:
                toks[0] = a
        parts.append(' '.join(toks))
    return ', '.join(parts)

IMG_RE = re.compile(r'<img\b([^>]*)>', re.S)
PICTURE_RE = re.compile(r'<picture\b.*?</picture>', re.S)
SRCSET_RE = re.compile(r'\ssrcset="([^"]+)"')
SRC_RE = re.compile(r'\ssrc="([^"]+)"')

def add_avif_to_picture(block):
    if 'image/avif' in block:
        return block
    ss_m = SRCSET_RE.search(block)
    if ss_m:
        av_ss = avif_srcset(ss_m.group(1))
        if not av_ss or av_ss == ss_m.group(1):
            return block
        new_src = f'<source type="image/avif" srcset="{av_ss}">'
        return block.replace('<picture>', '<picture>' + new_src, 1)
    img_m = IMG_RE.search(block)
    if img_m:
        s_m = SRC_RE.search(img_m.group(1))
        if s_m:
            av = avif_of(s_m.group(1))
            if av:
                new_src = f'<source type="image/avif" srcset="{av}">'
                return block.replace('<picture>', '<picture>' + new_src, 1)
    return block

def wrap_img(m):
    attrs = m.group(1)
    s_m = SRC_RE.search(attrs)
    if not s_m:
        return m.group(0)
    av = avif_of(s_m.group(1))
    if not av:
        return m.group(0)
    ss_m = SRCSET_RE.search(attrs)
    av_ss = avif_srcset(ss_m.group(1)) if ss_m else av
    source = f'<source type="image/avif" srcset="{av_ss}">'
    return f'<picture>{source}<img{attrs}></picture>'

def process_file(path):
    html = open(path, encoding='utf-8').read()
    # 1) augment existing <picture> blocks (add AVIF source) and stash them
    stash = {}
    def stash_pic(m):
        key = f'\x00PIC{len(stash)}\x00'
        stash[key] = add_avif_to_picture(m.group(0))
        return key
    html, _ = PICTURE_RE.subn(stash_pic, html)
    # 2) wrap bare <img> (those inside stashed pictures are gone now)
    html, _ = IMG_RE.subn(wrap_img, html)
    # 3) restore augmented pictures
    for k, v in stash.items():
        html = html.replace(k, v)
    open(path, 'w', encoding='utf-8').write(html)

def main():
    if not glob.glob(os.path.join(REPO, 'images', '*.avif')):
        print('No .avif files found in images/. Run make_avif.cjs first.')
        return
    count = 0
    for f in glob.glob(os.path.join(REPO, '**', '*.html'), recursive=True):
        if '/.git/' in f or os.path.sep + 'src' + os.path.sep in f:
            continue
        before = open(f, encoding='utf-8').read()
        if '<img' not in before:
            continue
        process_file(f)
        after = open(f, encoding='utf-8').read()
        if after != before:
            count += 1
            print('updated:', os.path.relpath(f, REPO))
    print(f'Done. {count} HTML files updated with AVIF sources.')

if __name__ == '__main__':
    main()
