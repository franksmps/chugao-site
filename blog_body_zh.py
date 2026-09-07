# -*- coding: utf-8 -*-
"""Chinese body copy for the 3 newest Field Notes posts (blog-6/7/8).

These posts were authored in English and fanned out to all 11 languages with
only the *shell* localized (nav, title, description). Their body text stayed
English for every language. This module supplies a fully-Chinese <main>
block so zh/blog-6|7|8 read natively.

build_i18n.build_page swaps the whole `<main class="article">…</main>` region
for lang == 'zh' with the string below, *after* apply_translations() has run
(so the shell is already localized and the swap replaces the English body).
All internal links keep the site's root-absolute style (/blog-2/, /#inquiry)
so they match the existing behaviour of every other zh blog page.
"""
BLOG_BODY_ZH = {}

BLOG_BODY_ZH['blog-6'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>IP67 还是 IP65：你需要哪种防水 LED 驱动？</h1>
<div class="meta">技术指南 · 2026 年 6 月 · 阅读约 9 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="IP67 防水 LED 驱动电源与 IP65 防雨驱动电源并排放置" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>“防水”不是一个规格，而是一项测试结果。IP65 与 IP67 驱动电源在参数表上几乎一模一样，却能扛住完全不同的工况；选错是我们在现场见到的最常见的户外早期失效原因。</p>

<p>本指南拆解每种等级真正防护什么、各自在哪里会失效，以及如何做决定——而不必为用不上的防护多花钱。</p>

<h2>两位数分别代表什么</h2>

<p>每个 IP 代码由两位数字组成。第一位是固体（防尘），第二位是液体（防水）。对 LED 驱动电源来说，第一位几乎都是 6，即完全防尘。所以真正的差别在第二位。</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">等级</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">必须通过的测试</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">能扛住的工况</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">任意方向 6.3 mm 水流喷射，3 分钟</td><td style="padding:10px 14px;border:1px solid var(--b)">雨水、溅水、远距离冲洗、粉尘</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">浸入 1 米水深 30 分钟</td><td style="padding:10px 14px;border:1px solid var(--b)">短时浸水、积水、冲洗、盐雾</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">持续浸水，深度与厂家约定</td><td style="padding:10px 14px;border:1px solid var(--b)">喷泉、水池、地下井</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>重要：</strong> IP67 不能替代 IP65。一个驱动电源可能通过浸水测试（IP67），但如果厂家只按喷流测试，其喷流等级仍可能只是“5”。这就是为什么 CHUGAO 的防水系列标为 <strong>IP67 / IP68</strong>，并且额外做了喷流测试——请向供应商确认实际做了哪些测试，而不只是看印在上面的数字。
</div>

<h2>IP65 何时是正确选择</h2>

<p>只要驱动电源暴露在天气中、但从不泡在水里，IP65 就是最划算的选择：</p>

<ul>
<li><strong>标识与发光字</strong>——驱动电源装在密封的标识箱体内。</li>
<li><strong>广告牌与灯箱</strong>——雨水从外壳流走，不会积存。</li>
<li><strong>有顶走廊、雨棚、半户外吊顶</strong>——潮湿多尘，但保持干燥。</li>
<li><strong>大功率 100-600W</strong>——带通风口的金属外壳比密封灌封单元散热好得多，这正是该系列能做到 600W 的原因。</li>
</ul>

<p>如果你的安装属于以上任意一种，我们的 <a href="/products/ip65/">IP65 防雨驱动电源</a> 比灌封方案更便宜、温度更低。在这里为 IP67 多花钱，只会换来一个更烫的驱动电源。</p>

<h2>何时必须升级到 IP67</h2>

<p>当水可能在外壳周围积存，或空气本身具有腐蚀性时，请选择全灌封的 <a href="/products/ip67/">IP67 防水驱动电源</a>：</p>

<ul>
<li><strong>地面或地下安装</strong>——花园灯、步道灯、暴雨后积水的柱灯。</li>
<li><strong>喷泉、泳池、水景</strong>——溅水和短时浸水是常态，不是意外。</li>
<li><strong>沿海与近海场所</strong>——盐雾会从内部腐蚀带通风口的金属外壳；硅胶灌封加盐雾测试才是唯一耐用的方案。</li>
<li><strong>冲洗区域</strong>——食品加工、洗车场、定期冲洗的隧道。</li>
<li><strong>热带暴雨</strong>——带压力的大雨更像喷流，而不是阵雨。</li>
</ul>

<h2>没人写进参数表的那笔权衡</h2>

<p>密封挡得住水，也留住了热。全灌封的 IP67 单元只能靠外壳散热，因此在相同负载下比带通风口的 IP65 外壳更烫。实际后果：</p>

<ol>
<li><strong>留更多余量。</strong> 当 IP67 驱动电源装在闷热、密闭的空间时，按额定负载的 70-80% 选型，而不是 80-90%。</li>
<li><strong>装在通风处，不要埋起来。</strong> 把灌封驱动电源丢进没有气流的密封坑里，无论什么 IP 等级都会煮坏。</li>
<li><strong>预期上限更短。</strong> 这就是为什么 CHUGAO 的 IP67 系列止步于 400W，而带通风口的 IP65 系列能做到 600W——这是物理，不是营销。</li>
</ol>

<h2>你实际在为什么买单</h2>

<p>在同等 200W 单元上，灌封增加了材料和工艺成本：硅胶材料、真空灌封、更长固化时间，以及 100% 检漏。实际中每只只是适度溢价——而比起去海边工地换坏驱动电源的上门成本，这点溢价便宜得多。真正昂贵的不是驱动电源，而是<strong>那次上门</strong>。</p>

<h2>四个问题就能定</h2>

<ol>
<li><strong>驱动电源所在位置会积水吗？</strong> 会 → IP67。不会 → IP65 即可。</li>
<li><strong>在沿海，或会被冲洗吗？</strong> 会 → 带盐雾测试的 IP67。</li>
<li><strong>需要超过 400W 吗？</strong> 会 → 带通风口的 IP65 系列，装在遮蔽处。</li>
<li><strong>驱动电源在密封灯具或标识箱内吗？</strong> 会 → IP65 就够了，而且温度更低。</li>
</ol>

<p>还在犹豫？把安装位置的照片和负载发给我们。我们会如实告诉你该买哪个系列——包括什么时候更便宜的 IP65 才是正确答案。我们发出的每一个单元，无论哪个系列，都通过 CE 与 RoHS 认证，出厂前经过 48 小时满载老化，并享 3 年质保，50 台起订，支持 OEM/ODM。</p>

<div class="cta-box">
<h3>还不确定你的现场需要哪种等级？</h3>
<p>把安装位置的照片和负载（瓦数）发给我们。我们会告诉你该买哪个系列——包括什么时候更便宜的 IP65 才是正确答案。</p>
<a href="/#inquiry" class="btn">获取选型建议</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口的金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">3 步选对 LED 电源</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">选购指南</span><span class="rel-title">12V 还是 24V：LED 电源怎么选</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-5/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a><a class="pn-next" href="/blog-7/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">12V 还是 24V：LED 电源怎么选</span></a></nav>
</main>"""

BLOG_BODY_ZH['blog-7'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>12V 还是 24V：LED 电源怎么选</h1>
<div class="meta">选购指南 · 2026 年 7 月 · 阅读约 8 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-adapter.avif"><source type="image/webp" srcset="/images/product-adapter.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-adapter.jpg" alt="12V 与 24V LED 电源并排放置" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>12V 和 24V 都能驱动 LED 灯带。差别体现在电缆上的发热——而它决定了灯带末端变暗之前你能拉多长。下面是其中的数学，以及由此得出的简单法则。</p>

<h2>电压到底改变了什么</h2>

<p>在相同功率下，24V 系统的电流只有 12V 系统的一半：</p>

<div class="highlight">
<strong>功率 = 电压 × 电流。</strong> 一个 96W 负载在 12V 下抽取 <strong>8 A</strong>，在 24V 下仅 <strong>4 A</strong>。电缆上的压降与电流成正比，因此电流减半大致让损耗降到四分之一——在相同亮度损失下，线缆长度大约能拉到两倍。
</div>

<h2>能拉多长？</h2>

<p>恒压 LED 灯带的经验法则：把压降控制在 <strong>5%</strong> 以内（12V 下为 0.6V，24V 下为 1.2V）。从一端供电时，实际的单段长度上限：</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">负载</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">线缆</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">12V 最大长度</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">24V 最大长度</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">24 W（2 A / 1 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">1.5 mm²（16 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">约 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">约 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">48 W（4 A / 2 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">2.5 mm²（14 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">约 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">约 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">96 W（8 A / 4 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">4 mm²（12 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">约 7 m</td><td style="padding:10px 14px;border:1px solid var(--b)">约 14 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">192 W（16 A / 8 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">6 mm²（10 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">约 5 m</td><td style="padding:10px 14px;border:1px solid var(--b)">约 10 m</td></tr>
</tbody>
</table>

<p>比这更长？从两端给灯带供电，或把它拆成同一驱动电源下的并联段。这两招在 12V 上都有效，但 24V 在大多数房间里直接免除了这个问题。</p>

<h2>何时 12V 仍是正确的答案</h2>

<ul>
<li><strong>5 m 以内的短距离</strong>——橱柜底灯、展示柜、层架灯、小标识。</li>
<li><strong>房车、船舶与太阳能系统</strong>——整套系统本来就跑在 12V 电池上。</li>
<li><strong>替换工程</strong>——现有的灯带和控制器是 12V；改电压意味着全部重新布线。</li>
<li><strong>极小负载</strong>——单个展示用的 15W 适配器，12V 更简单也更便宜。</li>
</ul>

<p>我们的 <a href="/products/adapters/">LED 适配器 5-200W</a> 以单一通用 100-240V 输入覆盖 12V、24V、36V、48V，一个型号即可发往任何市场。</p>

<h2>何时 24V 胜出</h2>

<ul>
<li><strong>超过 5 m 的距离</strong>，或任何无法从两端回供电缆的走线。</li>
<li><strong>商业吊顶与线性走线</strong>——一个 24V 驱动电源能喂一长条连续灯带，而 12V 需要三个电源。</li>
<li><strong>100W 以上</strong>——12V 下的电流大到让线缆成本和接头发热开始成为问题。</li>
<li><strong>建筑项目</strong>，其中末端可见的亮度衰减不可接受。</li>
</ul>

<h2>我们常看到的两个错误</h2>

<ol>
<li><strong>在一个驱动电源上混用电压。</strong> 24V 电源上的 12V 灯带会立刻烧毁。通电前先核对灯带标签。</li>
<li><strong>按驱动电源而非按走线选线缆。</strong> 问题不在驱动电源额定值——而在距离。用上面的表，若线缆埋设或与市电捆绑，再升一号线径。</li>
</ol>

<h2>恒压与恒流</h2>

<p>12V 和 24V 灯带都是<em>恒压</em>：驱动电源保持电压，灯带的电阻决定电流。大功率灯具（筒灯、投光灯）通常是<em>恒流</em>——以 mA 而非伏特标注。如果你的灯具标称 350 mA 或 700 mA，你需要恒流驱动电源，12V/24V 的问题不适用。把灯具规格告诉我们，我们会为你匹配。</p>

<h2>快速决策</h2>

<p><strong>距离 5 m 以内、电池系统，或同规格替换 &rarr; 12V。</strong><br>
<strong>距离超过 5 m、商业吊顶，或负载高于 100W &rarr; 24V。</strong></p>

<p>每一台 CHUGAO 驱动电源都通过 CE 与 RoHS 认证，经过 48 小时满载老化，并享 3 年质保。最小起订 50 台，可按您的规格在 OEM/ODM 下生产 12V/24V/36V/48V 版本。</p>

<div class="cta-box">
<h3>需要为您的走线长度选对电压？</h3>
<p>告诉我们负载、线缆走线长度和灯带类型。我们会确认 12V 还是 24V，以及能让每一米都保持满亮度的型号。</p>
<a href="/#inquiry" class="btn">获取电压建议</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口的金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">3 步选对 LED 电源</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">技术指南</span><span class="rel-title">IP67 还是 IP65：你需要哪种防水 LED 驱动</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技术指南</span><span class="rel-title">LED 电源功率怎么选：瓦数与余量</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">技术指南</span><span class="rel-title">IP20、IP65、IP67、IP68 怎么选</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-6/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">IP67 还是 IP65：你需要哪种防水 LED 驱动</span></a><a class="pn-next" href="/blog-8/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">LED 电源功率怎么选：瓦数与余量</span></a></nav>
</main>"""

BLOG_BODY_ZH['blog-8'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 返回现场笔记</a>

<h1>LED 电源功率怎么选：瓦数与余量</h1>
<div class="meta">技术指南 · 2026 年 8 月 · 阅读约 7 分钟</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="为商业照明负载选配的室内 LED 驱动电源" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 电源选小了，会发烫、提前变暗、一年内报废；选得过大，则为用不上的容量买单。两者之间是一道大多买家跳过的 20 分钟计算。</p>

<h2>第一步：累加真实负载</h2>

<p>把驱动电源要带的每一个灯具的功率相加。用灯具的<strong>输入</strong>功率，而不是“等效”标称——一个“50W 等效”的筒灯可能只耗 9W。</p>

<ul>
<li>LED 灯带：每米瓦数 × 米数（看灯带标签：常见 4.8W/m、9.6W/m、14.4W/m）。</li>
<li>面板灯与格栅灯：灯具上的铭牌。</li>
<li>标识模组：模组数 × 单模组瓦数。</li>
</ul>

<p>示例：12 米 14.4W/m 灯带 = <strong>173W</strong>。</p>

<h2>第二步：加 20% 余量</h2>

<p>乘以 1.2。这 20% 不是冗余——它覆盖了三件都会缩短驱动电源寿命的事：</p>

<ol>
<li><strong>发热。</strong> 在 40°C 吊顶里满载运行的驱动电源，比同款 80% 负载时烫得多。每超过额定温度 10°C，电容寿命大约减半。</li>
<li><strong>市电波动。</strong> 输入电压跌落与浪涌，有余量时吸收得更从容。</li>
<li><strong>日后扩容。</strong> 明年有人再加一段灯带。</li>
</ol>

<p>173W × 1.2 = <strong>208W</strong> &rarr; 选 <strong>240W 或 250W</strong> 型号，即比你的数值高一号的标准额定。</p>

<div class="highlight">
<strong>经验法则：</strong> 让驱动电源运行在<strong>额定值的 80% 或更低</strong>。从 60W 升到 100W 只多几美元；派人换一台坏掉的驱动电源，成本是其上百倍。
</div>

<h2>第三步：选断路器前先核对浪涌电流</h2>

<p>开关电源通电瞬间会抽取很大但极短的浪涌——通常 30-60 A，持续几毫秒，大功率单元有时更高。如果把十个驱动电源接在同一个开关或接触器上，浪涌会叠加，可能在第一天就跳闸或焊死继电器。</p>

<ul>
<li><strong>多个小驱动电源？</strong> 用时间延时继电器错开启动，或用按叠加浪涌额定选型的接触器。</li>
<li><strong>单个大驱动电源？</strong> 用 C 型或 D 型断路器，而非 B 型。</li>
<li><strong>索要浪涌数值</strong>——它写在规格书上，给不出来的供应商是在猜。</li>
</ul>

<h2>第四步：按温度降额</h2>

<p>大多数驱动电源在 40°C 及以下环境可满额输出。超过后需降额——通常每升高 1°C 输出降 2-3%，但具体看型号的曲线。实际情形：</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">安装位置</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">典型环境温度</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">应对方法</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">开放式室内吊顶</td><td style="padding:10px 14px;border:1px solid var(--b)">25-35°C</td><td style="padding:10px 14px;border:1px solid var(--b)">标准 20% 余量已足够</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">密闭吊顶空隙</td><td style="padding:10px 14px;border:1px solid var(--b)">45-55°C</td><td style="padding:10px 14px;border:1px solid var(--b)">再加 30-40% 余量，或把驱动电源移到开阔通风处</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">户外直晒</td><td style="padding:10px 14px;border:1px solid var(--b)">50-65°C</td><td style="padding:10px 14px;border:1px solid var(--b)">给设备遮阴，或升一号并用灌封的 <a href="/products/ip67/">IP67</a> 型号</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">密闭标识箱内</td><td style="padding:10px 14px;border:1px solid var(--b)">45-60°C</td><td style="padding:10px 14px;border:1px solid var(--b)">给箱体通风，或用带通风口的 <a href="/products/ip65/">IP65</a> 外壳</td></tr>
</tbody>
</table>

<h2>算例：店面招牌，8 个模组</h2>

<p>招牌模组：8 × 1.5W = 12W。灯带点缀：4 m × 9.6W/m = 38W。合计 = 50W。余量 ×1.2 = 60W。装在夏季达 50°C 的密闭箱内 &rarr; 再加 30% &rarr; 78W。选 <strong>100W</strong> 单元。它将以约一半负载运行，保持低温，寿命超过招牌本身。</p>

<h2>五个选配错误</h2>

<ol>
<li><strong>用“等效瓦数”</strong>而非真实功耗。</li>
<li><strong>按 100% 负载选型</strong>，不留余量。</li>
<li><strong>忽略密闭外壳内的环境温度</strong>。</li>
<li><strong>十个驱动电源接一个开关</strong>却不核对浪涌。</li>
<li><strong>忘记日后</strong>——多出的那段灯带、第二个招牌。</li>
</ol>

<h2>我们需要您提供什么</h2>

<p>把负载（瓦数）、输出电压（12V 或 24V）、安装位置与大致环境温度，以及所需数量发给我们。我们会推荐合适的额定值——并在更小的便宜型号确实够用时如实相告。</p>

<div class="cta-box">
<h3>要我们帮您核对选型吗？</h3>
<p>把负载、输出电压、安装位置与数量发给我们。我们会确认合适的额定值——或告诉您更小的型号就够。</p>
<a href="/#inquiry" class="btn">获取选型核对</a>
</div>

<section class="product-crosslink" aria-label="相关产品"><h2 class="related-h">了解 CHUGAO 产品</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 适配器 5-200W</span><span class="pc-desc">适用于灯带、模组与标识的紧凑型 12V/24V 单元。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">室内 LED 驱动电源 50-400W</span><span class="pc-desc">带主动 PFC 的恒压驱动，适用于吊灯与面板灯。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水驱动电源 10-400W</span><span class="pc-desc">全灌封、盐雾测试，适用于潮湿与沿海场所。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨驱动电源 100-600W</span><span class="pc-desc">带通风口的金属外壳，适用于标识与半户外安装。</span></a></div></section>

<section class="related" aria-label="相关文章">
  <h2 class="related-h">更多现场笔记</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技术</span><span class="rel-title">3 步选对 LED 电源</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">选购指南</span><span class="rel-title">12V 还是 24V：LED 电源怎么选</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">技术指南</span><span class="rel-title">IP67 还是 IP65：你需要哪种防水 LED 驱动</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">技术深读</span><span class="rel-title">LED 驱动寿命：MTBF、L70 与真实使用寿命</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="文章导航"><a class="pn-prev" href="/blog-7/" rel="prev"><span class="pn-lab">上一篇</span><span class="pn-t">12V 还是 24V：LED 电源怎么选</span></a><a class="pn-next" href="/blog/" rel="next"><span class="pn-lab">下一篇</span><span class="pn-t">现场笔记</span></a></nav>
</main>"""
