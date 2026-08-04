#!/usr/bin/env python3
# gen_pages.py -- generate the 7 P2-A static pages under src/ from templates.
# These are English-only this round; the build pipeline will localize them once
# their T keys are translated (flip LOCALIZED in build_i18n.py).
import os, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
DOMAIN = 'https://www.chugaopower.com'

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
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
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
<p class="ss" style="margin:0 auto 48px">Zhongshan Chugao Electronic Technology Co., Ltd. makes LED switching power supplies in a 6,000 m&sup2; factory in Guzhen, Zhongshan &mdash; the lighting manufacturing hub of China. We run 38 people on the floor and 8 in sales, shipping to 42 countries across Europe, North America, the Middle East, and Southeast Asia.</p>

<div class="wg" style="margin-bottom:60px">
<div class="wc"><div class="wi">6,000</div><h3>m&sup2; Factory</h3><p>Guzhen, Zhongshan &mdash; China's lighting capital, with the full supply chain next door.</p></div>
<div class="wc"><div class="wi">38+</div><h3>Floor staff</h3><p>Skilled SMT, wave-soldering, potting and QC operators on four dedicated lines.</p></div>
<div class="wc"><div class="wi">42</div><h3>Countries</h3><p>Distributors, brands and contractors across Europe, North America, the Middle East and SE Asia.</p></div>
<div class="wc"><div class="wi">2008</div><h3>Trading since</h3><p>Over 15 years building LED drivers and AC/DC adapters for global buyers.</p></div>
<div class="wc"><div class="wi">4</div><h3>Product lines</h3><p>Adapters, indoor drivers, IP67 and IP65 &mdash; one stop for low-voltage LED power.</p></div>
<div class="wc"><div class="wi">48h</div><h3>Burn-in</h3><p>Every unit runs a 48-hour full-load burn-in before it is packed and shipped.</p></div>
</div>

<div class="ag" style="margin-bottom:60px">
<div class="at">
<h2>What we make</h2>
<p>Four product lines cover most low-voltage LED jobs: AC/DC adapters (5-200W), indoor LED drivers (50-400W), IP67 waterproof drivers (10-400W), and IP65 rainproof drivers (100-600W). Together they run everything from a short strip behind a shelf to a weatherproof sign outside a shop.</p>
<p>Every unit passes 48 hours of burn-in before it ships, and carries CE and RoHS as standard. UL and BIS are available per model for the North American and Indian markets.</p>
</div>
<div class="aimg"><img src="/images/factory.jpg.webp" alt="CHUGAO LED power supply factory in Zhongshan, China" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>
</div>

<h2>Manufacturing &amp; quality control</h2>
<p>Production runs on four dedicated lines fed by SMT assembly and wave soldering, then finished on in-house potting and enclosure lines. Each driver moves through incoming component inspection and automated ICT, then a 48-hour full-load burn-in at elevated temperature before it is packed. On the line we check output voltage, ripple, efficiency, and the four protective functions &mdash; over-voltage, over-current, over-temperature, and short-circuit &mdash; so a weak unit is caught before it reaches you.</p>

<div class="proof-grid" style="margin:36px 0">
<div class="proof-card"><span>SMT</span><h3>Automated assembly</h3><p>Surface-mount and wave soldering with automated optical and in-circuit inspection.</p></div>
<div class="proof-card"><span>ICT</span><h3>In-circuit test</h3><p>Every board is tested for shorts, opens and component values before potting.</p></div>
<div class="proof-card"><span>48h</span><h3>Full-load burn-in</h3><p>Units run at full load in a hot chamber so early failures show up before shipping.</p></div>
<div class="proof-card"><span>4P</span><h3>Four protections</h3><p>Over-voltage, over-current, over-temperature and short-circuit protection on every model.</p></div>
</div>

<h2>Engineering &amp; customization</h2>
<p>Our engineering team supports OEM and ODM changes to output voltage, enclosure size, connector type, and cable length. Where a project calls for it, we can add dimming control (0-10V or PWM) or adjust the input range. Custom samples are built from your spec sheet and verified against the same test routine used in mass production, so what you approve is what ships.</p>

<h2>Global markets &amp; support</h2>
<p>We supply distributors, lighting brands, and project contractors in 42 countries, with the strongest presence in Europe, North America, the Middle East, and Southeast Asia. Sales and engineering reply in English, Spanish, French, Russian, Arabic, and Chinese, and aim to respond within 1 hour during China business hours (GMT+8).</p>

<h2>OEM and ODM</h2>
<p>We build custom drivers for clients in Germany, Brazil, and Saudi Arabia. The minimum is 500 pcs for custom tooling, and tooling is free on repeat orders over 2,000 pcs. Send us your spec sheet and we return a quote, a sample lead time, and the certification plan for your target market.</p>

<h2>Why buy factory direct</h2>
<p>Buying from the manufacturer removes the trader margin and shortens the path from a design change to shipment. You can also request the exact certificate package your market needs instead of a generic one. Every shipment includes a commercial invoice, packing list, certificate of origin, and CE/RoHS reports, with original documents shipped with the goods.</p>

<div class="proof-strip">
<div><strong>Need a quote or certificate plan?</strong><p>Tell us your market and model &mdash; we reply within 1 hour in China business hours.</p></div>
<a class="btn-p" href="/#inquiry">Contact sales</a>
</div>

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
<p>Every CHUGAO model ships with the documentation your market requires. Certificate PDFs are sent before you place an order, so you can clear customs and meet local electrical rules without surprises.</p>

<h2>CE &amp; RoHS (standard on every model)</h2>
<p>CE marking and RoHS compliance are standard on every unit. Our LED drivers are assessed against the EU directives that apply to lighting power supplies - the Low Voltage Directive and the EMC Directive - and RoHS confirms that restricted substances stay below the allowed limits. The test report and Declaration of Conformity are available on request.</p>

<h2>UL</h2>
<p>UL certification is handled per model and takes 4-6 weeks from order confirmation. We start the application once you confirm the model and quantity, and we keep you updated on the file status. UL is typically required for the North American market.</p>

<h2>BIS (India)</h2>
<p>BIS certification for the India market is available on request for selected models. Tell us your target models and we confirm lead time and cost. Plan this early, because BIS registration runs in parallel with production rather than after it.</p>

<h2>What we send with each shipment</h2>
<ul>
<li>Commercial invoice and packing list</li>
<li>Certificate of origin</li>
<li>CE and RoHS test reports / Declaration of Conformity</li>
<li>UL file reference where applicable</li>
</ul>
<p>Original documents ship with the goods; PDF copies are emailed before the container leaves the factory.</p>

<h2>Need a specific certificate?</h2>
<p>Standards and proof requirements differ by country. Tell us the destination market and the model you plan to import, and we will confirm which certificate applies and how long it takes. See the <a href="/faq/">FAQ</a> for lead times and minimum order quantities, or <a href="/#contact">contact sales</a> for a quote.</p>
</div></section>'''
page('certs.html', 'Certifications - CE, RoHS, UL, BIS for CHUGAO LED drivers',
     'CHUGAO LED power supplies carry CE and RoHS on every model, UL per model, and BIS for India on request. Certificate PDFs provided before order.',
     certs_body, breadcrumb('Certifications', '/certs/'))

# ---------- Product category template ----------
# Product index for cross-links shown on every product page
PRODUCTS = [
    ('products/adapters', 'LED Adapters (5-200W)', '/images/product-adapter.webp'),
    ('products/indoor', 'Indoor LED Drivers (50-400W)', '/images/product-indoor.webp'),
    ('products/ip67', 'IP67 Waterproof LED Drivers (10-400W)', '/images/product-waterproof.webp'),
    ('products/ip65', 'IP65 Rainproof LED Drivers (100-600W)', '/images/product-rainproof.webp'),
]

def product_page(path, name, rng, ip, feat, desc, blurb, img, inp='', outp='', related=None, extra=''):
    rel_block = ''
    if related:
        items = ''.join(f'<li><a href="/{b}.html">{t}</a></li>' for b, t in related)
        rel_block = f'''
<h2>Related reading</h2>
<ul class="rl">{items}</ul>'''
    other = ''.join(
        f'<a class="bc" href="/{p}/"><div class="bi">'
        f'<img src="{i}" alt="{n}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>'
        f'<div class="bn"><h3>{n}</h3><p>View specifications &rarr;</p></div></a>'
        for (p, n, i) in PRODUCTS if p != path)
    other_block = f'''
<h2>Other CHUGAO product lines</h2>
<div class="bg" style="margin-top:24px">{other}</div>'''
    body = f'''
<section class="sec sa"><div class="c">
<h1>{name}</h1>
<p class="ss" style="margin:0 auto 44px">{blurb}</p>

<div class="ag" style="margin-bottom:56px">
<div class="at">
<h2>Overview</h2>
<p>{desc}</p>
<div class="quote-card" style="padding:20px 24px;margin-top:18px">
<ul style="list-style:none;padding-left:0;margin:0">
<li><strong>Power range:</strong> {rng}</li>
<li><strong>Protection:</strong> {ip}</li>
<li><strong>Input:</strong> {inp}</li>
<li><strong>Output:</strong> {outp}</li>
</ul>
</div>
</div>
<div class="aimg"><img src="{img}" alt="{name}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>
</div>

<h2>Specifications</h2>
<table class="spec-table">
<tr><th>Parameter</th><th>Detail</th></tr>
<tr><td>Power range</td><td>{rng}</td></tr>
<tr><td>Ingress protection</td><td>{ip}</td></tr>
<tr><td>Input voltage</td><td>{inp}</td></tr>
<tr><td>Output voltage</td><td>{outp}</td></tr>
<tr><td>Key features</td><td>{feat}</td></tr>
</table>

<h2>Key features</h2>
<div class="wg" style="margin:24px 0">
<div class="wc"><div class="wi">&#9889;</div><h3>Wide input</h3><p>{inp} &mdash; one SKU covers most international sites.</p></div>
<div class="wc"><div class="wi">&#127754;</div><h3>Dual output</h3><p>{outp} options fit the common LED strips and modules.</p></div>
<div class="wc"><div class="wi">&#128274;</div><h3>Four protections</h3><p>Over-voltage, over-current, over-temperature and short-circuit.</p></div>
<div class="wc"><div class="wi">&#9989;</div><h3>Certified</h3><p>CE and RoHS standard; UL / BIS available per model.</p></div>
</div>
{extra}
{other_block}
<p style="margin-top:36px"><a href="/#inquiry" class="btn-p">Get a quote for {name}</a> &nbsp; <a href="/products/adapters/" data-i18n="n_p" style="color:var(--a);font-weight:600">View all products</a></p>{rel_block}
</div></section>'''
    return page(path, f'{name} - CHUGAO LED power supply', desc, body,
                breadcrumb(name, '/' + path + '/'), og_image=img)

product_page('products/adapters.html', 'LED Adapters (5-200W)',
    '5W - 200W', 'IP20 (indoor)', 'Wall-mount and desktop, AC 100-240V universal input, DC 12/24/36/48V output',
    'Compact AC/DC adapters for LED strips, modules, and signage. CE/UL available, 3-year warranty.',
    'AC/DC adapters for LED strips and modules, 5W-200W, 100-240V input.', '/images/product-adapter.webp',
    inp='AC 100-240V universal', outp='DC 12/24/36/48V',
    related=[('blog-1','Pick the Right LED Power Supply in 3 Steps'),
             ('blog-5','LED Driver Lifespan: MTBF, L70, and How Long They Really Last')],
    extra='''
<h2>Where adapters are used</h2>
<p>AC/DC adapters power 12V and 24V LED strips, LED modules, edge-lit signs, and small fixtures that plug into a wall outlet. The 100-240V universal input means one SKU ships worldwide - you only change the local plug or cord.</p>
<h2>How to size an adapter</h2>
<p>Add up the wattage of every LED you will run, then add a 20% margin so the adapter runs below its rated load. For example, 80W of strips needs at least a 100W adapter. Running below 80% load keeps the adapter cooler and extends its life.</p>
<h2>What is built in</h2>
<p>Each adapter has over-voltage, over-current, over-temperature, and short-circuit protection. Output options of 12V, 24V, 36V, and 48V cover most LED strips and modules.</p>
''')
product_page('products/indoor.html', 'Indoor LED Drivers (50-400W)',
    '50W - 400W', 'IP20', 'Built-in active PFC, fan-less silent operation',
    'Indoor LED drivers for ceiling lights and panel lights. High efficiency with active power-factor correction.',
    'Built-in PFC indoor LED drivers, 50W-400W, for ceiling and panel lights.', '/images/product-indoor.webp',
    inp='AC 190-264V', outp='DC 12/24V',
    related=[('blog-1','Pick the Right LED Power Supply in 3 Steps'),
             ('blog-5','LED Driver Lifespan: MTBF, L70, and How Long They Really Last')],
    extra='''
<h2>Where indoor drivers are used</h2>
<p>Indoor drivers feed ceiling lights, panel lights, troffers, and linear fixtures inside buildings. Built-in active PFC keeps the power factor high, which matters on commercial projects that put many fittings on one circuit.</p>
<h2>How to size an indoor driver</h2>
<p>Match the driver wattage to the total LED load plus a 20% margin, and confirm the output voltage (usually 12V or 24V DC) matches the fixture. For dimming projects, tell us the control type so we spec the right model.</p>
<h2>What is built in</h2>
<p>Active PFC, fan-less silent operation, and protection against over-voltage, over-current, over-temperature, and short-circuit. The IP20 enclosure is for dry indoor locations only.</p>
''')
product_page('products/ip67.html', 'IP67 Waterproof LED Drivers (10-400W)',
    '10W - 400W', 'IP67 / IP68', 'Fully sealed silicone potting, salt-spray tested',
    'Waterproof drivers for outdoor LED strips, fountains, and marine lighting. Built to survive wet environments.',
    'Fully potted IP67/IP68 waterproof LED drivers, 10W-400W, for outdoor and wet use.', '/images/product-waterproof.webp',
    inp='AC 90-305V', outp='DC 12/24V',
    related=[('blog-2','IP20 vs IP65 vs IP67 vs IP68')],
    extra='''
<h2>Where IP67 drivers are used</h2>
<p>IP67 and IP68 drivers go where water is. Use them for outdoor LED strips, garden and landscape lighting, fountains, pools, and marine or coastal installs. The fully sealed silicone potting blocks water and salt spray.</p>
<h2>How to size a waterproof driver</h2>
<p>Total the LED load, add a 20% margin, and pick a model rated above that sum. For hot environments or sealed enclosures, leave extra headroom so the driver runs cool. The 190-340V input covers most international sites.</p>
<h2>What is built in</h2>
<p>Sealed potting, salt-spray resistance, and over-voltage, over-current, over-temperature, and short-circuit protection. Rated for full outdoor and wet use - not for permanent submersion unless the model is marked IP68.</p>
''')
product_page('products/ip65.html', 'IP65 Rainproof LED Drivers (100-600W)',
    '100W - 600W', 'IP65', 'Metal case with mesh vents, corrosion resistant',
    'Rainproof drivers for signage, billboards, and semi-outdoor installations. Metal housing with ventilation.',
    'Metal-case IP65 rainproof LED drivers, 100W-600W, for signage and semi-outdoor.', '/images/product-rainproof.webp',
    inp='AC 190-264V', outp='DC 12/24V',
    related=[('blog-2','IP20 vs IP65 vs IP67 vs IP68')],
    extra='''
<h2>Where IP65 drivers are used</h2>
<p>IP65 rainproof drivers suit signage, billboards, channel letters, and semi-outdoor installs that face rain and dust but not direct water jets. The metal case with mesh vents sheds heat while keeping weather out.</p>
<h2>How to size a rainproof driver</h2>
<p>Add the wattage of all connected signs, add a 20% margin, and choose a model above that total. The 190-264V input covers standard commercial mains. Mount the case where air can flow through the vents.</p>
<h2>What is built in</h2>
<p>Corrosion-resistant metal case, ventilation for high-power runs, and over-voltage, over-current, over-temperature, and short-circuit protection. For full outdoor wet use, choose the IP67 line instead.</p>
''')

print("All pages generated.")
