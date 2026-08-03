import re, os
pages = ['about/index.html','certs/index.html','products/adapters/index.html',
         'products/indoor/index.html','products/ip67/index.html','products/ip65/index.html']
out=[]
for p in pages:
    t=open(p,encoding='utf-8').read()
    words=len(re.findall(r'\S+', re.sub(r'<[^>]+>',' ', t)))
    expanded = any(k in t for k in ['Manufacturing','Where adapters','Where indoor','Where IP67','Where IP65','Why buy factory'])
    avif = t.count('image/avif')
    can = re.search(r'rel="canonical" href="([^"]*)"', t)
    out.append(f'{p}: words={words} expanded={expanded} avif={avif} canon={can.group(1) if can else "NONE"}')
open('C:/Users/Admin/WorkBuddy/2026-07-07-14-01-01/verify2.txt','w',encoding='ascii',errors='replace').write('\n'.join(out))
