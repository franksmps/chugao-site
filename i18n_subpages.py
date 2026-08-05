# -*- coding: utf-8 -*-
"""Subpage body translations for chugao-site.

The homepage localizes at runtime via main.js T dict (all 11 langs present).
The subpages (about / faq / certs / products/*) have hardcoded English body
text that build_i18n.py copies verbatim into every language folder. This module
provides per-language phrase replacements so each language gets a static,
SEO-friendly translated body.

Keys are EXACT English substrings as they appear in the built HTML. Phrases not
found are left in English (graceful fallback). Translation is a machine draft for
human review.
"""

# The 6 priority market languages (es/pt/ar/ru/fr/de). en/zh already localized.
TARGET_LANGS = ["es", "pt", "ar", "ru", "fr", "de"]

SUBTR = {
    "es": {
        # ---------- Titles (also cover og:title / twitter:title / JSON-LD name) ----------
        "About CHUGAO - LED power supply factory, Zhongshan China": "Acerca de CHUGAO - f\u00e1brica de fuentes de alimentaci\u00f3n LED, Zhongshan China",
        "FAQ - CHUGAO LED power supply questions answered": "Preguntas frecuentes - respuestas sobre fuentes de alimentaci\u00f3n LED CHUGAO",
        "Certifications - CE, RoHS, UL, BIS for CHUGAO LED drivers": "Certificaciones - CE, RoHS, UL, BIS para controladores LED CHUGAO",
        "LED Adapters (5-200W) - CHUGAO LED power supply": "Adaptadores LED (5-200W) - CHUGAO fuentes de alimentaci\u00f3n LED",
        "Indoor LED Drivers (50-400W) - CHUGAO LED power supply": "Controladores LED de interior (50-400W) - CHUGAO fuentes de alimentaci\u00f3n LED",
        "IP67 Waterproof LED Drivers (10-400W) - CHUGAO LED power supply": "Controladores LED impermeables IP67 (10-400W) - CHUGAO fuentes de alimentaci\u00f3n LED",
        "IP65 Rainproof LED Drivers (100-600W) - CHUGAO LED power supply": "Controladores LED resistentes a la lluvia IP65 (100-600W) - CHUGAO fuentes de alimentaci\u00f3n LED",
        # ---------- About ----------
        "About CHUGAO": "Acerca de CHUGAO",
        "Zhongshan Chugao Electronic Technology Co., Ltd. makes LED switching power supplies in a 6,000 m\u00b2 factory in Guzhen, Zhongshan \u2014 the lighting manufacturing hub of China. We run 38 people on the floor and 8 in sales, shipping to 42 countries across Europe, North America, the Middle East, and Southeast Asia.": "Zhongshan Chugao Electronic Technology Co., Ltd. fabrica fuentes de alimentaci\u00f3n conmutadas LED en una f\u00e1brica de 6.000 m\u00b2 en Guzhen, Zhongshan \u2014 la capital de la iluminaci\u00f3n de China. Contamos con 38 personas en planta y 8 en ventas, enviando a 42 pa\u00edses de Europa, Norteam\u00e9rica, Oriente Medio y el sudeste asi\u00e1tico.",
        "m\u00b2 Factory": "m\u00b2 F\u00e1brica",
        "Guzhen, Zhongshan \u2014 China's lighting capital, with the full supply chain next door.": "Guzhen, Zhongshan \u2014 la capital de la iluminaci\u00f3n de China, con toda la cadena de suministro al lado.",
        "Floor staff": "Personal de planta",
        "Skilled SMT, wave-soldering, potting and QC operators on four dedicated lines.": "Operarios cualificados de SMT, soldadura por ola, encapsulado y control de calidad en cuatro l\u00edneas dedicadas.",
        "Countries": "Pa\u00edses",
        "Distributors, brands and contractors across Europe, North America, the Middle East and SE Asia.": "Distribuidores, marcas y contratistas en Europa, Norteam\u00e9rica, Oriente Medio y el sudeste asi\u00e1tico.",
        "Trading since": "Comercializando desde",
        "Over 15 years building LED drivers and AC/DC adapters for global buyers.": "M\u00e1s de 15 a\u00f1os fabricando controladores LED y adaptadores AC/DC para compradores de todo el mundo.",
        "Product lines": "L\u00edneas de productos",
        "Adapters, indoor drivers, IP67 and IP65 \u2014 one stop for low-voltage LED power.": "Adaptadores, controladores de interior, IP67 e IP65 \u2014 un solo proveedor para la alimentaci\u00f3n LED de baja tensi\u00f3n.",
        "Burn-in": "Burn-in",
        "Every unit runs a 48-hour full-load burn-in before it is packed and shipped.": "Cada unidad pasa 48 horas de burn-in a plena carga antes de empacarse y enviarse.",
        "What we make": "Qu\u00e9 fabricamos",
        "Four product lines cover most low-voltage LED jobs: AC/DC adapters (5-200W), indoor LED drivers (50-400W), IP67 waterproof drivers (10-400W), and IP65 rainproof drivers (100-600W). Together they run everything from a short strip behind a shelf to a weatherproof sign outside a shop.": "Cuatro l\u00edneas de productos cubren la mayor\u00eda de trabajos LED de baja tensi\u00f3n: adaptadores AC/DC (5-200W), controladores de interior (50-400W), controladores impermeables IP67 (10-400W) y controladores resistentes a la lluvia IP65 (100-600W). En conjunto alimentan desde una tira corta detr\u00e1s de un estante hasta un letrero impermeable frente a una tienda.",
        "Every unit passes 48 hours of burn-in before it ships, and carries CE and RoHS as standard. UL and BIS are available per model for the North American and Indian markets.": "Cada unidad pasa 48 horas de burn-in antes de enviarse y lleva CE y RoHS de serie. UL y BIS est\u00e1n disponibles por modelo para los mercados de Norteam\u00e9rica y la India.",
        "Manufacturing & quality control": "Fabricaci\u00f3n y control de calidad",
        "Production runs on four dedicated lines fed by SMT assembly and wave soldering, then finished on in-house potting and enclosure lines. Each driver moves through incoming component inspection and automated ICT, then a 48-hour full-load burn-in at elevated temperature before it is packed. On the line we check output voltage, ripple, efficiency, and the four protective functions \u2014 over-voltage, over-current, over-temperature, and short-circuit \u2014 so a weak unit is caught before it reaches you.": "La producci\u00f3n funciona en cuatro l\u00edneas dedicadas alimentadas por ensamblaje SMT y soldadura por ola, y se termina en l\u00edneas propias de encapsulado y carcasa. Cada controlador pasa por inspecci\u00f3n de componentes y TIC automatizado, y luego 48 horas de burn-in a plena carga y alta temperatura antes de empacarse. En l\u00ednea verificamos voltaje de salida, rizado, eficiencia y las cuatro protecciones \u2014 sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito \u2014 para detectar una unidad d\u00e9bil antes de que llegue a usted.",
        "Automated assembly": "Ensamblaje automatizado",
        "Surface-mount and wave soldering with automated optical and in-circuit inspection.": "Montaje superficial y soldadura por ola con inspecci\u00f3n \u00f3ptica e in-circuito automatizada.",
        "In-circuit test": "Prueba in-circuit",
        "Every board is tested for shorts, opens and component values before potting.": "Cada placa se prueba en cortos, abiertos y valores de componentes antes del encapsulado.",
        "Full-load burn-in": "Burn-in a plena carga",
        "Units run at full load in a hot chamber so early failures show up before shipping.": "Las unidades funcionan a plena carga en una c\u00e1mara caliente para que las fallas tempranas aparezcan antes del env\u00edo.",
        "Four protections": "Cuatro protecciones",
        "Over-voltage, over-current, over-temperature and short-circuit protection on every model.": "Protecci\u00f3n contra sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito en cada modelo.",
        "Engineering & customization": "Ingenier\u00eda y personalizaci\u00f3n",
        "Our engineering team supports OEM and ODM changes to output voltage, enclosure size, connector type, and cable length. Where a project calls for it, we can add dimming control (0-10V or PWM) or adjust the input range. Custom samples are built from your spec sheet and verified against the same test routine used in mass production, so what you approve is what ships.": "Nuestro equipo de ingenier\u00eda apoya cambios OEM y ODM de voltaje de salida, tama\u00f1o de carcasa, tipo de conector y longitud de cable. Cuando el proyecto lo requiere, podemos a\u00f1adir control de atenuaci\u00f3n (0-10V o PWM) o ajustar el rango de entrada. Las muestras personalizadas se construyen seg\u00fan su hoja de especificaciones y se verifican con la misma rutina de pruebas de la producci\u00f3n en serie, para que lo que aprueba es lo que se env\u00eda.",
        "Global markets & support": "Mercados globales y soporte",
        "We supply distributors, lighting brands, and project contractors in 42 countries, with the strongest presence in Europe, North America, the Middle East, and Southeast Asia. Sales and engineering reply in English, Spanish, French, Russian, Arabic, and Chinese, and aim to respond within 1 hour during China business hours (GMT+8).": "Suministramos a distribuidores, marcas de iluminaci\u00f3n y contratistas de proyectos en 42 pa\u00edses, con mayor presencia en Europa, Norteam\u00e9rica, Oriente Medio y el sudeste asi\u00e1tico. Ventas e ingenier\u00eda responden en ingl\u00e9s, espa\u00f1ol, franc\u00e9s, ruso, \u00e1rabe y chino, y buscan responder en 1 hora dentro del horario comercial de China (GMT+8).",
        "OEM and ODM": "OEM y ODM",
        "We build custom drivers for clients in Germany, Brazil, and Saudi Arabia. The minimum is 500 pcs for custom tooling, and tooling is free on repeat orders over 2,000 pcs. Send us your spec sheet and we return a quote, a sample lead time, and the certification plan for your target market.": "Fabricamos controladores personalizados para clientes en Alemania, Brasil y Arabia Saudita. El m\u00ednimo es 500 uds. para herramental personalizado, y el herramental es gratis en pedidos repetidos de m\u00e1s de 2.000 uds. Env\u00edenos su hoja de especificaciones y le devolvemos una cotizaci\u00f3n, un tiempo de muestra y el plan de certificaci\u00f3n para su mercado objetivo.",
        "Why buy factory direct": "Por qu\u00e9 comprar directo de f\u00e1brica",
        "Buying from the manufacturer removes the trader margin and shortens the path from a design change to shipment. You can also request the exact certificate package your market needs instead of a generic one. Every shipment includes a commercial invoice, packing list, certificate of origin, and CE/RoHS reports, with original documents shipped with the goods.": "Comprar al fabricante elimina el margen del intermediario y acorta el camino desde un cambio de dise\u00f1o hasta el env\u00edo. Tambi\u00e9n puede solicitar el paquete de certificados exacto que su mercado necesita en lugar de uno gen\u00e9rico. Cada env\u00edo incluye factura comercial, lista de empaque, certificado de origen e informes CE/RoHS, con documentos originales enviados con la mercanc\u00eda.",
        "Need a quote or certificate plan?": "\u00bfNecesita una cotizaci\u00f3n o un plan de certificaci\u00f3n?",
        "Tell us your market and model \u2014 we reply within 1 hour in China business hours.": "D\u00edganos su mercado y modelo \u2014 respondemos en 1 hora dentro del horario comercial de China.",
        "Contact sales": "Contacte a ventas",
        # ---------- FAQ ----------
        "Frequently asked questions": "Preguntas frecuentes",
        "Plain answers about orders, certification, and product selection.": "Respuestas claras sobre pedidos, certificaci\u00f3n y selecci\u00f3n de productos.",
        "What is the minimum order quantity?": "\u00bfCu\u00e1l es la cantidad m\u00ednima de pedido?",
        "50 pieces per model for stock items. 500 pieces for custom OEM. We do not accept 1-piece orders.": "50 unidades por modelo para art\u00edculos en stock. 500 unidades para OEM personalizado. No aceptamos pedidos de 1 unidad.",
        "What certifications do you have?": "\u00bfQu\u00e9 certificaciones tienen?",
        "CE and RoHS on every model. UL is per model and costs extra. We send certificate PDFs before you order. BIS for India is available on request.": "CE y RoHS en cada modelo. UL es por modelo y tiene costo adicional. Enviamos los PDF de certificados antes de pedir. BIS para la India est\u00e1 disponible a petici\u00f3n.",
        "What is the warranty?": "\u00bfCu\u00e1l es la garant\u00eda?",
        "3 years on stock items. OEM warranty is defined in the contract. Warranty does not cover lightning, water damage, or incorrect wiring.": "3 a\u00f1os en art\u00edculos en stock. La garant\u00eda OEM se define en el contrato. La garant\u00eda no cubre rayos, da\u00f1os por agua ni cableado incorrecto.",
        "Do you do OEM?": "\u00bfHacen OEM?",
        "Yes. Minimum 500 pcs. Send us your spec sheet. Tooling is charged on the first order and free on repeat orders over 2,000 pcs.": "S\u00ed. M\u00ednimo 500 uds. Env\u00edennos su hoja de especificaciones. El herramental se cobra en el primer pedido y es gratis en pedidos repetidos de m\u00e1s de 2.000 uds.",
        "What are the payment terms?": "\u00bfCu\u00e1les son las condiciones de pago?",
        "New customers: 30% T/T deposit, 70% before shipment. After 3 orders we can discuss L/C. We do not accept credit cards for bulk orders.": "Clientes nuevos: 30% de dep\u00f3sito T/T, 70% antes del env\u00edo. Tras 3 pedidos podemos hablar de L/C. No aceptamos tarjetas de cr\u00e9dito para pedidos al por mayor.",
        "What is the lead time?": "\u00bfCu\u00e1l es el tiempo de entrega?",
        "Stock: 3-7 days. OEM: 25-30 days. Samples: 5 days, charged plus shipping, refunded on a bulk order.": "Stock: 3-7 d\u00edas. OEM: 25-30 d\u00edas. Muestras: 5 d\u00edas, se cobran m\u00e1s env\u00edo, se reembolsan en un pedido al por mayor.",
        "Which input voltages do your drivers support?": "\u00bfQu\u00e9 voltajes de entrada soportan sus controladores?",
        "Adapters accept 100-240V AC universal. Indoor drivers are 190-264V AC; IP67 are 190-340V AC; IP65 are 190-264V AC. Confirm the range for your market.": "Los adaptadores aceptan 100-240V AC universal. Los controladores de interior son 190-264V AC; IP67 son 190-340V AC; IP65 son 190-264V AC. Confirme el rango para su mercado.",
        "How do I choose IP20, IP65, or IP67?": "\u00bfC\u00f3mo elijo IP20, IP65 o IP67?",
        "IP20 for indoor dry locations. IP65 for semi-outdoor with rain and dust. IP67 for full outdoor and wet environments such as fountains and marine lighting.": "IP20 para interiores secos. IP65 para semi-exterior con lluvia y polvo. IP67 para exterior completo y ambientes h\u00famedos como fuentes y iluminaci\u00f3n marina.",
        "Still have a question?": "\u00bfA\u00fan tiene una pregunta?",
        "Contact our sales team": "Contacte a nuestro equipo de ventas",
        # ---------- Certs ----------
        "Certifications & compliance": "Certificaciones y cumplimiento",
        "Every CHUGAO model ships with the documentation your market requires. Certificate PDFs are sent before you place an order, so you can clear customs and meet local electrical rules without surprises.": "Cada modelo CHUGAO se env\u00eda con la documentaci\u00f3n que su mercado exige. Los PDF de certificados se env\u00edan antes de hacer el pedido, para despachar aduanas y cumplir las normas el\u00e9ctricas locales sin sorpresas.",
        "CE & RoHS (standard on every model)": "CE y RoHS (est\u00e1ndar en cada modelo)",
        "CE marking and RoHS compliance are standard on every unit. Our LED drivers are assessed against the EU directives that apply to lighting power supplies - the Low Voltage Directive and the EMC Directive - and RoHS confirms that restricted substances stay below the allowed limits. The test report and Declaration of Conformity are available on request.": "El marcado CE y el cumplimiento RoHS son est\u00e1ndar en cada unidad. Nuestros controladores LED se eval\u00faan seg\u00fan las directivas de la UE aplicables a fuentes de alimentaci\u00f3n de iluminaci\u00f3n \u2014 la Directiva de Baja Tensi\u00f3n y la Directiva EMC \u2014 y RoHS confirma que las sustancias restringidas est\u00e1n por debajo de los l\u00edmites permitidos. El informe de prueba y la Declaraci\u00f3n de Conformidad est\u00e1n disponibles a petici\u00f3n.",
        "UL": "UL",
        "UL certification is handled per model and takes 4-6 weeks from order confirmation. We start the application once you confirm the model and quantity, and we keep you updated on the file status. UL is typically required for the North American market.": "La certificaci\u00f3n UL se gestiona por modelo y tarda 4-6 semanas desde la confirmaci\u00f3n del pedido. Iniciamos la solicitud una vez que confirma modelo y cantidad, y le informamos del estado del expediente. UL suele requerirse para el mercado de Norteam\u00e9rica.",
        "BIS (India)": "BIS (India)",
        "BIS certification for the India market is available on request for selected models. Tell us your target models and we confirm lead time and cost. Plan this early, because BIS registration runs in parallel with production rather than after it.": "La certificaci\u00f3n BIS para el mercado de la India est\u00e1 disponible a petici\u00f3n para modelos seleccionados. D\u00edganos sus modelos objetivo y confirmamos tiempo y costo. Planif\u00edquelo pronto, porque el registro BIS corre en paralelo con la producci\u00f3n y no despu\u00e9s.",
        "What we send with each shipment": "Qu\u00e9 enviamos con cada pedido",
        "Commercial invoice and packing list": "Factura comercial y lista de empaque",
        "Certificate of origin": "Certificado de origen",
        "CE and RoHS test reports / Declaration of Conformity": "Informes de prueba CE y RoHS / Declaraci\u00f3n de Conformidad",
        "UL file reference where applicable": "Referencia de expediente UL cuando aplique",
        "Original documents ship with the goods; PDF copies are emailed before the container leaves the factory.": "Los documentos originales se env\u00edan con la mercanc\u00eda; las copias PDF se env\u00edan por correo antes de que el contenedor salga de la f\u00e1brica.",
        "Need a specific certificate?": "\u00bfNecesita un certificado espec\u00edfico?",
        "Standards and proof requirements differ by country. Tell us the destination market and the model you plan to import, and we will confirm which certificate applies and how long it takes. See the": "Las normas y requisitos de comprobaci\u00f3n difieren seg\u00fan el pa\u00eds. D\u00edganos el mercado de destino y el modelo que planea importar, y confirmaremos qu\u00e9 certificado aplica y cu\u00e1nto tarda. Vea las",
        "for lead times and minimum order quantities, or": "para tiempos de entrega y cantidades m\u00ednimas de pedido, o",
        "contact sales": "contacte a ventas",
        "for a quote.": "para una cotizaci\u00f3n.",
        # ---------- Product pages: shared ----------
        "Overview": "Resumen",
        "Power range:": "Rango de potencia:",
        "Protection:": "Protecci\u00f3n:",
        "Input:": "Entrada:",
        "Output:": "Salida:",
        "Specifications": "Especificaciones",
        "Parameter": "Par\u00e1metro",
        "Detail": "Detalle",
        "Ingress protection": "Protecci\u00f3n de ingreso",
        "Input voltage": "Voltaje de entrada",
        "Output voltage": "Voltaje de salida",
        "Key features": "Caracter\u00edsticas clave",
        "Wide input": "Entrada amplia",
        "one SKU covers most international sites.": "un solo SKU cubre la mayor\u00eda de instalaciones internacionales.",
        "Dual output": "Salida doble",
        "options fit the common LED strips and modules.": "opciones para las tiras y m\u00f3dulos LED comunes.",
        "Four protections": "Cuatro protecciones",
        "Over-voltage, over-current, over-temperature and short-circuit.": "Sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito.",
        "Certified": "Certificado",
        "CE and RoHS standard; UL / BIS available per model.": "CE y RoHS de serie; UL / BIS disponibles por modelo.",
        "Related reading": "Lecturas relacionadas",
        "Other CHUGAO product lines": "Otras l\u00edneas de productos CHUGAO",
        "View specifications &rarr;": "Ver especificaciones &rarr;",
        "Get a quote for": "Solicitar cotizaci\u00f3n para",
        "View all products": "Ver todos los productos",
        # ---------- Product pages: adapters ----------
        "LED Adapters (5-200W)": "Adaptadores LED (5-200W)",
        "AC/DC adapters for LED strips and modules, 5W-200W, 100-240V input.": "Adaptadores AC/DC para tiras y m\u00f3dulos LED, 5W-200W, entrada 100-240V.",
        "Compact AC/DC adapters for LED strips, modules, and signage. CE/UL available, 3-year warranty.": "Adaptadores AC/DC compactos para tiras, m\u00f3dulos y letreros LED. CE/UL disponibles, garant\u00eda de 3 a\u00f1os.",
        "Where adapters are used": "D\u00f3nde se usan los adaptadores",
        "AC/DC adapters power 12V and 24V LED strips, LED modules, edge-lit signs, and small fixtures that plug into a wall outlet. The 100-240V universal input means one SKU ships worldwide - you only change the local plug or cord.": "Los adaptadores AC/DC alimentan tiras y m\u00f3dulos LED de 12V y 24V, m\u00f3dulos de borde y peque\u00f1os accesorios conectados a la red. La entrada universal 100-240V significa que un solo SKU se env\u00eda a todo el mundo: s\u00f3lo cambia el enchufe o cable local.",
        "How to size an adapter": "C\u00f3mo dimensionar un adaptador",
        "Add up the wattage of every LED you will run, then add a 20% margin so the adapter runs below its rated load. For example, 80W of strips needs at least a 100W adapter. Running below 80% load keeps the adapter cooler and extends its life.": "Sume la potencia de cada LED que usar\u00e1 y a\u00f1ada un margen del 20% para que el adaptador trabaje por debajo de su carga nominal. Por ejemplo, 80W de tiras requieren al menos un adaptador de 100W. Trabajar por debajo del 80% de carga mantiene el adaptador m\u00e1s fresco y alarga su vida.",
        "What is built in": "Qu\u00e9 incluye",
        "Each adapter has over-voltage, over-current, over-temperature, and short-circuit protection. Output options of 12V, 24V, 36V, and 48V cover most LED strips and modules.": "Cada adaptador tiene protecci\u00f3n contra sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito. Las opciones de salida de 12V, 24V, 36V y 48V cubren la mayor\u00eda de tiras y m\u00f3dulos LED.",
        # ---------- Product pages: indoor ----------
        "Indoor LED Drivers (50-400W)": "Controladores LED de interior (50-400W)",
        "Built-in PFC indoor LED drivers, 50W-400W, for ceiling and panel lights.": "Controladores de interior con PFC integrado, 50W-400W, para luces de techo y paneles.",
        "Indoor LED drivers for ceiling lights and panel lights. High efficiency with active power-factor correction.": "Controladores LED de interior para luces de techo y paneles. Alta eficiencia con correcci\u00f3n activa del factor de potencia.",
        "Where indoor drivers are used": "D\u00f3nde se usan los controladores de interior",
        "Indoor drivers feed ceiling lights, panel lights, troffers, and linear fixtures inside buildings. Built-in active PFC keeps the power factor high, which matters on commercial projects that put many fittings on one circuit.": "Los controladores de interior alimentan luces de techo, paneles, troffers y fijaciones lineales dentro de edificios. El PFC activo integrado mantiene alto el factor de potencia, lo que importa en proyectos comerciales que ponen muchas luminarias en un mismo circuito.",
        "How to size an indoor driver": "C\u00f3mo dimensionar un controlador de interior",
        "Match the driver wattage to the total LED load plus a 20% margin, and confirm the output voltage (usually 12V or 24V DC) matches the fixture. For dimming projects, tell us the control type so we spec the right model.": "Iguale la potencia del controlador a la carga LED total m\u00e1s un margen del 20%, y confirme que el voltaje de salida (normalmente 12V o 24V DC) coincide con la luminaria. Para proyectos de atenuaci\u00f3n, ind\u00edquenos el tipo de control para especificar el modelo correcto.",
        "Active PFC, fan-less silent operation, and protection against over-voltage, over-current, over-temperature, and short-circuit. The IP20 enclosure is for dry indoor locations only.": "PFC activo, funcionamiento silencioso sin ventilador, y protecci\u00f3n contra sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito. La caja IP20 es s\u00f3lo para interiores secos.",
        # ---------- Product pages: ip67 ----------
        "IP67 Waterproof LED Drivers (10-400W)": "Controladores LED impermeables IP67 (10-400W)",
        "Fully potted IP67/IP68 waterproof LED drivers, 10W-400W, for outdoor and wet use.": "Controladores IP67/IP68 totalmente encapsulados, 10W-400W, para exterior y humedad.",
        "Waterproof drivers for outdoor LED strips, fountains, and marine lighting. Built to survive wet environments.": "Controladores impermeables para tiras LED exteriores, fuentes e iluminaci\u00f3n marina. Hechos para ambientes h\u00famedos.",
        "Where IP67 drivers are used": "D\u00f3nde se usan los controladores IP67",
        "IP67 and IP68 drivers go where water is. Use them for outdoor LED strips, garden and landscape lighting, fountains, pools, and marine or coastal installs. The fully sealed silicone potting blocks water and salt spray.": "Los controladores IP67 e IP68 van donde hay agua. \u00daselos para tiras LED exteriores, jardines e iluminaci\u00f3n de paisaje, fuentes, piscinas e instalaciones marinas o costeras. El encapsulado de silicona bloquea el agua y la sal.",
        "How to size a waterproof driver": "C\u00f3mo dimensionar un controlador impermeable",
        "Total the LED load, add a 20% margin, and pick a model rated above that sum. For hot environments or sealed enclosures, leave extra headroom so the driver runs cool. The 190-340V input covers most international sites.": "Sume la carga LED, a\u00f1ada un margen del 20% y elija un modelo por encima de esa suma. Para ambientes calurosos o cajas selladas, deje margen extra para que el controlador trabaje fresco. La entrada 190-340V cubre la mayor\u00eda de instalaciones internacionales.",
        "Sealed potting, salt-spray resistance, and over-voltage, over-current, over-temperature, and short-circuit protection. Rated for full outdoor and wet use - not for permanent submersion unless the model is marked IP68.": "Encapsulado, resistencia a la sal, y protecci\u00f3n contra sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito. Calificado para exterior h\u00famedo; no para inmersi\u00f3n permanente salvo que el modelo indique IP68.",
        # ---------- Product pages: ip65 ----------
        "IP65 Rainproof LED Drivers (100-600W)": "Controladores LED resistentes a la lluvia IP65 (100-600W)",
        "Metal-case IP65 rainproof LED drivers, 100W-600W, for signage and semi-outdoor.": "Controladores IP65 de caja met\u00e1lica, 100W-600W, para letreros y semi-exterior.",
        "Rainproof drivers for signage, billboards, and semi-outdoor installations. Metal housing with ventilation.": "Controladores resistentes a la lluvia para letreros, vallas e instalaciones semi-exteriores. Caja met\u00e1lica con ventilaci\u00f3n.",
        "Where IP65 drivers are used": "D\u00f3nde se usan los controladores IP65",
        "IP65 rainproof drivers suit signage, billboards, channel letters, and semi-outdoor installs that face rain and dust but not direct water jets. The metal case with mesh vents sheds heat while keeping weather out.": "Los controladores IP65 resisten lluvia son ideales para letreros, vallas, letras canalizadas e instalaciones semi-exteriores expuestas a lluvia y polvo pero no a chorros de agua directos. La caja met\u00e1lica con rejillas ventila mientras mantiene el clima afuera.",
        "How to size a rainproof driver": "C\u00f3mo dimensionar un controlador resistente a la lluvia",
        "Add the wattage of all connected signs, add a 20% margin, and choose a model above that total. The 190-264V input covers standard commercial mains. Mount the case where air can flow through the vents.": "Sume la potencia de todos los letreros conectados, a\u00f1ada un margen del 20% y elija un modelo por encima del total. La entrada 190-264V cubre la red comercial est\u00e1ndar. Monte la caja donde el aire pueda fluir por las rejillas.",
        "Corrosion-resistant metal case, ventilation for high-power runs, and over-voltage, over-current, over-temperature, and short-circuit protection. For full outdoor wet use, choose the IP67 line instead.": "Caja met\u00e1lica resistente a la corrosi\u00f3n, ventilaci\u00f3n para ejecuciones de alta potencia, y protecci\u00f3n contra sobretensi\u00f3n, sobrecorriente, sobretemperatura y cortocircuito. Para uso exterior h\u00famedo completo, elija la l\u00ednea IP67.",
        # ---------- Footer links (hardcoded in template, not data-i18n) ----------
        '<a href="/products/adapters/">Adapters</a>': '<a href="/products/adapters/">Adaptadores</a>',
        '<a href="/products/indoor/">Indoor drivers</a>': '<a href="/products/indoor/">Controladores de interior</a>',
        '<a href="/products/ip67/">IP67 waterproof</a>': '<a href="/products/ip67/">IP67 impermeables</a>',
        '<a href="/products/ip65/">IP65 rainproof</a>': '<a href="/products/ip65/">IP65 resistentes a la lluvia</a>',
        '<a href="/about/">About</a>': '<a href="/about/">Acerca de</a>',
        '<a href="/certs/">Certifications</a>': '<a href="/certs/">Certificaciones</a>',
        '<a href="/faq/">FAQ</a>': '<a href="/faq/">Preguntas frecuentes</a>',
        '<a href="/#contact">Contact</a>': '<a href="/#contact">Contacto</a>',
        '<a href="mailto:info@chugaopower.com">Email</a>': '<a href="mailto:info@chugaopower.com">Correo</a>',
        '<a href="https://wa.me/8618933373873" target="_blank" rel="noopener noreferrer">WhatsApp</a>': '<a href="https://wa.me/8618933373873" target="_blank" rel="noopener noreferrer">WhatsApp</a>',
        'All Rights Reserved.</p>': 'Todos los derechos reservados.</p>',
        # ---------- Product spec lines (gen_pages product_page 4th arg) ----------
        "Wall-mount and desktop, AC 100-240V universal input, DC 12/24/36/48V output": "Montaje en pared y de escritorio, entrada AC 100-240V universal, salida DC 12/24/36/48V",
        "Built-in active PFC, fan-less silent operation": "PFC activo integrado, funcionamiento silencioso sin ventilador",
        "Fully sealed silicone potting, salt-spray tested": "Encapsulado de silicona totalmente sellado, probado contra salpicaduras de sal",
        "Metal case with mesh vents, corrosion resistant": "Caja metálica con rejillas de ventilación, resistente a la corrosión",
        # ---------- FAQ / certs CTA ----------
        " - we reply within 1 hour during China business hours.": " - respondemos en 1 hora dentro del horario comercial de China.",
        "— we reply within 1 hour in China business hours.": "— respondemos en 1 hora dentro del horario comercial de China.",
    },
    # pt, ar, ru, fr, de to be filled in subsequent steps.
    "pt": {},
    "ar": {},
    "ru": {},
    "fr": {},
    "de": {},
}


def apply_translations(html, lang):
    """Replace known English phrases with the target language translation.

    The source templates use HTML entities (m&sup2;, &mdash;, &amp;). We unescape
    the HTML once so entity forms and Unicode form match the translation keys,
    then perform substring replacement. Untranslated fragments stay in English.
    """
    import html as _html
    pack = SUBTR.get(lang)
    if not pack:
        return html
    h = _html.unescape(html)
    for en, tr in pack.items():
        if en and en in h:
            h = h.replace(en, tr)
    return h
