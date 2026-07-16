# -*- coding: utf-8 -*-
import io

p = "main.js"
lines = open(p, encoding="utf-8").read().split("\n")
orig = list(lines)

# ---- new key -> English (source) ----
EN = {
 "qg_title":"Choose the right power supply faster",
 "qg_sub":"For a precise quote, start from the application, then confirm voltage, wattage, IP rating, quantity, and destination market.",
 "qg_k1":"LED strip / modules",
 "qg_t1":"Adapter or indoor driver",
 "qg_d1":"Best for indoor signs, shelves, cabinet lighting, and short LED strip runs.",
 "qg_l1a":"Confirm DC 12V / 24V / 36V / 48V",
 "qg_l1b":"Add 20-30% power margin",
 "qg_l1c":"Ask for plug type and label artwork",
 "qg_k2":"Outdoor projects",
 "qg_t2":"IP67 waterproof line",
 "qg_d2":"Best for exposed strips, fountains, facade lighting, and wet installation areas.",
 "qg_l2a":"Confirm cable length and connector",
 "qg_l2b":"Confirm salt-spray or high-humidity use",
 "qg_l2c":"Ask for CE / RoHS PDF by model",
 "qg_k3":"Signage / billboard",
 "qg_t3":"IP65 rainproof line",
 "qg_d3":"Best for semi-outdoor signage cabinets where airflow and higher wattage matter.",
 "qg_l3a":"Confirm 12V / 24V output",
 "qg_l3b":"Confirm cabinet ventilation",
 "qg_l3c":"Confirm carton weight and pallet need",
 "qg_k4":"OEM / distributor",
 "qg_t4":"Custom label or housing",
 "qg_d4":"Best when you need your logo, fixed SKU list, market files, or packaging control.",
 "qg_l4a":"MOQ starts from 500 pcs",
 "qg_l4b":"Send target label and spec sheet",
 "qg_l4c":"Lead time usually 25-30 days",
 "qg_tip_h":"Quote tip:",
 "qg_tip_t":"send output voltage, wattage, quantity, destination port, and target market in one message.",
 "qg_tip_a":"Use the inquiry form",
 "ct_title":"Certificates & QC proof before order",
 "ct_sub":"Buyers should not have to guess. Tell us the model and target market, and we send the matching files before you confirm the order.",
 "ct_c1h":"CE / RoHS PDFs",
 "ct_c1d":"Certificate and report files are matched by model and application, not sent as generic screenshots.",
 "ct_c2h":"48-hour burn-in record",
 "ct_c2d":"Every unit is tested before shipment. Failed units do not leave the factory floor.",
 "ct_c3h":"Datasheet & label artwork",
 "ct_c3d":"We confirm input, output, protection, case size, label text, and plug or cable details.",
 "ct_c4h":"Shipping documents",
 "ct_c4d":"Commercial invoice, packing list, certificate of origin, and cartons or pallets are confirmed before loading.",
 "ct_need_h":"Need UL?",
 "ct_need_d":"UL is handled per model. Send your market and quantity first; we confirm cost and schedule before application.",
 "ct_btn":"Request matching files",
 "inq_tmpl_h":"Best message format",
 "inq_tmpl_p":"Copy this into the message field for a faster answer:",
 "inq_tmpl_l1":"Output voltage and wattage",
 "inq_tmpl_l2":"Quantity and sample need",
 "inq_tmpl_l3":"Indoor, rainproof, or waterproof use",
 "inq_tmpl_l4":"Destination port and target market",
 "inq_tmpl_l5":"Certificate or label requirements",
 "inq_w6":"Certificate PDFs for your target market",
}

# ---- new key -> Chinese ----
ZH = {
 "qg_title":"更快选对电源",
 "qg_sub":"要拿到精准报价，先从应用场景出发，再确认电压、功率、防护等级、数量和目标市场。",
 "qg_k1":"LED 灯带 / 模组",
 "qg_t1":"适配器或室内驱动",
 "qg_d1":"适用于室内招牌、货架、柜体照明及短距离灯带。",
 "qg_l1a":"确认 DC 12V / 24V / 36V / 48V",
 "qg_l1b":"预留 20-30% 功率余量",
 "qg_l1c":"确认插头类型与标签设计",
 "qg_k2":"户外项目",
 "qg_t2":"IP67 防水系列",
 "qg_d2":"适用于裸露灯带、喷泉、建筑立面及潮湿安装环境。",
 "qg_l2a":"确认线长与接头",
 "qg_l2b":"确认盐雾或高湿环境使用",
 "qg_l2c":"按型号索取 CE / RoHS 证书 PDF",
 "qg_k3":"招牌 / 广告牌",
 "qg_t3":"IP65 防雨系列",
 "qg_d3":"适用于半户外招牌箱体，需要通风与更高功率的场景。",
 "qg_l3a":"确认 12V / 24V 输出",
 "qg_l3b":"确认箱体通风",
 "qg_l3c":"确认纸箱重量与托盘需求",
 "qg_k4":"OEM / 经销商",
 "qg_t4":"定制标签或外壳",
 "qg_d4":"当你需要自己的 logo、固定 SKU 清单、市场资料或包装管控时最合适。",
 "qg_l4a":"最小起订量 500 件起",
 "qg_l4b":"发送目标标签与规格表",
 "qg_l4c":"交期通常 25-30 天",
 "qg_tip_h":"报价小贴士：",
 "qg_tip_t":"请在一句话里写清输出电压、功率、数量、目的港和目标市场。",
 "qg_tip_a":"使用询价表单",
 "ct_title":"下单前提供证书与 QC 证明",
 "ct_sub":"买家不必靠猜。告诉我们型号和目标市场，我们会在您确认订单前发送对应文件。",
 "ct_c1h":"CE / RoHS 证书 PDF",
 "ct_c1d":"证书与报告按型号和应用匹配，不会发通用截图。",
 "ct_c2h":"48 小时老化记录",
 "ct_c2d":"每台出货前都经过测试，不良品不会离开车间。",
 "ct_c3h":"规格书与标签设计",
 "ct_c3d":"我们确认输入、输出、保护、外壳尺寸、标签文字以及插头或线材细节。",
 "ct_c4h":"出货单据",
 "ct_c4d":"商业发票、装箱单、原产地证、纸箱或托盘在装柜前确认。",
 "ct_need_h":"需要 UL？",
 "ct_need_d":"UL 按型号处理。先发来您的市场与数量，我们在申请前确认费用与时间。",
 "ct_btn":"索取对应文件",
 "inq_tmpl_h":"最佳留言格式",
 "inq_tmpl_p":"复制以下内容到留言框，回复更快：",
 "inq_tmpl_l1":"输出电压与功率",
 "inq_tmpl_l2":"数量与样品需求",
 "inq_tmpl_l3":"室内、防雨或防水用途",
 "inq_tmpl_l4":"目的港与目标市场",
 "inq_tmpl_l5":"证书或标签要求",
 "inq_w6":"面向您目标市场的证书 PDF",
}

def block(d):
    out = []
    for k, v in d.items():
        # escape double quotes inside value (none expected, but safe)
        v = v.replace('"', '\\"')
        out.append('  %s:"%s",' % (k, v))
    return out

def insert_before_closing(lines, header):
    # find header line
    hi = None
    for i, ln in enumerate(lines):
        if ln.startswith(header):
            hi = i
            break
    if hi is None:
        raise SystemExit("header not found: " + header)
    # find first line that is exactly "};" after header
    ci = None
    for i in range(hi + 1, len(lines)):
        if lines[i].strip() == "};":
            ci = i
            break
    if ci is None:
        raise SystemExit("closing }; not found for " + header)
    # ensure the line just before the closing }; ends with a comma (object literal)
    prev = lines[ci - 1]
    if prev.strip() and not prev.rstrip().endswith((",", ";")):
        lines[ci - 1] = prev.rstrip() + ","
    newblock = block(EN if header == "T.en = {" else ZH)
    # insert before ci, with a leading comment line
    ins = ["  // --- added: quote-guide / certs / inquiry i18n (49 keys) ---"] + newblock
    lines[ci:ci] = ins
    return ci

insert_before_closing(lines, "T.en = {")
insert_before_closing(lines, "T.zh = {")

# ---- remove testimonials dead keys from KEYS array (regex) ----
joined = "\n".join(lines)
import re
pattern = r'\s*"t_title","t_sub","t1_d","t1_n","t1_r","t2_d","t2_n","t2_r","t3_d","t3_n","t3_r",\n'
if re.search(pattern, joined):
    joined = re.sub(pattern, "\n", joined)
    print("removed testimonials dead KEYS")
else:
    print("WARN: testimonials dead KEYS line not found")

open(p, "w", encoding="utf-8").write(joined)
print("wrote", p, "lines:", len(joined.split("\n")))
