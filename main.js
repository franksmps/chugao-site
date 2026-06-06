/* CHUGAO Power - main.js
 * 修复记录 (2026-06-06):
 * 1. 把单行 var texts={...} 拆成多行结构化对象，避免长行 / 引号隐藏问题
 * 2. 补齐 11 国语言包 (en/zh/es/fr/de/pt/ru/ja/ko/ar/it)
 * 3. setLang() 增加调试日志，缺失 key 时 fallback 到 en
 * 4. 表单提交后 gtag 事件统一在 finally 中复位按钮文案
 */

var KEYS = [
  "n_h","n_a","n_p","n_s","n_w","n_b","n_f","n_c",
  "h_badge","h_title","h_sub","h_btn_p","h_btn_q",
  "s_y","s_y_l","s_c","s_c_l","s_m","s_m_l","h_img_cap",
  "t_ce","t_ul","t_rohs","t_iso","t_moq","t_ship",
  "a_title","a_p1","a_p2","a_p3",
  "f_fac","f_fac_d","f_qc","f_qc_d","f_log","f_log_d","f_sup","f_sup_d",
  "p_title","p_sub",
  "p1_n","p1_d","p2_n","p2_d","p3_n","p3_d","p4_n","p4_d","p_cta",
  "sp_title","sp_sub",
  "sp_h1","sp_h2","sp_h3","sp_h4","sp_h5","sp_h6","sp_h7",
  "sp_r1_n","sp_r2_n","sp_r3_n","sp_r4_n",
  "sp_cta",
  "w_title","w_sub",
  "w1_t","w1_d","w2_t","w2_d","w3_t","w3_d","w4_t","w4_d","w5_t","w5_d","w6_t","w6_d",
  "b_title","b_sub",
  "b1_t","b1_d","b2_t","b2_d","b3_t","b3_d",
  "t_title","t_sub",
  "t1_d","t1_n","t1_r","t2_d","t2_n","t2_r","t3_d","t3_n","t3_r",
  "faq_title","faq_sub",
  "faq1_q","faq1_a","faq2_q","faq2_a","faq3_q","faq3_a","faq4_q","faq4_a","faq5_q","faq5_a","faq6_q","faq6_a",
  "cta_title","cta_sub","cta_btn_c","cta_btn_w","cta_btn_e",
  "inq_title","inq_sub","inq_ok",
  "inq_name","inq_email","inq_phone","inq_company",
  "inq_product","inq_sel","inq_opt1","inq_opt2","inq_opt3","inq_opt4","inq_opt5",
  "inq_qty","inq_msg","inq_submit",
  "inq_emailto","inq_via","inq_copy","inq_note",
  "inq_why","inq_w1","inq_w2","inq_w3","inq_w4","inq_w5","inq_fast","inq_fast_d","inq_wa",
  "co_title","co_addr_t","co_phone_t","co_wa_t","co_wa_a","co_email_t","co_hours_t","co_hours_d",
  "f_desc","f_prod","f_p1","f_p2","f_p3","f_p4",
  "f_comp","f_c1","f_c2","f_c3","f_c4",
  "f_supp","f_s1","f_s2","f_s3","f_s4",
  "f_slogan"
];

var T = {};

T.en = {
  n_h:"Home",n_a:"About",n_p:"Products",n_s:"Specs",n_w:"Why Us",n_b:"News",n_f:"FAQ",n_c:"Contact",
  h_badge:"Trusted by 500+ Global Partners",
  h_title:"Professional LED Switching Power Supply Manufacturer",
  h_sub:"CHUGAO - Factory-direct LED power supplies from Zhongshan, China. CE/UL certified adapters, indoor drivers, waterproof IP67/IP68 units, and rainproof models. Serving B2B buyers worldwide since 2014.",
  h_btn_p:"View Products",h_btn_q:"Get a Free Quote",
  s_y:"10+",s_y_l:"Years Experience",s_c:"50+",s_c_l:"Countries Served",s_m:"200+",s_m_l:"Product Models",
  h_img_cap:"CHUGAO - LED Power Supply Factory in Zhongshan, China",
  t_ce:"CE Certified",t_ul:"UL Listed",t_rohs:"RoHS Compliant",t_iso:"ISO 9001 Factory",t_moq:"Low MOQ Available",t_ship:"Global Shipping",
  a_title:"About CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. is a high-tech enterprise specializing in R&D, production, and sales of LED switching power supplies. Located in Guzhen - the world-renowned lighting capital of China - we deliver efficient, stable, and energy-saving power solutions to global customers.",
  a_p2:"With over 10 years of experience, CHUGAO has built a comprehensive product line covering adapters, indoor power supplies, waterproof power supplies (IP67/IP68), and rainproof power supplies. Products are exported to 50+ countries and widely used in commercial lighting, industrial lighting, and outdoor signage.",
  a_p3:"Adhering to \"Quality First, Customer Priority\", every product undergoes rigorous testing before delivery. We provide OEM/ODM services for global brands.",
  f_fac:"Own Factory",f_fac_d:"10,000m2 production base",f_qc:"Quality Control",f_qc_d:"100% aging test before ship",f_log:"Fast Logistics",f_log_d:"7-15 days to global ports",f_sup:"Technical Support",f_sup_d:"24h response guaranteed",
  p_title:"Our Products",p_sub:"Full-series LED power supply solutions - from compact adapters to heavy-duty waterproof units.",
  p1_n:"Adapter Series",p1_d:"High efficiency, compact design. Universal AC input 100-240V. Safe and stable DC output for LED strips and modules.",
  p2_n:"Indoor Power Supply",p2_d:"Compact size, excellent heat dissipation. Silent operation. Wide input range with active PFC. Ideal for indoor LED lighting projects.",
  p3_n:"Waterproof Power (IP67)",p3_d:"IP67/IP68 rating. Fully sealed silicone potting. UV resistant housing. Ideal for outdoor LED strips, fountains, and marine lighting.",
  p4_n:"Rainproof Power (IP65)",p4_d:"Robust metal casing with protective coating. Corrosion resistant. Perfect for humid environments and semi-outdoor LED installations.",
  p_cta:"Inquire Now \u2192",
  sp_title:"Product Specifications",sp_sub:"Compare key parameters across our LED power supply series.",
  sp_h1:"Series",sp_h2:"Power Range",sp_h3:"Input Voltage",sp_h4:"Output Voltage",sp_h5:"IP Rating",sp_h6:"Efficiency",sp_h7:"Warranty",
  sp_r1_n:"Adapter Series",sp_r2_n:"Indoor Power",sp_r3_n:"Waterproof (IP67)",sp_r4_n:"Rainproof (IP65)",
  sp_cta:"Request Full Datasheet",
  w_title:"Why Choose CHUGAO",w_sub:"What sets us apart in the competitive LED power supply market.",
  w1_t:"Factory Direct Pricing",w1_d:"As a manufacturer, we eliminate middlemen - giving you competitive pricing without compromising quality. Bulk orders get even better rates.",
  w2_t:"Certified Quality",w2_d:"All products pass CE, UL, and RoHS certifications. Every unit undergoes 100% aging testing and full inspection before shipment.",
  w3_t:"R&D Capability",w3_d:"Dedicated R&D team with 10+ engineers. We offer custom OEM/ODM solutions tailored to your specific project requirements.",
  w4_t:"Fast Delivery",w4_d:"Standard products ship within 7-15 working days. Sample orders welcome with fast turnaround.",
  w5_t:"Stable Supply Chain",w5_d:"In-house production ensures consistent quality and supply. No dependency on third-party factories.",
  w6_t:"Professional Support",w6_d:"Multilingual sales team (English, Spanish, French, Chinese, German, Portuguese, Russian, Japanese, Korean, Arabic, Italian). 24-hour response time for all inquiries.",
  b_title:"Industry News & Insights",b_sub:"Stay updated with the latest trends in LED lighting and power supply technology.",
  b1_t:"How to Choose the Right LED Power Supply for Your Project",
  b1_d:"A comprehensive guide covering wattage calculation, IP rating selection, and installation tips for LED strip projects.",
  b2_t:"Understanding IP Ratings: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Learn the difference between waterproof ratings and how to select the right level of protection for your installation environment.",
  b3_t:"2026 LED Lighting Market Report: Growth Drivers and Opportunities",
  b3_d:"An analysis of the global LED lighting market, emerging applications, and how manufacturers can capture new opportunities.",
  t_title:"What Our Clients Say",t_sub:"Trusted by B2B partners and lighting distributors around the world.",
  t1_d:"\"We have been sourcing LED power supplies from CHUGAO for 3 years. Their waterproof IP67 units are consistently reliable. The technical support team responds quickly and helps us select the right products every time.\"",
  t1_n:"Marco R.",t1_r:"Lighting Distributor, Italy",
  t2_d:"\"CHUGAO's factory direct pricing saves us significant costs compared to our previous supplier. Quality is excellent and deliveries are always on time. Highly recommended for bulk orders.\"",
  t2_n:"Sarah K.",t2_r:"LED Project Contractor, USA",
  t3_d:"\"The OEM service is outstanding. CHUGAO helped us develop a custom power supply for our product line. Their R&D team is professional and the final product exceeded our expectations.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Brand Owner, France",
  faq_title:"Frequently Asked Questions",faq_sub:"Quick answers to common questions from global buyers.",
  faq1_q:"What is your minimum order quantity (MOQ)?",
  faq1_a:"Our standard MOQ is 50 pieces per model. However, for first-time buyers, we offer sample orders with lower MOQ. Bulk orders of 500+ pieces qualify for discounted pricing.",
  faq2_q:"What certifications do your products have?",
  faq2_a:"All our LED power supplies are CE and RoHS certified. Most products also carry UL listing. Specific certifications vary by product model. Please contact us for the certification documents you need.",
  faq3_q:"What is the warranty period?",
  faq3_a:"We offer a 3-year warranty on all standard products. Custom OEM products have warranty terms negotiated on a per-project basis. Warranty covers manufacturing defects under normal use conditions.",
  faq4_q:"Can you provide OEM/ODM services?",
  faq4_a:"Yes, we provide full OEM/ODM services including custom branding, packaging design, and product specifications. Our R&D team works closely with clients to develop products that meet their exact requirements.",
  faq5_q:"What are your payment terms?",
  faq5_a:"For new customers, we typically accept T/T 30% deposit, 70% balance before shipment. For established partners, we offer L/C and other payment terms. We also accept PayPal and Alibaba Trade Assurance for sample orders.",
  faq6_q:"How long is the production lead time?",
  faq6_a:"Standard products: 7-15 working days after order confirmation. Custom OEM products: 20-30 working days depending on complexity. Sample orders are typically ready within 5-7 working days.",
  cta_title:"Ready to Get Started?",cta_sub:"Contact us today for a free product consultation and customized quote.",
  cta_btn_c:"Contact Us Now",cta_btn_w:"Chat on WhatsApp",cta_btn_e:"Email Us",
  inq_title:"Send Us an Inquiry",inq_sub:"Tell us about your project and we will get back to you within 24 hours with a customized solution.",
  inq_ok:"Thank you! Your inquiry has been submitted. We will contact you shortly.",
  inq_name:"Your Name *",inq_email:"Email Address *",inq_phone:"Phone / WhatsApp",inq_company:"Company Name",
  inq_product:"Product Interest *",inq_sel:"Select a product series",
  inq_opt1:"Adapter Series (5W-200W)",inq_opt2:"Indoor Power Supply (50W-400W)",inq_opt3:"Waterproof Power IP67/IP68 (10W-400W)",inq_opt4:"Rainproof Power IP65 (100W-600W)",inq_opt5:"Custom OEM / ODM",
  inq_qty:"Estimated Quantity",inq_msg:"Project Details / Message *",inq_submit:"Submit Inquiry",
  inq_emailto:"Your inquiry will be sent to",inq_via:"via your email app.",inq_copy:"No email app? Click to copy content.",inq_note:"By submitting this form, you agree to our privacy policy. We never share your information with third parties.",
  inq_why:"Why Inquire with CHUGAO?",
  inq_w1:"Free technical consultation within 24 hours",inq_w2:"Customized product recommendation",inq_w3:"Competitive factory-direct quotation",inq_w4:"Sample support for first-time buyers",inq_w5:"Full certification documents provided",
  inq_fast:"Prefer a faster response?",inq_fast_d:"Reach us directly via WhatsApp for instant communication.",inq_wa:"Chat on WhatsApp",
  co_title:"Contact Us",co_addr_t:"Address",co_phone_t:"Phone",co_wa_t:"WhatsApp",co_wa_a:"Chat Now",co_email_t:"Email",co_hours_t:"Business Hours",co_hours_d:"Mon-Sat: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - Professional LED switching power supply manufacturer from Zhongshan, China. Serving global B2B buyers since 2014.",
  f_prod:"Products",f_p1:"Adapter Series",f_p2:"Indoor Power",f_p3:"Waterproof Power",f_p4:"Rainproof Power",
  f_comp:"Company",f_c1:"About Us",f_c2:"Why Choose Us",f_c3:"News",f_c4:"FAQ",
  f_supp:"Support",f_s1:"Contact",f_s2:"Email Us",f_s3:"WhatsApp",f_s4:"Downloads",
  f_slogan:"One-Stop LED Power Supply Manufacturer"
};

T.zh = {
  n_h:"首页",n_a:"关于我们",n_p:"产品",n_s:"规格",n_w:"优势",n_b:"新闻",n_f:"常见问题",n_c:"联系我们",
  h_badge:"全球 500+ 合作伙伴的信赖之选",
  h_title:"专业 LED 开关电源制造商",
  h_sub:"CHUGAO 楚高——中国中山工厂直供 LED 电源。CE/UL 认证适配器、室内驱动、防水 IP67/IP68 电源、防雨电源,自 2014 年起服务全球 B2B 客户。",
  h_btn_p:"查看产品",h_btn_q:"免费询价",
  s_y:"10+",s_y_l:"年行业经验",s_c:"50+",s_c_l:"出口国家",s_m:"200+",s_m_l:"产品型号",
  h_img_cap:"CHUGAO 楚高——中国中山 LED 电源工厂",
  t_ce:"CE 认证",t_ul:"UL 列名",t_rohs:"RoHS 合规",t_iso:"ISO 9001 工厂",t_moq:"支持小单",t_ship:"全球发货",
  a_title:"关于楚高",
  a_p1:"中山市楚高电子科技有限公司是一家专注于 LED 开关电源研发、生产、销售于一体的高新技术企业。公司位于中国灯饰之都——中山古镇,为全球客户提供高效、稳定、节能的电源解决方案。",
  a_p2:"凭借 10 年以上行业经验,楚高已建立完善的产品线,涵盖适配器、室内电源、防水电源(IP67/IP68)、防雨电源等系列产品。产品远销 50 多个国家,广泛应用于商业照明、工业照明、户外标识等领域。",
  a_p3:"秉持\"质量第一、客户至上\"的理念,每件产品出货前均经过严格老化测试。我们为全球品牌提供 OEM/ODM 服务。",
  f_fac:"自有工厂",f_fac_d:"10,000m2 生产基地",f_qc:"品质管控",f_qc_d:"100% 老化测试出厂",f_log:"快速物流",f_log_d:"7-15 天送达全球港口",f_sup:"技术支持",f_sup_d:"24 小时响应保障",
  p_title:"产品中心",p_sub:"全系列 LED 电源解决方案——从紧凑型适配器到重型防水电源。",
  p1_n:"适配器系列",p1_d:"高效紧凑,通用 AC 100-240V 输入,稳定 DC 输出,适用于 LED 灯带和模组。",
  p2_n:"室内电源",p2_d:"体积小巧、散热优异、运行安静,宽输入电压带主动 PFC,适合室内 LED 照明项目。",
  p3_n:"防水电源(IP67)",p3_d:"IP67/IP68 防护等级,全密封硅胶灌封,抗紫外线外壳,适用于户外灯带、喷泉、船舶照明。",
  p4_n:"防雨电源(IP65)",p4_d:"坚固金属外壳加防护涂层,耐腐蚀,适合潮湿环境和半户外 LED 安装。",
  p_cta:"立即询价 \u2192",
  sp_title:"产品规格",sp_sub:"对比各系列 LED 电源的关键参数。",
  sp_h1:"系列",sp_h2:"功率范围",sp_h3:"输入电压",sp_h4:"输出电压",sp_h5:"防护等级",sp_h6:"效率",sp_h7:"质保",
  sp_r1_n:"适配器系列",sp_r2_n:"室内电源",sp_r3_n:"防水电源(IP67)",sp_r4_n:"防雨电源(IP65)",
  sp_cta:"索取完整规格书",
  w_title:"为什么选择楚高",w_sub:"在竞争激烈的 LED 电源市场中,我们的差异化优势。",
  w1_t:"工厂直供价格",w1_d:"作为制造商,我们省去中间环节,在不牺牲品质的前提下为您提供有竞争力的价格,大批量订单价格更优。",
  w2_t:"认证品质",w2_d:"所有产品通过 CE、UL、RoHS 认证,每台设备出货前均经过 100% 老化测试和全检。",
  w3_t:"研发实力",w3_d:"10+ 资深工程师组成的研发团队,可根据您的具体项目需求提供定制 OEM/ODM 解决方案。",
  w4_t:"快速交付",w4_d:"标准产品 7-15 个工作日内发货,支持样品订单,响应迅速。",
  w5_t:"稳定供应链",w5_d:"自有生产线,品质和供货稳定,不依赖第三方代工厂。",
  w6_t:"专业支持",w6_d:"多语种销售团队(英、西、法、中、德、葡、俄、日、韩、阿、意),24 小时响应。",
  b_title:"行业资讯",b_sub:"掌握 LED 照明与电源技术的最新趋势。",
  b1_t:"如何为项目选择合适的 LED 电源",
  b1_d:"涵盖功率计算、IP 防护等级选择及 LED 灯带安装技巧的全面指南。",
  b2_t:"了解 IP 防护等级:IP20 与 IP65、IP67、IP68 的区别",
  b2_d:"学习不同防水等级的区别,以及如何为您的安装环境选择合适的防护等级。",
  b3_t:"2026 LED 照明市场报告:增长驱动力与机遇",
  b3_d:"分析全球 LED 照明市场、新兴应用场景,以及制造商如何把握新机遇。",
  t_title:"客户评价",t_sub:"全球 B2B 合作伙伴与照明经销商的信赖之选。",
  t1_d:"\"我们与楚高合作 3 年了,他们的 IP67 防水电源稳定可靠,技术支持团队响应迅速,每次都帮我们选到合适的产品。\"",
  t1_n:"Marco R.",t1_r:"意大利 照明经销商",
  t2_d:"\"楚高工厂直供价格相比之前的供应商节省了大量成本,品质优秀,交货准时,大批量订单强烈推荐。\"",
  t2_n:"Sarah K.",t2_r:"美国 LED 项目承包商",
  t3_d:"\"OEM 服务一流。楚高帮我们开发了一款定制电源,研发团队专业,最终产品超出我们的预期。\"",
  t3_n:"Jean-Pierre L.",t3_r:"法国 品牌商",
  faq_title:"常见问题",faq_sub:"全球买家的快速答疑。",
  faq1_q:"起订量(MOQ)是多少?",
  faq1_a:"标准起订量为每款 50 件。首次采购客户可申请样品小单,500 件以上大单可享折扣价。",
  faq2_q:"产品有哪些认证?",
  faq2_a:"所有 LED 电源均通过 CE 和 RoHS 认证,大部分产品同时具备 UL 列名。具体认证因型号而异,请联系我们获取所需认证文件。",
  faq3_q:"质保期多久?",
  faq3_a:"标准产品提供 3 年质保。定制 OEM 产品的质保条款根据项目协商。质保涵盖正常使用条件下的制造缺陷。",
  faq4_q:"是否提供 OEM/ODM 服务?",
  faq4_a:"是的,我们提供全方位 OEM/ODM 服务,包括品牌定制、包装设计、规格定制,研发团队与客户紧密合作开发满足需求的产品。",
  faq5_q:"付款方式有哪些?",
  faq5_a:"新客户通常采用 T/T 30% 定金 + 70% 发货前付清。合作客户可接受 L/C 等方式。样品订单也接受 PayPal 和阿里巴巴信保订单。",
  faq6_q:"生产交期多久?",
  faq6_a:"标准产品:订单确认后 7-15 个工作日。定制 OEM 产品:20-30 个工作日,视复杂度而定。样品订单通常 5-7 个工作日内完成。",
  cta_title:"准备开始合作?",cta_sub:"立即联系我们,享受免费产品咨询和定制报价。",
  cta_btn_c:"立即联系",cta_btn_w:"WhatsApp 沟通",cta_btn_e:"发送邮件",
  inq_title:"发送询价",inq_sub:"告诉我们您的项目需求,24 小时内为您回复定制方案。",
  inq_ok:"感谢您的询价!我们已收到,会尽快与您联系。",
  inq_name:"您的姓名 *",inq_email:"邮箱地址 *",inq_phone:"电话 / WhatsApp",inq_company:"公司名称",
  inq_product:"意向产品 *",inq_sel:"请选择产品系列",
  inq_opt1:"适配器系列(5W-200W)",inq_opt2:"室内电源(50W-400W)",inq_opt3:"防水电源 IP67/IP68(10W-400W)",inq_opt4:"防雨电源 IP65(100W-600W)",inq_opt5:"定制 OEM / ODM",
  inq_qty:"预计数量",inq_msg:"项目详情 / 留言 *",inq_submit:"提交询价",
  inq_emailto:"询价将发送至",inq_via:"通过您的邮件应用。",inq_copy:"无邮件应用?点击复制内容。",inq_note:"提交表单即表示您同意我们的隐私政策,我们绝不会将您的信息分享给第三方。",
  inq_why:"为什么选择楚高?",
  inq_w1:"24 小时内免费技术咨询",inq_w2:"定制化产品推荐",inq_w3:"工厂直供的竞争性报价",inq_w4:"首次采购支持样品",inq_w5:"提供完整认证文件",
  inq_fast:"想要更快回复?",inq_fast_d:"直接通过 WhatsApp 与我们联系,沟通更高效。",inq_wa:"WhatsApp 沟通",
  co_title:"联系我们",co_addr_t:"公司地址",co_phone_t:"电话",co_wa_t:"WhatsApp",co_wa_a:"立即聊天",co_email_t:"邮箱",co_hours_t:"营业时间",co_hours_d:"周一至周六:8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO 楚高——中国中山专业 LED 开关电源制造商,自 2014 年起服务全球 B2B 客户。",
  f_prod:"产品",f_p1:"适配器系列",f_p2:"室内电源",f_p3:"防水电源",f_p4:"防雨电源",
  f_comp:"公司",f_c1:"关于我们",f_c2:"为什么选择我们",f_c3:"新闻资讯",f_c4:"常见问题",
  f_supp:"支持",f_s1:"联系我们",f_s2:"邮件咨询",f_s3:"WhatsApp",f_s4:"资料下载",
  f_slogan:"一站式 LED 电源制造商"
};

T.es = {
  n_h:"Inicio",n_a:"Nosotros",n_p:"Productos",n_s:"Specs",n_w:"Ventajas",n_b:"Noticias",n_f:"FAQ",n_c:"Contacto",
  h_badge:"La eleccion de mas de 500 socios globales",
  h_title:"Fabricante profesional de fuentes de alimentacion LED",
  h_sub:"CHUGAO - Fuentes de alimentacion LED directamente de fabrica en Zhongshan, China. Adaptadores, drivers para interior, impermeables IP67/IP68 y modelos a prueba de lluvia con certificacion CE/UL. Sirviendo a compradores B2B en todo el mundo desde 2014.",
  h_btn_p:"Ver productos",h_btn_q:"Solicitar cotizacion",
  s_y:"10+",s_y_l:"Anos de experiencia",s_c:"50+",s_c_l:"Paises servidos",s_m:"200+",s_m_l:"Modelos de producto",
  h_img_cap:"CHUGAO - Fabrica de fuentes de alimentacion LED en Zhongshan, China",
  t_ce:"Certificado CE",t_ul:"Listado UL",t_rohs:"Cumple RoHS",t_iso:"Fabrica ISO 9001",t_moq:"MOQ bajo disponible",t_ship:"Envio global",
  a_title:"Sobre CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. es una empresa de alta tecnologia especializada en I+D, produccion y venta de fuentes de alimentacion LED conmutadas. Ubicada en Guzhen, la capital mundial de la iluminacion en China.",
  a_p2:"Con mas de 10 anos de experiencia, CHUGAO ha construido una linea completa que cubre adaptadores, fuentes de interior, impermeables (IP67/IP68) y a prueba de lluvia. Los productos se exportan a mas de 50 paises.",
  a_p3:"Bajo el principio de \"Calidad primero, prioridad del cliente\", cada producto se somete a pruebas rigurosas antes de la entrega. Ofrecemos servicios OEM/ODM para marcas globales.",
  f_fac:"Fabrica propia",f_fac_d:"Base de produccion de 10.000m2",f_qc:"Control de calidad",f_qc_d:"100% prueba de envejecimiento",f_log:"Logistica rapida",f_log_d:"7-15 dias a puertos globales",f_sup:"Soporte tecnico",f_sup_d:"Respuesta garantizada en 24h",
  p_title:"Nuestros productos",p_sub:"Soluciones completas de fuentes LED - desde adaptadores compactos hasta unidades impermeables de alta potencia.",
  p1_n:"Serie adaptadores",p1_d:"Alta eficiencia, diseno compacto. Entrada AC 100-240V universal. Salida DC estable y segura para tiras y modulos LED.",
  p2_n:"Fuente para interior",p2_d:"Tamano compacto, excelente disipacion de calor. Operacion silenciosa. Amplio rango de entrada con PFC activo.",
  p3_n:"Fuente impermeable (IP67)",p3_d:"Grado IP67/IP68. Encapsulado de silicona. Carcasa resistente a UV. Ideal para tiras LED exteriores, fuentes y marina.",
  p4_n:"Fuente a prueba de lluvia (IP65)",p4_d:"Carcasa metalica robusta con recubrimiento protector. Resistente a la corrosion. Perfecta para ambientes humedos.",
  p_cta:"Consultar ahora \u2192",
  sp_title:"Especificaciones",sp_sub:"Compare parametros clave entre nuestras series de fuentes LED.",
  sp_h1:"Serie",sp_h2:"Rango de potencia",sp_h3:"Tension de entrada",sp_h4:"Tension de salida",sp_h5:"Grado IP",sp_h6:"Eficiencia",sp_h7:"Garantia",
  sp_r1_n:"Serie adaptadores",sp_r2_n:"Fuente interior",sp_r3_n:"Impermeable (IP67)",sp_r4_n:"A prueba de lluvia (IP65)",
  sp_cta:"Solicitar ficha tecnica",
  w_title:"Por que elegir CHUGAO",w_sub:"Lo que nos diferencia en el mercado competitivo de fuentes LED.",
  w1_t:"Precio directo de fabrica",w1_d:"Como fabricantes eliminamos intermediarios, ofreciendo precios competitivos sin comprometer la calidad.",
  w2_t:"Calidad certificada",w2_d:"Todos los productos cuentan con certificaciones CE, UL y RoHS. Cada unidad pasa por pruebas de envejecimiento al 100%.",
  w3_t:"Capacidad de I+D",w3_d:"Equipo de I+D con mas de 10 ingenieros. Ofrecemos soluciones OEM/ODM a medida.",
  w4_t:"Entrega rapida",w4_d:"Productos estandar enviados en 7-15 dias habiles. Aceptamos pedidos de muestra.",
  w5_t:"Cadena de suministro estable",w5_d:"Produccion propia que garantiza calidad y suministro constante.",
  w6_t:"Soporte profesional",w6_d:"Equipo de ventas multilingue (ingles, espanol, frances, chino, aleman, portugues, ruso, japones, coreano, arabe, italiano).",
  b_title:"Noticias del sector",b_sub:"Mantengase al dia con las ultimas tendencias en iluminacion LED.",
  b1_t:"Como elegir la fuente LED adecuada para su proyecto",
  b1_d:"Guia completa sobre calculo de potencia, seleccion de grado IP y consejos de instalacion.",
  b2_t:"Entendiendo los grados IP: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Aprenda las diferencias entre los grados de impermeabilidad y como elegir el adecuado.",
  b3_t:"Informe del mercado LED 2026: impulsores y oportunidades",
  b3_d:"Analisis del mercado global de iluminacion LED y oportunidades para fabricantes.",
  t_title:"Lo que dicen nuestros clientes",t_sub:"Confianza de socios B2B y distribuidores en todo el mundo.",
  t1_d:"\"Llevamos 3 anos comprando fuentes LED a CHUGAO. Sus unidades IP67 son fiables. El soporte tecnico responde rapido y nos ayuda a elegir el producto adecuado.\"",
  t1_n:"Marco R.",t1_r:"Distribuidor de iluminacion, Italia",
  t2_d:"\"El precio directo de fabrica de CHUGAO nos ahorra costes importantes. La calidad es excelente y las entregas siempre puntuales.\"",
  t2_n:"Sarah K.",t2_r:"Contratista de proyectos LED, EE.UU.",
  t3_d:"\"El servicio OEM es excepcional. CHUGAO nos ayudo a desarrollar una fuente personalizada y el resultado supero nuestras expectativas.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Propietario de marca, Francia",
  faq_title:"Preguntas frecuentes",faq_sub:"Respuestas rapidas a preguntas comunes.",
  faq1_q:"Cual es su cantidad minima de pedido (MOQ)?",
  faq1_a:"Nuestro MOQ estandar es de 50 piezas por modelo. Para nuevos compradores ofrecemos pedidos de muestra con MOQ menor. Pedidos de 500+ piezas califican para precios con descuento.",
  faq2_q:"Que certificaciones tienen sus productos?",
  faq2_a:"Todas nuestras fuentes LED cuentan con certificaciones CE y RoHS. La mayoria tambien con listado UL. Las certificaciones especificas varian segun el modelo.",
  faq3_q:"Cual es el periodo de garantia?",
  faq3_a:"Ofrecemos 3 anos de garantia en todos los productos estandar. Los productos OEM personalizados tienen terminos negociados por proyecto.",
  faq4_q:"Ofrecen servicios OEM/ODM?",
  faq4_a:"Si, ofrecemos servicios completos de OEM/ODM que incluyen marca personalizada, diseno de empaque y especificaciones a medida.",
  faq5_q:"Cuales son sus condiciones de pago?",
  faq5_a:"Para clientes nuevos, normalmente T/T 30% deposito, 70% antes del envio. Para socios establecidos, aceptamos L/C y otros terminos.",
  faq6_q:"Cual es el plazo de produccion?",
  faq6_a:"Productos estandar: 7-15 dias habiles. OEM personalizado: 20-30 dias habiles. Muestras: 5-7 dias habiles.",
  cta_title:"Listo para comenzar?",cta_sub:"Contactenos hoy para una consulta gratuita y cotizacion personalizada.",
  cta_btn_c:"Contactenos ahora",cta_btn_w:"Chat en WhatsApp",cta_btn_e:"Enviar correo",
  inq_title:"Envienos una consulta",inq_sub:"Cuentenos sobre su proyecto y le responderemos en 24 horas.",
  inq_ok:"Gracias! Su consulta ha sido enviada. Le contactaremos pronto.",
  inq_name:"Su nombre *",inq_email:"Correo electronico *",inq_phone:"Telefono / WhatsApp",inq_company:"Empresa",
  inq_product:"Producto de interes *",inq_sel:"Seleccione una serie",
  inq_opt1:"Serie adaptadores (5W-200W)",inq_opt2:"Fuente interior (50W-400W)",inq_opt3:"Impermeable IP67/IP68 (10W-400W)",inq_opt4:"A prueba de lluvia IP65 (100W-600W)",inq_opt5:"OEM / ODM personalizado",
  inq_qty:"Cantidad estimada",inq_msg:"Detalles del proyecto *",inq_submit:"Enviar consulta",
  inq_emailto:"Su consulta sera enviada a",inq_via:"desde su app de correo.",inq_copy:"Sin app de correo? Haga clic para copiar.",inq_note:"Al enviar este formulario, acepta nuestra politica de privacidad.",
  inq_why:"Por que consultar con CHUGAO?",
  inq_w1:"Consulta tecnica gratuita en 24 horas",inq_w2:"Recomendacion personalizada",inq_w3:"Cotizacion directa de fabrica",inq_w4:"Soporte de muestras",inq_w5:"Documentos de certificacion completos",
  inq_fast:"Prefiere una respuesta mas rapida?",inq_fast_d:"Contactenos directamente por WhatsApp.",inq_wa:"Chat en WhatsApp",
  co_title:"Contactenos",co_addr_t:"Direccion",co_phone_t:"Telefono",co_wa_t:"WhatsApp",co_wa_a:"Chatear ahora",co_email_t:"Correo",co_hours_t:"Horario",co_hours_d:"Lun-Sab: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - Fabricante profesional de fuentes de alimentacion LED conmutadas de Zhongshan, China. Sirviendo a compradores B2B desde 2014.",
  f_prod:"Productos",f_p1:"Serie adaptadores",f_p2:"Fuente interior",f_p3:"Fuente impermeable",f_p4:"Fuente a prueba de lluvia",
  f_comp:"Empresa",f_c1:"Sobre nosotros",f_c2:"Por que elegirnos",f_c3:"Noticias",f_c4:"FAQ",
  f_supp:"Soporte",f_s1:"Contacto",f_s2:"Email",f_s3:"WhatsApp",f_s4:"Descargas",
  f_slogan:"Fabricante de fuentes LED todo en uno"
};

T.fr = {
  n_h:"Accueil",n_a:"A propos",n_p:"Produits",n_s:"Specs",n_w:"Avantages",n_b:"Actualites",n_f:"FAQ",n_c:"Contact",
  h_badge:"Choisi par plus de 500 partenaires mondiaux",
  h_title:"Fabricant professionnel d'alimentations LED",
  h_sub:"CHUGAO - Alimentations LED direct usine depuis Zhongshan, Chine. Adaptateurs, drivers interieurs, etanches IP67/IP68 et resistants a la pluie, certifies CE/UL. Au service des acheteurs B2B du monde entier depuis 2014.",
  h_btn_p:"Voir les produits",h_btn_q:"Devis gratuit",
  s_y:"10+",s_y_l:"Annees d'experience",s_c:"50+",s_c_l:"Pays servis",s_m:"200+",s_m_l:"Modeles",
  h_img_cap:"CHUGAO - Usine d'alimentations LED a Zhongshan, Chine",
  t_ce:"Certifie CE",t_ul:"Liste UL",t_rohs:"Conforme RoHS",t_iso:"Usine ISO 9001",t_moq:"MOQ bas disponible",t_ship:"Expedition mondiale",
  a_title:"A propos de CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. est une entreprise haute technologie specialisee dans la R&D, la production et la vente d'alimentations LED commutees. Situee a Guzhen, la capitale mondiale de l'eclairage en Chine.",
  a_p2:"Avec plus de 10 ans d'experience, CHUGAO a developpe une gamme complete couvrant les adaptateurs, alimentations interieures, etanches (IP67/IP68) et resistantes a la pluie. Produits exportes vers plus de 50 pays.",
  a_p3:"Selon le principe \"Qualite d'abord, client prioritaire\", chaque produit subit des tests rigoureux avant livraison. Nous fournissons des services OEM/ODM aux marques mondiales.",
  f_fac:"Usine proprietaire",f_fac_d:"Base de production de 10 000m2",f_qc:"Controle qualite",f_qc_d:"100% test de vieillissement",f_log:"Logistique rapide",f_log_d:"7-15 jours vers les ports",f_sup:"Support technique",f_sup_d:"Reponse garantie sous 24h",
  p_title:"Nos produits",p_sub:"Solutions completes d'alimentations LED - des adaptateurs compacts aux unites etanches haute puissance.",
  p1_n:"Serie adaptateurs",p1_d:"Haute efficacite, design compact. Entree AC 100-240V universelle. Sortie DC stable et sure pour bandes et modules LED.",
  p2_n:"Alimentation interieure",p2_d:"Taille compacte, excellente dissipation thermique. Fonctionnement silencieux. Large plage d'entree avec PFC actif.",
  p3_n:"Alimentation etanche (IP67)",p3_d:"Indice IP67/IP68. Encapsulation silicone. Boitier resistant aux UV. Ideal pour bandes LED exterieures, fontaines et marine.",
  p4_n:"Alimentation anti-pluie (IP65)",p4_d:"Boitier metallique robuste avec revetement protecteur. Resistant a la corrosion.",
  p_cta:"Demander un devis \u2192",
  sp_title:"Specifications produit",sp_sub:"Comparez les parametres cles de nos series d'alimentations LED.",
  sp_h1:"Serie",sp_h2:"Plage de puissance",sp_h3:"Tension d'entree",sp_h4:"Tension de sortie",sp_h5:"Indice IP",sp_h6:"Rendement",sp_h7:"Garantie",
  sp_r1_n:"Serie adaptateurs",sp_r2_n:"Alimentation interieure",sp_r3_n:"Etanche (IP67)",sp_r4_n:"Anti-pluie (IP65)",
  sp_cta:"Demander la fiche technique",
  w_title:"Pourquoi choisir CHUGAO",w_sub:"Ce qui nous distingue sur le marche competitif des alimentations LED.",
  w1_t:"Prix direct usine",w1_d:"En tant que fabricant, nous eliminons les intermediaires - vous beneficiez de prix competitifs sans compromis sur la qualite.",
  w2_t:"Qualite certifiee",w2_d:"Tous les produits passent les certifications CE, UL et RoHS. Chaque unite subit un test de vieillissement a 100%.",
  w3_t:"Capacite R&D",w3_d:"Equipe R&D de plus de 10 ingenieurs. Solutions OEM/ODM personnalisees selon vos besoins.",
  w4_t:"Livraison rapide",w4_d:"Produits standards expedies sous 7-15 jours ouvrables. Commandes d'echantillons bienvenues.",
  w5_t:"Chaine d'approvisionnement stable",w5_d:"Production interne garantissant qualite et approvisionnement constants.",
  w6_t:"Support professionnel",w6_d:"Equipe commerciale multilingue (anglais, espagnol, francais, chinois, allemand, portugais, russe, japonais, coreen, arabe, italien).",
  b_title:"Actualites du secteur",b_sub:"Restez informe des dernieres tendances de l'eclairage LED.",
  b1_t:"Comment choisir la bonne alimentation LED pour votre projet",
  b1_d:"Guide complet couvrant le calcul de puissance, le choix de l'indice IP et les conseils d'installation.",
  b2_t:"Comprendre les indices IP : IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Apprenez les differences entre les niveaux d'etancheite et choisissez la bonne protection.",
  b3_t:"Rapport marche LED 2026 : moteurs de croissance",
  b3_d:"Analyse du marche mondial de l'eclairage LED et opportunites pour les fabricants.",
  t_title:"Avis de nos clients",t_sub:"La confiance de partenaires B2B et distributeurs du monde entier.",
  t1_d:"\"Nous nous approvisionnons chez CHUGAO depuis 3 ans. Leurs unites IP67 sont fiables. Le support technique repond rapidement et nous aide a choisir.\"",
  t1_n:"Marco R.",t1_r:"Distributeur d'eclairage, Italie",
  t2_d:"\"Les prix direct usine de CHUGAO nous font economiser beaucoup par rapport a notre fournisseur precedent. Qualite excellente, livraisons a l'heure.\"",
  t2_n:"Sarah K.",t2_r:"Contractant de projets LED, USA",
  t3_d:"\"Le service OEM est remarquable. CHUGAO nous a aide a developper une alimentation personnalisee et le resultat a depasse nos attentes.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Proprietaire de marque, France",
  faq_title:"Questions frequentes",faq_sub:"Reponses rapides aux questions courantes.",
  faq1_q:"Quelle est votre quantite minimum de commande (MOQ) ?",
  faq1_a:"Notre MOQ standard est de 50 pieces par modele. Pour les nouveaux acheteurs, nous acceptons des echantillons avec un MOQ inferieur. Les commandes de 500+ pieces beneficient de tarifs preferentiels.",
  faq2_q:"Quelles certifications ont vos produits ?",
  faq2_a:"Toutes nos alimentations LED sont certifiees CE et RoHS. La plupart sont egalement listees UL.",
  faq3_q:"Quelle est la periode de garantie ?",
  faq3_a:"Nous offrons 3 ans de garantie sur tous les produits standards. Les produits OEM personnalises ont des termes negocies par projet.",
  faq4_q:"Fournissez-vous des services OEM/ODM ?",
  faq4_a:"Oui, nous fournissons des services OEM/ODM complets incluant la marque, l'emballage et les specifications personnalisees.",
  faq5_q:"Quelles sont vos conditions de paiement ?",
  faq5_a:"Pour les nouveaux clients : T/T 30% d'acompte, 70% avant expedition. Pour les partenaires etablis : L/C et autres conditions.",
  faq6_q:"Quel est le delai de production ?",
  faq6_a:"Produits standards : 7-15 jours ouvrables. OEM personnalise : 20-30 jours ouvrables. Echantillons : 5-7 jours ouvrables.",
  cta_title:"Pret a commencer ?",cta_sub:"Contactez-nous pour une consultation gratuite et un devis personnalise.",
  cta_btn_c:"Nous contacter",cta_btn_w:"Discuter sur WhatsApp",cta_btn_e:"Envoyer un email",
  inq_title:"Envoyez-nous une demande",inq_sub:"Parlez-nous de votre projet et nous vous repondrons sous 24 heures.",
  inq_ok:"Merci ! Votre demande a ete envoyee. Nous vous contacterons bientot.",
  inq_name:"Votre nom *",inq_email:"Adresse e-mail *",inq_phone:"Telephone / WhatsApp",inq_company:"Societe",
  inq_product:"Produit d'interet *",inq_sel:"Selectionnez une serie",
  inq_opt1:"Adaptateurs (5W-200W)",inq_opt2:"Alimentation interieure (50W-400W)",inq_opt3:"Etanche IP67/IP68 (10W-400W)",inq_opt4:"Anti-pluie IP65 (100W-600W)",inq_opt5:"OEM / ODM personnalise",
  inq_qty:"Quantite estimee",inq_msg:"Details du projet *",inq_submit:"Envoyer la demande",
  inq_emailto:"Votre demande sera envoyee a",inq_via:"via votre application e-mail.",inq_copy:"Pas d'application e-mail ? Cliquez pour copier.",inq_note:"En soumettant ce formulaire, vous acceptez notre politique de confidentialite.",
  inq_why:"Pourquoi demander un devis a CHUGAO ?",
  inq_w1:"Consultation technique gratuite sous 24h",inq_w2:"Recommandation produit personnalisee",inq_w3:"Devis direct usine competitif",inq_w4:"Support echantillon pour nouveaux acheteurs",inq_w5:"Documents de certification complets",
  inq_fast:"Vous preferez une reponse plus rapide ?",inq_fast_d:"Contactez-nous directement par WhatsApp.",inq_wa:"Discuter sur WhatsApp",
  co_title:"Nous contacter",co_addr_t:"Adresse",co_phone_t:"Telephone",co_wa_t:"WhatsApp",co_wa_a:"Discuter maintenant",co_email_t:"E-mail",co_hours_t:"Horaires",co_hours_d:"Lun-Sam : 8h00 - 18h00 (GMT+8)",
  f_desc:"CHUGAO - Fabricant professionnel d'alimentations LED commutees de Zhongshan, Chine. Au service des acheteurs B2B depuis 2014.",
  f_prod:"Produits",f_p1:"Adaptateurs",f_p2:"Alimentation interieure",f_p3:"Alimentation etanche",f_p4:"Alimentation anti-pluie",
  f_comp:"Societe",f_c1:"A propos",f_c2:"Pourquoi nous",f_c3:"Actualites",f_c4:"FAQ",
  f_supp:"Support",f_s1:"Contact",f_s2:"E-mail",f_s3:"WhatsApp",f_s4:"Telechargements",
  f_slogan:"Fabricant d'alimentations LED tout-en-un"
};

T.de = {
  n_h:"Start",n_a:"Ueber uns",n_p:"Produkte",n_s:"Specs",n_w:"Vorteile",n_b:"News",n_f:"FAQ",n_c:"Kontakt",
  h_badge:"Vertrauen von 500+ globalen Partnern",
  h_title:"Professioneller Hersteller von LED-Schaltnetzteilen",
  h_sub:"CHUGAO - LED-Netzteile direkt ab Werk in Zhongshan, China. CE/UL zertifizierte Adapter, Innenraum-Treiber, wasserdichte IP67/IP68-Geraete und regenfeste Modelle. Weltweiter B2B-Service seit 2014.",
  h_btn_p:"Produkte ansehen",h_btn_q:"Kostenloses Angebot",
  s_y:"10+",s_y_l:"Jahre Erfahrung",s_c:"50+",s_c_l:"Belieferte Laender",s_m:"200+",s_m_l:"Produktmodelle",
  h_img_cap:"CHUGAO - LED-Netzteil-Fabrik in Zhongshan, China",
  t_ce:"CE-zertifiziert",t_ul:"UL-gelistet",t_rohs:"RoHS-konform",t_iso:"ISO 9001 Werk",t_moq:"Niedrige MOQ verfuegbar",t_ship:"Weltweiter Versand",
  a_title:"Ueber CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. ist ein High-Tech-Unternehmen, spezialisiert auf F&E, Produktion und Vertrieb von LED-Schaltnetzteilen. Ansässig in Guzhen, der weltberuehmten Lichthauptstadt Chinas.",
  a_p2:"Mit ueber 10 Jahren Erfahrung bietet CHUGAO eine umfassende Produktpalette: Adapter, Innenraum-Netzteile, wasserdichte Netzteile (IP67/IP68) und regenfeste Netzteile. Export in mehr als 50 Laender.",
  a_p3:"Nach dem Prinzip \"Qualitaet zuerst, Kunde im Mittelpunkt\" wird jedes Produkt vor der Auslieferung streng geprueft. Wir bieten OEM/ODM-Service fuer globale Marken.",
  f_fac:"Eigenes Werk",f_fac_d:"10.000m2 Produktionsflaeche",f_qc:"Qualitaetskontrolle",f_qc_d:"100% Alterungstest",f_log:"Schnelle Logistik",f_log_d:"7-15 Tage zu globalen Haefen",f_sup:"Technischer Support",f_sup_d:"24h Antwort garantiert",
  p_title:"Unsere Produkte",p_sub:"Komplette LED-Netzteilloesungen - von kompakten Adaptern bis zu Hochleistungs-Wasserdicht-Geraeten.",
  p1_n:"Adapter-Serie",p1_d:"Hohe Effizienz, kompaktes Design. Universeller AC-Eingang 100-240V. Stabiler DC-Ausgang fuer LED-Streifen und Module.",
  p2_n:"Innenraum-Netzteil",p2_d:"Kompakte Groesse, hervorragende Waermeabfuhr. Lautloser Betrieb. Breiter Eingangsbereich mit aktivem PFC.",
  p3_n:"Wasserdichtes Netzteil (IP67)",p3_d:"IP67/IP68-Schutzart. Vollvergossene Silikondichtung. UV-bestaendiges Gehaeuse. Ideal fuer Outdoor-LED-Streifen, Brunnen und Marinebeleuchtung.",
  p4_n:"Regenfestes Netzteil (IP65)",p4_d:"Robustes Metallgehaeuse mit Schutzbeschichtung. Korrosionsbestaendig. Perfekt fuer feuchte Umgebungen.",
  p_cta:"Jetzt anfragen \u2192",
  sp_title:"Produktspezifikationen",sp_sub:"Vergleichen Sie die wichtigsten Parameter unserer LED-Netzteil-Serien.",
  sp_h1:"Serie",sp_h2:"Leistungsbereich",sp_h3:"Eingangsspannung",sp_h4:"Ausgangsspannung",sp_h5:"IP-Schutzart",sp_h6:"Wirkungsgrad",sp_h7:"Garantie",
  sp_r1_n:"Adapter-Serie",sp_r2_n:"Innenraum-Netzteil",sp_r3_n:"Wasserdicht (IP67)",sp_r4_n:"Regenfest (IP65)",
  sp_cta:"Datenblatt anfordern",
  w_title:"Warum CHUGAO waehlen",w_sub:"Was uns im wettbewerbsintensiven LED-Netzteilmarkt auszeichnet.",
  w1_t:"Werksdirektpreise",w1_d:"Als Hersteller eliminieren wir Zwischenhaendler - wettbewerbsfaehige Preise ohne Qualitaetsverlust.",
  w2_t:"Zertifizierte Qualitaet",w2_d:"Alle Produkte verfuegen ueber CE-, UL- und RoHS-Zertifizierungen. 100% Alterungstest vor Versand.",
  w3_t:"F&E-Faehigkeit",w3_d:"F&E-Team mit ueber 10 Ingenieuren. Kundenspezifische OEM/ODM-Loesungen.",
  w4_t:"Schnelle Lieferung",w4_d:"Standardprodukte werden innerhalb von 7-15 Werktagen versandt. Musterbestellungen willkommen.",
  w5_t:"Stabile Lieferkette",w5_d:"Eigene Produktion garantiert gleichbleibende Qualitaet und Versorgung.",
  w6_t:"Professioneller Support",w6_d:"Mehrsprachiges Vertriebsteam (EN, ES, FR, ZH, DE, PT, RU, JA, KO, AR, IT). 24h-Antwortzeit.",
  b_title:"Branchennachrichten",b_sub:"Bleiben Sie auf dem Laufenden mit den neuesten Trends in der LED-Beleuchtung.",
  b1_t:"Wie Sie das richtige LED-Netzteil fuer Ihr Projekt auswaehlen",
  b1_d:"Umfassender Leitfaden zu Leistungsberechnung, IP-Schutzart-Auswahl und Installationstipps.",
  b2_t:"IP-Schutzarten verstehen: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Lernen Sie die Unterschiede zwischen den Wasserdichtigkeitsstufen und waehlen Sie die richtige Schutzart.",
  b3_t:"LED-Beleuchtungsmarkt 2026: Wachstumstreiber und Chancen",
  b3_d:"Analyse des globalen LED-Beleuchtungsmarktes und neuer Chancen fuer Hersteller.",
  t_title:"Was unsere Kunden sagen",t_sub:"Vertrauen von B2B-Partnern und Lichtdistributoren weltweit.",
  t1_d:"\"Wir beziehen LED-Netzteile seit 3 Jahren von CHUGAO. Ihre IP67-Geraete sind zuverlaessig. Das technische Support-Team reagiert schnell.\"",
  t1_n:"Marco R.",t1_r:"Lichtdistributor, Italien",
  t2_d:"\"CHUGAOs Werkspreise sparen uns erhebliche Kosten im Vergleich zu unserem frueheren Lieferanten. Qualitaet hervorragend, Lieferung puenktlich.\"",
  t2_n:"Sarah K.",t2_r:"LED-Projektunternehmer, USA",
  t3_d:"\"Der OEM-Service ist hervorragend. CHUGAO hat uns bei der Entwicklung eines kundenspezifischen Netzteils geholfen. Das Endergebnis uebertraf unsere Erwartungen.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Markeninhaber, Frankreich",
  faq_title:"Haeufig gestellte Fragen",faq_sub:"Schnelle Antworten auf gaengige Fragen globaler Kaeufer.",
  faq1_q:"Was ist Ihre Mindestbestellmenge (MOQ)?",
  faq1_a:"Unsere Standard-MOQ betraegt 50 Stueck pro Modell. Fuer Erstkaeufer bieten wir Musterbestellungen mit niedrigerer MOQ an. Bestellungen ab 500 Stueck erhalten Mengenrabatt.",
  faq2_q:"Welche Zertifizierungen haben Ihre Produkte?",
  faq2_a:"Alle unsere LED-Netzteile sind CE- und RoHS-zertifiziert. Die meisten Produkte sind auch UL-gelistet.",
  faq3_q:"Wie lang ist die Garantiezeit?",
  faq3_a:"Wir bieten 3 Jahre Garantie auf alle Standardprodukte. Bei kundenspezifischen OEM-Produkten werden die Garantiebedingungen pro Projekt vereinbart.",
  faq4_q:"Bieten Sie OEM/ODM-Service an?",
  faq4_a:"Ja, wir bieten umfassende OEM/ODM-Dienstleistungen einschliesslich kundenspezifischem Branding, Verpackungsdesign und Spezifikationen.",
  faq5_q:"Was sind Ihre Zahlungsbedingungen?",
  faq5_a:"Fuer Neukunden: T/T 30% Anzahlung, 70% vor Versand. Fuer etablierte Partner: L/C und andere Bedingungen.",
  faq6_q:"Wie lang ist die Produktionsvorlaufzeit?",
  faq6_a:"Standardprodukte: 7-15 Werktage. Kundenspezifische OEM-Produkte: 20-30 Werktage. Musterbestellungen: 5-7 Werktage.",
  cta_title:"Bereit zu starten?",cta_sub:"Kontaktieren Sie uns noch heute fuer eine kostenlose Produktberatung und ein individuelles Angebot.",
  cta_btn_c:"Jetzt kontaktieren",cta_btn_w:"Chat auf WhatsApp",cta_btn_e:"E-Mail senden",
  inq_title:"Senden Sie uns eine Anfrage",inq_sub:"Erzaehlen Sie uns von Ihrem Projekt und wir melden uns innerhalb von 24 Stunden mit einer massgeschneiderten Loesung.",
  inq_ok:"Vielen Dank! Ihre Anfrage wurde uebermittelt. Wir werden Sie in Kuerze kontaktieren.",
  inq_name:"Ihr Name *",inq_email:"E-Mail-Adresse *",inq_phone:"Telefon / WhatsApp",inq_company:"Firmenname",
  inq_product:"Produktinteresse *",inq_sel:"Wahlen Sie eine Produktserie",
  inq_opt1:"Adapter-Serie (5W-200W)",inq_opt2:"Innenraum-Netzteil (50W-400W)",inq_opt3:"Wasserdicht IP67/IP68 (10W-400W)",inq_opt4:"Regenfest IP65 (100W-600W)",inq_opt5:"Kundenspezifisch OEM / ODM",
  inq_qty:"Geschaetzte Menge",inq_msg:"Projektdetails / Nachricht *",inq_submit:"Anfrage senden",
  inq_emailto:"Ihre Anfrage wird gesendet an",inq_via:"ueber Ihre E-Mail-App.",inq_copy:"Keine E-Mail-App? Klicken Sie zum Kopieren.",inq_note:"Mit dem Absenden stimmen Sie unserer Datenschutzrichtlinie zu.",
  inq_why:"Warum bei CHUGAO anfragen?",
  inq_w1:"Kostenlose technische Beratung innerhalb von 24 Stunden",inq_w2:"Personalisierte Produktempfehlung",inq_w3:"Wettbewerbsfaehiges Werksangebot",inq_w4:"Musterunterstuetzung fuer Erstkaeufer",inq_w5:"Vollstaendige Zertifizierungsdokumente",
  inq_fast:"Bevorzugen Sie eine schnellere Antwort?",inq_fast_d:"Erreichen Sie uns direkt ueber WhatsApp fuer sofortige Kommunikation.",inq_wa:"Chat auf WhatsApp",
  co_title:"Kontaktieren Sie uns",co_addr_t:"Adresse",co_phone_t:"Telefon",co_wa_t:"WhatsApp",co_wa_a:"Jetzt chatten",co_email_t:"E-Mail",co_hours_t:"Geschaeftszeiten",co_hours_d:"Mo-Sa: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - Professioneller Hersteller von LED-Schaltnetzteilen aus Zhongshan, China. Weltweiter B2B-Service seit 2014.",
  f_prod:"Produkte",f_p1:"Adapter-Serie",f_p2:"Innenraum-Netzteil",f_p3:"Wasserdichtes Netzteil",f_p4:"Regenfestes Netzteil",
  f_comp:"Unternehmen",f_c1:"Ueber uns",f_c2:"Warum wir",f_c3:"News",f_c4:"FAQ",
  f_supp:"Support",f_s1:"Kontakt",f_s2:"E-Mail",f_s3:"WhatsApp",f_s4:"Downloads",
  f_slogan:"Ihr One-Stop-LED-Netzteilhersteller"
};

T.pt = {
  n_h:"Inicio",n_a:"Sobre",n_p:"Produtos",n_s:"Specs",n_w:"Vantagens",n_b:"Noticias",n_f:"FAQ",n_c:"Contato",
  h_badge:"A escolha de mais de 500 parceiros globais",
  h_title:"Fabricante profissional de fontes de alimentacao LED",
  h_sub:"CHUGAO - Fontes de alimentacao LED direto da fabrica em Zhongshan, China. Adaptadores, drivers internos, a prova d'agua IP67/IP68 e modelos a prova de chuva com certificacao CE/UL. Atendendo compradores B2B em todo o mundo desde 2014.",
  h_btn_p:"Ver produtos",h_btn_q:"Orcamento gratis",
  s_y:"10+",s_y_l:"Anos de experiencia",s_c:"50+",s_c_l:"Paises atendidos",s_m:"200+",s_m_l:"Modelos",
  h_img_cap:"CHUGAO - Fabrica de fontes LED em Zhongshan, China",
  t_ce:"Certificado CE",t_ul:"Listado UL",t_rohs:"Conforme RoHS",t_iso:"Fabrica ISO 9001",t_moq:"MOQ baixo",t_ship:"Envio global",
  a_title:"Sobre a CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. e uma empresa de alta tecnologia especializada em P&D, producao e vendas de fontes de alimentacao LED chaveadas. Localizada em Guzhen, capital mundial da iluminacao na China.",
  a_p2:"Com mais de 10 anos de experiencia, a CHUGAO construiu uma linha completa cobrindo adaptadores, fontes internas, a prova d'agua (IP67/IP68) e a prova de chuva. Produtos exportados para mais de 50 paises.",
  a_p3:"Seguindo o principio \"Qualidade em primeiro lugar, cliente prioritario\", cada produto passa por testes rigorosos antes da entrega. Oferecemos servicos OEM/ODM para marcas globais.",
  f_fac:"Fabrica propria",f_fac_d:"Base de producao de 10.000m2",f_qc:"Controle de qualidade",f_qc_d:"100% teste de envelhecimento",f_log:"Logistica rapida",f_log_d:"7-15 dias para portos globais",f_sup:"Suporte tecnico",f_sup_d:"Resposta garantida em 24h",
  p_title:"Nossos produtos",p_sub:"Solucoes completas de fontes LED - de adaptadores compactos a unidades a prova d'agua de alta potencia.",
  p1_n:"Serie adaptadores",p1_d:"Alta eficiencia, design compacto. Entrada AC 100-240V universal. Saida DC estavel e segura para fitas e modulos LED.",
  p2_n:"Fonte interna",p2_d:"Tamanho compacto, excelente dissipacao de calor. Operacao silenciosa. Ampla faixa de entrada com PFC ativo.",
  p3_n:"Fonte a prova d'agua (IP67)",p3_d:"Classificacao IP67/IP68. Encapsulamento de silicone. Carcaca resistente a UV. Ideal para fitas LED externas, fontes e iluminacao maritima.",
  p4_n:"Fonte a prova de chuva (IP65)",p4_d:"Carcaa metalica robusta com revestimento protetor. Resistente a corrosao.",
  p_cta:"Consultar agora \u2192",
  sp_title:"Especificacoes",sp_sub:"Compare parametros-chave entre nossas series de fontes LED.",
  sp_h1:"Serie",sp_h2:"Faixa de potencia",sp_h3:"Tensao de entrada",sp_h4:"Tensao de saida",sp_h5:"Classificacao IP",sp_h6:"Eficiencia",sp_h7:"Garantia",
  sp_r1_n:"Serie adaptadores",sp_r2_n:"Fonte interna",sp_r3_n:"A prova d'agua (IP67)",sp_r4_n:"A prova de chuva (IP65)",
  sp_cta:"Solicitar ficha tecnica",
  w_title:"Por que escolher a CHUGAO",w_sub:"O que nos diferencia no mercado competitivo de fontes LED.",
  w1_t:"Preco direto da fabrica",w1_d:"Como fabricantes eliminamos intermediarios - precos competitivos sem comprometer a qualidade.",
  w2_t:"Qualidade certificada",w2_d:"Todos os produtos passam por certificacoes CE, UL e RoHS. Cada unidade passa por 100% de teste de envelhecimento.",
  w3_t:"Capacidade de P&D",w3_d:"Equipe de P&D com mais de 10 engenheiros. Solucoes OEM/ODM personalizadas.",
  w4_t:"Entrega rapida",w4_d:"Produtos padrao enviados em 7-15 dias uteis. Pedidos de amostra sao bem-vindos.",
  w5_t:"Cadeia de suprimentos estavel",w5_d:"Producao propria garante qualidade e fornecimento consistentes.",
  w6_t:"Suporte profissional",w6_d:"Equipe de vendas multilíngue (EN, ES, FR, ZH, DE, PT, RU, JA, KO, AR, IT). Resposta em 24h.",
  b_title:"Noticias do setor",b_sub:"Mantenha-se atualizado com as ultimas tendencias em iluminacao LED.",
  b1_t:"Como escolher a fonte LED certa para seu projeto",
  b1_d:"Guia completo sobre calculo de potencia, selecao de classificacao IP e dicas de instalacao.",
  b2_t:"Entendendo as classificacoes IP: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Aprenda as diferencas entre os graus de impermeabilidade e como escolher a protecao certa.",
  b3_t:"Relatorio do mercado LED 2026: impulsionadores de crescimento",
  b3_d:"Analise do mercado global de iluminacao LED e oportunidades para fabricantes.",
  t_title:"O que nossos clientes dizem",t_sub:"Confianca de parceiros B2B e distribuidores em todo o mundo.",
  t1_d:"\"Ha 3 anos adquirimos fontes LED da CHUGAO. Suas unidades IP67 sao confiaveis. O suporte tecnico responde rapido.\"",
  t1_n:"Marco R.",t1_r:"Distribuidor de iluminacao, Italia",
  t2_d:"\"Os precos direto da fabrica da CHUGAO nos economizam custos significativos. Qualidade excelente e entregas sempre pontuais.\"",
  t2_n:"Sarah K.",t2_r:"Contratante de projetos LED, EUA",
  t3_d:"\"O servico OEM e excepcional. A CHUGAO nos ajudou a desenvolver uma fonte personalizada e o resultado superou nossas expectativas.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Proprietario de marca, Franca",
  faq_title:"Perguntas frequentes",faq_sub:"Respostas rapidas a perguntas comuns.",
  faq1_q:"Qual e a quantidade minima de pedido (MOQ)?",
  faq1_a:"Nosso MOQ padrao e de 50 pecas por modelo. Para novos compradores, oferecemos pedidos de amostra com MOQ menor. Pedidos de 500+ pecas qualify para precos com desconto.",
  faq2_q:"Quais certificacoes seus produtos tem?",
  faq2_a:"Todas as nossas fontes LED sao certificadas CE e RoHS. A maioria tambem possui listagem UL.",
  faq3_q:"Qual e o periodo de garantia?",
  faq3_a:"Oferecemos 3 anos de garantia em todos os produtos padrao. Produtos OEM personalizados tem termos negociados por projeto.",
  faq4_q:"Voces fornecem servicos OEM/ODM?",
  faq4_a:"Sim, fornecemos servicos completos de OEM/ODM incluindo marca personalizada, design de embalagem e especificacoes sob medida.",
  faq5_q:"Quais sao seus termos de pagamento?",
  faq5_a:"Para novos clientes: T/T 30% de deposito, 70% antes do envio. Para parceiros estabelecidos: L/C e outros termos.",
  faq6_q:"Qual e o prazo de producao?",
  faq6_a:"Produtos padrao: 7-15 dias uteis. OEM personalizado: 20-30 dias uteis. Amostras: 5-7 dias uteis.",
  cta_title:"Pronto para comecar?",cta_sub:"Entre em contato hoje para uma consulta gratuita e orcamento personalizado.",
  cta_btn_c:"Fale conosco",cta_btn_w:"Chat no WhatsApp",cta_btn_e:"Enviar e-mail",
  inq_title:"Envie-nos uma consulta",inq_sub:"Conte-nos sobre seu projeto e responderemos em 24 horas com uma solucao personalizada.",
  inq_ok:"Obrigado! Sua consulta foi enviada. Entraremos em contato em breve.",
  inq_name:"Seu nome *",inq_email:"Endereco de e-mail *",inq_phone:"Telefone / WhatsApp",inq_company:"Empresa",
  inq_product:"Produto de interesse *",inq_sel:"Selecione uma serie",
  inq_opt1:"Adaptadores (5W-200W)",inq_opt2:"Fonte interna (50W-400W)",inq_opt3:"A prova d'agua IP67/IP68 (10W-400W)",inq_opt4:"A prova de chuva IP65 (100W-600W)",inq_opt5:"OEM / ODM personalizado",
  inq_qty:"Quantidade estimada",inq_msg:"Detalhes do projeto *",inq_submit:"Enviar consulta",
  inq_emailto:"Sua consulta sera enviada para",inq_via:"atraves do seu app de e-mail.",inq_copy:"Sem app de e-mail? Clique para copiar.",inq_note:"Ao enviar este formulario, voce concorda com nossa politica de privacidade.",
  inq_why:"Por que consultar a CHUGAO?",
  inq_w1:"Consulta tecnica gratuita em 24 horas",inq_w2:"Recomendacao personalizada",inq_w3:"Orcamento direto da fabrica",inq_w4:"Suporte de amostra para novos compradores",inq_w5:"Documentos de certificacao completos",
  inq_fast:"Prefere uma resposta mais rapida?",inq_fast_d:"Fale conosco diretamente pelo WhatsApp.",inq_wa:"Chat no WhatsApp",
  co_title:"Fale conosco",co_addr_t:"Endereco",co_phone_t:"Telefone",co_wa_t:"WhatsApp",co_wa_a:"Conversar agora",co_email_t:"E-mail",co_hours_t:"Horario",co_hours_d:"Seg-Sab: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - Fabricante profissional de fontes de alimentacao LED chaveadas de Zhongshan, China. Atendendo compradores B2B desde 2014.",
  f_prod:"Produtos",f_p1:"Adaptadores",f_p2:"Fonte interna",f_p3:"A prova d'agua",f_p4:"A prova de chuva",
  f_comp:"Empresa",f_c1:"Sobre nos",f_c2:"Por que nos",f_c3:"Noticias",f_c4:"FAQ",
  f_supp:"Suporte",f_s1:"Contato",f_s2:"E-mail",f_s3:"WhatsApp",f_s4:"Downloads",
  f_slogan:"Fabricante de fontes LED tudo-em-um"
};

T.ru = {
  n_h:"Главная",n_a:"О нас",n_p:"Продукция",n_s:"Характеристики",n_w:"Преимущества",n_b:"Новости",n_f:"FAQ",n_c:"Контакты",
  h_badge:"Выбор более 500 глобальных партнёров",
  h_title:"Профессиональный производитель импульсных блоков питания для LED",
  h_sub:"CHUGAO - блоки питания для LED напрямую с завода в Чжуншане, Китай. Адаптеры, драйверы для помещений, влагозащищённые IP67/IP68 и влагозащищённые от дождя, сертифицированные CE/UL. Обслуживаем B2B-покупателей по всему миру с 2014 года.",
  h_btn_p:"Смотреть продукцию",h_btn_q:"Бесплатное КП",
  s_y:"10+",s_y_l:"Лет опыта",s_c:"50+",s_c_l:"Стран",s_m:"200+",s_m_l:"Моделей",
  h_img_cap:"CHUGAO - завод LED-блоков питания в Чжуншане, Китай",
  t_ce:"Сертификат CE",t_ul:"Внесён в UL",t_rohs:"Соответствует RoHS",t_iso:"Завод ISO 9001",t_moq:"Низкий MOQ",t_ship:"Глобальная доставка",
  a_title:"О компании CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. - высокотехнологичное предприятие, специализирующееся на НИОКР, производстве и продаже импульсных блоков питания для LED. Расположено в Гужене - мировой столице освещения в Китае.",
  a_p2:"Имея более 10 лет опыта, CHUGAO предлагает полный ассортимент: адаптеры, блоки для помещений, влагозащищённые (IP67/IP68) и для защиты от дождя. Продукция экспортируется в более чем 50 стран.",
  a_p3:"Следуя принципу «Качество прежде всего, клиент - главный приоритет», каждое изделие проходит строгие испытания перед отгрузкой. Мы предоставляем услуги OEM/ODM для глобальных брендов.",
  f_fac:"Собственный завод",f_fac_d:"Производственная база 10 000 м2",f_qc:"Контроль качества",f_qc_d:"100% тест на старение",f_log:"Быстрая логистика",f_log_d:"7-15 дней до мировых портов",f_sup:"Техподдержка",f_sup_d:"Ответ в течение 24 часов",
  p_title:"Наша продукция",p_sub:"Полный спектр LED-блоков питания - от компактных адаптеров до мощных влагозащищённых моделей.",
  p1_n:"Серия адаптеров",p1_d:"Высокая эффективность, компактный дизайн. Универсальный вход AC 100-240В. Стабильный выход DC для LED-лент и модулей.",
  p2_n:"Блок питания для помещений",p2_d:"Компактный размер, отличный теплоотвод. Бесшумная работа. Широкий диапазон входа с активным PFC.",
  p3_n:"Влагозащищённый блок (IP67)",p3_d:"Степень защиты IP67/IP68. Полная силиконовая заливка. УФ-стойкий корпус. Идеален для наружных LED-лент, фонтанов и морского освещения.",
  p4_n:"Дождезащитный блок (IP65)",p4_d:"Прочный металлический корпус с защитным покрытием. Устойчив к коррозии.",
  p_cta:"Запросить сейчас \u2192",
  sp_title:"Технические характеристики",sp_sub:"Сравните ключевые параметры наших серий LED-блоков питания.",
  sp_h1:"Серия",sp_h2:"Диапазон мощности",sp_h3:"Входное напряжение",sp_h4:"Выходное напряжение",sp_h5:"Класс IP",sp_h6:"КПД",sp_h7:"Гарантия",
  sp_r1_n:"Серия адаптеров",sp_r2_n:"Блок для помещений",sp_r3_n:"Влагозащищённый (IP67)",sp_r4_n:"Дождезащитный (IP65)",
  sp_cta:"Запросить полный даташит",
  w_title:"Почему выбирают CHUGAO",w_sub:"Что отличает нас на конкурентном рынке LED-блоков питания.",
  w1_t:"Цены напрямую с завода",w1_d:"Как производитель мы убираем посредников - конкурентные цены без потери качества.",
  w2_t:"Сертифицированное качество",w2_d:"Вся продукция прошла сертификацию CE, UL и RoHS. Каждое изделие проходит 100% тест на старение.",
  w3_t:"Возможности НИОКР",w3_d:"Команда НИОКР из более чем 10 инженеров. Индивидуальные OEM/ODM-решения.",
  w4_t:"Быстрая доставка",w4_d:"Стандартная продукция отгружается за 7-15 рабочих дней. Принимаем заказы образцов.",
  w5_t:"Стабильная цепочка поставок",w5_d:"Собственное производство гарантирует стабильное качество и поставки.",
  w6_t:"Профессиональная поддержка",w6_d:"Многоязычная команда продаж (EN, ES, FR, ZH, DE, PT, RU, JA, KO, AR, IT). Ответ в течение 24 часов.",
  b_title:"Новости отрасли",b_sub:"Будьте в курсе последних тенденций в LED-освещении.",
  b1_t:"Как выбрать правильный LED-блок питания для вашего проекта",
  b1_d:"Полное руководство по расчёту мощности, выбору класса IP и советам по установке.",
  b2_t:"Понимание классов IP: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Узнайте разницу между уровнями влагозащиты и как выбрать подходящую защиту.",
  b3_t:"Обзор рынка LED-освещения 2026: драйверы роста и возможности",
  b3_d:"Анализ глобального рынка LED-освещения и возможностей для производителей.",
  t_title:"Отзывы клиентов",t_sub:"Доверие B2B-партнёров и дистрибьюторов по всему миру.",
  t1_d:"«Уже 3 года закупаем LED-блоки у CHUGAO. Их IP67-блоки надёжны. Техподдержка отвечает быстро и помогает с выбором.»",
  t1_n:"Marco R.",t1_r:"Дистрибьютор освещения, Италия",
  t2_d:"«Цены CHUGAO напрямую с завода экономят нам значительные средства. Качество отличное, поставки всегда в срок.»",
  t2_n:"Sarah K.",t2_r:"Подрядчик LED-проектов, США",
  t3_d:"«OEM-сервис выдающийся. CHUGAO помогли нам разработать индивидуальный блок питания, и результат превзошёл наши ожидания.»",
  t3_n:"Jean-Pierre L.",t3_r:"Владелец бренда, Франция",
  faq_title:"Частые вопросы",faq_sub:"Быстрые ответы на распространённые вопросы.",
  faq1_q:"Каков ваш минимальный объём заказа (MOQ)?",
  faq1_a:"Стандартный MOQ - 50 штук на модель. Для новых покупателей доступны заказы образцов с меньшим MOQ. Заказы от 500+ штук получают скидки.",
  faq2_q:"Какие сертификаты имеет ваша продукция?",
  faq2_a:"Все наши LED-блоки сертифицированы CE и RoHS. Большинство также внесены в UL.",
  faq3_q:"Какой гарантийный срок?",
  faq3_a:"Мы предоставляем 3-летнюю гарантию на всю стандартную продукцию. Условия для OEM обсуждаются индивидуально.",
  faq4_q:"Предоставляете ли вы услуги OEM/ODM?",
  faq4_a:"Да, мы предоставляем полный спектр OEM/ODM-услуг, включая брендирование, дизайн упаковки и индивидуальные спецификации.",
  faq5_q:"Каковы ваши условия оплаты?",
  faq5_a:"Для новых клиентов: T/T 30% предоплата, 70% перед отгрузкой. Для постоянных партнёров: L/C и другие условия.",
  faq6_q:"Каковы сроки производства?",
  faq6_a:"Стандартная продукция: 7-15 рабочих дней. Индивидуальные OEM: 20-30 рабочих дней. Образцы: 5-7 рабочих дней.",
  cta_title:"Готовы начать?",cta_sub:"Свяжитесь с нами сегодня для бесплатной консультации и индивидуального расчёта.",
  cta_btn_c:"Связаться",cta_btn_w:"Чат в WhatsApp",cta_btn_e:"Написать на email",
  inq_title:"Отправьте запрос",inq_sub:"Расскажите о вашем проекте, и мы ответим в течение 24 часов с индивидуальным решением.",
  inq_ok:"Спасибо! Ваш запрос отправлен. Мы свяжемся с вами в ближайшее время.",
  inq_name:"Ваше имя *",inq_email:"Электронная почта *",inq_phone:"Телефон / WhatsApp",inq_company:"Компания",
  inq_product:"Интересующая продукция *",inq_sel:"Выберите серию",
  inq_opt1:"Адаптеры (5W-200W)",inq_opt2:"Блок для помещений (50W-400W)",inq_opt3:"Влагозащищённый IP67/IP68 (10W-400W)",inq_opt4:"Дождезащитный IP65 (100W-600W)",inq_opt5:"Индивидуальный OEM / ODM",
  inq_qty:"Предполагаемое количество",inq_msg:"Детали проекта *",inq_submit:"Отправить запрос",
  inq_emailto:"Ваш запрос будет отправлен на",inq_via:"через ваше почтовое приложение.",inq_copy:"Нет почтового приложения? Нажмите для копирования.",inq_note:"Отправляя форму, вы соглашаетесь с нашей политикой конфиденциальности.",
  inq_why:"Почему стоит обратиться в CHUGAO?",
  inq_w1:"Бесплатная техконсультация в течение 24 часов",inq_w2:"Индивидуальная рекомендация продукции",inq_w3:"Конкурентная цена напрямую с завода",inq_w4:"Поддержка образцов для новых покупателей",inq_w5:"Полный комплект сертификатов",
  inq_fast:"Хотите более быстрый ответ?",inq_fast_d:"Свяжитесь с нами напрямую через WhatsApp для мгновенной коммуникации.",inq_wa:"Чат в WhatsApp",
  co_title:"Свяжитесь с нами",co_addr_t:"Адрес",co_phone_t:"Телефон",co_wa_t:"WhatsApp",co_wa_a:"Написать сейчас",co_email_t:"E-mail",co_hours_t:"Часы работы",co_hours_d:"Пн-Сб: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - профессиональный производитель импульсных блоков питания для LED из Чжуншаня, Китай. Обслуживаем B2B-покупателей с 2014 года.",
  f_prod:"Продукция",f_p1:"Адаптеры",f_p2:"Блок для помещений",f_p3:"Влагозащищённый блок",f_p4:"Дождезащитный блок",
  f_comp:"Компания",f_c1:"О нас",f_c2:"Почему мы",f_c3:"Новости",f_c4:"FAQ",
  f_supp:"Поддержка",f_s1:"Контакты",f_s2:"E-mail",f_s3:"WhatsApp",f_s4:"Загрузки",
  f_slogan:"Универсальный производитель LED-блоков питания"
};

T.ja = {
  n_h:"ホーム",n_a:"会社概要",n_p:"製品",n_s:"仕様",n_w:"強み",n_b:"ニュース",n_f:"FAQ",n_c:"お問い合わせ",
  h_badge:"500社以上のグローバルパートナーに選ばれています",
  h_title:"プロ仕様のLEDスイッチング電源メーカー",
  h_sub:"CHUGAO - 中国・中山の工場直送LED電源。CE/UL認証取得のアダプタ、屋内用ドライバー、防水IP67/IP68モデル、防雨モデルを、2014年より世界のB2Bバイヤー様へお届けしています。",
  h_btn_p:"製品を見る",h_btn_q:"無料お見積もり",
  s_y:"10+",s_y_l:"年の実績",s_c:"50+",s_c_l:"対応国",s_m:"200+",s_m_l:"製品モデル",
  h_img_cap:"CHUGAO - 中国・中山のLED電源工場",
  t_ce:"CE認証",t_ul:"UL取得",t_rohs:"RoHS適合",t_iso:"ISO 9001工場",t_moq:"小ロット対応",t_ship:"全世界発送",
  a_title:"CHUGAOについて",
  a_p1:"中山市楚高電子科技有限公司は、LEDスイッチング電源のR&D、製造、販売に特化したハイテク企業です。世界の照明の都として知られる中山古鎮に立地し、効率的で安定した省エネ電源ソリューションを世界のお客様に提供しています。",
  a_p2:"10年以上の実績を持ち、CHUGAOはアダプタ、屋内用電源、防水電源(IP67/IP68)、防雨電源を取り揃えています。製品は50カ国以上に輸出され、商業照明、産業照明、屋外サイネージで広く使用されています。",
  a_p3:"「品質第一、顧客優先」の理念のもと、出荷前に全品厳格な検査を実施。世界のブランド向けにOEM/ODMサービスを提供しています。",
  f_fac:"自社工場",f_fac_d:"10,000m2の生産拠点",f_qc:"品質管理",f_qc_d:"出荷前100%エージングテスト",f_log:"迅速な物流",f_log_d:"7-15日で世界各港へ",f_sup:"技術サポート",f_sup_d:"24時間以内回答保証",
  p_title:"製品一覧",p_sub:"コンパクトアダプタから高出力防水モデルまで、フルシリーズのLED電源ソリューション。",
  p1_n:"アダプタシリーズ",p1_d:"高効率、コンパクト設計。ユニバーサルAC 100-240V入力。LEDストリップ・モジュール向け安全・安定DC出力。",
  p2_n:"屋内用電源",p2_d:"コンパクトサイズ、優れた放熱性。静音動作。アクティブPFC搭載で広い入力範囲に対応。",
  p3_n:"防水電源(IP67)",p3_d:"IP67/IP68等級。完全密封シリコン充填。UV耐性ハウジング。屋外LEDストリップ、噴水、船舶照明に最適。",
  p4_n:"防雨電源(IP65)",p4_d:"堅牢な金属ケースと保護コーティング。耐食性。湿度環境や半屋外LED設置に最適。",
  p_cta:"今すぐお問い合わせ \u2192",
  sp_title:"製品仕様",sp_sub:"LED電源シリーズ間の主要パラメータを比較。",
  sp_h1:"シリーズ",sp_h2:"出力範囲",sp_h3:"入力電圧",sp_h4:"出力電圧",sp_h5:"IP等級",sp_h6:"効率",sp_h7:"保証",
  sp_r1_n:"アダプタシリーズ",sp_r2_n:"屋内用電源",sp_r3_n:"防水(IP67)",sp_r4_n:"防雨(IP65)",
  sp_cta:"データシートを請求",
  w_title:"CHUGAOが選ばれる理由",w_sub:"競争の激しいLED電源市場で私たちを選ぶ理由。",
  w1_t:"工場直販価格",w1_d:"メーカーとして中間業者を排除し、品質を損なうことなく競争力のある価格を実現。大量注文でさらにお得。",
  w2_t:"認証品質",w2_d:"全製品がCE、UL、RoHS認証を取得。出荷前に全台100%エージングテストと全数検査を実施。",
  w3_t:"R&D力",w3_d:"10名以上のエンジニアによるR&Dチーム。プロジェクト要件に合わせたカスタムOEM/ODMソリューションを提供。",
  w4_t:"迅速な納期",w4_d:"標準製品は7-15営業日以内に発送。サンプル注文も歓迎。",
  w5_t:"安定したサプライチェーン",w5_d:"社内生産により、品質と供給を安定確保。第三者工場に依存しません。",
  w6_t:"プロフェッショナルサポート",w6_d:"多言語営業チーム(英、西、仏、中、独、葡、露、日、韓、阿、伊)。24時間以内回答。",
  b_title:"業界ニュース",b_sub:"LED照明・電源技術の最新トレンドをお届け。",
  b1_t:"プロジェクトに合ったLED電源の選び方",
  b1_d:"ワット数計算、IP等級選定、設置のヒントまで網羅した総合ガイド。",
  b2_t:"IP等級の理解:IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"防水等級のと違いと、設置環境に適した保護レベルの選び方を解説。",
  b3_t:"2026年LED照明市場レポート:成長ドライバーとチャンス",
  b3_d:"世界のLED照明市場、新興用途、製造業の機会を分析。",
  t_title:"お客様の声",t_sub:"世界各国のB2Bパートナーと照明販売代理店から信頼されています。",
  t1_d:"「3年前からCHUGAOからLED電源を調達しています。IP67防水モデルは一貫して信頼性が高く、技術サポートも迅速で的確です。」",
  t1_n:"Marco R.",t1_r:"イタリア 照明販売代理店",
  t2_d:"「CHUGAOの工場直販価格は以前のサプライヤーより大幅なコスト削減。品質は優秀で納期も正確です。」",
  t2_n:"Sarah K.",t2_r:"アメリカ LEDプロジェクト請負業者",
  t3_d:"「OEMサービスは卓越しています。CHUGAOは当社のカスタム電源開発を支援してくれ、最終製品は期待以上でした。」",
  t3_n:"Jean-Pierre L.",t3_r:"フランス ブランドオーナー",
  faq_title:"よくある質問",faq_sub:"世界のバイヤー様からよくいただく質問への回答。",
  faq1_q:"最小発注数量(MOQ)は?",
  faq1_a:"標準MOQは1モデルあたり50個です。新規のお客様には低MOQのサンプル注文をご用意しています。500個以上の大量注文は割引価格の対象です。",
  faq2_q:"製品の認証は?",
  faq2_a:"全LED電源がCEおよびRoHS認証を取得。多くはUL取得済み。詳細はお問い合わせください。",
  faq3_q:"保証期間は?",
  faq3_a:"標準製品には3年保証。カスタムOEMは案件ごとに保証条件を協議。",
  faq4_q:"OEM/ODMサービスはありますか?",
  faq4_a:"はい。カスタムブランド、包装設計、仕様カスタマイズを含むフルOEM/ODMサービスを提供しています。",
  faq5_q:"支払い条件は?",
  faq5_a:"新規のお客様: T/T 30%前金、出荷前70%。既存パートナー: L/Cなど各種対応。サンプル注文はPayPal、アリババ信用保証も対応。",
  faq6_q:"生産リードタイムは?",
  faq6_a:"標準製品: 7-15営業日。カスタムOEM: 20-30営業日。サンプル: 5-7営業日。",
  cta_title:"始める準備はできましたか?",cta_sub:"無料製品コンサルティングとカスタム見積もりについては今すぐお問い合わせください。",
  cta_btn_c:"今すぐお問い合わせ",cta_btn_w:"WhatsAppでチャット",cta_btn_e:"メールを送る",
  inq_title:"お問い合わせを送信",inq_sub:"プロジェクトについてお聞かせください。24時間以内にカスタマイズされたソリューションでお返しします。",
  inq_ok:"ありがとうございます!お問い合わせを受け付けました。追ってご連絡いたします。",
  inq_name:"お名前 *",inq_email:"メールアドレス *",inq_phone:"電話 / WhatsApp",inq_company:"会社名",
  inq_product:"ご関心のある製品 *",inq_sel:"製品シリーズを選択",
  inq_opt1:"アダプタシリーズ(5W-200W)",inq_opt2:"屋内用電源(50W-400W)",inq_opt3:"防水電源 IP67/IP68(10W-400W)",inq_opt4:"防雨電源 IP65(100W-600W)",inq_opt5:"カスタム OEM / ODM",
  inq_qty:"想定数量",inq_msg:"プロジェクト詳細 / メッセージ *",inq_submit:"送信",
  inq_emailto:"お問い合わせ送信先",inq_via:"メールアプリ経由で送信されます。",inq_copy:"メールアプリがない?クリックでコピー。",inq_note:"フォーム送信により、プライバシーポリシーに同意したものとみなされます。",
  inq_why:"CHUGAOに問い合わせる理由は?",
  inq_w1:"24時間以内の無料技術相談",inq_w2:"カスタマイズされた製品推奨",inq_w3:"競争力のある工場直販見積もり",inq_w4:"新規バイヤー様へのサンプル対応",inq_w5:"完全な認証書類",
  inq_fast:"より迅速な返信をご希望ですか?",inq_fast_d:"WhatsAppで直接ご連絡いただければ、即時対応できます。",inq_wa:"WhatsAppでチャット",
  co_title:"お問い合わせ",co_addr_t:"住所",co_phone_t:"電話",co_wa_t:"WhatsApp",co_wa_a:"今すぐチャット",co_email_t:"メール",co_hours_t:"営業時間",co_hours_d:"月〜土: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - 中国・中山のプロ仕様LEDスイッチング電源メーカー。2014年より世界のB2Bバイヤー様へお届けしています。",
  f_prod:"製品",f_p1:"アダプタシリーズ",f_p2:"屋内用電源",f_p3:"防水電源",f_p4:"防雨電源",
  f_comp:"会社",f_c1:"会社概要",f_c2:"選ばれる理由",f_c3:"ニュース",f_c4:"FAQ",
  f_supp:"サポート",f_s1:"お問い合わせ",f_s2:"メール",f_s3:"WhatsApp",f_s4:"ダウンロード",
  f_slogan:"ワンストップLED電源メーカー"
};

T.ko = {
  n_h:"홈",n_a:"회사 소개",n_p:"제품",n_s:"사양",n_w:"장점",n_b:"뉴스",n_f:"FAQ",n_c:"문의",
  h_badge:"500개 이상의 글로벌 파트너가 선택",
  h_title:"전문 LED 스위칭 전원 공급 장치 제조사",
  h_sub:"CHUGAO - 중국 중산 공장 직송 LED 전원. CE/UL 인증 어댑터, 실내용 드라이버, 방수 IP67/IP68 모델, 방우 모델을 2014년부터 전 세계 B2B 바이어에게 공급하고 있습니다.",
  h_btn_p:"제품 보기",h_btn_q:"무료 견적 요청",
  s_y:"10+",s_y_l:"년 업력",s_c:"50+",s_c_l:"수출 국가",s_m:"200+",s_m_l:"제품 모델",
  h_img_cap:"CHUGAO - 중국 중산 LED 전원 공장",
  t_ce:"CE 인증",t_ul:"UL 등재",t_rohs:"RoHS 준수",t_iso:"ISO 9001 공장",t_moq:"소량 MOQ 가능",t_ship:"전 세계 배송",
  a_title:"CHUGAO 소개",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd.는 LED 스위칭 전원 공급 장치의 R&D, 생산 및 판매를 전문으로 하는 하이테크 기업입니다. 세계적인 조명의 도시 중국 구전(古鎮)에 위치합니다.",
  a_p2:"10년 이상의 경험을 바탕으로 CHUGAO는 어댑터, 실내용 전원, 방수 전원(IP67/IP68), 방우 전원 등 완벽한 제품 라인을 구축했습니다. 제품은 50개국 이상에 수출됩니다.",
  a_p3:"\"품질 우선, 고객 우선\"의 원칙을 지키며, 모든 제품은 출하 전에 엄격한 테스트를 거칩니다. 글로벌 브랜드에 OEM/ODM 서비스를 제공합니다.",
  f_fac:"자체 공장",f_fac_d:"10,000m2 생산 단지",f_qc:"품질 관리",f_qc_d:"출하 전 100% 에이징 테스트",f_log:"신속한 물류",f_log_d:"7-15일 전 세계 항구 도착",f_sup:"기술 지원",f_sup_d:"24시간 응답 보장",
  p_title:"제품 소개",p_sub:"컴팩트 어댑터부터 고출력 방수 모델까지 풀 라인업 LED 전원 솔루션.",
  p1_n:"어댑터 시리즈",p1_d:"고효율, 컴팩트 디자인. 범용 AC 100-240V 입력. LED 스트립 및 모듈용 안전하고 안정적인 DC 출력.",
  p2_n:"실내용 전원",p2_d:"컴팩트 사이즈, 뛰어난 방열. 무소음 작동. 액티브 PFC로 넓은 입력 범위 지원.",
  p3_n:"방수 전원 (IP67)",p3_d:"IP67/IP68 등급. 완전 밀봉 실리콘 충진. UV 저항 하우징. 야외 LED 스트립, 분수, 선박 조명에 이상적.",
  p4_n:"방우 전원 (IP65)",p4_d:"견고한 금속 케이스와 보호 코팅. 내식성. 습한 환경과 반 야외 LED 설치에 적합.",
  p_cta:"지금 문의 \u2192",
  sp_title:"제품 사양",sp_sub:"LED 전원 시리즈의 핵심 파라미터를 비교하세요.",
  sp_h1:"시리즈",sp_h2:"출력 범위",sp_h3:"입력 전압",sp_h4:"출력 전압",sp_h5:"IP 등급",sp_h6:"효율",sp_h7:"보증",
  sp_r1_n:"어댑터 시리즈",sp_r2_n:"실내용 전원",sp_r3_n:"방수 (IP67)",sp_r4_n:"방우 (IP65)",
  sp_cta:"전체 데이터시트 요청",
  w_title:"CHUGAO를 선택하는 이유",w_sub:"경쟁激烈的인 LED 전원 시장에서 우리의 차별점.",
  w1_t:"공장 직거래 가격",w1_d:"제조사로서 중간상을 제거하여 품질을損하지 않으면서 경쟁력 있는 가격을 제공합니다.",
  w2_t:"인증된 품질",w2_d:"모든 제품은 CE, UL, RoHS 인증을 획득했습니다. 출하 전 100% 에이징 테스트를 거칩니다.",
  w3_t:"R&D 역량",w3_d:"10명 이상의 엔지니어로 구성된 R&D 팀. 맞춤형 OEM/ODM 솔루션 제공.",
  w4_t:"신속한 배송",w4_d:"표준 제품은 영업일 기준 7-15일 내 배송. 샘플 주문 환영.",
  w5_t:"안정적인 공급망",w5_d:"자체 생산으로 일관된 품질과 공급을 보장. 제3자 공장 의존 없음.",
  w6_t:"전문적인 지원",w6_d:"다국어 영업팀(영, 서, 불, 중, 독, 포, 러, 일, 한, 아, 이). 24시간 내 응답.",
  b_title:"업계 뉴스",b_sub:"LED 조명 및 전원 기술의 최신 트렌드를 만나보세요.",
  b1_t:"프로젝트에 적합한 LED 전원 선택 방법",
  b1_d:"와트 계산, IP 등급 선택, 설치 팁을 다루는 종합 가이드.",
  b2_t:"IP 등급 이해: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"방수 등급의 차이점과 설치 환경에 맞는 보호 수준 선택 방법을 알아보세요.",
  b3_t:"2026 LED 조명 시장 보고서: 성장 동력과 기회",
  b3_d:"글로벌 LED 조명 시장과 신흥 용도, 제조업체의 기회를 분석합니다.",
  t_title:"고객 후기",t_sub:"전 세계 B2B 파트너와 조명 유통업체의 신뢰.",
  t1_d:"\"3년 동안 CHUGAO에서 LED 전원을 조달해왔습니다. IP67 방수 모델은 안정적이고, 기술 지원팀이 빠르게 응답하여 적합한 제품을 선택하도록 도와줍니다.\"",
  t1_n:"Marco R.",t1_r:"이탈리아 조명 유통업체",
  t2_d:"\"CHUGAO의 공장 직거래 가격은 이전 공급업체에 비해 상당한 비용을 절감해줍니다. 품질이 우수하고 배송은 항상准时합니다.\"",
  t2_n:"Sarah K.",t2_r:"미국 LED 프로젝트 시공사",
  t3_d:"\"OEM 서비스가 매우 훌륭합니다. CHUGAO는 당사의 맞춤형 전원 개발을 도와주었고, 최종 제품은 기대 이상이었습니다.\"",
  t3_n:"Jean-Pierre L.",t3_r:"프랑스 브랜드 소유자",
  faq_title:"자주 묻는 질문",faq_sub:"글로벌 바이어의 일반적인 질문에 대한 빠른 답변.",
  faq1_q:"최소 주문 수량(MOQ)은?",
  faq1_a:"표준 MOQ는 모델당 50개입니다. 첫 주문 고객에게는 더 낮은 MOQ의 샘플 주문을 제공합니다. 500개 이상의 대량 주문은 할인 가격이 적용됩니다.",
  faq2_q:"제품의 인증은?",
  faq2_a:"모든 LED 전원은 CE 및 RoHS 인증을 받았습니다. 대부분 UL 등재도 되어 있습니다. 모델별로 다를 수 있으니 자세한 내용은 문의해 주세요.",
  faq3_q:"보증 기간은?",
  faq3_a:"표준 제품에는 3년 보증을 제공합니다. 맞춤형 OEM 제품은 프로젝트별로 보증 조건을 협의합니다.",
  faq4_q:"OEM/ODM 서비스를 제공하나요?",
  faq4_a:"예, 맞춤 브랜딩, 패키지 디자인, 사양을 포함한 전체 OEM/ODM 서비스를 제공합니다.",
  faq5_q:"결제 조건은?",
  faq5_a:"신규 고객: T/T 30% 보증금, 출하 전 70%. 기존 파트너: L/C 및 기타 조건 가능. 샘플 주문은 PayPal, 알리바바 무역 보증도 가능합니다.",
  faq6_q:"생산 리드타임은?",
  faq6_a:"표준 제품: 영업일 7-15일. 맞춤형 OEM: 영업일 20-30일. 샘플: 영업일 5-7일.",
  cta_title:"시작할 준비가 되셨나요?",cta_sub:"무료 제품 상담과 맞춤형 견적을 위해 오늘 문의하세요.",
  cta_btn_c:"지금 문의하기",cta_btn_w:"WhatsApp으로 채팅",cta_btn_e:"이메일 보내기",
  inq_title:"문의 보내기",inq_sub:"프로젝트에 대해 알려주시면 24시간 내에 맞춤형 솔루션으로 답변드리겠습니다.",
  inq_ok:"감사합니다! 문의가 제출되었습니다. 곧 연락드리겠습니다.",
  inq_name:"이름 *",inq_email:"이메일 주소 *",inq_phone:"전화 / WhatsApp",inq_company:"회사명",
  inq_product:"관심 제품 *",inq_sel:"제품 시리즈 선택",
  inq_opt1:"어댑터 시리즈(5W-200W)",inq_opt2:"실내용 전원(50W-400W)",inq_opt3:"방수 전원 IP67/IP68(10W-400W)",inq_opt4:"방우 전원 IP65(100W-600W)",inq_opt5:"맞춤형 OEM / ODM",
  inq_qty:"예상 수량",inq_msg:"프로젝트 상세 / 메시지 *",inq_submit:"문의 제출",
  inq_emailto:"문의가 전송될 주소",inq_via:"이메일 앱을 통해 전송됩니다.",inq_copy:"이메일 앱이 없으신가요? 클릭하여 복사하세요.",inq_note:"이 양식을 제출함으로써 당사의 개인정보 보호정책에 동의하게 됩니다.",
  inq_why:"CHUGAO에 문의해야 하는 이유?",
  inq_w1:"24시간 내 무료 기술 상담",inq_w2:"맞춤형 제품 추천",inq_w3:"경쟁력 있는 공장 직거래 견적",inq_w4:"첫 주문 고객을 위한 샘플 지원",inq_w5:"전체 인증 문서 제공",
  inq_fast:"더 빠른 응답을 원하시나요?",inq_fast_d:"WhatsApp으로 직접 연락주시면 즉시 소통할 수 있습니다.",inq_wa:"WhatsApp 채팅",
  co_title:"문의하기",co_addr_t:"주소",co_phone_t:"전화",co_wa_t:"WhatsApp",co_wa_a:"지금 채팅",co_email_t:"이메일",co_hours_t:"영업 시간",co_hours_d:"월-토: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - 중국 중산의 전문 LED 스위칭 전원 공급 장치 제조사. 2014년부터 전 세계 B2B 바이어에게 서비스를 제공합니다.",
  f_prod:"제품",f_p1:"어댑터 시리즈",f_p2:"실내용 전원",f_p3:"방수 전원",f_p4:"방우 전원",
  f_comp:"회사",f_c1:"회사 소개",f_c2:"선택해야 하는 이유",f_c3:"뉴스",f_c4:"FAQ",
  f_supp:"지원",f_s1:"문의",f_s2:"이메일",f_s3:"WhatsApp",f_s4:"다운로드",
  f_slogan:"원스톱 LED 전원 공급 장치 제조사"
};

T.ar = {
  n_h:"الرئيسية",n_a:"من نحن",n_p:"المنتجات",n_s:"المواصفات",n_w:"لماذا نحن",n_b:"الأخبار",n_f:"الأسئلة",n_c:"اتصل بنا",
  h_badge:"اختيار أكثر من 500 شريك عالمي",
  h_title:"شركة مصنعة احترافية لمصادر طاقة LED",
  h_sub:"CHUGAO - مصادر طاقة LED مباشرة من المصنع في تشونغشان، الصين. محولات معتمدة CE/UL، ومحركات داخلية، ووحدات مقاومة للماء IP67/IP68، ونماذج مقاومة للمطر. نخدم مشتري B2B حول العالم منذ 2014.",
  h_btn_p:"عرض المنتجات",h_btn_q:"احصل على عرض سعر",
  s_y:"10+",s_y_l:"سنوات الخبرة",s_c:"50+",s_c_l:"البلدان المخدومة",s_m:"200+",s_m_l:"طرازات المنتجات",
  h_img_cap:"CHUGAO - مصنع مصادر طاقة LED في تشونغشان، الصين",
  t_ce:"معتمد CE",t_ul:"مسجل في UL",t_rohs:"متوافق مع RoHS",t_iso:"مصنع ISO 9001",t_moq:"حد أدنى منخفض متاح",t_ship:"شحن عالمي",
  a_title:"عن CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. هي مؤسسة عالية التقنية متخصصة في البحث والتطوير وإنتاج وبيع مصادر طاقة LED. تقع في غوزن - عاصمة الإضاءة العالمية في الصين.",
  a_p2:"مع أكثر من 10 سنوات من الخبرة، بنت CHUGAO خطًا شاملاً يغطي المحولات ومصادر الطاقة الداخلية ومصادر مقاومة الماء (IP67/IP68) ومصادر مقاومة المطر. يتم تصدير المنتجات إلى أكثر من 50 دولة.",
  a_p3:"وفقًا لمبدأ \"الجودة أولاً، العميل أولاً\"، يخضع كل منتج لاختبارات صارمة قبل التسليم. نقدم خدمات OEM/ODM للعلامات التجارية العالمية.",
  f_fac:"مصنع خاص",f_fac_d:"قاعدة إنتاج 10,000m2",f_qc:"مراقبة الجودة",f_qc_d:"اختبار تقادم 100% قبل الشحن",f_log:"خدمات لوجستية سريعة",f_log_d:"7-15 يومًا إلى الموانئ العالمية",f_sup:"الدعم الفني",f_sup_d:"استجابة مضمونة خلال 24 ساعة",
  p_title:"منتجاتنا",p_sub:"حلول شاملة لمصادر طاقة LED - من المحولات المدمجة إلى الوحدات المقاومة للماء عالية الطاقة.",
  p1_n:"سلسلة المحولات",p1_d:"كفاءة عالية، تصميم مدمج. دخل AC 100-240V عام. خرج DC مستقر وآمن لشرائط ووحدات LED.",
  p2_n:"مصدر طاقة داخلي",p2_d:"حجم مدمج، تبديد حرارة ممتاز. تشغيل صامت. نطاق دخل واسع مع PFC نشط.",
  p3_n:"مصدر طاقة مقاوم للماء (IP67)",p3_d:"تصنيف IP67/IP68. حشو سيليكون محكم بالكامل. هيكل مقاوم للأشعة فوق البنفسجية. مثالي لشرائط LED الخارجية والنوافير والإضاءة البحرية.",
  p4_n:"مصدر طاقة مقاوم للمطر (IP65)",p4_d:"هيكل معدني قوي مع طلاء واقي. مقاوم للتآكل. مثالي للبيئات الرطبة.",
  p_cta:"استفسر الآن \u2192",
  sp_title:"مواصفات المنتج",sp_sub:"قارن المعايير الرئيسية عبر سلاسل مصادر طاقة LED.",
  sp_h1:"السلسلة",sp_h2:"نطاق الطاقة",sp_h3:"جهد الدخل",sp_h4:"جهد الخرج",sp_h5:"تصنيف IP",sp_h6:"الكفاءة",sp_h7:"الضمان",
  sp_r1_n:"سلسلة المحولات",sp_r2_n:"مصدر داخلي",sp_r3_n:"مقاوم للماء (IP67)",sp_r4_n:"مقاوم للمطر (IP65)",
  sp_cta:"اطلب ورقة البيانات الكاملة",
  w_title:"لماذا تختار CHUGAO",w_sub:"ما يميزنا في سوق مصادر طاقة LED التنافسي.",
  w1_t:"أسعار مباشرة من المصنع",w1_d:"كشركة مصنعة، نقضي على الوسطاء - نقدم أسعارًا تنافسية دون المساس بالجودة.",
  w2_t:"جودة معتمدة",w2_d:"جميع المنتجات حاصلة على شهادات CE وUL وRoHS. تخضع كل وحدة لاختبار تقادم بنسبة 100%.",
  w3_t:"قدرات البحث والتطوير",w3_d:"فريق بحث وتطوير يضم أكثر من 10 مهندسين. نقدم حلول OEM/ODM مخصصة.",
  w4_t:"تسليم سريع",w4_d:"يتم شحن المنتجات القياسية في غضون 7-15 يوم عمل. نرحب بطلبات العينات.",
  w5_t:"سلسلة توريد مستقرة",w5_d:"الإنتاج الداخلي يضمن جودة وإمدادًا ثابتين.",
  w6_t:"دعم احترافي",w6_d:"فريق مبيعات متعدد اللغات (EN, ES, FR, ZH, DE, PT, RU, JA, KO, AR, IT). استجابة خلال 24 ساعة.",
  b_title:"أخبار الصناعة",b_sub:"ابق على اطلاع بآخر اتجاهات إضاءة LED.",
  b1_t:"كيفية اختيار مصدر طاقة LED المناسب لمشروعك",
  b1_d:"دليل شامل يغطي حساب القدرة واختيار تصنيف IP ونصائح التثبيت.",
  b2_t:"فهم تصنيفات IP: IP20 مقابل IP65 مقابل IP67 مقابل IP68",
  b2_d:"تعلم الفرق بين مستويات مقاومة الماء وكيفية اختيار مستوى الحماية المناسب.",
  b3_t:"تقرير سوق إضاءة LED 2026: محركات النمو والفرص",
  b3_d:"تحليل لسوق إضاءة LED العالمي والفرص الجديدة للمصنعين.",
  t_title:"ماذا يقول عملاؤنا",t_sub:"موثوق به من شركاء B2B وموزعي الإضاءة حول العالم.",
  t1_d:"\"نستورد مصادر طاقة LED من CHUGAO منذ 3 سنوات. وحدات IP67 الخاصة بهم موثوقة باستمرار. فريق الدعم الفني يستجيب بسرعة.\"",
  t1_n:"Marco R.",t1_r:"موزع إضاءة، إيطاليا",
  t2_d:"\"أسعار CHUGAO المباشرة من المصنع توفر لنا تكاليف كبيرة. الجودة ممتازة والتسليم في الوقت المحدد دائمًا.\"",
  t2_n:"Sarah K.",t2_r:"مقاول مشاريع LED، الولايات المتحدة",
  t3_d:"\"خدمة OEM متميزة. ساعدتنا CHUGAO في تطوير مصدر طاقة مخصص، والمنتج النهائي تجاوز توقعاتنا.\"",
  t3_n:"Jean-Pierre L.",t3_r:"مالك علامة تجارية، فرنسا",
  faq_title:"الأسئلة الشائعة",faq_sub:"إجابات سريعة على الأسئلة الشائعة من المشترين العالميين.",
  faq1_q:"ما هو الحد الأدنى لكمية الطلب (MOQ)؟",
  faq1_a:"الحد الأدنى القياسي لدينا هو 50 قطعة لكل طراز. للمشترين الجدد، نقدم طلبات عينات بحد أدنى أقل. طلبات 500+ قطعة مؤهلة لأسعار مخفضة.",
  faq2_q:"ما هي الشهادات التي تحملها منتجاتكم؟",
  faq2_a:"جميع مصادر طاقة LED لدينا حاصلة على شهادات CE وRoHS. معظم المنتجات مسجلة أيضًا في UL.",
  faq3_q:"ما هي فترة الضمان؟",
  faq3_a:"نقدم ضمانًا لمدة 3 سنوات على جميع المنتجات القياسية. يتم التفاوض على شروط الضمان لمنتجات OEM المخصصة لكل مشروع.",
  faq4_q:"هل تقدمون خدمات OEM/ODM؟",
  faq4_a:"نعم، نقدم خدمات OEM/ODM كاملة تشمل العلامة التجارية المخصصة وتصميم التغليف والمواصفات المخصصة.",
  faq5_q:"ما هي شروط الدفع لديكم؟",
  faq5_a:"للعملاء الجدد: T/T 30% عربون، 70% قبل الشحن. للشركاء الدائمين: L/C وشروط أخرى.",
  faq6_q:"ما هي مدة الإنتاج؟",
  faq6_a:"المنتجات القياسية: 7-15 يوم عمل. OEM مخصص: 20-30 يوم عمل. العينات: 5-7 أيام عمل.",
  cta_title:"هل أنت مستعد للبدء؟",cta_sub:"اتصل بنا اليوم للحصول على استشارة مجانية وعرض سعر مخصص.",
  cta_btn_c:"اتصل بنا الآن",cta_btn_w:"دردشة على WhatsApp",cta_btn_e:"أرسل بريدًا",
  inq_title:"أرسل لنا استفسارًا",inq_sub:"أخبرنا عن مشروعنا وسنرد عليك خلال 24 ساعة بحل مخصص.",
  inq_ok:"شكرًا لك! تم تقديم استفسارك. سنتواصل معك قريبًا.",
  inq_name:"اسمك *",inq_email:"عنوان البريد الإلكتروني *",inq_phone:"الهاتف / WhatsApp",inq_company:"اسم الشركة",
  inq_product:"المنتج محل الاهتمام *",inq_sel:"اختر سلسلة المنتج",
  inq_opt1:"سلسلة المحولات (5W-200W)",inq_opt2:"مصدر داخلي (50W-400W)",inq_opt3:"مقاوم للماء IP67/IP68 (10W-400W)",inq_opt4:"مقاوم للمطر IP65 (100W-600W)",inq_opt5:"OEM / ODM مخصص",
  inq_qty:"الكمية المقدرة",inq_msg:"تفاصيل المشروع / الرسالة *",inq_submit:"إرسال الاستفسار",
  inq_emailto:"سيتم إرسال استفسارك إلى",inq_via:"عبر تطبيق البريد الإلكتروني الخاص بك.",inq_copy:"لا يوجد تطبيق بريد؟ انقر للنسخ.",inq_note:"بإرسال هذا النموذج، فإنك توافق على سياسة الخصوصية الخاصة بنا.",
  inq_why:"لماذا تستفسر من CHUGAO؟",
  inq_w1:"استشارة فنية مجانية خلال 24 ساعة",inq_w2:"توصية منتج مخصصة",inq_w3:"عرض سعر مباشر تنافسي من المصنع",inq_w4:"دعم العينات للمشترين الجدد",inq_w5:"وثائق شهادة كاملة",
  inq_fast:"تفضل استجابة أسرع؟",inq_fast_d:"تواصل معنا مباشرة عبر WhatsApp للتواصل الفوري.",inq_wa:"دردشة على WhatsApp",
  co_title:"اتصل بنا",co_addr_t:"العنوان",co_phone_t:"الهاتف",co_wa_t:"WhatsApp",co_wa_a:"دردش الآن",co_email_t:"البريد الإلكتروني",co_hours_t:"ساعات العمل",co_hours_d:"الإثنين-السبت: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - شركة مصنعة احترافية لمصادر طاقة LED من تشونغشان، الصين. نخدم مشتري B2B منذ 2014.",
  f_prod:"المنتجات",f_p1:"سلسلة المحولات",f_p2:"مصدر داخلي",f_p3:"مصدر مقاوم للماء",f_p4:"مصدر مقاوم للمطر",
  f_comp:"الشركة",f_c1:"من نحن",f_c2:"لماذا تختارنا",f_c3:"الأخبار",f_c4:"الأسئلة",
  f_supp:"الدعم",f_s1:"اتصل",f_s2:"البريد الإلكتروني",f_s3:"WhatsApp",f_s4:"التنزيلات",
  f_slogan:"مصنع مصادر طاقة LED الشامل"
};

T.it = {
  n_h:"Home",n_a:"Chi siamo",n_p:"Prodotti",n_s:"Specifiche",n_w:"Vantaggi",n_b:"Notizie",n_f:"FAQ",n_c:"Contatti",
  h_badge:"La scelta di oltre 500 partner globali",
  h_title:"Produttore professionale di alimentatori LED",
  h_sub:"CHUGAO - Alimentatori LED direttamente dalla fabbrica di Zhongshan, Cina. Adattatori certificati CE/UL, driver per interni, impermeabili IP67/IP68 e modelli resistenti alla pioggia. Al servizio degli acquirenti B2B in tutto il mondo dal 2014.",
  h_btn_p:"Vedi prodotti",h_btn_q:"Preventivo gratuito",
  s_y:"10+",s_y_l:"Anni di esperienza",s_c:"50+",s_c_l:"Paesi serviti",s_m:"200+",s_m_l:"Modelli",
  h_img_cap:"CHUGAO - Stabilimento di alimentatori LED a Zhongshan, Cina",
  t_ce:"Certificato CE",t_ul:"Listato UL",t_rohs:"Conforme RoHS",t_iso:"Stabilimento ISO 9001",t_moq:"MOQ basso disponibile",t_ship:"Spedizione globale",
  a_title:"Su CHUGAO",
  a_p1:"Zhongshan Chugao Electronic Technology Co., Ltd. è un'azienda high-tech specializzata in R&S, produzione e vendita di alimentatori LED a commutazione. Situata a Guzhen, la capitale mondiale dell'illuminazione in Cina.",
  a_p2:"Con oltre 10 anni di esperienza, CHUGAO ha costruito una linea completa che copre adattatori, alimentatori per interni, impermeabili (IP67/IP68) e resistenti alla pioggia. Prodotti esportati in oltre 50 paesi.",
  a_p3:"Seguendo il principio \"Qualità prima, cliente prioritario\", ogni prodotto viene sottoposto a test rigorosi prima della consegna. Offriamo servizi OEM/ODM per marchi globali.",
  f_fac:"Stabilimento proprio",f_fac_d:"Base produttiva di 10.000m2",f_qc:"Controllo qualità",f_qc_d:"100% test di invecchiamento",f_log:"Logistica rapida",f_log_d:"7-15 giorni ai porti globali",f_sup:"Supporto tecnico",f_sup_d:"Risposta garantita in 24h",
  p_title:"I nostri prodotti",p_sub:"Soluzioni complete di alimentatori LED - dagli adattatori compatti alle unità impermeabili ad alta potenza.",
  p1_n:"Serie adattatori",p1_d:"Alta efficienza, design compatto. Ingresso AC 100-240V universale. Uscita DC stabile e sicura per strisce e moduli LED.",
  p2_n:"Alimentatore per interni",p2_d:"Dimensioni compatte, eccellente dissipazione del calore. Funzionamento silenzioso. Ampio range di ingresso con PFC attivo.",
  p3_n:"Alimentatore impermeabile (IP67)",p3_d:"Grado IP67/IP68. Riempimento in silicone. Alloggiamento resistente ai raggi UV. Ideale per strisce LED esterne, fontane e illuminazione marina.",
  p4_n:"Alimentatore resistente alla pioggia (IP65)",p4_d:"Robusto alloggiamento in metallo con rivestimento protettivo. Resistente alla corrosione.",
  p_cta:"Richiedi ora \u2192",
  sp_title:"Specifiche del prodotto",sp_sub:"Confronta i parametri chiave tra le nostre serie di alimentatori LED.",
  sp_h1:"Serie",sp_h2:"Gamma di potenza",sp_h3:"Tensione di ingresso",sp_h4:"Tensione di uscita",sp_h5:"Grado IP",sp_h6:"Efficienza",sp_h7:"Garanzia",
  sp_r1_n:"Serie adattatori",sp_r2_n:"Alimentatore interno",sp_r3_n:"Impermeabile (IP67)",sp_r4_n:"Resistente alla pioggia (IP65)",
  sp_cta:"Richiedi scheda tecnica",
  w_title:"Perché scegliere CHUGAO",w_sub:"Cosa ci distingue nel competitivo mercato degli alimentatori LED.",
  w1_t:"Prezzi diretti dalla fabbrica",w1_d:"Come produttori eliminiamo gli intermediari - prezzi competitivi senza compromettere la qualità.",
  w2_t:"Qualità certificata",w2_d:"Tutti i prodotti hanno certificazioni CE, UL e RoHS. Ogni unità è sottoposta al 100% di test di invecchiamento.",
  w3_t:"Capacità R&S",w3_d:"Team R&S con oltre 10 ingegneri. Soluzioni OEM/ODM personalizzate.",
  w4_t:"Consegna rapida",w4_d:"Prodotti standard spediti in 7-15 giorni lavorativi. Ordini di campioni benvenuti.",
  w5_t:"Catena di fornitura stabile",w5_d:"La produzione interna garantisce qualità e fornitura costanti.",
  w6_t:"Supporto professionale",w6_d:"Team di vendita multilingue (EN, ES, FR, ZH, DE, PT, RU, JA, KO, AR, IT). Risposta in 24h.",
  b_title:"Notizie del settore",b_sub:"Rimani aggiornato sulle ultime tendenze nell'illuminazione LED.",
  b1_t:"Come scegliere il giusto alimentatore LED per il tuo progetto",
  b1_d:"Guida completa su calcolo della potenza, selezione del grado IP e suggerimenti per l'installazione.",
  b2_t:"Capire i gradi IP: IP20 vs IP65 vs IP67 vs IP68",
  b2_d:"Impara le differenze tra i livelli di impermeabilità e come scegliere la protezione giusta.",
  b3_t:"Rapporto mercato LED 2026: driver di crescita e opportunità",
  b3_d:"Analisi del mercato globale dell'illuminazione LED e nuove opportunità per i produttori.",
  t_title:"Cosa dicono i nostri clienti",t_sub:"La fiducia di partner B2B e distributori di illuminazione in tutto il mondo.",
  t1_d:"\"Acquistiamo alimentatori LED da CHUGAO da 3 anni. Le loro unità IP67 sono affidabili. Il supporto tecnico risponde rapidamente e ci aiuta a scegliere i prodotti giusti.\"",
  t1_n:"Marco R.",t1_r:"Distributore di illuminazione, Italia",
  t2_d:"\"I prezzi diretti dalla fabbrica di CHUGAO ci fanno risparmiare costi significativi. Qualità eccellente e consegne sempre puntuali.\"",
  t2_n:"Sarah K.",t2_r:"Imprenditore di progetti LED, USA",
  t3_d:"\"Il servizio OEM è eccezionale. CHUGAO ci ha aiutato a sviluppare un alimentatore personalizzato e il prodotto finale ha superato le nostre aspettative.\"",
  t3_n:"Jean-Pierre L.",t3_r:"Proprietario di marchio, Francia",
  faq_title:"Domande frequenti",faq_sub:"Risposte rapide alle domande comuni degli acquirenti globali.",
  faq1_q:"Qual è la vostra quantità minima d'ordine (MOQ)?",
  faq1_a:"Il nostro MOQ standard è di 50 pezzi per modello. Per i nuovi acquirenti offriamo ordini di campioni con MOQ inferiore. Ordini di 500+ pezzi qualify per prezzi scontati.",
  faq2_q:"Quali certificazioni hanno i vostri prodotti?",
  faq2_a:"Tutti i nostri alimentatori LED sono certificati CE e RoHS. La maggior parte è anche listata UL.",
  faq3_q:"Qual è il periodo di garanzia?",
  faq3_a:"Offriamo 3 anni di garanzia su tutti i prodotti standard. I prodotti OEM personalizzati hanno termini negoziati per progetto.",
  faq4_q:"Fornite servizi OEM/ODM?",
  faq4_a:"Sì, forniamo servizi OEM/ODM completi che includono marchio personalizzato, design dell'imballo e specifiche su misura.",
  faq5_q:"Quali sono i vostri termini di pagamento?",
  faq5_a:"Per i nuovi clienti: T/T 30% di deposito, 70% prima della spedizione. Per i partner affermati: L/C e altri termini.",
  faq6_q:"Qual è il tempo di produzione?",
  faq6_a:"Prodotti standard: 7-15 giorni lavorativi. OEM personalizzato: 20-30 giorni lavorativi. Campioni: 5-7 giorni lavorativi.",
  cta_title:"Pronto per iniziare?",cta_sub:"Contattaci oggi per una consulenza gratuita e un preventivo personalizzato.",
  cta_btn_c:"Contattaci ora",cta_btn_w:"Chat su WhatsApp",cta_btn_e:"Invia email",
  inq_title:"Inviaci una richiesta",inq_sub:"Raccontaci del tuo progetto e ti risponderemo entro 24 ore con una soluzione personalizzata.",
  inq_ok:"Grazie! La tua richiesta è stata inviata. Ti contatteremo a breve.",
  inq_name:"Il tuo nome *",inq_email:"Indirizzo email *",inq_phone:"Telefono / WhatsApp",inq_company:"Azienda",
  inq_product:"Prodotto di interesse *",inq_sel:"Seleziona una serie",
  inq_opt1:"Adattatori (5W-200W)",inq_opt2:"Alimentatore interno (50W-400W)",inq_opt3:"Impermeabile IP67/IP68 (10W-400W)",inq_opt4:"Resistente alla pioggia IP65 (100W-600W)",inq_opt5:"OEM / ODM personalizzato",
  inq_qty:"Quantità stimata",inq_msg:"Dettagli del progetto *",inq_submit:"Invia richiesta",
  inq_emailto:"La tua richiesta sarà inviata a",inq_via:"tramite la tua app email.",inq_copy:"Senza app email? Clicca per copiare.",inq_note:"Inviando questo modulo, accetti la nostra informativa sulla privacy.",
  inq_why:"Perché richiedere a CHUGAO?",
  inq_w1:"Consulenza tecnica gratuita entro 24 ore",inq_w2:"Raccomandazione prodotto personalizzata",inq_w3:"Preventivo diretto dalla fabbrica",inq_w4:"Supporto campioni per nuovi acquirenti",inq_w5:"Documenti di certificazione completi",
  inq_fast:"Preferisci una risposta più rapida?",inq_fast_d:"Raggiungici direttamente tramite WhatsApp per una comunicazione immediata.",inq_wa:"Chat su WhatsApp",
  co_title:"Contattaci",co_addr_t:"Indirizzo",co_phone_t:"Telefono",co_wa_t:"WhatsApp",co_wa_a:"Chatta ora",co_email_t:"Email",co_hours_t:"Orari",co_hours_d:"Lun-Sab: 8:00 - 18:00 (GMT+8)",
  f_desc:"CHUGAO - Produttore professionale di alimentatori LED a commutazione di Zhongshan, Cina. Al servizio degli acquirenti B2B dal 2014.",
  f_prod:"Prodotti",f_p1:"Adattatori",f_p2:"Alimentatore interno",f_p3:"Impermeabile",f_p4:"Resistente alla pioggia",
  f_comp:"Azienda",f_c1:"Chi siamo",f_c2:"Perché noi",f_c3:"Notizie",f_c4:"FAQ",
  f_supp:"Supporto",f_s1:"Contatti",f_s2:"Email",f_s3:"WhatsApp",f_s4:"Download",
  f_slogan:"Produttore di alimentatori LED tutto in uno"
};

// ==================== 核心切换函数 ====================
var SUPPORTED = ["en","zh","es","fr","de","pt","ru","ja","ko","ar","it"];

function setLang(lang) {
  if (T[lang] === undefined) {
    console.warn("[CHUGAO] Language pack missing for: " + lang + ", fallback to en");
    lang = "en";
  }
  var t = T[lang];
  var nodes = document.querySelectorAll("[data-i18n]");
  var missingCount = 0;
  for (var i = 0; i < nodes.length; i++) {
    var node = nodes[i];
    var key = node.getAttribute("data-i18n");
    var val = t[key];
    if (val === undefined) {
      // Fallback to en for missing keys
      val = T.en[key];
      if (val === undefined) {
        missingCount++;
        continue;
      }
    }
    if (node.tagName === "INPUT" || node.tagName === "TEXTAREA") {
      node.placeholder = val;
    } else {
      node.textContent = val;
    }
  }
  if (missingCount > 0) {
    console.warn("[CHUGAO] " + missingCount + " i18n keys missing in '" + lang + "' and 'en'");
  }

  // Update language selector highlight
  for (var j = 0; j < SUPPORTED.length; j++) {
    var code = SUPPORTED[j];
    var dd = document.getElementById("lang-" + code);
    if (dd) dd.classList.remove("active");
    var ml = document.getElementById("ml-" + code);
    if (ml) ml.classList.remove("active");
  }
  var active = document.getElementById("lang-" + lang);
  if (active) active.classList.add("active");
  var activeMl = document.getElementById("ml-" + lang);
  if (activeMl) activeMl.classList.add("active");

  // Update current language display
  var curLang = document.getElementById("current-lang");
  if (curLang) curLang.textContent = lang.toUpperCase();

  // Update <html lang> attribute
  document.documentElement.lang = (lang === "zh") ? "zh-CN" : lang;

  // Persist preference
  try { localStorage.setItem("chugao_lang", lang); } catch (e) {}

  // Update dir for RTL languages
  document.documentElement.dir = (lang === "ar") ? "rtl" : "ltr";

  console.log("[CHUGAO] Language switched to: " + lang + " (" + nodes.length + " nodes updated)");
}

function toggleLangDropdown() {
  var dd = document.getElementById("lang-dropdown");
  var btn = document.querySelector(".lang-btn");
  if (dd) dd.classList.toggle("open");
  if (btn) btn.classList.toggle("open");
}

// ==================== 通用事件 ====================
document.addEventListener("click", function(e) {
  var selector = document.querySelector(".lang-selector");
  var dd = document.getElementById("lang-dropdown");
  var btn = document.querySelector(".lang-btn");
  if (selector && !selector.contains(e.target)) {
    if (dd) dd.classList.remove("open");
    if (btn) btn.classList.remove("open");
  }
});

document.addEventListener("click", function(e) {
  var faqQ = e.target.closest(".faq-q");
  if (faqQ) { toggleFaq(faqQ); }
});

function toggleFaq(el) {
  var item = el.closest(".faq-i");
  if (!item) return;
  var wasOpen = item.classList.contains("open");
  var allItems = document.querySelectorAll(".faq-i");
  for (var i = 0; i < allItems.length; i++) {
    allItems[i].classList.remove("open");
    var btn = allItems[i].querySelector(".faq-q");
    if (btn) btn.setAttribute("aria-expanded", "false");
  }
  if (!wasOpen) {
    item.classList.add("open");
    el.setAttribute("aria-expanded", "true");
  }
}

function toggleMobileMenu() {
  var m = document.getElementById("mobileMenu");
  var t = document.getElementById("mobileToggle");
  if (!m || !t) return;
  var isOpen = m.classList.toggle("open");
  t.classList.toggle("open");
  t.setAttribute("aria-expanded", isOpen ? "true" : "false");
}
function closeMobileMenu() {
  var m = document.getElementById("mobileMenu");
  var t = document.getElementById("mobileToggle");
  if (m) m.classList.remove("open");
  if (t) t.classList.remove("open");
}

window.addEventListener("scroll", function() {
  var btn = document.getElementById("backToTop");
  if (!btn) return;
  if (window.scrollY > 300) btn.classList.add("show");
  else btn.classList.remove("show");
});

function observeFadeUp() {
  if (typeof IntersectionObserver === "undefined") return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) { entry.target.classList.add("visible"); }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll(".fu").forEach(function(el) { observer.observe(el); });
}

// ==================== 询价表单 ====================
function handleInquiry(e) {
  e.preventDefault();
  var form = document.getElementById("inquiryForm");
  if (!form) return false;
  var success = document.getElementById("formSuccess");
  var submitBtn = form.querySelector('button[type="submit"]');
  var data = new FormData(form);

  if (typeof gtag !== "undefined") {
    gtag("event", "submit_inquiry", { product: data.get("product") || "General" });
  }

  if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Submitting..."; }

  /*
  // Formspree 集成示例 - 取消注释并替换 YOUR_FORMSPREE_ID
  fetch("https://formspree.io/f/YOUR_FORMSPREE_ID", {
    method: "POST",
    body: data,
    headers: { "Accept": "application/json" }
  })
  .then(function(res) {
    if (res.ok) {
      form.reset();
      success.textContent = "Thank you! Your inquiry has been submitted. We will contact you within 24 hours.";
      success.classList.add("show");
      if (typeof gtag !== "undefined") gtag("event", "inquiry_success");
      setTimeout(function() { success.classList.remove("show"); }, 8000);
    } else { throw new Error("Server error"); }
  })
  .catch(function() {
    success.textContent = "Submission failed. Please try again or contact us via WhatsApp.";
    success.style.background = "#fee2e2"; success.style.color = "#991b1b";
    success.classList.add("show");
  })
  .finally(function() {
    if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = "Submit Inquiry"; }
  });
  return false;
  */

  var body = "New Inquiry from CHUGAO Website\n\n";
  body += "Name: " + (data.get("name") || "") + "\n";
  body += "Email: " + (data.get("email") || "") + "\n";
  body += "Phone: " + (data.get("phone") || "") + "\n";
  body += "Company: " + (data.get("company") || "") + "\n";
  body += "Product: " + (data.get("product") || "") + "\n";
  body += "Quantity: " + (data.get("quantity") || "") + "\n";
  body += "Message: " + (data.get("message") || "") + "\n";
  body += "\nSent from: " + window.location.href;
  var mailtoLink = "mailto:info@chugaopower.com?subject=" + encodeURIComponent("New Product Inquiry - " + (data.get("product") || "General")) + "&body=" + encodeURIComponent(body);
  window.location.href = mailtoLink;
  form.reset();
  success.textContent = "Thank you! Your inquiry has been prepared. Please send the email from your mail app, or use WhatsApp for instant contact.";
  success.classList.add("show");
  if (typeof gtag !== "undefined") gtag("event", "inquiry_mailto");
  setTimeout(function() { success.classList.remove("show"); }, 8000);
  if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = "Submit Inquiry"; }
  return false;
}

function copyInquiry() {
  var form = document.getElementById("inquiryForm");
  if (!form) return;
  var data = new FormData(form);
  var name = data.get("name") || "", email = data.get("email") || "", phone = data.get("phone") || "";
  var company = data.get("company") || "", product = data.get("product") || "", qty = data.get("quantity") || "";
  var msg = data.get("message") || "";
  if (!name && !email && !msg) { alert("Please fill in the form first before copying."); return; }
  var text = "CHUGAO Product Inquiry\n";
  text += "------------------------\n";
  text += "Name: " + name + "\n";
  text += "Email: " + email + "\n";
  text += "Phone: " + phone + "\n";
  text += "Company: " + company + "\n";
  text += "Product: " + product + "\n";
  text += "Quantity: " + qty + "\n";
  text += "Message: " + msg + "\n";
  text += "------------------------\n";
  text += "Send to: info@chugaopower.com";
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(function() {
      alert("Inquiry content copied! You can paste it into WhatsApp, WeChat, or any email app and send to info@chugaopower.com");
    }).catch(function() {
      fallbackCopy(text);
    });
  } else {
    fallbackCopy(text);
  }
}
function fallbackCopy(text) {
  var ta = document.createElement("textarea");
  ta.value = text; document.body.appendChild(ta); ta.select();
  try { document.execCommand("copy"); } catch(e) {}
  document.body.removeChild(ta);
  alert("Inquiry content copied! You can paste it into WhatsApp, WeChat, or any email app and send to info@chugaopower.com");
}

// ==================== 启动 ====================
document.addEventListener("DOMContentLoaded", function() {
  var savedLang = "en";
  try { savedLang = localStorage.getItem("chugao_lang") || "en"; } catch(e) {}
  if (SUPPORTED.indexOf(savedLang) === -1) savedLang = "en";
  setLang(savedLang);
  observeFadeUp();
  console.log("[CHUGAO] Site initialized, language: " + savedLang);
});
