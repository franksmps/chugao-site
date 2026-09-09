#!/usr/bin/env python3
# gen_pages.py -- generate the 7 P2-A static pages under src/ from templates.
# These are English-only this round; the build pipeline will localize them once
# their T keys are translated (flip LOCALIZED in build_i18n.py).
import os, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
DOMAIN = 'https://www.chugaopower.com'

NAV = '''<header><div class="c"><div class="ni"><a href="/" class="logo"><img src="/logo.png" alt="CHUGAO Power Logo" width="169" height="44" fetchpriority="high" loading="eager"></a><nav><ul class="nl"><li><a href="/" data-i18n="n_h">Home</a></li><li><a href="/about/" data-i18n="n_a">About</a></li><li><a href="/products/adapters/" data-i18n="n_p">Products</a></li><li><a href="/#specs" data-i18n="n_s">Specs</a></li><li><a href="/#why" data-i18n="n_w">Why us</a></li><li><a href="/blog/" data-i18n="n_b">News</a></li><li><a href="/faq/" data-i18n="n_f">FAQ</a></li><li><a href="/#contact" data-i18n="n_c">Contact</a></li></ul></nav><div style="display:flex;align-items:center"><div class="lang-selector"><button class="lang-btn" onclick="toggleLangDropdown()" aria-haspopup="true" aria-expanded="false" aria-controls="lang-dropdown"><span id="current-lang">EN</span><svg width="10" height="10" viewBox="0 0 10 10" fill="currentColor"><path d="M1 3l4 4 4-4H1z"/></svg></button><div class="lang-dropdown" id="lang-dropdown"><!--LANG_DROPDOWN--></div></div><button class="mt" id="mobileToggle" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button></div></div></div></header>
<div class="mm" id="mobileMenu"><a href="/" onclick="closeMobileMenu()" data-i18n="n_h">Home</a><a href="/about/" onclick="closeMobileMenu()" data-i18n="n_a">About</a><a href="/products/adapters/" onclick="closeMobileMenu()" data-i18n="n_p">Products</a><a href="/#specs" onclick="closeMobileMenu()" data-i18n="n_s">Specs</a><a href="/#why" onclick="closeMobileMenu()" data-i18n="n_w">Why us</a><a href="/blog/" onclick="closeMobileMenu()" data-i18n="n_b">News</a><a href="/faq/" onclick="closeMobileMenu()" data-i18n="n_f">FAQ</a><a href="/#contact" onclick="closeMobileMenu()" data-i18n="n_c">Contact</a><div class="ml"><!--LANG_MOBILE--></div></div>'''

FOOTER = '''<footer><div class="c"><div class="fg"><div class="fb"><a href="/" class="logo"><img src="/logo.png" alt="CHUGAO" class="logo-white" style="height:32px" loading="lazy"></a><p data-i18n="f_desc">CHUGAO - LED power supply factory in Zhongshan, China. Factory direct.</p></div><div class="fc"><h3 data-i18n="f_prod">Products</h3><a href="/products/adapters/">Adapters</a><a href="/products/indoor/">Indoor drivers</a><a href="/products/ip67/">IP67 waterproof</a><a href="/products/ip65/">IP65 rainproof</a></div><div class="fc"><h3 data-i18n="f_comp">Company</h3><a href="/about/">About</a><a href="/certs/">Certifications</a><a href="/faq/">FAQ</a></div><div class="fc"><h3 data-i18n="f_supp">Support</h3><a href="/#contact">Contact</a><a href="mailto:info@chugaopower.com">Email</a><a href="https://wa.me/8618933373873" target="_blank" rel="noopener noreferrer">WhatsApp</a></div></div><div class="fb2"><p>&copy; 2026 Zhongshan Chugao Electronic Technology Co., Ltd. All Rights Reserved.</p></div></div></footer>'''

def page(path, title, desc, body, json_ld=None, og_image='/images/factory.jpg'):
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0f172a">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/logo.png">
<link rel="stylesheet" href="/style.css?v=11">
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
{NAV}
<main id="main">
{body}
</main>
{json_ld or ''}
{FOOTER}
<script src="/main.min.js?v=3" defer></script>
<script src="/analytics.js?v=1" defer></script>
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

<div class="statgrid" style="margin-bottom:60px">
<div class="wc"><div class="wi">6,000</div><h2>m&sup2; Factory</h2><p>Guzhen, Zhongshan &mdash; China's lighting capital, with the full supply chain next door.</p></div>
<div class="wc"><div class="wi">38+</div><h2>Floor staff</h2><p>Skilled SMT, wave-soldering, potting and QC operators on four dedicated lines.</p></div>
<div class="wc"><div class="wi">42</div><h2>Countries</h2><p>Distributors, brands and contractors across Europe, North America, the Middle East and SE Asia.</p></div>
<div class="wc"><div class="wi">2008</div><h2>Trading since</h2><p>Over 15 years building LED drivers and AC/DC adapters for global buyers.</p></div>
<div class="wc"><div class="wi">4</div><h2>Product lines</h2><p>Adapters, indoor drivers, IP67 and IP65 &mdash; one stop for low-voltage LED power.</p></div>
<div class="wc"><div class="wi">48h</div><h2>Burn-in</h2><p>Every unit runs a 48-hour full-load burn-in before it is packed and shipped.</p></div>
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

<h2>Exhibitions &amp; trade shows</h2>
<p>We exhibit at major LED and lighting trade shows every year, meeting distributors and brand owners face to face. The photos below are from our booth appearances at the Zhongshan Guzhen, Guangzhou, Canton Fair, and Shanghai lighting exhibitions between 2018 and 2024 &mdash; the team on the floor, the products on display, and the conversations that turn into long-term supply partnerships.</p>

<div class="gallery">
<figure><img src="/images/exhibition-1.jpg.webp" alt="CHUGAO booth at the 2018 Zhongshan Guzhen lighting fair" loading="lazy"><figcaption>2018 Zhongshan Guzhen International Lighting Fair</figcaption></figure>
<figure><img src="/images/exhibition-2.jpg.webp" alt="CHUGAO LED power supplies on display at the 2024 Guangzhou lighting exhibition" loading="lazy"><figcaption>2024 Guangzhou International Lighting Exhibition</figcaption></figure>
<figure><img src="/images/exhibition-3.jpg.webp" alt="CHUGAO stand at the 2020 Canton Fair" loading="lazy"><figcaption>2020 Canton Fair (China Import and Export Fair)</figcaption></figure>
<figure><img src="/images/exhibition-4.jpg.webp" alt="CHUGAO booth at the 2022 Shanghai international lighting exhibition" loading="lazy"><figcaption>2022 Shanghai International Lighting Exhibition</figcaption></figure>
</div>

<div class="proof-strip">
<div><strong>Need a quote or certificate plan?</strong><p>Tell us your market and model &mdash; we reply within 1 hour in China business hours.</p></div>
<a class="btn-p" href="/#inquiry">Contact sales</a>
</div>

</div></section>'''
page('about.html', 'About CHUGAO - LED power supply factory, Zhongshan China',
     'CHUGAO is an LED switching power supply manufacturer in Zhongshan, China. 6,000 m2 factory, 4 product lines, CE/RoHS on every unit, OEM/ODM since 2008.',
     about_body)

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
 ("Can I order a sample before a bulk order?", "Yes. Samples ship in about 5 days and are charged at unit price plus shipping. The sample fee is refunded against your first bulk order. Most buyers test one or two units on their own fixtures before committing."),
 ("Should I choose 12V or 24V?", "24V is the safer default for anything longer than a few metres: at the same power it halves the current, so you lose less voltage over the cable and can run longer strips. 12V is fine for short runs, channel letters, and small fixtures already wired for 12V. Tell us the run length and we will size it for you."),
 ("Constant voltage or constant current - which do I need?", "Constant voltage (12V/24V/36V/48V) powers LED strips, modules, and signage that have their own resistors or regulators. Constant current (e.g. 350mA-1500mA) powers bare high-power LEDs such as downlights, floodlights, and street lights without on-board regulation. If you are unsure, send a photo of the LED label and we will match it."),
 ("Can you print my logo on the driver and the packaging?", "Yes, on OEM orders from 500 pcs. We silkscreen or laser-mark the housing, print your label artwork with your part number and barcodes, and pack in your printed cartons. Send the artwork as AI or PDF and we return a layout proof before tooling."),
 ("Do your drivers support dimming?", "Selected indoor and IP67 models support 0-10V, PWM, and TRIAC (phase-cut) dimming from 100W upward. Dimming is not available on the smallest adapters. Tell us which dimmer or control system you use and we will confirm compatibility before you order."),
 ("What is your monthly production capacity?", "Around 120,000 units per month across four lines, with roughly 60% of that allocated to stock models. High-wattage IP65 units take more line time, so confirm capacity with sales if you are planning a container-level repeat order."),
 ("Can you arrange UL for the North American market?", "Yes, per model. UL listing takes 4-6 weeks from application and is charged per file. We usually start it after you confirm the model and quantity, and we send the file reference as soon as it is issued so you can clear customs."),
 ("Do you accept third-party inspection or a factory audit?", "Yes. Buyers are welcome to send SGS, TUV, Intertek, or their own QA team for pre-shipment inspection, and we host factory audits by appointment. We supply the burn-in records and test reports for the batch being inspected."),
 ("What is the expected service life of your drivers?", "30,000 hours for adapters and IP65 units, 50,000 hours for indoor and IP67 units, both rated at full load in a 25C ambient. Real life depends mainly on case temperature: every 10C reduction roughly doubles capacitor life, so leave room for ventilation."),
 ("Do you keep stock in Europe or the United States?", "No. Everything ships from our Zhongshan factory, which is why factory-direct pricing works. Stock models leave within 3-7 days, and sea freight to Northern Europe or the US West Coast typically takes 25-35 days. Air and rail options are available for urgent orders."),
 ("Which ports do you ship from?", "FOB Shenzhen or FOB Zhongshan, your choice. We pack in export cartons of 20-25 kg, palletise on request, and prepare the commercial invoice, packing list, and certificate of origin with every shipment."),
 ("What is the warranty claim process?", "Send the model, quantity, and photos or a short video of the failure. After we confirm it, replacements ship with your next order or immediately if the quantity is small. Failures caused by lightning, water ingress beyond the rated IP level, or incorrect wiring are not covered."),
 ("Can you match a competitor's driver I already use?", "Usually yes. Send the existing model number or its label photo and we will quote an equivalent with the same output voltage, current, and dimensions. Where the enclosure differs we confirm a mechanical drawing before you commit."),
]
faq_items = ''.join(
    f'<div class="faq-item"><h2>{q}</h2><p>{a}</p></div>' for q,a in faq_qa)
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
     faq_body, faq_json)

# ---------- Certifications ----------
certs_body = '''
<section class="sec sa"><div class="c">
<h1>Certifications &amp; compliance</h1>
<p>Every CHUGAO model ships with the documentation your market requires, and certificate PDFs are sent before you place an order - not after. That way you can clear customs, register the product, and satisfy your own customers' compliance checks without a delay at the port.</p>
<p>What is standard and what is on request, by market:</p>

<div class="table-wrap">
<table class="spec-table">
<thead><tr><th>Market</th><th>What is normally required</th><th>How we handle it</th><th>Timeline</th></tr></thead>
<tbody>
<tr><td>European Union</td><td>CE (Low Voltage + EMC directives), RoHS</td><td>Standard on every model, Declaration of Conformity issued</td><td>Already in place</td></tr>
<tr><td>North America</td><td>UL or ETL listing, FCC</td><td>Applied per model once you confirm model and quantity</td><td>4-6 weeks</td></tr>
<tr><td>India</td><td>BIS registration (CRS)</td><td>On request for selected models, handled per model</td><td>Runs parallel with production</td></tr>
<tr><td>United Kingdom</td><td>UKCA</td><td>Available on request using the CE technical file</td><td>1-2 weeks</td></tr>
<tr><td>Australia / New Zealand</td><td>SAA approval, RCM marking</td><td>On request</td><td>2-4 weeks</td></tr>
<tr><td>South Korea</td><td>KC</td><td>On request</td><td>4-6 weeks</td></tr>
<tr><td>Russia / EAEU</td><td>EAC</td><td>On request</td><td>2-3 weeks</td></tr>
<tr><td>Brazil</td><td>INMETRO</td><td>On request, per model</td><td>6-8 weeks</td></tr>
<tr><td>Other markets</td><td>CB Scheme test report, local registration</td><td>CB report available; we support your local registration</td><td>Confirmed per case</td></tr>
</tbody>
</table>
</div>

<h2>CE &amp; RoHS (standard on every model)</h2>
<p>CE marking and RoHS compliance are standard on every unit, at no extra cost. Our LED drivers are assessed against the EU directives that apply to lighting power supplies - the Low Voltage Directive and the EMC Directive - and RoHS confirms that restricted substances stay below the allowed limits. REACH statements are available for buyers who need them. The test report and the Declaration of Conformity are sent as PDFs with your quote, so your compliance team can file them before the goods ship.</p>

<h2>UL and ETL (North America)</h2>
<p>UL listing is handled per model, because the file is tied to a specific construction and component list. It takes 4-6 weeks from application, and the fee is charged per file rather than per unit. We usually start the application after you confirm the model and quantity, and we send the file reference as soon as it is issued so you can clear customs and list the product with your distributor. Class 2 output is available on selected adapter models - tell us if your installation requires it.</p>

<h2>BIS (India)</h2>
<p>BIS registration for the India market is available on request for selected models. Tell us the target models and we confirm cost and lead time. Plan this early: registration is best run in parallel with production rather than after it, otherwise the goods sit at the port waiting for a number.</p>

<h2>Other marks, on request</h2>
<p>Where your market is not in the table above, the usual route is a CB Scheme test report from an accredited lab, which most national schemes accept as the technical basis for local registration. We supply the report, the circuit diagrams, the component list, and labelled samples so your local agent can complete the filing.</p>

<h2>How to plan your certification timeline</h2>
<ol>
<li>Tell us the destination market and the model you plan to import.</li>
<li>We confirm which of your requirements are already covered as standard.</li>
<li>Anything missing is quoted separately, with cost and weeks attached.</li>
<li>You receive certificate PDFs before you place the order.</li>
<li>Original documents ship with the goods.</li>
</ol>
<p>The practical rule: build certification into the order timeline from day one. A certificate applied after production is a shipment that waits.</p>

<h2>What we send with each shipment</h2>
<ul>
<li>Commercial invoice and packing list</li>
<li>Certificate of origin</li>
<li>CE and RoHS test reports plus Declaration of Conformity</li>
<li>UL file reference or BIS registration where applicable</li>
<li>Batch burn-in and QC records, on request</li>
</ul>
<p>Original documents ship with the goods; PDF copies are emailed before the container leaves the factory.</p>

<h2>Need a specific certificate?</h2>
<p>Standards and proof requirements differ by country. Tell us the destination market and the model you plan to import, and we will confirm which certificate applies and how long it takes. See the <a href="/faq/">FAQ</a> for lead times and minimum order quantities, or <a href="/#contact">contact sales</a> for a quote.</p>
</div></section>'''
page('certs.html', 'Certifications - CE, RoHS, UL, BIS for CHUGAO LED drivers',
     'CHUGAO LED power supplies carry CE and RoHS on every model, UL per model, and BIS for India on request. Certificate PDFs provided before order.',
     certs_body)

# ---------- Product category template ----------
# Product index for cross-links shown on every product page
PRODUCTS = [
    ('products/adapters', 'LED Adapters (5-200W)', '/images/product-adapter.webp'),
    ('products/indoor', 'Indoor LED Drivers (50-400W)', '/images/product-indoor.webp'),
    ('products/ip67', 'IP67 Waterproof LED Drivers (10-400W)', '/images/product-waterproof.webp'),
    ('products/ip65', 'IP65 Rainproof LED Drivers (100-600W)', '/images/product-rainproof.webp'),
]

# Cross-line comparison table (reuses the exact spec strings already localized
# via SUBTR in each product page's spec table, so no new translation keys needed).
PRODUCT_COMPARE = {
    'products/adapters': ('5W - 200W', 'IP20 (indoor)', 'AC 100-240V universal', 'DC 12/24/36/48V'),
    'products/indoor':   ('50W - 400W', 'IP20', 'AC 190-264V', 'DC 12/24V'),
    'products/ip67':     ('10W - 400W', 'IP67 / IP68', 'AC 90-305V', 'DC 12/24V'),
    'products/ip65':     ('100W - 600W', 'IP65', 'AC 190-264V', 'DC 12/24V'),
}

def _compare_table(current):
    """Side-by-side comparison of all four CHUGAO product lines."""
    rows = [('Power range', 0), ('Ingress protection', 1),
            ('Input voltage', 2), ('Output voltage', 3)]
    head = ''.join(
        f'<th{" style=\"background:#0f172a;color:#fff" if p == current else ""}>{n}</th>'
        for (p, n, i) in PRODUCTS)
    body_rows = ''
    for label, idx in rows:
        cells = ''.join(
            f'<td{" style=\"background:#eef4ff;font-weight:600" if p == current else ""}>'
            f'{PRODUCT_COMPARE[p][idx]}</td>'
            for (p, n, i) in PRODUCTS)
        body_rows += f'<tr><th>{label}</th>{cells}</tr>'
    return ('\n<h2>Compare all CHUGAO lines</h2>\n'
            '<p>Four product lines cover most low-voltage LED jobs. Pick by power, '
            'protection, and input range.</p>\n'
            '<table class="spec-table">\n'
            f'<tr><th>Line</th>{head}</tr>\n{body_rows}</table>')

# product path -> (spec sheet filename, <select> value used by the inquiry form)
SPEC_PDF = {
    'products/adapters': ('chugao-led-adapters-5-200w.pdf', 'adapter'),
    'products/indoor': ('chugao-indoor-led-drivers-50-400w.pdf', 'indoor'),
    'products/ip67': ('chugao-ip67-waterproof-led-drivers-10-400w.pdf', 'waterproof'),
    'products/ip65': ('chugao-ip65-rainproof-led-drivers-100-600w.pdf', 'rainproof'),
}


def _spec2_table(rows):
    if not rows:
        return ''
    body = ''.join(f'<tr><td>{l}</td><td>{v}</td></tr>' for l, v in rows)
    return (f'<h2>Electrical &amp; environmental</h2>\n'
            f'<table class="spec-table">\n'
            f'<tr><th>Parameter</th><th>Detail</th></tr>\n{body}</table>\n')


def _model_table(models):
    if not models:
        return ''
    rows = ''.join(f'<tr><td>{p}</td><td>{o}</td></tr>' for p, o in models)
    return (f'<h2>Available power ratings</h2>\n'
            f'<table class="spec-table">\n'
            f'<tr><th>Power</th><th>Output voltage</th></tr>\n{rows}</table>\n')


def _faq_block(faqs):
    if not faqs:
        return ''
    items = ''.join(f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q, a in faqs)
    return f'<h2>Frequently asked questions</h2>\n{items}\n'


def _datasheet_cta(path=''):
    """Link to the real PDF spec sheet; fall back to the inquiry anchor if unknown."""
    info = SPEC_PDF.get(path[:-5] if path.endswith('.html') else path)
    if info:
        return ('<p style="margin:28px 0">'
                '<a href="/specs/%s" class="btn-p" target="_blank" rel="noopener" download>'
                'Request full specification sheet (PDF)</a></p>\n' % info[0])
    return ('<p style="margin:28px 0">'
            '<a href="/#inquiry" class="btn-p">Request full specification sheet (PDF)</a></p>\n')


# Shared buying/quality sections for every product page.
# Every English string below already exists as a SUBTR key across all 10
# localized languages, so this adds substantial content with ZERO new
# translation work and no risk of English leakage.
_BUYING = '''<h2>Manufacturing &amp; quality control</h2>
<p>Production runs on four dedicated lines fed by SMT assembly and wave soldering, then finished on in-house potting and enclosure lines. Each driver moves through incoming component inspection and automated ICT, then a 48-hour full-load burn-in at elevated temperature before it is packed. On the line we check output voltage, ripple, efficiency, and the four protective functions \u2014 over-voltage, over-current, over-temperature, and short-circuit \u2014 so a weak unit is caught before it reaches you.</p>
<h2>Certifications &amp; compliance</h2>
<p>CE and RoHS on every model. UL is per model and costs extra. We send certificate PDFs before you order. BIS for India is available on request.</p>
<p>Every CHUGAO model ships with the documentation your market requires. Certificate PDFs are sent before you place an order, so you can clear customs and meet local electrical rules without surprises.</p>
<h2>What is the minimum order quantity?</h2>
<p>50 pieces per model for stock items. 500 pieces for custom OEM. We do not accept 1-piece orders.</p>
<h2>What is the lead time?</h2>
<p>Stock: 3-7 days. OEM: 25-30 days. Samples: 5 days, charged plus shipping, refunded on a bulk order.</p>
<h2>What is the warranty?</h2>
<p>3 years on stock items. OEM warranty is defined in the contract. Warranty does not cover lightning, water damage, or incorrect wiring.</p>
<h2>OEM and ODM</h2>
<p>Our engineering team supports OEM and ODM changes to output voltage, enclosure size, connector type, and cable length. Where a project calls for it, we can add dimming control (0-10V or PWM) or adjust the input range. Custom samples are built from your spec sheet and verified against the same test routine used in mass production, so what you approve is what ships.</p>
<h2>Why buy factory direct</h2>
<p>Buying from the manufacturer removes the trader margin and shortens the path from a design change to shipment. You can also request the exact certificate package your market needs instead of a generic one. Every shipment includes a commercial invoice, packing list, certificate of origin, and CE/RoHS reports, with original documents shipped with the goods.</p>
<p>We supply distributors, lighting brands, and project contractors in 42 countries, with the strongest presence in Europe, North America, the Middle East, and Southeast Asia. Sales and engineering reply in English, Spanish, French, Russian, Arabic, and Chinese, and aim to respond within 1 hour during China business hours (GMT+8).</p>
'''


def _buying_block():
    return _BUYING


# Per-product selection guidance (translated in SUBTR for all 10 languages).
COMPARE_ADAPTERS = (
    "Choose an adapter when the LED load sits close to a wall socket — strips under cabinets, edge-lit signs, display cases, and small fixtures that plug in. Adapters are the smallest and lowest-cost way to get from mains to 12V or 24V DC, and the 100-240V universal input means one SKU ships to any market. Step up to the indoor driver line once you pass 200W, need a hard-wired enclosure inside a ceiling or fixture, or need active PFC for a commercial project with many fittings on one circuit."
)
COMPARE_INDOOR = (
    "Choose an indoor driver when the fitting is hard-wired into a building — ceiling lights, panel lights, troffers, and linear fixtures. You get active power-factor correction, fan-less silent running, a 5-year warranty, and up to 400W in a case that mounts in a ceiling void or inside the fixture body. These are IP20, so they stay in dry interiors. If the install faces rain, dust, or wash-down, use the IP65 rainproof line for signage or the IP67 waterproof line for open outdoor sites."
)
COMPARE_IP67 = (
    "Choose IP67 when the driver will sit where water collects — outdoor strips, landscape and garden lighting, fountains, pools, and coastal or marine installs. The fully potted silicone enclosure blocks water jets, driving rain, and salt spray, and 6kV surge protection handles exposed sites. IP65 costs less and runs cooler, but it only resists rain and dust. Under a roof or inside a sealed sign, IP65 is enough; in the open or near standing water, pay for IP67."
)
COMPARE_IP65 = (
    "Choose IP65 when the install is semi-outdoor — signage, billboards, channel letters, and covered walkways that face rain and dust but never direct water jets. The vented metal case sheds heat better than a sealed potted unit, which is why this line reaches 600W, and it is the value choice for weather-exposed but not water-exposed jobs. If the driver will sit in standing water, be hosed down, or face salt spray, choose the IP67 line instead."
)


def product_page(path, name, rng, ip, feat, desc, blurb, img, inp='', outp='',
                 related=None, extra='', spec2=None, models=None, faq=None,
                 compare=None, title=None, meta_desc=None):
    rel_block = ''
    if related:
        items = ''.join(f'<li><a href="/{b}/">{t}</a></li>' for b, t in related)
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
    structured = _spec2_table(spec2) + _model_table(models) + _datasheet_cta(path) + _faq_block(faq)
    buying = _buying_block()
    _sp = SPEC_PDF.get(path[:-5] if path.endswith('.html') else path)
    inq = _sp[1] if _sp else ''
    compare_block = ''
    if compare:
        compare_block = ('\n<h2>Which line fits your project?</h2>\n'
                         '<p>%s</p>\n' % compare)
    compare_table_block = _compare_table(path)
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
{structured}
{extra}
{compare_block}
{compare_table_block}
{buying}
{other_block}
<p style="margin-top:36px"><a href="/#inquiry?product={inq}" class="btn-p">Get a quote for {name}</a> &nbsp; <a href="/products/adapters/" data-i18n="n_p" style="color:var(--a);font-weight:600">View all products</a></p>{rel_block}
</div></section>'''
    product_data = {
        "@context": "https://schema.org",
        "@type": "Product",
        "inLanguage": "en",
        "name": name,
        "image": [DOMAIN + img],
        "description": desc,
        "brand": {"@type": "Brand", "name": "CHUGAO Power"},
        "category": "LED power supply",
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Power range", "value": rng},
            {"@type": "PropertyValue", "name": "Ingress protection", "value": ip},
            {"@type": "PropertyValue", "name": "Input voltage", "value": inp},
            {"@type": "PropertyValue", "name": "Output voltage", "value": outp},
        ],
        "offers": {
            "@type": "Offer",
            "url": DOMAIN + "/" + path + "/",
            "availability": "https://schema.org/InStock",
            "priceCurrency": "USD",
            "seller": {"@type": "Organization",
                       "name": "Zhongshan Chugao Electronic Technology Co., Ltd."}
        }
    }
    product_json = '<script type="application/ld+json">' + \
        json.dumps(product_data, ensure_ascii=False) + '</script>'
    faq_json = ''
    if faq:
        faq_data = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "en",
                    "mainEntity": [{"@type": "Question", "name": q,
                                    "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
        faq_json = '<script type="application/ld+json">' + \
            json.dumps(faq_data, ensure_ascii=False) + '</script>'
    # `title` / `meta_desc` carry the Tier-1 buyer-intent wording (manufacturer /
    # OEM ODM / 50 pcs MOQ). `desc` remains the Overview paragraph, so product
    # pages need a separate meta description instead of reusing it.
    return page(path, title or f'{name} - CHUGAO LED power supply',
                meta_desc or desc, body,
                product_json + faq_json, og_image=img.replace('.webp', '.jpg'))

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
''',
    spec2=[
        ("Efficiency", "≥83%"),
        ("Ripple and noise", "≤120mV"),
        ("Surge protection", "4kV"),
        ("Operating temperature", "-20°C to +50°C"),
        ("MTBF", "50,000 hours"),
        ("Warranty", "3 years"),
    ],
    models=[
        ("5W", "12V"),
        ("12W", "12V / 24V"),
        ("24W", "12V / 24V"),
        ("36W", "12V / 24V / 36V"),
        ("60W", "12V / 24V"),
        ("100W", "12V / 24V / 36V / 48V"),
        ("150W", "12V / 24V / 36V / 48V"),
        ("200W", "12V / 24V / 36V / 48V"),
    ],
    faq=[
        ("Can I use one adapter for both 12V and 24V strips?",
         "No. Choose the output voltage that matches your LED. We make 12V, 24V, 36V and 48V models - check the label on your strip before ordering."),
        ("Do you fit a plug for my country?",
         "The adapter accepts 100-240V worldwide. We fit the local plug or AC cord for your market (US, EU, UK, AU and others) at no extra charge."),
    ],
    compare=COMPARE_ADAPTERS,
    title="LED Adapter Manufacturer 5-200W | OEM ODM, MOQ 50 pcs",
    meta_desc="China LED adapter manufacturer: 5-200W 12V/24V AC/DC adapters for strips, modules and signage. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.")
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
''',
    spec2=[
        ("Efficiency", "≥88%"),
        ("Power factor", "≥0.95"),
        ("Ripple and noise", "≤100mV"),
        ("Surge protection", "4kV"),
        ("Operating temperature", "-30°C to +60°C"),
        ("MTBF", "100,000 hours"),
        ("Warranty", "5 years"),
    ],
    models=[
        ("50W", "12V / 24V"),
        ("75W", "12V / 24V"),
        ("100W", "12V / 24V"),
        ("150W", "12V / 24V"),
        ("200W", "12V / 24V"),
        ("300W", "12V / 24V"),
        ("400W", "12V / 24V"),
    ],
    faq=[
        ("Do these drivers support dimming?",
         "Selected models support 0-10V or PWM dimming. Tell us your control system and we will specify the correct driver."),
        ("Can they be mounted above a ceiling?",
         "Yes. The IP20 drivers are made for dry indoor use such as above ceilings and inside fixtures. Leave some air space and do not bury them in insulation."),
    ],
    compare=COMPARE_INDOOR,
    title="Indoor LED Driver Manufacturer 50-400W | OEM ODM MOQ 50",
    meta_desc="China indoor LED driver manufacturer: 50-400W constant voltage, active PFC, fan-less. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.")
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
''',
    spec2=[
        ("Efficiency", "≥87%"),
        ("Power factor", "≥0.95"),
        ("Ripple and noise", "≤100mV"),
        ("Ingress protection", "IP67 / IP68 (potting)"),
        ("Surge protection", "6kV"),
        ("Operating temperature", "-30°C to +60°C"),
        ("MTBF", "80,000 hours"),
        ("Warranty", "5 years"),
    ],
    models=[
        ("10W", "12V / 24V"),
        ("20W", "12V / 24V"),
        ("30W", "12V / 24V"),
        ("60W", "12V / 24V"),
        ("100W", "12V / 24V"),
        ("150W", "12V / 24V"),
        ("200W", "12V / 24V"),
        ("300W", "12V / 24V"),
        ("400W", "12V / 24V"),
    ],
    faq=[
        ("Can an IP67 driver be submerged?",
         "IP67 resists brief immersion; IP68 models handle continuous submersion. For fountains and pools choose the IP68 version, and we will confirm the depth rating."),
        ("How do I wire a waterproof driver outdoors?",
         "Use waterproof connectors and keep joints inside a sealed junction box. We supply IP67 cable glands so the entry points stay watertight."),
    ],
    compare=COMPARE_IP67,
    title="IP67 Waterproof LED Driver Manufacturer, 10-400W",
    meta_desc="China IP67 waterproof LED driver manufacturer: 10-400W, fully potted, salt-spray tested, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.")
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
''',
    spec2=[
        ("Efficiency", "≥88%"),
        ("Power factor", "≥0.95"),
        ("Ripple and noise", "≤120mV"),
        ("Ingress protection", "IP65 (metal case)"),
        ("Surge protection", "6kV"),
        ("Operating temperature", "-30°C to +60°C"),
        ("MTBF", "100,000 hours"),
        ("Warranty", "5 years"),
    ],
    models=[
        ("100W", "12V / 24V"),
        ("150W", "12V / 24V"),
        ("200W", "12V / 24V"),
        ("300W", "12V / 24V"),
        ("400W", "12V / 24V"),
        ("500W", "12V / 24V"),
        ("600W", "12V / 24V"),
    ],
    faq=[
        ("What is the difference between IP65 and IP67?",
         "IP65 blocks rain and dust but not water jets; IP67 is fully sealed against brief immersion. For weather-exposed signage IP65 is usually enough; for wet or wash-down areas choose IP67."),
        ("Can the metal case be used outside?",
         "Yes. The corrosion-resistant metal case suits semi-outdoor signage and billboards. For full outdoor wet use, the IP67 line is the better choice."),
    ],
    compare=COMPARE_IP65,
    title="IP65 Rainproof LED Driver Manufacturer, 100-600W",
    meta_desc="China IP65 rainproof LED driver manufacturer for signage and billboards: 100-600W, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.")


# ---------------------------------------------------------------------------
# Individual SKU spec pages (first 16 hero models). Each gets a shareable URL
# /products/<slug>/ and a Product JSON-LD. Generated here (not hand-written
# HTML) so they survive future rebuilds. Body is English (same convention as
# the four product-line pages); build_i18n fans the shell out to all 11 langs.
# ---------------------------------------------------------------------------
def sku_page(spec):
    slug, model = spec['slug'], spec['model']
    line_url, line_name = spec['line_url'], spec['line_name']
    img = spec['img']
    other = ''.join(
        f'<a class="bc" href="/{p}/"><div class="bi">'
        f'<img src="{i}" alt="{n}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>'
        f'<div class="bn"><h3>{n}</h3><p>View specifications &rarr;</p></div></a>'
        for (p, n, i) in PRODUCTS if p != 'products/' + spec['line'])
    other_block = (f'<h2>Other CHUGAO product lines</h2>'
                   f'<div class="bg" style="margin-top:24px">{other}</div>')
    body = f'''<section class="sec sa"><div class="c">
<nav class="bc-nav"><a href="/">Home</a> &rsaquo; <a href="{line_url}">{line_name}</a> &rsaquo; <span>{model}</span></nav>
<h1>{model} &mdash; {line_name}</h1>
<p class="ss" style="margin:0 auto 44px">{spec['blurb']}</p>
<div class="ag" style="margin-bottom:56px">
<div class="at">
<h2>Overview</h2>
<p>{spec['desc']}</p>
<div class="quote-card" style="padding:20px 24px;margin-top:18px">
<ul style="list-style:none;padding-left:0;margin:0">
<li><strong>Power:</strong> {spec['watt']}</li>
<li><strong>Output:</strong> {spec['volt']}</li>
<li><strong>Ingress protection:</strong> {spec['ip']}</li>
<li><strong>Input:</strong> {spec['inp']}</li>
<li><strong>Certification:</strong> CE / RoHS; UL on request</li>
</ul>
</div>
</div>
<div class="aimg"><img src="{img}" alt="{model} {line_name}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>
</div>
<h2>Specifications</h2>
<table class="spec-table">
<tr><th>Parameter</th><th>Detail</th></tr>
<tr><td>Model</td><td>{model}</td></tr>
<tr><td>Power</td><td>{spec['watt']}</td></tr>
<tr><td>Output voltage</td><td>{spec['volt']}</td></tr>
<tr><td>Ingress protection</td><td>{spec['ip']}</td></tr>
<tr><td>Input voltage</td><td>{spec['inp']}</td></tr>
<tr><td>Efficiency</td><td>{spec['eff']}</td></tr>
<tr><td>Protection</td><td>{spec['prot']}</td></tr>
<tr><td>Operating temperature</td><td>{spec['temp']}</td></tr>
<tr><td>Lifespan</td><td>{spec['life']}</td></tr>
<tr><td>Warranty</td><td>{spec['warranty']}</td></tr>
</table>
<h2>Typical applications</h2>
<p>{spec['application']}</p>
<h2>Certification</h2>
<p>CE and RoHS are standard on every CHUGAO unit. UL is available per model (4-6 weeks from order confirmation). BIS (India) is available on request for selected models. Certificate PDFs are sent before you place the order.</p>
{other_block}
<p style="margin-top:36px"><a href="/#inquiry?product={spec['inq']}" class="btn-p">Get a quote for {model}</a> &nbsp; <a href="{line_url}" style="color:var(--a);font-weight:600">View all {line_name}</a></p>
</div></section>'''
    product_data = {
        "@context": "https://schema.org",
        "@type": "Product",
        "inLanguage": "en",
        "name": model + " " + line_name,
        "image": [DOMAIN + img],
        "description": spec['desc'],
        "brand": {"@type": "Brand", "name": "CHUGAO Power"},
        "category": "LED power supply",
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Power", "value": spec['watt']},
            {"@type": "PropertyValue", "name": "Output voltage", "value": spec['volt']},
            {"@type": "PropertyValue", "name": "Ingress protection", "value": spec['ip']},
            {"@type": "PropertyValue", "name": "Input voltage", "value": spec['inp']},
        ],
        "offers": {
            "@type": "Offer",
            "url": DOMAIN + "/products/" + slug + "/",
            "availability": "https://schema.org/InStock",
            "priceCurrency": "USD",
            "seller": {"@type": "Organization", "name": "Zhongshan Chugao Electronic Technology Co., Ltd."}
        }
    }
    product_json = '<script type="application/ld+json">' + json.dumps(product_data, ensure_ascii=False) + '</script>'
    return page('products/' + slug + '.html', spec['title'], spec['meta_desc'], body, product_json,
                og_image=img.replace('.webp', '.jpg'))


SKU_SPECS = [
  # --- Adapters (AC/DC) ---
  dict(slug='cgm-12w', model='CGM-12W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='12W', volt='DC 12V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='12W AC/DC LED adapter, 12V output for LED strips and modules.',
       desc='The CGM-12W is a compact 12W AC/DC adapter for 12V LED strips, LED modules and small fixtures. The universal 100-240V input means one SKU ships worldwide; we fit the local plug for your market at no extra charge. CE/RoHS standard, 3-year warranty.',
       application='12V LED strip lighting, edge-lit signs, LED modules and small indoor fixtures that plug into a wall outlet.',
       title='CGM-12W 12V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-12W 12V 12W LED adapter manufacturer. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgm-24w', model='CGM-24W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='24W', volt='DC 12V / 24V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='24W AC/DC LED adapter, selectable 12V / 24V output.',
       desc='The CGM-24W AC/DC adapter delivers 24W with a switchable 12V or 24V output to match your LED load. Universal 100-240V input, local plug fitted per market, CE/RoHS standard and a 3-year warranty.',
       application='12V or 24V LED strips, sign modules, and cabinet or shelf lighting in shops and exhibitions.',
       title='CGM-24W 12V/24V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-24W 24W LED adapter, 12V/24V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgm-36w', model='CGM-36W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='36W', volt='DC 12V / 24V / 36V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='36W AC/DC LED adapter, 12V / 24V / 36V output options.',
       desc='The CGM-36W adapts 100-240V mains to 12V, 24V or 36V DC for higher-power LED strips and modules. Four protections built in, local plug fitted per market, CE/RoHS standard, 3-year warranty.',
       application='Longer 12/24/36V LED strip runs, light boxes, and medium signage that needs a stable DC supply.',
       title='CGM-36W 12V/24V/36V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-36W 36W LED adapter, 12V/24V/36V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgm-60w', model='CGM-60W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='60W', volt='DC 12V / 24V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='60W AC/DC LED adapter, 12V / 24V output for longer strip runs.',
       desc='The CGM-60W is a 60W AC/DC adapter for 12V or 24V LED strips and modules. Universal 100-240V input, local plug fitted per market, CE/RoHS standard and a 3-year warranty.',
       application='Long 12V/24V LED strip installations, edge-lit signs and larger cabinet lighting.',
       title='CGM-60W 12V/24V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-60W 60W LED adapter, 12V/24V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  # --- Indoor drivers ---
  dict(slug='c-100w', model='C-100W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='100W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='100W indoor LED driver, 12V / 24V, built-in active PFC.',
       desc='The C-100W is a 100W indoor LED driver with built-in active PFC and fan-less silent operation. Choose 12V or 24V DC output to match your fixtures. CE/RoHS standard, 3-year warranty.',
       application='Ceiling lights, panel lights, troffers and linear fixtures inside buildings.',
       title='C-100W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China C-100W 100W indoor LED driver, 12V/24V, active PFC. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='c-200w', model='C-200W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='200W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='200W indoor LED driver, 12V / 24V, built-in active PFC.',
       desc='The C-200W delivers 200W for 12V or 24V indoor LED fixtures with active PFC and fan-less operation. Four protections built in, CE/RoHS standard, 3-year warranty.',
       application='High-output ceiling and panel lights, and long linear fixtures in commercial interiors.',
       title='C-200W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China C-200W 200W indoor LED driver, 12V/24V, active PFC. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgc-100w', model='CGC-100W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='100W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGC-100W indoor LED driver, 12V / 24V, narrow metal case.',
       desc='The CGC-100W is a 100W indoor driver in a narrow metal case for 12V or 24V fixtures. Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='Slim ceiling lights, panel lights and linear fixtures where a narrow housing fits the luminaire.',
       title='CGC-100W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGC-100W 100W indoor LED driver, 12V/24V, narrow case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgc-200w', model='CGC-200W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='200W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGC-200W indoor LED driver, 12V / 24V, narrow metal case.',
       desc='The CGC-200W is a 200W indoor driver in a narrow metal case for 12V or 24V fixtures. Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='High-output panel and linear fixtures in commercial interiors needing a slim driver.',
       title='CGC-200W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGC-200W 200W indoor LED driver, 12V/24V, narrow case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgc-400w', model='CGC-400W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='400W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGC-400W indoor LED driver, 12V / 24V, narrow metal case.',
       desc='The CGC-400W is the 400W top of the narrow-case indoor range for 12V or 24V fixtures. Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='Large commercial panel and linear lighting where a slim high-power driver is required.',
       title='CGC-400W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGC-400W 400W indoor LED driver, 12V/24V, narrow case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgb-200w', model='CGB-200W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='200W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGB-200W indoor LED driver, 12V / 24V, dimming ready.',
       desc='The CGB-200W is a 200W indoor driver for 12V or 24V fixtures with dimming support (0-10V / PWM on selected models). Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='Dimmable ceiling and panel lights and commercial interiors with a lighting-control system.',
       title='CGB-200W Dimmable Indoor LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGB-200W 200W dimmable indoor LED driver, 12V/24V, 0-10V/PWM. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  # --- IP67 waterproof ---
  dict(slug='cgf-24w', model='CGF-24W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='24W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='24W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-24W is a 24W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Outdoor LED strips, garden and landscape lighting, fountains and wet indoor areas.',
       title='CGF-24W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-24W 24W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-100w', model='CGF-100W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='100W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='100W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-100W is a 100W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Outdoor LED strips, landscape lighting, fountains, pools and marine installations.',
       title='CGF-100W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-100W 100W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-200w', model='CGF-200W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='200W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='200W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-200W is a 200W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Larger outdoor LED strip runs, facade lighting and wet commercial installs.',
       title='CGF-200W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-200W 200W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-400w', model='CGF-400W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='400W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='400W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-400W is the 400W top of the waterproof range for 12V or 24V outdoor LEDs. Fully potted IP67/IP68, salt-spray tested, 90-305V input, CE/RoHS standard, 3-year warranty.',
       application='High-power outdoor LED strips, large facade lighting and marine or coastal installs.',
       title='CGF-400W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-400W 400W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  # --- IP65 rainproof ---
  dict(slug='fyg-400w', model='FYG-400W', line='ip65', line_name='IP65 Rainproof LED Drivers (100-600W)',
       line_url='/products/ip65/', img='/images/product-rainproof.webp', inq='rainproof',
       watt='400W', volt='DC 12V / 24V', ip='IP65', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP', temp='-20 ~ +50°C', life='30,000h', warranty='3 Years',
       blurb='FYG-400W IP65 rainproof LED driver, 12V / 24V, metal case.',
       desc='The FYG-400W is a 400W IP65 rainproof driver in a corrosion-resistant metal case for 12V or 24V signage. Mesh vents shed heat while keeping weather out. CE/RoHS standard, 3-year warranty.',
       application='Signage, billboards, channel letters and semi-outdoor installs exposed to rain and dust.',
       title='FYG-400W IP65 Rainproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China FYG-400W 400W IP65 rainproof LED driver, 12V/24V, metal case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='fyg-600w', model='FYG-600W', line='ip65', line_name='IP65 Rainproof LED Drivers (100-600W)',
       line_url='/products/ip65/', img='/images/product-rainproof.webp', inq='rainproof',
       watt='600W', volt='DC 12V / 24V', ip='IP65', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP', temp='-20 ~ +50°C', life='30,000h', warranty='3 Years',
       blurb='FYG-600W IP65 rainproof LED driver, 12V / 24V, metal case.',
       desc='The FYG-600W is the 600W top of the rainproof range for 12V or 24V signage. Corrosion-resistant metal case with mesh vents, CE/RoHS standard, 3-year warranty.',
       application='Large billboards, channel-letter signs and semi-outdoor installations needing high wattage.',
       title='FYG-600W IP65 Rainproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China FYG-600W 600W IP65 rainproof LED driver, 12V/24V, metal case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  # --- remaining adapters on the homepage ---
  dict(slug='cgm-6w', model='CGM-6W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='6W', volt='DC 12V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='6W AC/DC LED adapter, 12V output for small LED modules.',
       desc='The CGM-6W is a compact 6W AC/DC adapter for 12V LED strips and small modules. Universal 100-240V input, local plug fitted per market, CE/RoHS standard, 3-year warranty.',
       application='Small 12V LED strips, sign modules and compact indoor fixtures.',
       title='CGM-6W 12V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-6W 6W LED adapter, 12V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgm-48w', model='CGM-48W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='48W', volt='DC 12V / 24V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='48W AC/DC LED adapter, selectable 12V / 24V output.',
       desc='The CGM-48W AC/DC adapter delivers 48W with a switchable 12V or 24V output to match your LED load. Universal 100-240V input, local plug fitted per market, CE/RoHS standard and a 3-year warranty.',
       application='12V or 24V LED strips, sign modules, and cabinet or shelf lighting.',
       title='CGM-48W 12V/24V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-48W 48W LED adapter, 12V/24V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgm-72w', model='CGM-72W', line='adapters', line_name='LED Adapters (5-200W)',
       line_url='/products/adapters/', img='/images/product-adapter.webp', inq='adapter',
       watt='72W', volt='DC 12V / 24V', ip='IP20', inp='AC 100-240V', eff='≥83%',
       prot='OVP / OCP / OTP / SCP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='72W AC/DC LED adapter, 12V / 24V output for longer strip runs.',
       desc='The CGM-72W is a 72W AC/DC adapter for 12V or 24V LED strips and modules. Universal 100-240V input, local plug fitted per market, CE/RoHS standard and a 3-year warranty.',
       application='Long 12V/24V LED strip installations, edge-lit signs and larger cabinet lighting.',
       title='CGM-72W 12V/24V LED Adapter Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGM-72W 72W LED adapter, 12V/24V output. 100-240V input, CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  # --- remaining indoor drivers on the homepage ---
  dict(slug='c-60w', model='C-60W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='60W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='60W indoor LED driver, 12V / 24V, built-in active PFC.',
       desc='The C-60W is a 60W indoor LED driver with built-in active PFC and fan-less silent operation. Choose 12V or 24V DC output to match your fixtures. CE/RoHS standard, 3-year warranty.',
       application='Ceiling lights, panel lights, troffers and linear fixtures inside buildings.',
       title='C-60W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China C-60W 60W indoor LED driver, 12V/24V, active PFC. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgc-48w', model='CGC-48W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='48W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGC-48W indoor LED driver, 12V / 24V, narrow metal case.',
       desc='The CGC-48W is a 48W indoor driver in a narrow metal case for 12V or 24V fixtures. Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='Slim ceiling lights, panel lights and linear fixtures where a narrow housing fits the luminaire.',
       title='CGC-48W Indoor LED Driver 12V/24V Manufacturer | CHUGAO OEM ODM',
       meta_desc='China CGC-48W 48W indoor LED driver, 12V/24V, narrow case. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgb-100w', model='CGB-100W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='100W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGB-100W indoor LED driver, 12V / 24V, dimming ready.',
       desc='The CGB-100W is a 100W indoor driver for 12V or 24V fixtures with dimming support (0-10V / PWM on selected models). Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='Dimmable ceiling and panel lights and commercial interiors with a lighting-control system.',
       title='CGB-100W Dimmable Indoor LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGB-100W 100W dimmable indoor LED driver, 12V/24V, 0-10V/PWM. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  dict(slug='cgb-400w', model='CGB-400W', line='indoor', line_name='Indoor LED Drivers (50-400W)',
       line_url='/products/indoor/', img='/images/product-indoor.webp', inq='indoor',
       watt='400W', volt='DC 12V / 24V', ip='IP20', inp='AC 190-264V', eff='≥88%',
       prot='OVP / OCP / SCP / OTP', temp='-20 ~ +50°C', life='50,000h', warranty='3 Years',
       blurb='CGB-400W indoor LED driver, 12V / 24V, dimming ready.',
       desc='The CGB-400W is the 400W top of the dimming-ready indoor range for 12V or 24V fixtures (0-10V / PWM on selected models). Active PFC, fan-less, four protections, CE/RoHS standard, 3-year warranty.',
       application='High-output dimmable ceiling and panel lighting in commercial interiors.',
       title='CGB-400W Dimmable Indoor LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGB-400W 400W dimmable indoor LED driver, 12V/24V, 0-10V/PWM. CE/RoHS, 3-year warranty, 50 pcs MOQ, OEM ODM.'),
  # --- remaining IP67 waterproof drivers on the homepage ---
  dict(slug='cgf-36w', model='CGF-36W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='36W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='36W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-36W is a 36W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Outdoor LED strips, garden and landscape lighting, fountains and wet indoor areas.',
       title='CGF-36W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-36W 36W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-60w', model='CGF-60W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='60W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='60W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-60W is a 60W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Outdoor LED strips, landscape lighting, fountains, pools and marine installations.',
       title='CGF-60W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-60W 60W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-150w', model='CGF-150W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='150W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='150W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-150W is a 150W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='Larger outdoor LED strip runs, facade lighting and wet commercial installs.',
       title='CGF-150W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-150W 150W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
  dict(slug='cgf-300w', model='CGF-300W', line='ip67', line_name='IP67 Waterproof LED Drivers (10-400W)',
       line_url='/products/ip67/', img='/images/product-waterproof.webp', inq='waterproof',
       watt='300W', volt='DC 12V / 24V', ip='IP67 / IP68', inp='AC 90-305V', eff='≥87%',
       prot='OVP / OCP / SCP / OTP', temp='-30 ~ +60°C', life='50,000h', warranty='3 Years',
       blurb='300W IP67 waterproof LED driver, 12V / 24V, fully potted.',
       desc='The CGF-300W is a 300W fully potted IP67/IP68 waterproof driver for 12V or 24V outdoor LEDs. Silicone potting blocks water and salt spray; 90-305V input covers most sites. CE/RoHS standard, 3-year warranty.',
       application='High-power outdoor LED strips, large facade lighting and marine or coastal installs.',
       title='CGF-300W IP67 Waterproof LED Driver 12V/24V | CHUGAO OEM ODM',
       meta_desc='China CGF-300W 300W IP67 waterproof LED driver, 12V/24V. Fully potted, salt-spray tested, CE/RoHS, 3-year warranty.'),
]
for _s in SKU_SPECS:
    sku_page(_s)

print("All pages generated.")
