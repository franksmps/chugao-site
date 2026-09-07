# -*- coding: utf-8 -*-
"""Buyer-intent TDK + heading overrides for the product line pages.

Why this module exists
----------------------
The four product pages are the highest commercial-intent pages on the site,
but their <title>/<description>/<h1> were generic category names
("LED Adapters (5-200W) - CHUGAO LED power supply"). This module injects the
Tier-1 buyer-intent terms that importers actually type when they are shortlisting
a factory — manufacturer / fabricante / Hersteller / производитель / مصنع,
OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty — into:

  * PAGE_META    -> <title> + <meta description> (per page, per language)
  * PAGE_H1      -> the single <h1> of that page
  * SITE_HEADINGS-> recurring <h2> strings shared by several pages

All values are authored to fit the site-wide TDK guardrails
(title <= 70 chars, description <= 160 chars); build_i18n.trim_meta() enforces
them again as a safety net, so an over-long translation can never ship.

Languages covered: en + the 6 fully-localized market languages
(es/pt/ru/fr/de/ar). The hidden languages (zh/ja/ko/it) keep the English
template text, consistent with their pseudo-localized body.
"""
import re

# (page key as build_i18n sees it, i.e. rel_html without the .html suffix)
PAGE_META = {
    'products/adapters': {
        'en': {
            'title': "LED Adapter Manufacturer 5-200W | OEM ODM, MOQ 50 pcs",
            'desc': "China LED adapter manufacturer: 5-200W 12V/24V AC/DC adapters for strips, modules and signage. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'es': {
            'title': "Fabricante de adaptadores LED 5-200W | OEM ODM, MOQ 50",
            'desc': "Fabricante de adaptadores LED en China: 5-200W 12V/24V para tiras, módulos y letreros. OEM ODM, pedido mínimo 50 uds, 48h de burn-in, garantía 3 años, CE RoHS.",
        },
        'pt': {
            'title': "Fabricante de adaptadores LED 5-200W | OEM ODM, MOQ 50",
            'desc': "Fabricante de adaptadores LED na China: 5-200W 12V/24V para fitas e letreiros. OEM ODM, pedido mínimo 50 peças, 48h de burn-in, garantia 3 anos, CE RoHS.",
        },
        'ru': {
            'title': "Производитель адаптеров LED 5-200 Вт | OEM ODM, MOQ 50",
            'desc': "Производитель LED-адаптеров в Китае: 5-200 Вт, 12/24 В для лент, модулей и вывесок. OEM ODM, минимальный заказ 50 шт, приработка 48 ч, гарантия 3 года, CE RoHS.",
        },
        'fr': {
            'title': "Fabricant d'adaptateurs LED 5-200W | OEM ODM, MOQ 50",
            'desc': "Fabricant d'adaptateurs LED en Chine : 5-200W 12V/24V pour rubans et enseignes. OEM ODM, commande minimum 50 pièces, 48h de burn-in, garantie 3 ans, CE RoHS.",
        },
        'de': {
            'title': "LED-Adapter Hersteller 5-200W | OEM ODM, MOQ 50 Stk",
            'desc': "LED-Adapter Hersteller in China: 5-200W 12V/24V für Streifen, Module und Schilder. OEM ODM, Mindestmenge 50 Stk, 3 Jahre Garantie, CE RoHS.",
        },
        'ar': {
            'title': "مصنع محولات LED 5-200 واط | OEM ODM والحد الأدنى 50",
            'desc': "مصنع محولات LED في الصين: 5-200 واط، 12/24 فولت للشرائط والوحدات واللافتات. OEM ODM، حد أدنى 50 قطعة، اختبار إحماء 48 ساعة، ضمان 3 سنوات، CE RoHS.",
        },
    },
    'products/indoor': {
        'en': {
            'title': "Indoor LED Driver Manufacturer 50-400W | OEM ODM MOQ 50",
            'desc': "China indoor LED driver manufacturer: 50-400W constant voltage, active PFC, fan-less. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'es': {
            'title': "Fabricante de drivers LED interior 50-400W | OEM ODM",
            'desc': "Fabricante de drivers LED de interior en China: 50-400W tensión constante, PFC activo, sin ventilador. OEM ODM, pedido mínimo 50 uds, garantía 3 años, CE RoHS.",
        },
        'pt': {
            'title': "Fabricante de drivers LED indoor 50-400W | OEM ODM",
            'desc': "Fabricante de drivers LED de interior na China: 50-400W tensão constante, PFC ativo, sem ventoinha. OEM ODM, pedido mínimo 50 peças, garantia 3 anos, CE RoHS.",
        },
        'ru': {
            'title': "Производитель драйверов LED 50-400 Вт | OEM ODM, MOQ 50",
            'desc': "Производитель драйверов LED в Китае: 50-400 Вт, постоянное напряжение, активный PFC, без вентилятора. OEM ODM, заказ от 50 шт, гарантия 3 года, CE RoHS.",
        },
        'fr': {
            'title': "Fabricant de drivers LED intérieurs 50-400W | OEM ODM",
            'desc': "Fabricant de drivers LED d'intérieur en Chine : 50-400W tension constante, PFC actif, sans ventilateur. OEM ODM, MOQ 50 pièces, garantie 3 ans, CE RoHS.",
        },
        'de': {
            'title': "LED-Treiber Hersteller 50-400W Innen | OEM ODM, MOQ 50",
            'desc': "LED-Treiber Hersteller in China: 50-400W Konstantspannung, aktiver PFC, lüfterlos. OEM ODM, Mindestmenge 50 Stk, 48h Burn-in, 3 Jahre Garantie, CE RoHS.",
        },
        'ar': {
            'title': "مصنع مشغلات LED داخلية 50-400 واط | OEM ODM والحد 50",
            'desc': "مصنع مشغلات LED داخلية في الصين: 50-400 واط بجهد ثابت، وPFC نشط، وبدون مروحة. OEM ODM، حد أدنى 50 قطعة، ضمان 3 سنوات، CE RoHS.",
        },
    },
    'products/ip67': {
        'en': {
            'title': "IP67 Waterproof LED Driver Manufacturer, 10-400W",
            'desc': "China IP67 waterproof LED driver manufacturer: 10-400W, fully potted, salt-spray tested, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'es': {
            'title': "Fabricante de drivers LED IP67 impermeables 10-400W",
            'desc': "Fabricante de drivers LED IP67 en China: 10-400W, encapsulado total, probado en niebla salina, 12V/24V. OEM ODM, pedido mínimo 50 uds, garantía 3 años, CE RoHS.",
        },
        'pt': {
            'title': "Fabricante de drivers LED IP67 à prova d'água 10-400W",
            'desc': "Fabricante de drivers LED IP67 na China: 10-400W, encapsulamento total, teste de névoa salina. OEM ODM, pedido mínimo 50 peças, garantia 3 anos, CE RoHS.",
        },
        'ru': {
            'title': "Производитель драйверов LED IP67, 10-400 Вт, влагозащита",
            'desc': "Производитель драйверов LED IP67 в Китае: 10-400 Вт, полная заливка, тест соляным туманом, 12/24 В. OEM ODM, заказ от 50 шт, гарантия 3 года, CE RoHS.",
        },
        'fr': {
            'title': "Fabricant de drivers LED IP67 étanches 10-400W",
            'desc': "Fabricant de drivers LED IP67 en Chine : 10-400W, entièrement enrobés, testés au brouillard salin, 12V/24V. OEM ODM, MOQ 50 pièces, garantie 3 ans, CE RoHS.",
        },
        'de': {
            'title': "IP67 LED-Treiber Hersteller, wasserdicht, 10-400W",
            'desc': "IP67 LED-Treiber Hersteller in China: 10-400W, komplett vergossen, salzsprühgeprüft. OEM ODM, Mindestmenge 50 Stk, 3 Jahre Garantie, CE RoHS.",
        },
        'ar': {
            'title': "مصنع مشغلات LED مقاومة للماء IP67 بقدرة 10-400 واط",
            'desc': "مصنع مشغلات LED مقاومة للماء IP67 في الصين: 10-400 واط، معبأة بالكامل، ومختبرة برذاذ الملح، 12/24 فولت. OEM ODM، حد أدنى 50 قطعة، ضمان 3 سنوات، CE RoHS.",
        },
    },
    'products/ip65': {
        'en': {
            'title': "IP65 Rainproof LED Driver Manufacturer, 100-600W",
            'desc': "China IP65 rainproof LED driver manufacturer for signage and billboards: 100-600W, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'es': {
            'title': "Fabricante de drivers LED IP65 anti-lluvia 100-600W",
            'desc': "Fabricante de drivers LED IP65 en China para letreros y vallas: 100-600W, 12V/24V. OEM ODM, pedido mínimo 50 uds, 48h burn-in, garantía 3 años.",
        },
        'pt': {
            'title': "Fabricante de drivers LED IP65 à prova de chuva 100-600W",
            'desc': "Fabricante de drivers LED IP65 na China para letreiros e outdoors: 100-600W, 12V/24V. OEM ODM, pedido mínimo 50 peças, 48h burn-in, garantia 3 anos.",
        },
        'ru': {
            'title': "Производитель драйверов LED IP65, 100-600 Вт, антидождь",
            'desc': "Производитель дождезащищённых драйверов LED IP65 в Китае для вывесок и билбордов: 100-600 Вт, металлокорпус, 12/24 В. OEM ODM, заказ от 50 шт, гарантия 3 года.",
        },
        'fr': {
            'title': "Fabricant de drivers LED IP65 anti-pluie 100-600W",
            'desc': "Fabricant de drivers LED IP65 en Chine pour enseignes et panneaux : 100-600W, 12V/24V. OEM ODM, commande minimum 50 pièces, garantie 3 ans.",
        },
        'de': {
            'title': "IP65 LED-Treiber Hersteller, regengeschützt, 100-600W",
            'desc': "IP65 LED-Treiber Hersteller in China für Schilder und Werbetafeln: 100-600W Metallgehäuse, 12V/24V. OEM ODM, Mindestmenge 50 Stk, 48h Burn-in, 3 Jahre Garantie.",
        },
        'ar': {
            'title': "مصنع مشغلات LED مقاومة للمطر IP65 بقدرة 100-600 واط",
            'desc': "مصنع مشغلات LED مقاومة للمطر IP65 في الصين لللافتات واللوحات: 100-600 واط، هيكل معدني، 12/24 فولت. OEM ODM، حد أدنى 50 قطعة، ضمان 3 سنوات.",
        },
    },
}

# Localized <h1> carrying the local factory-intent word
# (fabricante / fabricante / производитель / Hersteller / مصنع) + MOQ.
PAGE_H1 = {
    'products/adapters': {
        'es': "Adaptadores LED 5-200W de fábrica en China (OEM ODM, MOQ 50)",
        'pt': "Adaptadores LED 5-200W direto da fábrica na China (OEM ODM, MOQ 50)",
        'ru': "Адаптеры LED 5-200 Вт от завода в Китае (OEM ODM, MOQ 50)",
        'fr': "Adaptateurs LED 5-200W d'usine en Chine (OEM ODM, MOQ 50)",
        'de': "LED-Adapter 5-200W direkt ab Werk in China (OEM ODM, MOQ 50)",
        'ar': "محولات LED 5-200 واط من المصنع في الصين (OEM ODM، الحد الأدنى 50)",
    },
    'products/indoor': {
        'es': "Drivers LED de interior 50-400W de fábrica (OEM ODM, MOQ 50)",
        'pt': "Drivers LED de interior 50-400W direto da fábrica (OEM ODM, MOQ 50)",
        'ru': "Драйверы LED для помещений 50-400 Вт от завода (OEM ODM, MOQ 50)",
        'fr': "Drivers LED intérieurs 50-400W d'usine (OEM ODM, MOQ 50)",
        'de': "LED-Treiber Innenbereich 50-400W ab Werk (OEM ODM, MOQ 50)",
        'ar': "مشغلات LED داخلية 50-400 واط من المصنع (OEM ODM، الحد الأدنى 50)",
    },
    'products/ip67': {
        'es': "Drivers LED IP67 impermeables 10-400W de fábrica (OEM ODM)",
        'pt': "Drivers LED IP67 à prova d'água 10-400W direto da fábrica (OEM ODM)",
        'ru': "Водонепроницаемые драйверы LED IP67 10-400 Вт от завода (OEM ODM)",
        'fr': "Drivers LED IP67 étanches 10-400W d'usine (OEM ODM)",
        'de': "IP67 wasserdichte LED-Treiber 10-400W ab Werk (OEM ODM)",
        'ar': "مشغلات LED مقاومة للماء IP67 بقدرة 10-400 واط من المصنع (OEM ODM)",
    },
    'products/ip65': {
        'es': "Drivers LED IP65 anti-lluvia 100-600W de fábrica (OEM ODM)",
        'pt': "Drivers LED IP65 à prova de chuva 100-600W direto da fábrica (OEM ODM)",
        'ru': "Дождезащищённые драйверы LED IP65 100-600 Вт от завода (OEM ODM)",
        'fr': "Drivers LED IP65 anti-pluie 100-600W d'usine (OEM ODM)",
        'de': "IP65 regengeschützte LED-Treiber 100-600W ab Werk (OEM ODM)",
        'ar': "مشغلات LED مقاومة للمطر IP65 بقدرة 100-600 واط من المصنع (OEM ODM)",
    },
}

# Recurring <h2> strings that appear on several pages.
SITE_HEADINGS = {
    "OEM and ODM": {
        'es': "OEM y ODM: drivers LED a medida desde fábrica",
        'pt': "OEM e ODM: drivers LED sob medida direto da fábrica",
        'ru': "OEM и ODM: драйверы LED по вашему ТЗ от завода",
        'fr': "OEM et ODM : drivers LED sur mesure depuis l'usine",
        'de': "OEM und ODM: maßgeschneiderte LED-Treiber ab Werk",
        'ar': "OEM وODM: مشغلات LED حسب الطلب من المصنع",
    },
    "Why buy factory direct": {
        'es': "Por qué comprar directo de fábrica (fabricante China, MOQ 50)",
        'pt': "Por que comprar direto da fábrica (fabricante China, MOQ 50)",
        'ru': "Почему покупать напрямую с завода (производитель, MOQ 50)",
        'fr': "Pourquoi acheter directement à l'usine (fabricant, MOQ 50)",
        'de': "Warum direkt ab Werk kaufen (Hersteller China, MOQ 50)",
        'ar': "لماذا تشتري مباشرة من المصنع (مصنّع في الصين، الحد الأدنى 50)",
    },
    "What is the minimum order quantity?": {
        'es': "¿Cuál es el pedido mínimo? (MOQ 50 unidades)",
        'pt': "Qual é o pedido mínimo? (MOQ 50 peças)",
        'ru': "Какой минимальный заказ? (MOQ 50 шт)",
        'fr': "Quelle est la commande minimum ? (MOQ 50 pièces)",
        'de': "Wie hoch ist die Mindestbestellmenge? (MOQ 50 Stk)",
        'ar': "ما هو الحد الأدنى للطلب؟ (50 قطعة)",
    },
}


def apply_heading_overrides(html, page, lang):
    """Rewrite the page <h1> and known <h2> strings with buyer-intent copy.

    Applied after apply_translations() (so the document is already unescaped)
    and before the breadcrumb schema is derived, so the structured data name
    matches the visible heading.
    """
    # 1. per-page H1
    local = PAGE_H1.get(page, {}).get(lang)
    if local:
        html = re.sub(r'(<h1[^>]*>).*?(</h1>)', lambda m: m.group(1) + local + m.group(2),
                      html, count=1, flags=re.S)
    # 2. recurring H2s shared across pages
    for en, pack in SITE_HEADINGS.items():
        tr = pack.get(lang)
        if not tr:
            continue
        html = re.sub(r'(<h2[^>]*>)' + re.escape(en) + r'(</h2>)',
                      lambda m: m.group(1) + tr + m.group(2), html, count=1)
    return html
