import re, io

p = "index.html"
html = open(p, encoding="utf-8").read()
orig = html

# ---------- 1) Fix <picture> srcset: replace trailing '1x' with real width descriptor ----------
html = html.replace('factory.jpg.webp 1x"', 'factory.jpg.webp 1216w"')      # base factory = 1216w
html = html.replace('.webp 1x"', '.webp 1024w"')                            # everything else base = 1024w
assert ' 1x"' not in html, "leftover 1x descriptor found!"

# ---------- 2) lang-item <div> -> <button> ----------
# <div class="lang-item ..."> ... </div>  (no nested divs inside) -> button
html = re.sub(
    r'<div class="lang-item([^>]*)>([\s\S]*?)</div>',
    r'<button type="button" class="lang-item\1>\2</button>',
    html
)

# ---------- 3) mobile .ml <span onclick=setLang> -> <button> + close menu ----------
def ml_repl(m):
    code = m.group(1)      # e.g. en  (from setLang('en'))
    attrs = m.group(3)     #  class="active"  (the [^>]* after id)
    label = m.group(4)     # EN
    return f'<button type="button" onclick="setLang(\'{code}\');closeMobileMenu()" id="ml-{code}"{attrs}>{label}</button>'
html = re.sub(
    r'<span onclick="setLang\(.(\w+).\)" id="ml-(\w+)"([^>]*)>([A-Z]+)</span>',
    ml_repl,
    html
)

# ---------- 4) fallback PNG -> optimized JPG ----------
for name in ["factory.jpg", "product-adapter", "product-indoor", "product-waterproof",
             "product-rainproof", "blog-1-led-power-supply", "blog-2-ip-rating", "blog-3-led-market"]:
    html = html.replace(f"images/{name}.png", f"images/{name}.jpg")

# ---------- 5) add data-i18n attributes to hardcoded sections ----------
i18n = [
    # quote-guide
    ("Choose the right power supply faster", "qg_title"),
    ("For a precise quote, start from the application, then confirm voltage, wattage, IP rating, quantity, and destination market.", "qg_sub"),
    ("LED strip / modules", "qg_k1"),
    ("Adapter or indoor driver", "qg_t1"),
    ("Best for indoor signs, shelves, cabinet lighting, and short LED strip runs.", "qg_d1"),
    ("Confirm DC 12V / 24V / 36V / 48V", "qg_l1a"),
    ("Add 20-30% power margin", "qg_l1b"),
    ("Ask for plug type and label artwork", "qg_l1c"),
    ("Outdoor projects", "qg_k2"),
    ("IP67 waterproof line", "qg_t2"),
    ("Best for exposed strips, fountains, facade lighting, and wet installation areas.", "qg_d2"),
    ("Confirm cable length and connector", "qg_l2a"),
    ("Confirm salt-spray or high-humidity use", "qg_l2b"),
    ("Ask for CE / RoHS PDF by model", "qg_l2c"),
    ("Signage / billboard", "qg_k3"),
    ("IP65 rainproof line", "qg_t3"),
    ("Best for semi-outdoor signage cabinets where airflow and higher wattage matter.", "qg_d3"),
    ("Confirm 12V / 24V output", "qg_l3a"),
    ("Confirm cabinet ventilation", "qg_l3b"),
    ("Confirm carton weight and pallet need", "qg_l3c"),
    ("OEM / distributor", "qg_k4"),
    ("Custom label or housing", "qg_t4"),
    ("Best when you need your logo, fixed SKU list, market files, or packaging control.", "qg_d4"),
    ("MOQ starts from 500 pcs", "qg_l4a"),
    ("Send target label and spec sheet", "qg_l4b"),
    ("Lead time usually 25-30 days", "qg_l4c"),
    ("Quote tip:", "qg_tip_h"),
    ("send output voltage, wattage, quantity, destination port, and target market in one message. ", "qg_tip_t"),
    ("Use the inquiry form", "qg_tip_a"),
    # certs
    ("Certificates &amp; QC proof before order", "ct_title"),
    ("Buyers should not have to guess. Tell us the model and target market, and we send the matching files before you confirm the order.", "ct_sub"),
    ("CE / RoHS PDFs", "ct_c1h"),
    ("Certificate and report files are matched by model and application, not sent as generic screenshots.", "ct_c1d"),
    ("48-hour burn-in record", "ct_c2h"),
    ("Every unit is tested before shipment. Failed units do not leave the factory floor.", "ct_c2d"),
    ("Datasheet &amp; label artwork", "ct_c3h"),
    ("We confirm input, output, protection, case size, label text, and plug or cable details.", "ct_c3d"),
    ("Shipping documents", "ct_c4h"),
    ("Commercial invoice, packing list, certificate of origin, and cartons or pallets are confirmed before loading.", "ct_c4d"),
    ("Need UL?", "ct_need_h"),
    ("UL is handled per model. Send your market and quantity first; we confirm cost and schedule before application.", "ct_need_d"),
    ("Request matching files", "ct_btn"),
    # inquiry sidebar
    ("Best message format", "inq_tmpl_h"),
    ("Copy this into the message field for a faster answer:", "inq_tmpl_p"),
    ("Output voltage and wattage", "inq_tmpl_l1"),
    ("Quantity and sample need", "inq_tmpl_l2"),
    ("Indoor, rainproof, or waterproof use", "inq_tmpl_l3"),
    ("Destination port and target market", "inq_tmpl_l4"),
    ("Certificate or label requirements", "inq_tmpl_l5"),
    ("Certificate PDFs for your target market", "inq_w6"),
]

missing = []
for text, key in i18n:
    token = ">" + text
    if token not in html:
        missing.append(text)
        continue
    html = html.replace(token, f' data-i18n="{key}">{text}', 1)

if missing:
    print("!!! MISSING TEXT (not replaced):")
    for m in missing:
        print("   -", m)
else:
    print(f"OK: all {len(i18n)} data-i18n attributes inserted")

# sanity checks
print("srcset '1x' remaining:", html.count(' 1x"'))
print("lang-item <button> count:", html.count('class="lang-item'))
print("ml <button> count:", html.count('id="ml-'))
print("data-i18n total:", html.count('data-i18n='))

open(p, "w", encoding="utf-8").write(html)
print("wrote", p, "bytes:", len(html), "(was", len(orig), ")")
