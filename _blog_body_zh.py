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
