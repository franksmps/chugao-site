import re, os
out=[]
# sitemap
sm=open('sitemap.xml',encoding='utf-8').read()
out.append('sitemap locs='+str(sm.count('<loc>')))
# language home canonical sample
for l in ['en','zh','es','fr']:
    f = 'index.html' if l=='en' else f'{l}/index.html'
    t=open(f,encoding='utf-8').read()
    can=re.search(r'rel="canonical" href="([^"]*)"',t)
    out.append(f'{l} canon={can.group(1) if can else "NONE"}')
# product pages expanded+avif
for p in ['products/adapters/index.html','products/ip67/index.html','certs/index.html','about/index.html']:
    t=open(p,encoding='utf-8').read()
    exp = ('Where' in t) or ('What we send' in t) or ('Manufacturing' in t)
    out.append(f'{p}: expanded={exp} avif={t.count("image/avif")}')
# all 11 lang dirs exist
langs=['zh','es','fr','de','pt','ru','ja','ko','ar','it']
miss=[l for l in langs if not os.path.exists(f'{l}/index.html')]
out.append('missing lang dirs='+str(miss))
open('C:/Users/Admin/WorkBuddy/2026-07-07-14-01-01/verify3.txt','w',encoding='ascii',errors='replace').write('\n'.join(out))
