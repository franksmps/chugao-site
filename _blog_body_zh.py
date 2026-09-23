# -*- coding: utf-8 -*-
"""Chinese body copy for blog-1..5 and blog-9..14.

Companion to blog_body_zh.py, which declares BLOG_BODY['zh'|'ja'|'ko'|'it'] and
supplies blog-6/7/8. This file EXTENDS the existing 'zh' sub-dict, so it must
only assign NEW keys -- never re-declare BLOG_BODY['zh'] = {} (that would wipe
blog-6/7/8).

Wired in build_i18n._load_zh_ja_ko_it_blog_bodies().
"""


BLOG_BODY['zh']['blog-1'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>三步选对 LED 电源</h1>
<div class="meta">LED 技术 &middot; 2026 年 3 月 &middot; 阅读约 6 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-1-led-power-supply-md.avif 1200w, /images/blog-1-led-power-supply.avif 1024w">
<source type="image/webp" srcset="/images/blog-1-led-power-supply-md.webp 1200w, /images/blog-1-led-power-supply.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-1-led-power-supply.jpg" alt="LED 电源选型指南" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>选 LED 电源听起来很技术，其实就看三件事：<strong>功率</strong>、<strong>IP 防护等级</strong>和<strong>输入电压</strong>。这三项选对，你就排除了 90% 的退货与现场故障。</p>

<p>本指南把下单前必须核对的要点逐条讲清——出自我们的工程团队，而不是市场部门。</p>

<h2>第一步：匹配功率</h2>

<p>最常见的错误是选小了。这是我们在 CHUGAO 用的经验法则：</p>

<div class="highlight">
<strong>负载功率 &times; 1.25 = 驱动电源最低额定值。</strong><br>
务必留出至少 25% 余量。让驱动电源 100% 满载运行会缩短寿命、温度更高。
</div>

<h3>示例</h3>
<p>如果你的 LED 灯带功耗 80W，不要买 80W 的驱动电源，而应买 100W（或更大）。多出的容量能让输出更稳、发热更低，并把寿命从约 3 年延长到 5 年以上。</p>

<h3>为什么余量重要</h3>
<ul>
<li><strong>温度：</strong>驱动电源在低于额定负载下运行更凉。温度每降低 10&deg;C，电容寿命大致翻倍。</li>
<li><strong>抗浪涌：</strong>LED 灯带启动瞬间可能拉出短暂尖峰。余量能吸收这些尖峰而不触发保护。</li>
<li><strong>电压稳定：</strong>轻载的驱动电源能把输出电压咬得更紧，亮度也更一致。</li>
</ul>

<h2>第二步：选对 IP 防护等级</h2>

<p>IP（防护等级）代码说明驱动电源抵御粉尘和水的程度。大多数项目就栽在这里——人们为驱动电源省下 2 美元，然后在淋一场雨后就把它换掉。</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">IP 等级</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">防尘</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">防水</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">适用场景</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP20</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">无防护</td><td style="padding:10px 14px;border:1px solid var(--b)">无防水</td><td style="padding:10px 14px;border:1px solid var(--b)">仅室内干燥场所</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">完全防尘</td><td style="padding:10px 14px;border:1px solid var(--b)">水流喷射（任意方向）</td><td style="padding:10px 14px;border:1px solid var(--b)">户外暴露、冲洗区域</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">完全防尘</td><td style="padding:10px 14px;border:1px solid var(--b)">浸入 1 米水深</td><td style="padding:10px 14px;border:1px solid var(--b)">短时浸水、有积水风险</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">完全防尘</td><td style="padding:10px 14px;border:1px solid var(--b)">持续浸水</td><td style="padding:10px 14px;border:1px solid var(--b)">水下灯具、深水浸没</td></tr>
</tbody>
</table>

<p>如果不确定，就往上选一档。100W 驱动电源上 IP20 与 IP65 的差价，按工厂直供价通常不到 3 美元。</p>

<h2>第三步：核对输入电压兼容性</h2>

<p>这一点容易被忽略，却造成最高的退货率：</p>

<ul>
<li><strong>北美、日本、中国台湾、中国大陆：</strong>110V AC / 60Hz</li>
<li><strong>欧洲、中国大陆、亚洲大部、非洲：</strong>220–240V AC / 50Hz</li>
<li><strong>巴西：</strong>127V/220V 混合（请核对当地插座）</li>
<li><strong>工业／船舶：</strong>常见 277V、380V 或 480V 三相</li>
</ul>

<p>输入范围因产品线而异。适配器覆盖 100–240V AC；室内、IP65 与 IP67 型号覆盖 190–264V（IP67 最高 340V）。请在我们的 <a href="/#specs">规格表</a> 中核对你的型号的确切输入范围，确认它与目的地电网电压匹配。</p>

<h2>快速核对清单</h2>

<ol>
<li>汇总 LED 总负载瓦数 &rarr; 乘以 1.25 &rarr; 向上取到最接近的标准驱动电源规格。</li>
<li>确认安装环境 &rarr; 室内（IP20）、户外/防雨（IP65），或有浸水风险（IP67/IP68）。</li>
<li>确认目的国电网电压 &rarr; 110V 地区还是 220V 地区。</li>
<li>可选：需要调光吗？（0-10V、PWM、DALI 或 Triac——下单时注明）</li>
<li>可选：需要 UL 认证吗？（增加成本，每个型号 2–3 周交期）</li>
</ol>

<div class="cta-box">
<h3>不确定哪款合适？</h3>
<p>把规格发给我们——瓦数、数量、目的港和目标市场。工作时间内 1 小时回复，附参数表与报价。</p>
<a href="/#inquiry" class="btn">获取报价</a>
</div>


<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">宽压输入的插墙式与桌面式适配器，适用于标识与灯带照明。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">适用于面板灯、筒灯与商业灯具的高效驱动。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">可浸水等级的电源，适用于户外与景观项目。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">行业趋势</span><span class="rel-title">2026 LED 市场：我们看到的</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">法规认证</span><span class="rel-title">LED 驱动电源 BIS 认证：印度进口指南</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog/"><span class="pn-lab">全部文章</span><span class="pn-t">现场笔记</span></a><a class="pn-next" href="/blog-2/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">IP20、IP65、IP67、IP68 怎么选</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-2'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>IP20、IP65、IP67、IP68 对比</h1>
<div class="meta">技术指南 &middot; 2026 年 2 月 &middot; 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-2-ip-rating-md.avif 1200w, /images/blog-2-ip-rating.avif 1024w">
<source type="image/webp" srcset="/images/blog-2-ip-rating-md.webp 1200w, /images/blog-2-ip-rating.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-2-ip-rating.jpg" alt="IP 等级对比图" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>每一款 LED 电源都有 IP 等级。它由两位数字组成——第一位是<strong>防尘／固体颗粒防护</strong>，第二位是<strong>防水防护</strong>。数字越大，密封越好。</p>

<p>本指南把每个常见 IP 等级的实际含义逐条拆解，让你既不超支、也不再选错规格。</p>

<h2>两位数字系统怎么读</h2>

<table class="ip-table">
<thead><tr><th>位数</th><th>衡量什么</th><th>刻度</th></tr></thead>
<tbody>
<tr><td><strong>第一位（0–6）</strong></td><td>固体颗粒／粉尘</td><td>0 = 无防护 &rarr; 6 = 完全防尘</td></tr>
<tr><td><strong>第二位（0–8）</strong></td><td>液体／水</td><td>0 = 无防护 &rarr; 8 = 持续浸水</td></tr>
</tbody>
</table>

<h2>第一位：防尘</h2>

<ul>
<li><strong>IPx0：</strong>无防护。任何商用 LED 驱动电源都不采用。</li>
<li><strong>IPx3 – IPx4：</strong>防电线、螺丝、手指进入。基本安全防护。</li>
<li><strong>IPx5：</strong>有限防尘。少量细尘会进入，但不足以影响运行。</li>
<li><strong>IPx6：</strong>完全防尘。零粉尘进入。这是所有户外等级驱动电源的标准。</li>
</ul>

<p>实际上，我们销售的每一个具备有效防水等级（第二位 4 以上）的驱动电源，都已达到 IPx6 防尘。这一位你基本不用单独操心。</p>

<h2>第二位：防水——决策就发生在这里</h2>

<h3>IP20 / IP21 — 仅限室内</h3>
<p>垂直方向滴水无影响（IP20）。偏离垂直 15&deg; 以内滴水无影响（IP21）。</p>
<ul>
<li>用于：室内吸顶灯具、封闭式灯具、干燥场所</li>
<li>避免：任何靠近窗户、浴室、厨房或暖通送风口的位置</li>
<li>成本：最低档</li>
</ul>

<h3>IP44 — 防溅水</h3>
<p>任意方向的溅水都不会造成损害。</p>
<ul>
<li>用于：浴室镜前灯、橱柜下灯带、厨房操作照明</li>
<li>不适合直接淋雨或冲洗</li>
</ul>

<h3>IP54 — 防尘 + 防溅</h3>
<p>有限防尘 + 任意方向防溅水。</p>
<ul>
<li>用于：零售陈列、展会展台、半户外有顶区域</li>
</ul>

<h3>IP65 — 任意方向水流喷射</h3>
<p>这是户外 LED 安装的主力等级。</p>
<div class="highlight">
<strong>IP65 = 完全防尘 + 抵御任意方向低压水流喷射（6.3mm 喷嘴，12.5 L/min）。</strong>
</div>
<ul>
<li>用于：户外标识、外立面照明、路灯、停车库灯具、需软管冲洗的食品加工区</li>
<li>覆盖 70% 以上的户外 LED 驱动电源需求</li>
<li>CHUGAO 按销量计最畅销的品类</li>
</ul>

<h3>IP67 — 短时浸入 1 米以内</h3>
<p>与 IP65 相同的防尘等级，并能承受浸入 1 米水深 30 分钟。</p>
<ul>
<li>用于：池塘或泳池附近的景观照明、隧道照明、地埋式灯具、易涝安装点</li>
<li>注：浸水深度从外壳底部量起，而不是顶部</li>
</ul>

<h3>IP68 — 超过 1 米的持续浸水</h3>
<p>最高等级。可长期在水下运行，深度由厂家规定（通常 1m–10m）。</p>
<ul>
<li>用于：泳池灯、喷泉灯具、水族照明、水下建筑景观、船舶应用</li>
<li>这些需要专用灌封与密封——成本显著高于 IP67</li>
</ul>

<div class="warn">
<strong>常见错误：</strong> 在会出现积水或有内涝风险的应用（例如地埋式灯具）中使用 IP65。每只多花 2–4 美元升到 IP67，就能避免一次代价高昂的保修退货。
</div>

<h2>CHUGAO 如何测试</h2>

<ol>
<li><strong>组装：</strong>驱动电源在密封的铝制或塑料外壳内以 PU 树脂灌封。</li>
<li><strong>IP 测试：</strong>每批次都按 IEC 60529 标准抽样，使用校准过的水流喷射与粉尘试验箱设备测试。</li>
<li><strong>老化测试：</strong>IP 密封后，产品在 40&deg;C 环境下满载运行 48 小时，以筛出潜在缺陷。</li>
</ol>

<h2>你该订哪一款？</h2>

<table class="ip-table">
<thead><tr><th>你的应用</th><th>最低 IP 等级</th><th>推荐</th></tr></thead>
<tbody>
<tr><td>室内吸顶／壁装</td><td>IP20</td><td>IP20</td></tr>
<tr><td>浴室／厨房</td><td>IP44</td><td>IP44</td></tr>
<tr><td>户外标识／建筑外立面</td><td>IP65</td><td>IP65</td></tr>
<tr><td>隧道／停车库</td><td>IP65</td><td>IP67</td></tr>
<tr><td>近水景观</td><td>IP67</td><td>IP67</td></tr>
<tr><td>泳池／喷泉／水下</td><td>IP68</td><td>IP68</td></tr>
</tbody>
</table>

<div class="cta-box">
<h3>需要帮忙把 IP 等级匹配到你的项目吗？</h3>
<p>告诉我们你的安装环境，我们会推荐合适的 IP 等级和型号。免费提供参数表。</p>
<a href="/#inquiry" class="btn">获取推荐</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">防尘且抗喷射的电源，适用于建筑外立面与标识。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">为隧道、泳池与易涝区域提供短时浸水防护。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">行业趋势</span><span class="rel-title">2026 LED 市场：我们看到的</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">法规认证</span><span class="rel-title">LED 驱动电源 BIS 认证：印度进口指南</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-1/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">三步选对 LED 电源</span></a><a class="pn-next" href="/blog-3/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">2026 LED 市场：我们看到的</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-3'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>2026 LED 市场：我们看到的</h1>
<div class="meta">行业趋势 &middot; 2026 年 1 月 &middot; 阅读约 8 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-3-led-market-md.avif 1200w, /images/blog-3-led-market.avif 1024w">
<source type="image/webp" srcset="/images/blog-3-led-market-md.webp 1200w, /images/blog-3-led-market.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-3-led-market.jpg" alt="2026 全球 LED 市场概览" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>这些是我们在 CHUGAO 中山工厂车间里的观察——不是分析师报告，也不是市场调研论文。这是客户在 2025 年实际下的单，以及进入 2026 年他们在问什么。</p>

<h2>数字（我们的订单簿）</h2>

<div class="stat-grid">
<div class="stat-card"><div class="stat-num">+34%</div><div class="stat-label">订单量同比增长<br>（2025 对 2024）</div></div>
<div class="stat-card"><div class="stat-num">47%</div><div class="stat-label">新订单指定<br>智能／调光功能</div></div>
<div class="stat-card"><div class="stat-num">#1</div><div class="stat-label">增长最快市场：<br>中东／海合会地区</div></div>
<div class="stat-card"><div class="stat-num">100W–200W</div><div class="stat-label">询单最多的<br>功率段</div></div>
</div>

<h2>趋势 1：IP67 已成为默认要求</h2>

<p>三年前，IP65 是户外标配。2025 年，<strong>我们 62% 的户外驱动电源订单指定了 IP67</strong>。100W 时两者差价已缩小到每只 1–3 美元，客户宁愿要浸水余量，也不想处理保修索赔。</p>

<p>这在以下领域尤其明显：</p>
<ul>
<li><strong>景观照明承包商</strong>——一场大雨就得搭上一个周末去换驱动电源</li>
<li><strong>标识制造商</strong>——安装点常积冷凝水，IP65 无法完全应付</li>
<li><strong>基础设施项目</strong>（停车、隧道、交通）——规格制定者现在默认写 IP67</li>
</ul>

<h2>趋势 2：智能／可调光驱动电源快速增长</h2>

<p>近一半的新询盘会问调光能力。客户实际下单的构成：</p>

<ul>
<li><strong>DALI：</strong>商业楼宇项目（办公、零售）。稳定，但单项目量小。</li>
<li><strong>0-10V：</strong>仍是北美的量王。简单、便宜、与一切兼容。</li>
<li><strong>PWM 调光：</strong>在需要精确控制的园艺照明与建筑照明中增长很快。</li>
<li><strong>Zigbee／WiFi／蓝牙：</strong>关注度高，实际订单仍少（约占调光订单 8%）。多数客户仍偏好独立智能控制器，让驱动电源保持简单。</li>
</ul>

<div class="highlight">
<strong>我们的判断：</strong> 如果你在 2026 年推出新产品线，围绕 0-10V + 可选 DALI 来设计。这能覆盖当前 85% 以上的调光需求，又不会过度设计。
</div>

<h2>趋势 3：区域格局变化</h2>

<h3>中东／海合会——我们增长最快的地区</h3>
<p>沙特（2030 愿景项目）、阿联酋（世博遗留建设）和卡塔尔在积极下单。主要特征：</p>
<ul>
<li>所有户外 = 最低 IP67，喷泉／泳池工程常用 IP68</li>
<li>220V 电网、50Hz——对我们是标准配置</li>
<li>交期敏感：现货 7 天发运，定制 OEM 25 天</li>
<li>认证重点：除 CE/RoHS 外，还要 SASO（沙特）、ESMA（阿联酋）</li>
</ul>

<h3>欧洲——稳定、价格敏感</h3>
<p>欧盟订单量同比持平，但平均订单金额略升。客户在整合供应商（更少 SKU、更大批量）。能效要求（ErP／生态设计）正推动对更高效率驱动电源的需求（满载 &ge;90%）。</p>

<h3>东南亚——量增、均价更低</h3>
<p>越南、泰国、印尼和菲律宾增长很快。这些大多是室内适配器与 IP20 驱动电源订单——单价更低但数量大。这里价格竞争激烈；工厂直供价是必需的。</p>

<h3>美洲——北美稳定，拉美崛起</h3>
<p>北美（美／加／墨）仍是我们按营收计最大的单一市场。110V 输入，任何进入永久安装的产品都要求 UL 认证。拉美（巴西、哥伦比亚、智利）正在崛起——220V，路灯与商业改造需求增长。</p>

<h2>趋势 4：2026 年的规格表长什么样</h2>

<p>与三年前相比，来的 RFQ（询价）一开始就要更详细的信息。如今最常被要求的规格：</p>

<ol>
<li><strong>50% 负载下效率 &ge;88%</strong>（过去只要求满载效率）</li>
<li><strong>50% 负载下功率因数 &ge;0.9</strong></li>
<li><strong>THD &lt;15%</strong>（总谐波失真——电网运营商越来越多地要求）</li>
<li><strong>工作温度范围 -20&deg;C 至 +50&deg;C</strong>（历史上是 -10&deg;C 至 +40&deg;C）</li>
<li><strong>浪涌防护 2kV 线-中性线</strong>（在雷电多发市场越来越常被要求）</li>
<li><strong>质保最低 3 年</strong>，越来越多要求 5 年</li>
</ol>

<h2>趋势 5：价格压力及其如何影响质量</h2>

<p>我们直说：在阿里巴巴上永远有人更便宜。当你以低于市场价 30% 的价格买 LED 驱动电源，你会得到什么：</p>

<ul>
<li>更细的 PCB 铜箔（持续负载下过热）</li>
<li>更小或杂牌电容（12–18 个月就坏，而不是 3–5 年）</li>
<li>没有真正的灌封（标称 IP 等级但未测试——几个月内就进水）</li>
<li>温度升高时输出电压漂出规格（LED 亮度不均或提前失效）</li>
</ul>

<div class="highlight">
<strong>我们的立场：</strong> 我们靠可靠性和交期竞争，而不是靠当最便宜的。一只贵 0.80 美元但能用 5 年（而不是 18 个月）的驱动电源，总拥有成本更低——尤其是把退货运费、重新安装的人工和现场失效带来的声誉损失算进去之后。
</div>

<h2>我们对 2026 下半年的预期</h2>

<ul>
<li><strong>海合会基础设施支出</strong>持续到年底（世界杯后续项目）。</li>
<li><strong>园艺 LED 驱动电源</strong>增长，因为欧洲和北美的受控环境农业规模化。</li>
<li><strong>USB-C / PD（Power Delivery）</strong>驱动电源开始出现在细分应用（家具集成、便携灯具）。现在量小，但值得关注。</li>
<li><strong>电池备份／应急驱动电源</strong>重获关注，因为多个国家的建筑规范要求应急照明合规。</li>
</ul>

<div class="cta-box">
<h3>正在规划 2026 年的采购？</h3>
<p>把物料清单或产品概念发给我们。我们会提供报价、交期评估，并为符合条件的项目提供免费样品。</p>
<a href="/#inquiry" class="btn">开始询盘</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">我们增长最快的出口产品线，用于户外与景观照明。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">用于标识箱体与外立面照明的大批量主力。</span></a><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">面向全球零售与住宅项目的紧凑型适配器。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">法规认证</span><span class="rel-title">LED 驱动电源 BIS 认证：印度进口指南</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-2/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">IP20、IP65、IP67、IP68 怎么选</span></a><a class="pn-next" href="/blog-4/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 驱动电源 BIS 认证：印度进口指南</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-4'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 驱动电源 BIS 认证：印度进口商须知</h1>
<div class="meta">法规认证 &middot; 2026 年 5 月 &middot; 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof-md.avif 1200w, /images/product-waterproof.avif 1024w">
<source type="image/webp" srcset="/images/product-waterproof-md.webp 1200w, /images/product-waterproof.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-waterproof.jpg" alt="面向印度市场的 BIS 认证 LED 电源" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>自 2018 年起，印度逐步扩大了对电子产品的强制性 <strong>BIS（印度标准局）</strong>注册要求。对任何向印度进口 LED 电源的人来说，BIS 不再是可选项——它是一道海关闸门。</p>

<p>本指南说明 BIS 对你的订单意味着什么、流程怎么走、为什么它影响你的交期，以及与像 CHUGAO 这样已获 BIS 认证的工厂合作，如何为你省下数周文书工作。</p>

<h2>什么是 BIS？</h2>

<p>BIS 是印度的国家标准机构。根据强制注册计划（CRS），受管控类别的产品在进口或销售到印度之前，必须带有 BIS 注册标志。</p>

<p>对 LED 开关电源，适用标准是 <strong>IS 13252（第 1 部分）：信息技术设备——安全——通用要求</strong>，涵盖：</p>
<ul>
<li>电气安全与绝缘</li>
<li>温升限值</li>
<li>防电击保护</li>
<li>防火外壳要求</li>
<li>元器件安全额定值</li>
</ul>

<div class="highlight">
<strong>关键点：</strong> 如果你的 LED 驱动电源没有 BIS 注册，印度海关可以拒收货物、延迟清关，或要求你自费退运。
</div>

<h2>BIS 与 CE / RoHS 对比</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">方面</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">CE / RoHS</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">BIS（印度）</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>主管机构</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">欧盟委员会／自我声明</td><td style="padding:10px 14px;border:1px solid var(--b)">印度政府（BIS）</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>是否强制？</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">欧盟市场强制</td><td style="padding:10px 14px;border:1px solid var(--b)">印度进口强制</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>测试地点</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">工厂实验室或第三方</td><td style="padding:10px 14px;border:1px solid var(--b)">印度境内 BIS 认可实验室</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>典型周期</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">每型号 2-4 周</td><td style="padding:10px 14px;border:1px solid var(--b)">每型号 4-8 周</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>有效期</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">无到期（自我声明）</td><td style="padding:10px 14px;border:1px solid var(--b)">2 年，可续期</td></tr>
</tbody>
</table>

<h2>BIS 流程怎么走</h2>

<ol>
<li><strong>申请：</strong>制造商（或其授权代表）通过门户向 BIS 在线提交申请，并附技术文件与认可实验室的测试报告。</li>
<li><strong>工厂审核：</strong>BIS 可能审核制造设施，以核实质量体系与生产一致性。</li>
<li><strong>测试：</strong>样品按 IS 13252（第 1 部分）测试，包括介电强度、温度、湿度和机械应力测试。</li>
<li><strong>授予许可：</strong>通过后，BIS 签发注册号，出现在产品标签与包装上。</li>
<li><strong>监督：</strong>注册后，BIS 会进行定期跟进审核，确保持续合规。</li>
</ol>

<h2>为什么这影响你的交期</h2>

<p>如果你要为印度市场订购 LED 驱动电源，有两条路：</p>

<ul>
<li><strong>路径 A——从非 BIS 工厂订购：</strong>BIS 由你自己办。货物可以发运前，预计需要 4-8 周测试 + 申请时间。另有实验室费用（每型号 500-2000 美元，视复杂度而定）。</li>
<li><strong>路径 B——从已获 BIS 认证的工厂订购：</strong>工厂已持有该型号系列的 BIS 许可。你的订单立即发运。你会随货运单据收到 BIS 证书副本。</li>
</ul>

<p>CHUGAO 的核心 LED 驱动电源型号已持有 BIS 注册。当你下印度订单时，我们会在你的货运档案中附上 BIS 证书 PDF——无需额外等待。</p>

<h2>给印度买家的实用建议</h2>

<ul>
<li><strong>尽早确认 BIS 覆盖范围。</strong>并非所有型号都已注册。在敲定 SKU 清单前，问我们哪些 SKU 的 BIS 状态有效。</li>
<li><strong>核对 HS 编码归类。</strong>LED 电源通常归入 HS 8504.40（电子镇流器／变换器）。由于规则会变，请与你的报关行确认。</li>
<li><strong>为印度口岸的 BIS 文件审核预留 2-3 天。</strong>即使文件正确，部分口岸也会对电子产品货运做抽查。</li>
<li><strong>标签要求：</strong>BIS 注册产品必须在单机和外箱上显示 BIS 标准标志。当你在订单上注明“印度目的地”时，我们会处理这项贴标。</li>
</ul>

<div class="cta-box">
<h3>正在为印度市场采购 LED 驱动电源？</h3>
<p>告诉我们你的目标型号、数量和目的港。我们在 1 小时内确认 BIS 状态，并随货附上所有证书。</p>
<a href="/#inquiry" class="btn">获取印度合规报价</a>
</div>


<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">已获 BIS 注册的型号，随时可发印度货。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">具备 BIS 覆盖且符合印度标签要求的电源。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">行业趋势</span><span class="rel-title">2026 LED 市场：我们看到的</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-3/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">2026 LED 市场：我们看到的</span></a><a class="pn-next" href="/blog-5/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-5'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 驱动寿命：MTBF、L70 与真实使用寿命</h1>
<div class="meta">技术深读 &middot; 2026 年 4 月 &middot; 阅读约 8 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor-md.avif 1200w, /images/product-indoor.avif 1024w">
<source type="image/webp" srcset="/images/product-indoor-md.webp 1200w, /images/product-indoor.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-indoor.jpg" alt="长寿命的室内 LED 驱动电源" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>参数表上写着“50,000 小时”。你算一下：那是<strong>5.7 年</strong>连续运行。那为什么有些工程 2-3 年就得换驱动电源？</p>

<p>答案是：额定寿命与真实寿命是两回事。本文说明这些数字到底代表什么、什么会让驱动电源提前夭折，以及如何为项目的预期服役寿命挑选合适的规格。</p>

<h2>三个关键指标</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">指标</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">衡量什么</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">典型值</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>MTBF</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">平均无故障时间——总体中两次故障之间的统计平均时间</td><td style="padding:10px 14px;border:1px solid var(--b)">50,000–100,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>L70 / L80</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">输出降至初始值 70% 或 80% 所需的小时数</td><td style="padding:10px 14px;border:1px solid var(--b)">30,000–50,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>质保期</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">厂家对缺陷的保证</td><td style="padding:10px 14px;border:1px solid var(--b)">2–5 年</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>关键洞察：</strong> 50,000 小时的 L70 额定值意味着驱动电源在测试条件下运行 50,000 小时后仍保持至少 70% 的原始输出。它并不意味着每台设备都能运行 50,000 小时才失效。
</div>

<h2>驱动电源为何提前失效</h2>

<h3>1. 热是头号杀手</h3>
<p>高于额定工作温度每 10&deg;C，电解电容寿命大致减半。装在密闭灯具内的 IP20 室内驱动电源，很容易比环境温度高出 20&deg;C。如果环境温度是 35&deg;C（夏季常见），内部元件温度可达 75-85&deg;C——远高于典型的 60&deg;C 设计点。</p>

<ul>
<li><strong>IP67 防水型号：</strong>通过金属外壳 + 硅胶灌封实现更好的散热。额定 -30 至 +60&deg;C。典型寿命：50,000h。</li>
<li><strong>IP20 室内型号：</strong>取决于灯具通风。在密闭外壳内，预计寿命比额定值短 40-60%。</li>
<li><strong>适配器：</strong>塑料外壳更易积热。典型寿命：30,000h。</li>
</ul>

<h3>2. 电压尖峰与浪涌</h3>
<p>电网电压波动（在新兴市场尤其明显）会冲击输入电容和压敏电阻。额定 AC 190-264V 的驱动电源，也许能扛住一两次 280V 瞬变，但反复浪涌会比正常磨损更快地劣化元件。</p>

<h3>3. 接近满载运行</h3>
<p>在 90-100% 额定负载下，流过输出电容的纹波电流增大。这会产生更多热量并加速老化。这是我们在 CHUGAO 推荐的经验法则：</p>

<div class="highlight">
<strong>负载功率 &times; 1.25 = 驱动电源最低额定值。</strong><br>
让驱动电源在 70-80% 容量（而不是 95%）下运行，可把有效寿命延长 30–50%。
</div>

<h2>不同应用需要什么</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">应用</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">推荐驱动电源</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">预期服役寿命</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">原因</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">零售标识（每天 8-12 小时）</td><td style="padding:10px 14px;border:1px solid var(--b)">适配器／室内 IP20</td><td style="padding:10px 14px;border:1px solid var(--b)">8-12 年</td><td style="padding:10px 14px;border:1px solid var(--b)">每日工时低，弥补了单机寿命较短</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">户外外立面照明（每天 12 小时以上）</td><td style="padding:10px 14px;border:1px solid var(--b)">IP67 防水</td><td style="padding:10px 14px;border:1px solid var(--b)">10-14 年</td><td style="padding:10px 14px;border:1px solid var(--b)">密封灌封可应对湿度与温差</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">工业 24/7（仓储）</td><td style="padding:10px 14px;border:1px solid var(--b)">IP65 防雨或工业级 CGS</td><td style="padding:10px 14px;border:1px solid var(--b)">5-7 年</td><td style="padding:10px 14px;border:1px solid var(--b)">连续高温运行加速磨损</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">船舶／喷泉</td><td style="padding:10px 14px;border:1px solid var(--b)">IP68 等级型号</td><td style="padding:10px 14px;border:1px solid var(--b)">8-12 年</td><td style="padding:10px 14px;border:1px solid var(--b)">全浸水等级，经盐雾测试</td></tr>
</tbody>
</table>

<h2>CHUGAO 如何测试</h2>

<p>每一台 CHUGAO 驱动电源在出厂前都要经过 <strong>48 小时老化测试</strong>。不合格的机器一律报废——不允许离开车间。这道出货前筛查能筛出早期失效（浴盆曲线的前段失效）。</p>

<p>对于 500 只以上的 OEM 订单，如果在采购订单中注明，我们提供延长老化测试选项（72-168 小时），不额外收费。</p>

<h2>快速决策指南</h2>

<ol>
<li><strong>每日运行时数？</strong>零售 8 小时与工业 24 小时天差地别。把目标项目寿命乘以每日小时数，得到总小时需求。</li>
<li><strong>环境温度？</strong>超过 40&deg;C 每高 10&deg;C，寿命约减半。要把这一点纳入型号选择。</li>
<li><strong>通风？</strong>密闭灯具需要 IP67 或更高。有通风的外壳可用 IP20/65。</li>
<li><strong>余量？</strong>始终加 25%。相比跑一趟现场更换故障机，60W 与 100W 驱动电源的差价微不足道。</li>
<li><strong>备件库存？</strong>对于 24/7 安装，常备 5-10% 的备用驱动电源。这比紧急发货更便宜。</li>
</ol>

<div class="cta-box">
<h3>不确定哪款驱动电源匹配你的寿命需求？</h3>
<p>告诉我们你的应用、每日运行时间和环境条件。我们会为你的具体安装推荐合适的系列，并给出贴近实际的预期寿命。</p>
<a href="/#inquiry" class="btn">获取寿命匹配推荐</a>
</div>


<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">每个功率段都提供 MTBF 数据的长寿命适配器。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">适用于商业与建筑灯具的 L70 等级驱动。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">灌封密封，延长户外服役寿命。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">为 50,000+ 小时户外运行设计的坚固驱动。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">行业趋势</span><span class="rel-title">2026 LED 市场：我们看到的</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">法规认证</span><span class="rel-title">LED 驱动电源 BIS 认证：印度进口指南</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-4/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">LED 驱动电源 BIS 认证：印度进口指南</span></a><a class="pn-next" href="/blog-6/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">IP67 与 IP65 LED 驱动电源：你需要哪种等级？</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-9'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>恒压还是恒流 LED 驱动：你需要哪种？</h1>
<div class="meta">技术指南 &middot; 2026 年 9 月 &middot; 阅读约 8 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="恒压与恒流 LED 驱动电源并排展示" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>两个词决定一款 LED 灯具到底能不能用：<strong>恒压</strong>与<strong>恒流</strong>。弄反了，LED 要么根本不亮，要么几天就烧掉。然而多数买家都是等灯具出故障后才接触到这两个词，所以这里给出我们最希望每张参数表都印在前面的简版说明。</p>

<h2>“恒压”是什么意思</h2>

<p>恒压（CV）驱动让输出电压保持稳定——通常是 12V、24V、36V 或 48V——由灯具自己决定拉多少电流。LED 灯带、标识模组以及大多数“12V/24V”产品本身就带限流电阻，所以它们需要一个固定电压电源。这是绝大多数装饰、建筑与标识工程的默认选择。</p>

<div class="highlight">
<strong>经验法则：</strong> 如果产品标签写着 <strong>12V</strong> 或 <strong>24V</strong>，它要的就是恒压驱动。驱动定电压，灯带定电流。
</div>

<h2>“恒流”是什么意思</h2>

<p>恒流（CC）驱动让电流保持稳定——通常是 350mA、500mA、700mA、1050mA 或 1500mA——并调整电压，以便在 LED 正向电压随温度变化时维持这个电流恒定。裸装的大功率 LED（筒灯、泛光灯、路灯、高棚模组）没有板载稳压，接到固定电压源上会拉出失控电流把自己烧坏。它们需要 CC 驱动。</p>

<p>如果标签写着 <strong>350 mA</strong> 或 <strong>700 mA</strong>，它要的就是恒流。把灯具规格告诉我们，我们帮你匹配。</p>

<h2>两者并排对比</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">属性</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">恒压</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">恒流</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">保持的输出</td><td style="padding:10px 14px;border:1px solid var(--b)">电压（12/24/36/48V）</td><td style="padding:10px 14px;border:1px solid var(--b)">电流（350-1500mA）</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">驱动什么</td><td style="padding:10px 14px;border:1px solid var(--b)">灯带、模组、标识</td><td style="padding:10px 14px;border:1px solid var(--b)">裸装大功率 LED、筒灯</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">板载稳压</td><td style="padding:10px 14px;border:1px solid var(--b)">在 LED 产品内</td><td style="padding:10px 14px;border:1px solid var(--b)">在驱动电源内</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">CHUGAO 典型产品线</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/adapters/">适配器 5-200W</a>、<a href="/products/indoor/">室内 50-400W</a></td><td style="padding:10px 14px;border:1px solid var(--b)">室内／IP67（按需）</td></tr>
</tbody>
</table>

<h2>为什么混用会毁掉灯具</h2>

<ol>
<li><strong>恒压驱动接恒流 LED</strong>——LED 会拉走它能拉到的所有电流，发热，然后烧毁。我们见得最多的情况，就是有人把 12V 灯带电源拿去做 350mA 筒灯。</li>
<li><strong>恒流驱动接恒压灯带</strong>——驱动强行灌入灯带电阻无法限制的电流，灯带过热或驱动报故障。无论哪种，都不亮。</li>
</ol>

<p>通电之前务必先看灯具标签。如有任何疑问，把标签照片发给我们，我们会告诉你需要哪种。</p>

<h2>一个驱动能兼顾两者吗？</h2>

<p>一些可编程或“双模式”驱动可以在固定输出下设为 CV 或 CC，但它们更贵，且很少需要。对标准安装来说，一次选对类型就能免去跑一趟现场。我们的 <a href="/products/indoor/">室内驱动</a> 与 <a href="/products/ip67/">IP67 驱动</a> 都提供 100W 起的恒流版本，用于大功率灯具工程。</p>

<h2>我们需要你提供什么</h2>

<p>请提供灯具标签（以伏特表示的电压，或以毫安表示的电流）、总功率、安装位置和数量。我们会确认是恒压还是恒流，并报出确切的型号——同时告诉你什么时候一款更便宜的现货产品就真的够用。</p>

<div class="cta-box">
<h3>不确定你的灯具是 CV 还是 CC？</h3>
<p>发一张 LED 标签的照片——以伏特表示的电压，或以毫安表示的电流。我们会确认类型并报出确切型号。</p>
<a href="/#inquiry" class="btn">确认 CV 还是 CC</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">选购指南</span><span class="rel-title">12V 还是 24V：LED 电源怎么选</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 电源功率怎么选：瓦数与余量</span></a><a class="rel-card" href="/blog-10/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 驱动调光详解：0-10V、PWM、DALI 与 TRIAC</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-8/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">LED 电源功率怎么选：瓦数与余量</span></a><a class="pn-next" href="/blog-10/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 驱动调光详解：0-10V、PWM、DALI 与 TRIAC</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-10'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 驱动调光详解：0-10V、PWM、DALI 与 TRIAC</h1>
<div class="meta">技术指南 &middot; 2026 年 9 月 &middot; 阅读约 9 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="LED 驱动调光标准对比" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>给 LED 工程做调光本该是一个设置项，而不是一个科研项目。实践中之所以出错，是因为四种调光标准共用同样的线，而它们之间没有一种可以互换。下面说明各自是什么，以及该指定哪一种，才能让你的控制系统真的能调光。</p>

<h2>四种标准，直白说</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">标准</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">如何工作</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">最适合</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>0-10V</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">一对独立的低压控制线，10V 时 100%，降到 0V 时约 10%</td><td style="padding:10px 14px;border:1px solid var(--b)">商业吊顶、新建项目</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>PWM</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">直流侧脉宽调制；非常平滑，无颜色偏移</td><td style="padding:10px 14px;border:1px solid var(--b)">标识、对摄像敏感的场所</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>DALI</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">数字可寻址总线；每台灯具可寻址并记录</td><td style="padding:10px 14px;border:1px solid var(--b)">大型智能楼宇</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>TRIAC</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">相位切割，沿用现有的市电调光器（前沿／后沿）</td><td style="padding:10px 14px;border:1px solid var(--b)">改造、现有墙壁调光器</td></tr>
</tbody>
</table>

<h2>0-10V：商业默认</h2>

<p>0-10V 是新建商业装修最常见的规格，因为接线简单又便宜——两根额外低压导体，无需数据。要注意的是它只能调到约 10%，不能完全熄灭，除非你为“关闭”加一个市电继电器。如果你的项目需要真正熄灭，请在规格中写明。</p>

<h2>PWM：最平滑，最适合标识</h2>

<p>PWM 调光以高频斩切直流输出。由于它从不改变电流大小，调光时不会有色温偏移——这对 <a href="/products/ip65/">标识</a> 以及任何不能接受频闪的摄像或广播环境都很重要。PWM 位于直流侧，因此与恒压驱动搭配。</p>

<h2>DALI：可寻址的楼宇控制</h2>

<p>DALI 把每台灯具挂到两线数字总线上，各有自己的地址，因此楼宇管理系统可以对分区调光、记录故障、场景调用。它在驱动和调试上更贵，但对一栋 20 层的办公楼来说，能在人工上回本。我们在 <a href="/products/indoor/">室内驱动</a> 上提供 100W 起的 DALI 版本。</p>

<h2>TRIAC：无需重新布线的改造</h2>

<p>TRIAC（相位切割）调光让 LED 驱动沿用现有的市电墙壁调光器，因此改造不必敷设新的控制电缆。陷阱在于：并非每个 LED 驱动都兼容 TRIAC，而便宜的调光器在低端会嗡嗡响或掉出。请使用后沿（ELV）调光器，并搭配明确标注兼容它的驱动。</p>

<div class="highlight">
<strong>兼容性优先：</strong> 一只“可调光 LED”只有在<em>驱动</em>能听懂调光器的语言时才能调光。告诉我们你用的是哪种调光器或控制系统，我们在你下单前确认兼容性——选定的室内与 IP67 型号从 100W 起支持 0-10V、PWM 与 TRIAC；最小的适配器不支持调光。
</div>

<h2>我们见到的三个错误</h2>

<ol>
<li><strong>买了“可调光”灯带，却配了不可调光的驱动。</strong>调光靠的是驱动，不是灯带。</li>
<li><strong>把 TRIAC 调光器与 0-10V 驱动混用。</strong>它们不是同一套系统；结果是频闪或不调光。</li>
<li><strong>忘了控制电缆。</strong>0-10V 与 DALI 需要在安装时就敷设它们额外的一对线，事后补不了。</li>
</ol>

<h2>我们需要你提供什么</h2>

<p>请提供调光器或控制系统型号、负载瓦数、输出电压，以及现场是新建还是改造。我们会确认调光标准与合适的型号——0-10V、PWM、DALI 或 TRIAC。</p>

<div class="cta-box">
<h3>需要一款真能调光的驱动？</h3>
<p>告诉我们调光器或控制系统、负载和电压。我们会确认调光标准与合适的型号。</p>
<a href="/#inquiry" class="btn">确认调光类型</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-11/"><span class="rel-cat">选购指南</span><span class="rel-title">功率因数校正与无频闪 LED 驱动</span></a><a class="rel-card" href="/blog-9/"><span class="rel-cat">技术指南</span><span class="rel-title">恒压还是恒流 LED 驱动：你需要哪种？</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">技术指南</span><span class="rel-title">IP67 还是 IP65：你需要哪种防水 LED 驱动？</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-9/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">恒压还是恒流 LED 驱动：你需要哪种？</span></a><a class="pn-next" href="/blog-11/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">功率因数校正与无频闪 LED 驱动</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-11'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>功率因数校正与无频闪 LED 驱动</h1>
<div class="meta">选购指南 &middot; 2026 年 9 月 &middot; 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="功率因数与无频闪 LED 驱动规格" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>“功率因数”和“频闪”是两项从不出现在零售包装上、却决定一个工程是通过验收还是让人头疼的规格。两者都在驱动阶段定型，所以下面是买家真正应该要求的。</p>

<h2>功率因数：为什么电网在意</h2>

<p>功率因数（PF）是你使用的有功功率与从电网取用的总功率之比。PF 0.5 的廉价驱动会拉取它所需两倍的电流，使线路过载并在商业建筑中触发限值。许多地区现在要求 5W 以上 PF 达到 0.9 或更高，EN 61000-3-2 正是为此设定了谐波限值。</p>

<div class="highlight">
<strong>有源 PFC 对无源：</strong> 我们的 <a href="/products/indoor/">室内驱动</a> 采用<strong>有源 PFC</strong>，在整个负载范围内达到 PF 0.95+——而不是只在满载下才起作用的那种无源“功率因数校正”贴纸。对一个 200 只的吊顶来说，这就是配电盘干净与断路器跳闸的区别。
</div>

<h2>频闪：为什么人在意</h2>

<p>LED 频闪来自驱动直流输出上的纹波。廉价驱动让纹波跑到 20-30%，肉眼也许看不出来，但摄像头、传感器以及一些人绝对能感受到——它表现为视频上的条纹、CCTV 上的频闪，以及办公室里的眼睛疲劳。优质驱动把纹波控制在 5-8% 以下，并标注为“无频闪”。</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">症状</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">原因</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">解决方案</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">摄像／CCTV 上出现条纹</td><td style="padding:10px 14px;border:1px solid var(--b)">输出纹波过高</td><td style="padding:10px 14px;border:1px solid var(--b)">无频闪驱动，纹波 &lt;8%</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">负载下断路器跳闸</td><td style="padding:10px 14px;border:1px solid var(--b)">功率因数低</td><td style="padding:10px 14px;border:1px solid var(--b)">有源 PFC 驱动，PF 0.95+</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">调光时嗡嗡响</td><td style="padding:10px 14px;border:1px solid var(--b)">调光不兼容</td><td style="padding:10px 14px;border:1px solid var(--b)">匹配的调光标准（见调光指南）</td></tr>
</tbody>
</table>

<h2>无频闪不可妥协的场合</h2>

<ul>
<li><strong>办公室与学校</strong>——全天暴露；劣质驱动会导致疲劳投诉。</li>
<li><strong>零售与博物馆</strong>——频闪会毁掉产品色彩与摄影。</li>
<li><strong>CCTV 与交通枢纽</strong>——条纹会让车牌和人脸无法辨认。</li>
<li><strong>任何有摄像头覆盖的场所</strong>——如果有手机在拍，就指定无频闪。</li>
</ul>

<h2>如何读参数表</h2>

<ol>
<li><strong>PF：</strong>要求给出整个负载范围内的数值，而不只是 100% 时。有源 PFC 能在全范围保持高值；无源做不到。</li>
<li><strong>纹波／频闪百分比：</strong>按多数规格制定者现在采用的 SVM 指标，8% 以下即为“无频闪”。</li>
<li><strong>THD</strong>（总谐波失真）：越低对供电越干净。有源 PFC 驱动远低于 EN 61000-3-2 限值。</li>
</ol>

<p>每一台 CHUGAO 室内与 IP67 驱动都按 PF 0.95+ 和无频闪输出作为标准制造，而不是付费选装。如果你的市场有特定的谐波限值，告诉我们，我们会随批次提供测试报告。</p>

<h2>我们需要你提供什么</h2>

<p>请提供现场类型（办公室、零售、有 CCTV 覆盖）、瓦数和电压，以及任何当地的 PF／谐波限值。我们会确认一款能通过的驱动——并在你下单前发送报告。</p>

<div class="cta-box">
<h3>为办公室或摄像场所做规格？</h3>
<p>发来现场类型、瓦数和任何当地 PF／谐波限值。我们会确认一款无频闪、高 PF 的驱动并提供测试报告。</p>
<a href="/#inquiry" class="btn">获取干净的驱动规格</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-10/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 驱动调光详解：0-10V、PWM、DALI 与 TRIAC</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a><a class="rel-card" href="/blog-9/"><span class="rel-cat">技术指南</span><span class="rel-title">恒压还是恒流 LED 驱动：你需要哪种？</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 对比</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-10/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">LED 驱动调光详解：0-10V、PWM、DALI 与 TRIAC</span></a><a class="pn-next" href="/blog-12/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 驱动的浪涌防护：雷电与瞬变</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-12'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 驱动的浪涌防护：雷电与瞬变</h1>
<div class="meta">技术指南 &middot; 2026 年 9 月 &middot; 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="带浪涌防护的 IP67 防水 LED 驱动" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>三条街外的一道闪电，就能毁掉一台完好的 LED 驱动。浪涌防护，决定了驱动是扛过暴雨还是变成电子垃圾——而大多数被归咎于“质量”的故障，其实只是输入端毫无防护。下面说说真正保护驱动的是什么。</p>

<h2>浪涌从哪里来</h2>

<ul>
<li><strong>雷电</strong>——非直接雷击会在长长的户外线路上感应出数千伏的尖峰。</li>
<li><strong>开关操作</strong>——接触器、电梯和大型电机会把瞬变灌进同一条馈线。</li>
<li><strong>感性反冲</strong>——哪怕一个继电器断开，也能激起数百伏的尖峰。</li>
</ul>

<p>接在干净楼宇市电上的室内驱动很少遇到这些。而长线缆上的户外与 <a href="/products/ip67/">潮湿场所驱动</a> 则持续面对，这正是浪涌等级属于 IP 故事的一部分、而非另一回事的原因。</p>

<h2>真正重要的两层</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">层级</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">作用</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">典型等级</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">内置 MOV</td><td style="padding:10px 14px;border:1px solid var(--b)">在驱动内部钳制小型瞬变</td><td style="padding:10px 14px;border:1px solid var(--b)">2-4 kV 差模</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">外部 SPD</td><td style="padding:10px 14px;border:1px solid var(--b)">在进线点吸收巨大雷击</td><td style="padding:10px 14px;border:1px solid var(--b)">10-20 kV，依据 IEC 61643</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>关键点：</strong> 驱动内部的浪涌钳位能应付日常噪声。真正的雷击事件需要在供电入口加装<strong>外部浪涌保护器（SPD）</strong>，因为没有任何一台在散热与成本之间取舍的驱动，能独自吞下数千安培的雷击。
</div>

<h2>如何为雷暴频繁的现场选型</h2>

<ol>
<li><strong>户外或沿海线路一律选灌封 IP67 驱动</strong>——密封外壳也是对潮湿故障的第一道防线。</li>
<li><strong>在进线处加装 SPD</strong>——在给灯具供电的配电箱上装一只 Type 2 浪涌保护器。</li>
<li><strong>线缆尽量离地、远离市电</strong>；平行走线会招来感应尖峰。</li>
<li><strong>正确接地外壳</strong>；未接地的驱动无法安全泄放雷击。</li>
</ol>

<h2>常见的浪涌误区</h2>

<ul>
<li><strong>“IP67 就等于防浪涌。”</strong> 不对——IP 管的是水，不是电压。这是两套规格，两者都要买。</li>
<li><strong>“保护一台驱动就保护了整串。”</strong> 雷击沿线缆传播；要保护的是进线，而不是某一台。</li>
<li><strong>“室内就安全。”</strong> 与电梯或压缩机共用馈线的室内驱动，照样会遇到开关尖峰——请索要内置钳位等级。</li>
</ul>

<p>我们的 <a href="/products/ip67/">IP67 防水驱动</a> 和 <a href="/products/ip65/">IP65 防雨驱动</a> 标配内部浪涌钳位；对于暴露现场，我们建议在供电处加装外部 SPD，并会与你一起选型。</p>

<h2>我们需要你提供什么</h2>

<p>请告知现场类型（屋顶、沿海、内陆）、线缆长度，以及配电箱上是否已有 SPD。我们会确认驱动的浪涌等级和建议加装的外部防护。</p>

<div class="cta-box">
<h3>正在保护户外或沿海现场？</h3>
<p>发来现场、线缆长度以及配电箱上是否已有 SPD。我们会确认浪涌等级和需加装的外部防护。</p>
<a href="/#inquiry" class="btn">获取浪涌方案</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-6/"><span class="rel-cat">技术指南</span><span class="rel-title">IP67 还是 IP65：你需要哪种防水 LED 驱动？</span></a><a class="rel-card" href="/blog-13/"><span class="rel-cat">选购指南</span><span class="rel-title">为户外与恶劣场所选择 LED 电源</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 对比</span></a><a class="rel-card" href="/blog-11/"><span class="rel-cat">选购指南</span><span class="rel-title">功率因数校正与无频闪 LED 驱动</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-11/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">功率因数校正与无频闪 LED 驱动</span></a><a class="pn-next" href="/blog-13/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">为户外与恶劣场所选择 LED 电源</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-13'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>为户外与恶劣场所选择 LED 电源</h1>
<div class="meta">选购指南 &middot; 2026 年 10 月 &middot; 阅读约 8 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="面向恶劣环境的户外 LED 电源选型" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>“户外”并不是一种环境。商场雨棚下密封的灯箱和防波堤上的驱动都叫“户外”，但两年后只有一个还能正常工作。这份指南带你从干燥一端走到潮湿一端，让你选到合适的型号，而不是最便宜的那一个。</p>

<h2>环境阶梯</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">环境</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">防护等级</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">CHUGAO 产品线</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">室内干燥</td><td style="padding:10px 14px;border:1px solid var(--b)">IP20</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/indoor/">室内 50-400W</a></td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">半户外，雨淋 + 粉尘</td><td style="padding:10px 14px;border:1px solid var(--b)">IP65</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/ip65/">IP65 100-600W</a></td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">潮湿、积水、沿海</td><td style="padding:10px 14px;border:1px solid var(--b)">IP67 / IP68</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/ip67/">IP67 10-400W</a></td></tr>
</tbody>
</table>

<h2>第 1 步：水会接触到驱动吗？</h2>

<p>如果驱动装在密封的灯箱或雨棚内，雨水会流走、不会积聚——<a href="/products/ip65/">IP65</a> 就足够，而且散热更好。如果水会在外壳周围积聚，请升级到全灌封的 <a href="/products/ip67/">IP67</a> 型号。</p>

<h2>第 2 步：是否靠海或需要冲洗？</h2>

<p>盐雾会从内部腐蚀带通风口的金属外壳。在防波堤、洗车场，或被水枪冲洗的食品厂里，你需要硅胶灌封<em>并且</em>通过盐雾测试。要问供应商实际做了哪些测试，而不只是印了哪个数字。</p>

<h2>第 3 步：会有多热？</h2>

<p>密封能挡水，却也把热闷在里面。灌封的 IP67 单元只能通过外壳散热，所以在高温、密封的空间里应按额定负载的 70-80% 来选型，装在通风处，并且要接受 IP67 产品线止步于 400W、而带通风的 IP65 产品线可达 600W 这一点。这是物理规律，不是推销。</p>

<div class="highlight">
<strong>高温是无声的杀手：</strong> 每超出额定温度 10&deg;C，电容寿命大约减半。一台在密封坑里被烤着的 400W IP67 驱动，会比一台选型正确、装在阴凉通风处的 IP65 单元坏得更快。要让等级匹配环境温度，而不只是匹配瓦数。
</div>

<h2>第 4 步：是否调光或暴露于浪涌？</h2>

<p>户外标识常常需要调光（夜间用 0-10V）并暴露于浪涌（长线路上的雷电）。请选择支持你所采用调光标准的驱动，并在进线处加装外部 SPD——参见<a href="/blog-10/">调光指南</a>与<a href="/blog-12/">浪涌指南</a>。</p>

<h2>一行决策</h2>

<p><strong>干燥 &rarr; 室内。有雨但无积水 &rarr; IP65。积水、沿海或需冲洗 &rarr; IP67。户外超过 400W &rarr; 有遮挡的带通风 IP65。</strong></p>

<p>发来安装位置的照片，再加上负载瓦数和线路长度。我们会如实告诉你该买哪条产品线——包括在更便宜的 IP65 才是正确答案的时候。</p>

<div class="cta-box">
<h3>不确定你的现场需要哪个等级？</h3>
<p>发来安装位置照片以及负载和线路长度。我们会如实告诉你该买哪条产品线。</p>
<a href="/#inquiry" class="btn">获取等级建议</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-6/"><span class="rel-cat">技术指南</span><span class="rel-title">IP67 还是 IP65：你需要哪种防水 LED 驱动？</span></a><a class="rel-card" href="/blog-12/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 驱动的浪涌防护：雷电与瞬变</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 对比</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 电源功率怎么选：瓦数与余量</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-12/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">LED 驱动的浪涌防护：雷电与瞬变</span></a><a class="pn-next" href="/blog-14/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 装置的线径与压降</span></a></nav>
</main>"""


BLOG_BODY['zh']['blog-14'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 装置的线径与压降</h1>
<div class="meta">技术指南 &middot; 2026 年 10 月 &middot; 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-adapter.avif"><source type="image/webp" srcset="/images/product-adapter.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-adapter.jpg" alt="面向压降的 LED 装置线缆选型" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>“远端 LED 变暗”最常见的单一原因不是驱动——而是线缆。线径选得太细，压降就会在灯还没看到电之前偷走亮度。这就是我们在每一次安装中使用的选型方法。</p>

<h2>决定一切的定律</h2>

<div class="highlight">
<strong>压降 = 电流 &times; 线缆电阻。</strong> 电阻随长度增加、随截面积减小而上升，所以线缆越长或越细，压降的电压就越多。把总压降控制在 <strong>5%</strong> 以内（12V 上为 0.6V，24V 上为 1.2V），远端就能保持明亮。
</div>

<h2>12V 与 24V 分别能跑多远？</h2>

<p>在相同瓦数下，24V 的电流只有 12V 的一半，因此损耗约为四分之一，能跑的距离大约翻倍：</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">负载</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">线缆</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">12V 最大长度</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">24V 最大长度</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">24 W</td><td style="padding:10px 14px;border:1px solid var(--b)">1.5 mm&sup2; (16 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">48 W</td><td style="padding:10px 14px;border:1px solid var(--b)">2.5 mm&sup2; (14 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">96 W</td><td style="padding:10px 14px;border:1px solid var(--b)">4 mm&sup2; (12 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~7 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~14 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">192 W</td><td style="padding:10px 14px;border:1px solid var(--b)">6 mm&sup2; (10 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~5 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~10 m</td></tr>
</tbody>
</table>

<h2>克服压降的三种方法</h2>

<ol>
<li><strong>改用 24V。</strong> 对于任何超过约 5 m 的线路，24V 在大多数房间里都能直接消除这个问题（见<a href="/blog-7/">12V 与 24V 指南</a>）。</li>
<li><strong>两端同时供电。</strong> 有效长度减半，压降也随之减半。</li>
<li><strong>加粗线缆。</strong> 升一档成本很低，却能解决远端偏暗；如果线缆埋地或与市电捆在一起，就升两档。</li>
</ol>

<h2>我们常见到的两个错误</h2>

<ul>
<li><strong>按驱动而不是按线路来选线。</strong> 驱动额定没问题；是距离在扼杀亮度。用上面的表，拿不准就再加粗。</li>
<li><strong>用音箱线。</strong> 细的“灯线”看着整洁，却让压降翻倍。请按负载所需截面积使用真正符合市电规格的软线。</li>
</ul>

<div class="highlight">
<strong>计算示例：</strong> 10 m 的 14.4W/m 灯带 = 24V 下 144W = 6A。通过 2.5 mm&sup2; 约产生 1.0V 压降——低于 1.2V（5%）的预算，所以仍然明亮。同样的负载在 12V 下要降到相同压降，大约需要 4 mm&sup2;。
</div>

<h2>我们需要你提供什么</h2>

<p>请提供负载瓦数、输出电压（12V 或 24V）、线缆长度以及计划使用的截面积。我们会确认这条线路是否安全——或者在安装前告诉你要升到 24V 或更粗的线缆。</p>

<div class="cta-box">
<h3>担心远端 LED 偏暗？</h3>
<p>发来负载、电压、线缆长度和截面积。我们会确认线路是否安全——或者告诉你要升到 24V 或更粗的线缆。</p>
<a href="/#inquiry" class="btn">核算我的线径</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-7/"><span class="rel-cat">选购指南</span><span class="rel-title">12V 还是 24V：LED 电源怎么选</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 电源功率怎么选：瓦数与余量</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">三步选对 LED 电源</span></a><a class="rel-card" href="/blog-13/"><span class="rel-cat">选购指南</span><span class="rel-title">为户外与恶劣场所选择 LED 电源</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-13/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">为户外与恶劣场所选择 LED 电源</span></a><a class="pn-next" href="/blog/"><span class="pn-lab">下一篇</span><span class="pn-t">现场笔记</span></a></nav>
</main>"""
