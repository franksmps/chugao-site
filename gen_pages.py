#!/usr/bin/env python3
# gen_pages.py -- generate the 7 P2-A static pages under src/ from templates.
# These are English-only this round; the build pipeline will localize them once
# their T keys are translated (flip LOCALIZED in build_i18n.py).
import os, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
DOMAIN = 'https://chugaopower.com'

NAV = '''<header><div class="c"><div class="ni"><a href="/" class="logo"><img src="/logo.png" alt="CHUGAO Power Logo" width="169" height="44" fetchpriority="high"></a><nav><ul class="nl"><li><a href="/" data-i18n="n_h">Home</a></li><li><a href="/about/" data-i18n="n_a">About</a></li><li><a href="/products/adapters/" data-i18n="n_p">Products</a></li><li><a href="/#specs" data-i18n="n_s">Specs</a></li><li><a href="/#why" data-i18n="n_w">Why us</a></li><li><a href="/#blog" data-i18n="n_b">News</a></li><li><a href="/faq/" data-i18n="n_f">FAQ</a></li><li><a href="/#contact" data-i18n="n_c">Contact</a></li></ul></nav><div style="display:flex;align-items:center"><div class="lang-selector"><button class="lang-btn" onclick="toggleLangDropdown()" aria-haspopup="true" aria-expanded="false" aria-controls="lang-dropdown"><span id="current-lang">EN</span><svg width="10" height="10" viewBox="0 0 10 10" fill="currentColor"><path d="M1 3l4 4 4-4H1z"/></svg></button><div class="lang-dropdown" id="lang-dropdown"><!--LANG_DROPDOWN--></div></div><button class="mt" id="mobileToggle" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button></div></div></div></header>
<div class="mm" id="mobileMenu"><a href="/" onclick="closeMobileMenu()" data-i18n="n_h">Home</a><a href="/about/" onclick="closeMobileMenu()" data-i18n="n_a">About</a><a href="/products/adapters/" onclick="closeMobileMenu()" data-i18n="n_p">Products</a><a href="/#specs" onclick="closeMobileMenu()" data-i18n="n_s">Specs</a><a href="/#why" onclick="closeMobileMenu()" data-i18n="n_w">Why us</a><a href="/#blog" onclick="closeMobileMenu()" data-i18n="n_b">News</a><a href="/faq/" onclick="closeMobileMenu()" data-i18n="n_f">FAQ</a><a href="/#contact" onclick="closeMobileMenu()" data-i18n="n_c">Contact</a><div class="ml"><!--LANG_MOBILE--></div></div>'''

FOOTER = '''<footer><div class="c"><div class="fg"><div class="fb"><a href="/" class="logo"><img src="/logo.png" alt="CHUGAO" class="logo-white" style="height:32px"></a><p data-i18n="f_desc">CHUGAO - LED power supply factory in Zhongshan, China. Factory direct.</p></div><div class="fc"><h4 data-i18n="f_prod">Products</h4><a href="/products/adapters/">Adapters</a><a href="/products/indoor/">Indoor drivers</a><a href="/products/ip67/">IP67 waterproof</a><a href="/products/ip65/">IP65 rainproof</a></div><div class="fc"><h4 data-i18n="f_comp">Company</h4><a href="/about/">About</a><a href="/certs/">Certifications</a><a href="/faq/">FAQ</a></div><div class="fc"><h4 data-i18n="f_supp">Support</h4><a href="/#contact">Contact</a><a href="mailto:info@chugaopower.com">Email</a><a href="https://wa.me/8618933373873" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></div><div class="fb2"><p>&copy; 2026 Zhongshan Chugao Electronic Technology Co., Ltd. All Rights Reserved.</p></div></div></footer>'''

def page(path, title, desc, body, json_ld=None, og_image='/images/factory.jpg.webp'):
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/logo.png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
{NAV}
<main>
{body}
</main>
{json_ld or ''}
{FOOTER}
<script src="/main.min.js" defer></script>
</body></html>'''
    out = os.path.join(SRC, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(head)
    print('wrote', path)

def breadcrumb(name, url):
    data = {"@context":"https://schema.org","@type":"BreadcrumbList","inLanguage":"en",
            "itemListElement":[
                {"@type":"ListItem","position":1,"name":"Home","item":DOMAIN+"/"},
                {"@type":"ListItem","position":2,"name":name,"item":DOMAIN+url}]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'

# ---------- About ----------
about_body = '''
<section class="sec sa"><div class="c">
<h1>About CHUGAO</h1>
<p>Zhongshan Chugao Electronic Technology Co., Ltd. makes LED switching power supplies in a 6,000 m&sup2; factory in Guzhen, Zhongshan, China. We run 38 people on the floor and 8 in sales, shipping to 42 countries across Europe, North America, the Middle East, and Southeast Asia.</p>
<h2>What we make</h2>
<p>Four product lines: AC/DC adapters (5-200W), indoor LED drivers (50-400W), IP67 waterproof drivers (10-400W), and IP65 rainproof drivers (100-600W). Every unit passes 48 hours of burn-in before it ships.</p>
<h2>Quality &amp; certification</h2>
<p>CE and RoHS on every model. UL is available per model. We send certificate PDFs before you order, and BIS certification for the India market is available on request. See our <a href="/certs/">certifications page</a>.</p>
<h2>OEM and ODM</h2>
<p>We build custom drivers for clients in Germany, Brazil, and Saudi Arabia. Minimum 500 pcs for custom tooling, free tooling on repeat orders over 2,000 pcs. Engineering support in English, Spanish, French, Russian, Arabic, and Chinese, with a 1-hour reply during China business hours (GMT+8).</p>
</div></section>'''
page('about.html', 'About CHUGAO - LED power supply factory, Zhongshan China',
     'CHUGAO is an LED switching power supply manufacturer in Zhongshan, China. 6,000 m2 factory, 4 product lines, CE/RoHS on every unit, OEM/ODM since 2008.',
     about_body, breadcrumb('About', '/about/'))

# ---------- FAQ ----------
faq_qa = [
 ("What is the minimum order quantity?", "50 pieces per model for stock items. 500 pieces for custom OEM. We do not accept 1-piece orders."),
 ("What certifications do you have?", "CE and RoHS on every model. UL is per model and costs extra. We send certificate PDFs before you order. BIS for India is available on request."),
 ("What is the warranty?", "3 years on stock items. OEM warranty is defined in the contract. Warranty does not cover lightning, water damage, or incorrect wiring."),
 ("Do you do OEM?", "Yes. Minimum 500 pcs. Send us your spec sheet. Tooling is charged on the first order and free on repeat orders over 2,000 pcs."),
 ("What are the payment terms?", "New customers: 30% T/T deposit, 70% before shipment. After 3 orders we can discuss L/C. We do not accept credit cards for bulk orders."),
 ("What is the lead time?", "Stock: 3-7 days. OEM: 25-30 days. Samples: 5 days, charged plus shipping, refunded on a bulk order."),
 ("Which input voltages do your drivers support?", "Adapters accept 100-240V AC universal. Indoor drivers are 190-264V AC; IP67 are 190-340V AC; IP65 are 190-264V AC. Confirm the range for your market."),
 ("How do I choose IP20, IP65, or IP67?", "IP20 for indoor dry locations. IP65 for semi-outdoor with rain and dust. IP67 for full outdoor and wet environments such as fountains and marine lighting."),
]
faq_items = ''.join(
    f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in faq_qa)
faq_data = {"@context":"https://schema.org","@type":"FAQPage","inLanguage":"en",
            "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qa]}
faq_json = '<script type="application/ld+json">' + json.dumps(faq_data, ensure_ascii=False) + '</script>'
faq_body = f'''
<section class="sec sa"><div class="c">
<h1>Frequently asked questions</h1>
<p class="ss">Plain answers about orders, certification, and product selection.</p>
<div class="faq-list">{faq_items}</div>
<p>Still have a question? <a href="/#contact">Contact our sales team</a> - we reply within 1 hour during China business hours.</p>
</div></section>'''
page('faq.html', 'FAQ - CHUGAO LED power supply questions answered',
     'Minimum order, certifications (CE/RoHS/UL/BIS), warranty, OEM, payment terms, lead time, and how to choose IP rating for LED drivers.',
     faq_body, faq_json + breadcrumb('FAQ', '/faq/'))

# ---------- Certifications ----------
certs_body = '''
<section class="sec sa"><div class="c">
<h1>Certifications &amp; compliance</h1>
<p>Every CHUGAO model ships with the documentation your market requires. Certificate PDFs are sent before you place an order.</p>
<h2>CE &amp; RoHS</h2>
<p>CE marking and RoHS compliance are standard on every unit. Test reports are available on request.</p>
<h2>UL</h2>
<p>UL certification is handled per model and takes 4-6 weeks from order confirmation. We start the application once you confirm the model and quantity.</p>
<h2>BIS (India)</h2>
<p>BIS certification for the India market is available on request for selected models. Tell us your target models and we confirm lead time and cost.</p>
<h2>Factory &amp; documents</h2>
<p>We provide commercial invoice, packing list, certificate of origin, and CE/RoHS reports with every shipment. Original documents ship with the goods.</p>
</div></section>'''
page('certs.html', 'Certifications - CE, RoHS, UL, BIS for CHUGAO LED drivers',
     'CHUGAO LED power supplies carry CE and RoHS on every model, UL per model, and BIS for India on request. Certificate PDFs provided before order.',
     certs_body, breadcrumb('Certifications', '/certs/'))

# ---------- Product category template ----------
def product_page(path, name, rng, ip, feat, desc, blurb, img):
    body = f'''
<section class="sec sa"><div class="c">
<h1>{name}</h1>
<p>{blurb}</p>
<div class="pc" style="max-width:760px;margin:0 auto">
<div class="pi"><img src="{img}" alt="{name}" loading="lazy" style="width:100%;border-radius:12px"></div>
<h2>Specifications</h2>
<ul>
<li><strong>Power range:</strong> {rng}</li>
<li><strong>Protection:</strong> {ip}</li>
<li><strong>Key features:</strong> {feat}</li>
</ul>
<p>{desc}</p>
<p><a href="/#inquiry" class="btn-p">Get a quote for {name}</a> &nbsp; <a href="/products/adapters/" data-i18n="n_p">View all products</a></p>
</div>
</div></section>'''
    return page(path, f'{name} - CHUGAO LED power supply', desc, body,
                breadcrumb(name, '/' + path.replace('src/','').replace('.html','/')), og_image=img)

product_page('products/adapters.html', 'LED Adapters (5-200W)',
    '5W - 200W', 'IP20 (indoor)', 'Wall-mount and desktop, AC 100-240V universal input, DC 12/24/36/48V output',
    'Compact AC/DC adapters for LED strips, modules, and signage. CE/UL available, 3-year warranty.',
    'AC/DC adapters for LED strips and modules, 5W-200W, 100-240V input.', '/images/product-adapter.webp')
product_page('products/indoor.html', 'Indoor LED Drivers (50-400W)',
    '50W - 400W', 'IP20', 'Built-in active PFC, fan-less silent operation',
    'Indoor LED drivers for ceiling lights and panel lights. High efficiency with active power-factor correction.',
    'Built-in PFC indoor LED drivers, 50W-400W, for ceiling and panel lights.', '/images/product-indoor.webp')
product_page('products/ip67.html', 'IP67 Waterproof LED Drivers (10-400W)',
    '10W - 400W', 'IP67 / IP68', 'Fully sealed silicone potting, salt-spray tested',
    'Waterproof drivers for outdoor LED strips, fountains, and marine lighting. Built to survive wet environments.',
    'Fully potted IP67/IP68 waterproof LED drivers, 10W-400W, for outdoor and wet use.', '/images/product-waterproof.webp')
product_page('products/ip65.html', 'IP65 Rainproof LED Drivers (100-600W)',
    '100W - 600W', 'IP65', 'Metal case with mesh vents, corrosion resistant',
    'Rainproof drivers for signage, billboards, and semi-outdoor installations. Metal housing with ventilation.',
    'Metal-case IP65 rainproof LED drivers, 100W-600W, for signage and semi-outdoor.', '/images/product-rainproof.webp')

print("All pages generated.")
