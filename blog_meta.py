# -*- coding: utf-8 -*-
"""P1-3: localized <title> / meta description for the Field Notes blog.

Only the 6 fully-localized SUBTR languages (es/pt/ru/fr/de/ar) are covered.
en + zh/ja/ko/it keep the English template text (consistent with their
pseudo-localized body). Consumed by build_i18n.build_page via set_title_desc.
"""
BLOG_META = {
    'blog': {
        'es': {
            'title': "Notas de Campo - Guías y análisis de fuentes de alimentación LED | CHUGAO",
            'desc': "Notas de Campo de CHUGAO: guías prácticas de fuentes LED, explicaciones de grados IP, novedades de mercado y consejos de certificación para importadores e instaladores.",
        },
        'pt': {
            'title': "Notas de Campo - Guias e análises de fontes de alimentação LED | CHUGAO",
            'desc': "Notas de Campo da CHUGAO: guias práticos de fontes LED, explicações de nível IP, novidades de mercado e dicas de certificação para importadores e instaladores.",
        },
        'ru': {
            'title': "Полевые заметки - руководства и обзоры блоков питания LED | CHUGAO",
            'desc': "Полевые заметки CHUGAO: практические руководства по блокам питания LED, разъяснение степеней защиты IP, заметки о рынке и советы по сертификации для импортёров и монтажников.",
        },
        'fr': {
            'title': "Notes de terrain - guides et analyses des alimentations LED | CHUGAO",
            'desc': "Notes de terrain CHUGAO : guides pratiques sur les alimentations LED, explications des indices IP, tendances du marché et conseils de certification pour les importateurs et installateurs.",
        },
        'de': {
            'title': "Feldbesuche - Leitfäden und Einblicke zu LED-Netzteilen | CHUGAO",
            'desc': "Feldbesuche von CHUGAO: praktische Leitfäden zu LED-Netzteilen, Erklärungen der IP-Schutzarten, Marktnotizen und Zertifizierungstipps für Importeure und Installateure.",
        },
        'ar': {
            'title': "ملاحظات ميدانية - أدلة ورؤى حول مزودات طاقة LED | CHUGAO",
            'desc': "ملاحظات ميدانية من CHUGAO: أدلة عملية حول مزودات طاقة LED، وشرح درجات الحماية IP، وملاحظات السوق ونصائح الشهادات للمستوردين والمركّبين.",
        },
    },
    'blog-1': {
        'es': {
            'title': "Elija la fuente de alimentación LED adecuada en 3 pasos | Notas de Campo CHUGAO",
            'desc': "Cómo elegir la fuente LED correcta: coincidencia de potencia, grado IP según el entorno y compatibilidad de voltaje de entrada, explicado de forma sencilla.",
        },
        'pt': {
            'title': "Escolha a fonte de alimentação LED certa em 3 passos | Notas de Campo CHUGAO",
            'desc': "Como escolher a fonte LED correta: correspondência de potência, nível IP conforme o ambiente e compatibilidade de tensão de entrada, explicado de forma simples.",
        },
        'ru': {
            'title': "Выберите подходящий блок питания LED за 3 шага | Полевые заметки CHUGAO",
            'desc': "Как выбрать правильный блок питания LED: подбор мощности, степень IP в зависимости от условий и совместимость по входному напряжению — простыми словами.",
        },
        'fr': {
            'title': "Choisir la bonne alimentation LED en 3 étapes | Notes de terrain CHUGAO",
            'desc': "Comment choisir la bonne alimentation LED : correspondance de puissance, indice IP selon l'environnement et compatibilité de la tension d'entrée, expliqué simplement.",
        },
        'de': {
            'title': "Das richtige LED-Netzteil in 3 Schritten wählen | Feldbesuche CHUGAO",
            'desc': "So wählen Sie das richtige LED-Netzteil: Leistungsabgleich, IP-Schutzart je nach Umgebung und Kompatibilität der Eingangsspannung – einfach erklärt.",
        },
        'ar': {
            'title': "اختر مزوّد طاقة LED المناسب في 3 خطوات | ملاحظات ميدانية CHUGAO",
            'desc': "كيفية اختيار مزوّد طاقة LED الصحيح: مطابقة القدرة، ودرجة IP حسب البيئة، وتوافق جهد الدخل، موضّحًا ببساطة.",
        },
    },
    'blog-2': {
        'es': {
            'title': "IP20 frente a IP65, IP67 e IP68 | Notas de Campo CHUGAO",
            'desc': "Grado IP explicado para fuentes LED: qué significan los números, dónde se usa cada grado y cómo elegir el adecuado para su proyecto.",
        },
        'pt': {
            'title': "IP20 vs IP65 vs IP67 vs IP68 | Notas de Campo CHUGAO",
            'desc': "Nível IP explicado para fontes LED: o que significam os números, onde cada nível é usado e como escolher o certo para o seu projeto.",
        },
        'ru': {
            'title': "IP20 против IP65, IP67 и IP68 | Полевые заметки CHUGAO",
            'desc': "Что означает степень IP для блоков питания LED: о чём говорят цифры, где применяется каждая степень и как выбрать подходящую для вашего проекта.",
        },
        'fr': {
            'title': "IP20 vs IP65 vs IP67 vs IP68 | Notes de terrain CHUGAO",
            'desc': "Indice IP expliqué pour les alimentations LED : ce que signifient les chiffres, où chaque indice est utilisé et comment choisir le bon pour votre projet.",
        },
        'de': {
            'title': "IP20 vs IP65 vs IP67 vs IP68 | Feldbesuche CHUGAO",
            'desc': "IP-Schutzart erklärt für LED-Netzteile: was die Zahlen bedeuten, wo jede Schutzart eingesetzt wird und wie Sie die richtige für Ihr Projekt auswählen.",
        },
        'ar': {
            'title': "IP20 مقابل IP65 وIP67 وIP68 | ملاحظات ميدانية CHUGAO",
            'desc': "شرح درجة IP لمزوّدات طاقة LED: ماذا تعني الأرقام، وأين تُستخدم كل درجة، وكيف تختار المناسب لمشروعك.",
        },
    },
    'blog-3': {
        'es': {
            'title': "Mercado LED 2026: lo que estamos viendo | Notas de Campo CHUGAO",
            'desc': "Observaciones directas desde la fábrica: tendencias de demanda de drivers LED en 2026 — qué mercados crecen, qué especificaciones piden más los compradores y cómo se mueven los precios.",
        },
        'pt': {
            'title': "Mercado LED 2026: o que estamos a ver | Notas de Campo CHUGAO",
            'desc': "Observações diretas do chão de fábrica: tendências de procura por drivers LED em 2026 — que mercados estão a crescer, que especificações os compradores mais pedem e como os preços se movem.",
        },
        'ru': {
            'title': "Рынок LED 2026: что мы наблюдаем | Полевые заметки CHUGAO",
            'desc': "Наблюдения прямо с завода: тенденции спроса на драйверы LED в 2026 году — какие рынки растут, какие характеристики покупатели запрашивают чаще всего и как движутся цены.",
        },
        'fr': {
            'title': "Marché LED 2026 : ce que nous observons | Notes de terrain CHUGAO",
            'desc': "Observations directes de l'atelier : tendances de la demande de drivers LED en 2026 — quels marchés se développent, quelles caractéristiques les acheteurs demandent le plus et comment les prix évoluent.",
        },
        'de': {
            'title': "LED-Markt 2026: was wir beobachten | Feldbesuche CHUGAO",
            'desc': "Beobachtungen direkt aus der Fertigung: Trends der Nachfrage nach LED-Treibern 2026 — welche Märkte wachsen, welche Spezifikationen Käufer am meisten wünschen und wie sich die Preise bewegen.",
        },
        'ar': {
            'title': "سوق LED لعام 2026: ما نلاحظه | ملاحظات ميدانية CHUGAO",
            'desc': "ملاحظات مباشرة من أرض المصنع: اتجاهات الطلب على محركات LED لعام 2026 — أي الأسواق تنمو، وأي المواصفات يطلبها المشترون أكثر، وكيف تتحرك الأسعار.",
        },
    },
    'blog-4': {
        'es': {
            'title': "Certificación BIS para drivers LED: guía de importación a India | Notas de Campo CHUGAO",
            'desc': "Qué significa la certificación BIS de India para los importadores de fuentes LED. Requisitos de IS 13252 Parte 1, proceso de prueba, plazos, coste y cómo un proveedor con BIS como CHUGAO le ayuda a pasar aduanas más rápido.",
        },
        'pt': {
            'title': "Certificação BIS para drivers LED: guia de importação para a Índia | Notas de Campo CHUGAO",
            'desc': "O que a certificação BIS da Índia significa para importadores de fontes LED. Requisitos da IS 13252 Parte 1, processo de teste, prazos, custo e como um fornecedor com BIS como a CHUGAO o ajuda a liberar a alfândega mais rápido.",
        },
        'ru': {
            'title': "Сертификация BIS для драйверов LED: руководство по импорту в Индию | Полевые заметки CHUGAO",
            'desc': "Что означает индийская сертификация BIS для импортёров блоков питания LED. Требования IS 13252 часть 1, процесс испытаний, сроки, стоимость и как поставщик с BIS, такой как CHUGAO, помогает быстрее пройти таможню.",
        },
        'fr': {
            'title': "Certification BIS pour les drivers LED : guide d'importation en Inde | Notes de terrain CHUGAO",
            'desc': "Ce que signifie la certification BIS indienne pour les importateurs d'alimentations LED. Exigences de la IS 13252 partie 1, processus de test, délais, coût et comment un fournisseur certifié BIS comme CHUGAO vous aide à dédouaner plus vite.",
        },
        'de': {
            'title': "BIS-Zertifizierung für LED-Treiber: Importleitfaden für Indien | Feldbesuche CHUGAO",
            'desc': "Was die indische BIS-Zertifizierung für Importeure von LED-Netzteilen bedeutet. Anforderungen der IS 13252 Teil 1, Prüfablauf, Zeitrahmen, Kosten und wie ein BIS-zertifizierter Lieferant wie CHUGAO Ihnen hilft, schneller durch den Zoll zu kommen.",
        },
        'ar': {
            'title': "شهادة BIS لمحركات LED: دليل استيراد إلى الهند | ملاحظات ميدانية CHUGAO",
            'desc': "ماذا تعني شهادة BIS الهندية لمستوردي مزوّدات طاقة LED. متطلبات IS 13252 الجزء 1، وعملية الاختبار، والجدول الزمني، والتكلفة، وكيف يساعدك مورّد حاصل على BIS مثل CHUGAO على تجاوز الجمارك أسرع.",
        },
    },
    'blog-5': {
        'es': {
            'title': "Vida útil de los drivers LED: MTBF, L70 y cuánto duran realmente | Notas de Campo CHUGAO",
            'desc': "¿Qué significan 50.000 horas para un driver LED? Comprensión de MTBF, la cifra L70, los efectos de la temperatura y la vida útil real de las fuentes conmutadas LED.",
        },
        'pt': {
            'title': "Vida útil dos drivers LED: MTBF, L70 e quanto realmente duram | Notas de Campo CHUGAO",
            'desc': "O que significam 50.000 horas para um driver LED? Compreender MTBF, a classificação L70, os efeitos da temperatura e a vida útil real das fontes comutadas LED.",
        },
        'ru': {
            'title': "Срок службы драйверов LED: MTBF, L70 и как долго они реально работают | Полевые заметки CHUGAO",
            'desc': "Что значат 50 000 часов для драйвера LED? Понимание MTBF, показателя L70, влияния температуры и реального срока службы импульсных блоков питания LED.",
        },
        'fr': {
            'title': "Durée de vie des drivers LED : MTBF, L70 et combien de temps ils durent réellement | Notes de terrain CHUGAO",
            'desc': "Que signifient 50 000 heures pour un driver LED ? Compréhension du MTBF, de la cote L70, des effets de la température et de la durée de vie réelle des alimentations à découpage LED.",
        },
        'de': {
            'title': "Lebensdauer von LED-Treibern: MTBF, L70 und wie lange sie wirklich halten | Feldbesuche CHUGAO",
            'desc': "Was bedeuten 50.000 Stunden für einen LED-Treiber? Verständnis von MTBF, L70-Wert, Temperatureffekten und der realen Lebensdauer von LED-Schaltnetzteilen.",
        },
        'ar': {
            'title': "العمر الافتراضي لمحركات LED: MTBF وL70 وكم تدوم فعليًا | ملاحظات ميدانية CHUGAO",
            'desc': "ماذا تعني 50,000 ساعة لمحرك LED؟ فهم MTBF، وتصنيف L70، وتأثيرات الحرارة، والعمر الافتراضي الحقيقي لمزوّدات طاقة LED المحوّلة.",
        },
    },
}
