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

Languages covered: all 11 public languages. en + zh + the 6 SUBTR market
languages (es/pt/ru/fr/de/ar) + ja/ko/it. The latter three are AI translations
pending native review, but their titles/descriptions are localized like the
others (the inner-page body is translated in SUBTR for every language).
"""
import re
from sku_meta import SKU_META

# (page key as build_i18n sees it, i.e. rel_html without the .html suffix)
PAGE_META = {
    'products/adapters': {
        'en': {
            'title': "LED Adapter Manufacturer 5-200W | OEM ODM, MOQ 50 pcs",
            'desc': "China LED adapter manufacturer: 5-200W 12V/24V AC/DC adapters for strips, modules and signage. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'zh': {
            'title': "LED 适配器厂家 5-200W | OEM ODM，起订 50 台",
            'desc': "中国 LED 适配器厂家：5-200W、12V/24V AC/DC 适配器，适用于灯带、模组与标识。OEM ODM，50 台起订，48 小时老化，3 年质保，CE RoHS。",
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
        'ja': {
            'title': "LED アダプター製造元 5-200W | OEM ODM、最小ロット 50 台",
            'desc': "中国の LED アダプター製造元：5-200W、12V/24V の AC/DC アダプター。テープライト、モジュール、サイン用。OEM ODM、最小ロット 50 台、48 時間エージング、3 年保証、CE RoHS。",
        },
        'ko': {
            'title': "LED 어댑터 제조사 5-200W | OEM ODM, MOQ 50대",
            'desc': "중국 LED 어댑터 제조사: 5-200W, 12V/24V AC/DC 어댑터. LED 스트립, 모듈, 간판용. OEM ODM, 최소 주문 50대, 48시간 에이징, 3년 보증, CE RoHS.",
        },
        'it': {
            'title': "Fabbrica di adattatori LED 5-200W | OEM ODM, MOQ 50 pz",
            'desc': "Fabbrica cinese di adattatori LED: 5-200W, adattatori AC/DC 12V/24V per strisce, moduli e insegne. OEM ODM, ordine minimo 50 pz, burn-in 48h, garanzia 3 anni, CE RoHS.",
        },
    },
    'products/indoor': {
        'en': {
            'title': "Indoor LED Driver Manufacturer 50-400W | OEM ODM MOQ 50",
            'desc': "China indoor LED driver manufacturer: 50-400W constant voltage, active PFC, fan-less. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'zh': {
            'title': "室内 LED 驱动电源厂家 50-400W | OEM ODM 起订 50 台",
            'desc': "中国室内 LED 驱动电源厂家：50-400W 恒压、主动 PFC、无风扇设计。OEM ODM，50 台起订，48 小时老化，3 年质保，CE RoHS。",
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
        'ja': {
            'title': "屋内用 LED ドライバー製造元 50-400W | OEM ODM、最小ロット 50 台",
            'desc': "中国の屋内用 LED ドライバー製造元：50-400W 定電圧、アクティブ PFC、ファンレス。OEM ODM、最小ロット 50 台、48 時間エージング、3 年保証、CE RoHS。",
        },
        'ko': {
            'title': "실내용 LED 구동장치 제조사 50-400W | OEM ODM MOQ 50대",
            'desc': "중국 실내용 LED 구동장치 제조사: 50-400W 정전압, 액티브 PFC, 팬리스. OEM ODM, 최소 주문 50대, 48시간 에이징, 3년 보증, CE RoHS.",
        },
        'it': {
            'title': "Fabbrica di driver LED da interno 50-400W | OEM ODM MOQ 50",
            'desc': "Fabbrica cinese di driver LED da interno: 50-400W a tensione costante, PFC attivo, senza ventola. OEM ODM, ordine minimo 50 pz, burn-in 48h, garanzia 3 anni, CE RoHS.",
        },
    },
    'products/ip67': {
        'en': {
            'title': "IP67 Waterproof LED Driver Manufacturer, 10-400W",
            'desc': "China IP67 waterproof LED driver manufacturer: 10-400W, fully potted, salt-spray tested, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'zh': {
            'title': "IP67 防水 LED 驱动电源厂家，10-400W",
            'desc': "中国 IP67 防水 LED 驱动电源厂家：10-400W 全灌封、盐雾测试、12V/24V。OEM ODM，50 台起订，48 小时老化，3 年质保，CE RoHS。",
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
        'ja': {
            'title': "IP67 防水 LED ドライバー製造元、10-400W",
            'desc': "中国の IP67 防水 LED ドライバー製造元：10-400W、完全ポッティング、塩水噴霧試験済み、12V/24V。OEM ODM、最小ロット 50 台、48 時間エージング、3 年保証、CE RoHS。",
        },
        'ko': {
            'title': "IP67 방수 LED 구동장치 제조사, 10-400W",
            'desc': "중국 IP67 방수 LED 구동장치 제조사: 10-400W, 완전 포팅, 염수 분무 시험, 12V/24V. OEM ODM, 최소 주문 50대, 48시간 에이징, 3년 보증, CE RoHS.",
        },
        'it': {
            'title': "Fabbrica di driver LED impermeabili IP67, 10-400W",
            'desc': "Fabbrica cinese di driver LED impermeabili IP67: 10-400W, completamente sigillati, test nebbia salina, 12V/24V. OEM ODM, ordine minimo 50 pz, burn-in 48h, garanzia 3 anni, CE RoHS.",
        },
    },
    'products/ip65': {
        'en': {
            'title': "IP65 Rainproof LED Driver Manufacturer, 100-600W",
            'desc': "China IP65 rainproof LED driver manufacturer for signage and billboards: 100-600W, 12V/24V. OEM ODM, 50 pcs MOQ, 48h burn-in, 3-year warranty, CE RoHS.",
        },
        'zh': {
            'title': "IP65 防雨 LED 驱动电源厂家，100-600W",
            'desc': "中国 IP65 防雨 LED 驱动电源厂家，适用于标识与广告牌：100-600W、12V/24V。OEM ODM，50 台起订，48 小时老化，3 年质保，CE RoHS。",
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
        'ja': {
            'title': "IP65 防雨 LED ドライバー製造元、100-600W",
            'desc': "中国の IP65 防雨 LED ドライバー製造元（サイン・看板向け）：100-600W、12V/24V。OEM ODM、最小ロット 50 台、48 時間エージング、3 年保証、CE RoHS。",
        },
        'ko': {
            'title': "IP65 방우 LED 구동장치 제조사, 100-600W",
            'desc': "중국 IP65 방우 LED 구동장치 제조사(간판·옥외 광고용): 100-600W, 12V/24V. OEM ODM, 최소 주문 50대, 48시간 에이징, 3년 보증, CE RoHS.",
        },
        'it': {
            'title': "Fabbrica di driver LED anti-pioggia IP65, 100-600W",
            'desc': "Fabbrica cinese di driver LED anti-pioggia IP65 per insegne e cartelloni: 100-600W, 12V/24V. OEM ODM, ordine minimo 50 pz, burn-in 48h, garanzia 3 anni, CE RoHS.",
        },
    },
    'products': {
        'en': {'title': "LED Power Supply Catalog | Adapters, Indoor, IP67, IP65 | CHUGAO",
               'desc': "CHUGAO LED power supply catalog: 5-200W adapters, 50-400W indoor, 10-400W IP67, 100-600W IP65. OEM ODM, MOQ 50, CE RoHS, 42 countries."},
        'zh': {'title': "LED 电源产品总览 | 适配器·室内·IP67·IP65 | CHUGAO",
               'desc': "楚高 LED 电源产品总览：5-200W 适配器、50-400W 室内驱动、10-400W IP67 与 100-600W IP65。OEM ODM，起订 50 台，CE RoHS，出口 42 国。"},
        'es': {'title': "Catálogo de fuentes LED | adaptadores, interior, IP67, IP65 | CHUGAO",
               'desc': "Catálogo de fuentes LED CHUGAO: adaptadores 5-200W, drivers interiores 50-400W, IP67 10-400W e IP65 100-600W. OEM ODM, MOQ 50, CE RoHS, exportación a 42 países."},
        'pt': {'title': "Catálogo de fontes LED | adaptadores, indoor, IP67, IP65 | CHUGAO",
               'desc': "Catálogo de fontes LED CHUGAO: adaptadores 5-200W, drivers indoor 50-400W, IP67 10-400W e IP65 100-600W. OEM ODM, MOQ 50, CE RoHS, exportação a 42 países."},
        'ru': {'title': "Каталог LED-блоков питания | адаптеры, интерьер, IP67, IP65 | CHUGAO",
               'desc': "Каталог блоков питания LED CHUGAO: адаптеры 5-200 Вт, драйверы для помещений 50-400 Вт, IP67 10-400 Вт и IP65 100-600 Вт. OEM ODM, MOQ 50, CE RoHS, экспорт в 42 страны."},
        'fr': {'title': "Catalogue d'alimentations LED | adaptateurs, intérieur, IP67, IP65 | CHUGAO",
               'desc': "Catalogue d'alimentations LED CHUGAO : adaptateurs 5-200W, drivers intérieurs 50-400W, IP67 10-400W et IP65 100-600W. OEM ODM, MOQ 50, CE RoHS, export vers 42 pays."},
        'de': {'title': "LED-Netzteile Katalog | Adapter, Innen, IP67, IP65 | CHUGAO",
               'desc': "CHUGAO Katalog LED-Netzteile: Adapter 5-200W, Innen-Treiber 50-400W, IP67 10-400W und IP65 100-600W. OEM ODM, MOQ 50, CE RoHS, Export in 42 Länder."},
        'ar': {'title': "كتالوج مزودات طاقة LED | محولات وداخلية وIP67 وIP65 | CHUGAO",
               'desc': "كتالوج مزودات طاقة LED من CHUGAO: محولات 5-200 واط، مشغلات داخلية 50-400 واط، IP67 10-400 واط وIP65 100-600 واط. OEM ODM، حد أدنى 50، CE RoHS، تصدير إلى 42 دولة."},
        'ja': {'title': "LED 電源カタログ | アダプター・室内・IP67・IP65 | CHUGAO",
               'desc': "CHUGAO の LED 電源カタログ：5-200W アダプター、50-400W 室内ドライバー、10-400W IP67、100-600W IP65。OEM ODM、最小ロット 50 台、CE RoHS、42 か国へ輸出。"},
        'ko': {'title': "LED 전원 카탈로그 | 어댑터·실내·IP67·IP65 | CHUGAO",
               'desc': "CHUGAO LED 전원 카탈로그: 5-200W 어댑터, 50-400W 실내 구동장치, 10-400W IP67, 100-600W IP65. OEM ODM, 최소 주문 50대, CE RoHS, 42개국 수출."},
        'it': {'title': "Catalogo alimentatori LED | adattatori, interni, IP67, IP65 | CHUGAO",
               'desc': "Catalogo alimentatori LED CHUGAO: adattatori 5-200W, driver da interno 50-400W, IP67 10-400W e IP65 100-600W. OEM ODM, MOQ 50, CE RoHS, export in 42 paesi."},
    },
    'oem-odm': {
        'en': {'title': "LED Driver OEM & ODM | Custom Power Supplies | CHUGAO",
               'desc': "CHUGAO makes custom LED drivers and AC/DC adapters via OEM/ODM: your voltage, enclosure, connector, cable. MOQ 500, free tooling over 2,000 pcs, CE RoHS."},
        'zh': {'title': "LED 驱动 OEM 与 ODM | 定制电源 | CHUGAO",
               'desc': "楚高按 OEM/ODM 定制 LED 驱动与 AC/DC 适配器：电压、外壳、接口与线长按您的规格。起订 500 台，复购超 2000 台免开模费，CE RoHS。"},
        'es': {'title': "Driver LED OEM y ODM | fuentes personalizadas | CHUGAO",
               'desc': "CHUGAO fabrica drivers LED y adaptadores AC/DC a medida en OEM y ODM: su tensión, caja, conector y cable. MOQ 500 uds, utillaje gratis en pedidos repetidos de 2.000+ uds, CE RoHS."},
        'pt': {'title': "Driver LED OEM e ODM | fontes personalizadas | CHUGAO",
               'desc': "CHUGAO fabrica drivers LED e adaptadores AC/DC sob medida em OEM e ODM: sua tensão, caixa, conector e cabo. MOQ 500 peças, ferramental grátis em pedidos repetidos de 2.000+ peças, CE RoHS."},
        'ru': {'title': "Драйверы LED OEM и ODM | индивидуальные блоки питания | CHUGAO",
               'desc': "CHUGAO производит драйверы LED и AC/DC адаптеры на заказ по OEM и ODM: ваше напряжение, корпус, разъём и кабель. MOQ 500 шт, бесплатная оснастка при повторных заказах от 2.000 шт, CE RoHS."},
        'fr': {'title': "Driver LED OEM et ODM | alimentations sur mesure | CHUGAO",
               'desc': "CHUGAO fabrique des drivers LED et adaptateurs AC/DC sur mesure en OEM et ODM : votre tension, boîtier, connecteur et câble. MOQ 500 pièces, outillage offert dès 2 000 pièces, CE RoHS."},
        'de': {'title': "LED-Treiber OEM und ODM | kundenspezifische Netzteile | CHUGAO",
               'desc': "CHUGAO fertigt LED-Treiber und AC/DC-Adapter als OEM/ODM nach Kundenwunsch: Ihre Spannung, Gehäuse, Stecker und Kabel. MOQ 500 Stk, Werkzeug frei ab 2.000 Stk, CE RoHS."},
        'ar': {'title': "مشغلات LED OEM وODM | مزودات طاقة مخصصة | CHUGAO",
               'desc': "CHUGAO تصنع مشغلات LED ومحولات AC/DC حسب الطلب عبر OEM وODM: جهدك وعلبتك وموصلك وكابلك. حد أدنى 500 قطعة، وتجيه مجاني عند الطلبات المتكررة فوق 2,000 قطعة، CE RoHS."},
        'ja': {'title': "LED ドライバー OEM・ODM | カスタム電源 | CHUGAO",
               'desc': "CHUGAO は OEM・ODM で LED ドライバーと AC/DC アダプターをカスタム製造：電圧・筐体・コネクタ・ケーブルは仕様通り。最小 500 台、2,000 台超の復注で金型費無料、CE RoHS。"},
        'ko': {'title': "LED 구동장치 OEM 및 ODM | 맞춤형 전원 | CHUGAO",
               'desc': "CHUGAO는 OEM·ODM으로 LED 구동장치와 AC/DC 어댑터를 맞춤 제작: 전압·케이스·커넥터·케이블은 귀사 사양대로. 최소 500대, 2,000대 이상 복주문 시 금형비 무료, CE RoHS."},
        'it': {'title': "Driver LED OEM e ODM | alimentatori su misura | CHUGAO",
               'desc': "CHUGAO produce driver LED e adattatori AC/DC su misura in OEM e ODM: la tua tensione, custodia, connettore e cavo. MOQ 500 pz, attrezzatura gratuita per ordini ripetuti oltre 2.000 pz, CE RoHS."},
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


# ---------------------------------------------------------------------------
# Description-only overrides for the three remaining inner pages.
#
# Why: about / faq / certs get their <title> translated by SUBTR (the English
# title string is a SUBTR key), but their <meta description> lives only in the
# src template, so every language was shipping the English sentence -- visible
# as an English snippet under a localized title in search results.
# Only 'desc' is supplied: no 'title' key means set_title_desc() leaves the
# SUBTR-translated title untouched.
# ---------------------------------------------------------------------------
PAGE_META.update({
    'about': {
        'en': {'desc': "CHUGAO is an LED switching power supply manufacturer in Zhongshan, China. 6,000 m2 factory, 4 product lines, CE/RoHS on every unit, OEM/ODM since 2008."},
        'zh': {'desc': "楚高是中国中山的 LED 开关电源厂家。6000 平方米工厂，4 条产品线，每台通过 CE/RoHS，2008 年起做 OEM/ODM。"},
        'es': {'desc': "CHUGAO es un fabricante de fuentes de alimentación LED en Zhongshan, China. Fábrica de 6.000 m², 4 líneas de producto, CE/RoHS en cada unidad, OEM/ODM desde 2008."},
        'pt': {'desc': "A CHUGAO é fabricante de fontes de alimentação LED em Zhongshan, China. Fábrica de 6.000 m², 4 linhas de produto, CE/RoHS em cada unidade, OEM/ODM desde 2008."},
        'ru': {'desc': "CHUGAO — производитель импульсных блоков питания для светодиодов в Чжуншане, Китай. Завод 6 000 м², 4 линейки продукции, CE/RoHS на каждом изделии, OEM/ODM с 2008 года."},
        'fr': {'desc': "CHUGAO est un fabricant d'alimentations LED à Zhongshan, en Chine. Usine de 6 000 m², 4 gammes de produits, CE/RoHS sur chaque unité, OEM/ODM depuis 2008."},
        'de': {'desc': "CHUGAO ist Hersteller von LED-Schaltnetzteilen in Zhongshan, China. 6.000 m² Werk, 4 Produktlinien, CE/RoHS an jedem Gerät, OEM/ODM seit 2008."},
        'ar': {'desc': "CHUGAO شركة مصنعة لمصادر طاقة LED في مدينة تشونغشان بالصين. مصنع بمساحة 6,000 م²، 4 خطوط إنتاج، شهادتا CE وRoHS لكل وحدة، وتصنيع OEM/ODM منذ 2008."},
        'ja': {'desc': "楚高（CHUGAO）は中国中山市の LED スイッチング電源メーカーです。6,000m² の工場、4 製品ライン、全機 CE/RoHS 対応、2008 年から OEM/ODM に対応しています。"},
        'ko': {'desc': "CHUGAO는 중국 중산에 있는 LED 스위칭 전원 공급 장치 제조업체입니다. 6,000m² 공장, 4개 제품 라인, 전 제품 CE/RoHS 인증, 2008년부터 OEM/ODM 생산."},
        'it': {'desc': "CHUGAO è un produttore di alimentatori switching LED a Zhongshan, in Cina. Fabbrica di 6.000 m², 4 linee di prodotto, CE/RoHS su ogni unità, OEM/ODM dal 2008."},
    },
    'faq': {
        'en': {'desc': "Minimum order, certifications (CE/RoHS/UL/BIS), warranty, OEM, payment terms, lead time, and how to choose IP rating for LED drivers."},
        'zh': {'desc': "起订量、认证（CE/RoHS/UL/BIS）、质保、OEM、付款方式、交期，以及 LED 驱动器防护等级怎么选。"},
        'es': {'desc': "Pedido mínimo, certificaciones (CE/RoHS/UL/BIS), garantía, OEM, condiciones de pago, plazo de entrega y cómo elegir el grado IP de un driver LED."},
        'pt': {'desc': "Pedido mínimo, certificações (CE/RoHS/UL/BIS), garantia, OEM, condições de pagamento, prazo de entrega e como escolher o grau IP de um driver LED."},
        'ru': {'desc': "Минимальный заказ, сертификаты (CE/RoHS/UL/BIS), гарантия, OEM, условия оплаты, сроки поставки и как выбрать степень защиты IP для LED-драйверов."},
        'fr': {'desc': "Commande minimale, certifications (CE/RoHS/UL/BIS), garantie, OEM, conditions de paiement, délais et comment choisir l'indice IP d'un driver LED."},
        'de': {'desc': "Mindestbestellmenge, Zertifizierungen (CE/RoHS/UL/BIS), Garantie, OEM, Zahlungsbedingungen, Lieferzeit und wie Sie die IP-Schutzart für LED-Treiber wählen."},
        'ar': {'desc': "الحد الأدنى للطلب، الشهادات (CE/RoHS/UL/BIS)، الضمان، تصنيع OEM، شروط الدفع، مدة التسليم، وكيفية اختيار درجة الحماية IP لمشغلات LED."},
        'ja': {'desc': "最小注文数量、認証（CE/RoHS/UL/BIS）、保証、OEM、支払い条件、納期、LED ドライバーの IP 等級の選び方。"},
        'ko': {'desc': "최소 주문 수량, 인증(CE/RoHS/UL/BIS), 보증, OEM, 결제 조건, 납기, LED 드라이버 IP 등급 선택 방법."},
        'it': {'desc': "Ordine minimo, certificazioni (CE/RoHS/UL/BIS), garanzia, OEM, termini di pagamento, tempi di consegna e come scegliere il grado IP di un driver LED."},
    },
    'certs': {
        'en': {'desc': "CHUGAO LED power supplies carry CE and RoHS on every model, UL per model, and BIS for India on request. Certificate PDFs provided before order."},
        'zh': {'desc': "楚高 LED 电源全系通过 CE 与 RoHS，UL 按型号申请，印度 BIS 可按需办理。下单前提供证书 PDF。"},
        'es': {'desc': "Las fuentes LED CHUGAO llevan CE y RoHS en todos los modelos, UL por modelo y BIS para India bajo pedido. PDF de certificados antes del pedido."},
        'pt': {'desc': "As fontes LED CHUGAO têm CE e RoHS em todos os modelos, UL por modelo e BIS para a Índia sob consulta. PDF dos certificados antes do pedido."},
        'ru': {'desc': "Блоки питания LED CHUGAO имеют CE и RoHS на каждой модели, UL — по модели, BIS для Индии — по запросу. PDF сертификатов предоставляем до заказа."},
        'fr': {'desc': "Les alimentations LED CHUGAO sont CE et RoHS sur tous les modèles, UL par modèle et BIS pour l'Inde sur demande. PDF des certificats avant commande."},
        'de': {'desc': "CHUGAO LED-Netzteile haben CE und RoHS bei jedem Modell, UL je Modell und BIS für Indien auf Anfrage. Zertifikats-PDFs vor der Bestellung."},
        'ar': {'desc': "مصادر طاقة LED من CHUGAO تحمل شهادتي CE وRoHS في كل طراز، وUL حسب الطراز، وBIS للهند عند الطلب. ملفات PDF للشهادات قبل الطلب."},
        'ja': {'desc': "CHUGAO の LED 電源は全機種 CE と RoHS 対応、UL は機種ごと、インド向け BIS は要望に応じて対応。ご注文前に証明書 PDF をご提出します。"},
        'ko': {'desc': "CHUGAO LED 전원장치는 모든 모델에 CE와 RoHS를 갖추고 있으며, UL은 모델별, 인도 BIS는 요청 시 대응합니다. 주문 전 인증서 PDF 제공."},
        'it': {'desc': "Gli alimentatori LED CHUGAO hanno CE e RoHS su tutti i modelli, UL per modello e BIS per l'India su richiesta. PDF dei certificati prima dell'ordine."},
    },
})

# 27 SKU spec pages, 11 languages — auto-generated in sku_meta.py by _gen_sku_meta.py.
PAGE_META.update(SKU_META)
