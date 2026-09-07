# -*- coding: utf-8 -*-
"""Per-language Chinese/Japanese/Korean/Italian body copy for the 3 newest
Field Notes posts (blog-6/7/8).

These posts were authored in English and fanned out to all 11 languages with
only the *shell* localized (nav, title, description). Their body text stayed
English for every language. This module supplies a fully-translated <main>
block per language so zh/ja/ko/it readers get the article natively.

build_i18n.build_page swaps the whole `<main class="article">…</main>` region
with BLOG_BODY[lang][name] (after apply_translations has run, so the shell is
already localized and the swap replaces the English body). All internal links
keep the site's root-absolute style (/blog-2/, /#inquiry) to match the existing
behaviour of every other localized blog page.

Note: ja/ko/it bodies here are AI translations pending native review, same
caveat as their SUBTR inner-page bodies.
"""
BLOG_BODY = {}

BLOG_BODY['zh'] = {}
BLOG_BODY['ja'] = {}
BLOG_BODY['ko'] = {}
BLOG_BODY['it'] = {}

# ============================ blog-6 (IP67 vs IP65) ============================
BLOG_BODY['zh']['blog-6'] = """<main class="article">
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

BLOG_BODY['ja']['blog-6'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>IP67 か IP65 か：どちらの防水 LED ドライバーが必要ですか？</h1>
<div class="meta">技術ガイド · 2026年6月 · 約9分</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="IP67 防水 LED ドライバーと IP65 防雨ドライバーの並び" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>「防水」は単一の仕様ではなく、試験結果です。IP65 と IP67 のドライバーは仕様書上ほぼ同じに見えますが、まったく異なる用途に耐えます。誤った選択は、現場で最もよく見る屋外の早期故障の原因です。</p>

<p>本ガイドでは、各等級が実際に守るもの、それぞれが破綻する境界、そして不要な保護にお金を払わずに決める方法を解説します。</p>

<h2>2 桁の数字の意味</h2>

<p>各 IP コードは 2 桁の数字です。1 桁目は固体（防塵）、2 桁目は液体（防水）です。LED ドライバーでは 1 桁目はほぼ常に 6（完全防塵）です。本当の違いは 2 桁目にあります。</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">等級</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">通過が必要な試験</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">耐えられる状況</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">任意の方向からの 6.3 mm の水流、3 分間</td><td style="padding:10px 14px;border:1px solid var(--b)">雨、飛沫、距離を置いた水洗い、粉塵</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">1 m の水深への 30 分間の浸漬</td><td style="padding:10px 14px;border:1px solid var(--b)">一時的な冠水、停滞水、水洗い、塩霧</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">継続的な浸漬（深度は製造元と協定）</td><td style="padding:10px 14px;border:1px solid var(--b)">噴水、プール、地中の井戸</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>重要：</strong> IP67 は IP65 に取って代わるものではありません。ドライバーは浸水試験（IP67）に合格していても、製造元が噴流試験を行った場合のみ噴流等級「5」となります。だからこそ CHUGAO の防水ラインは「IP67 / IP68」と表示され、さらに噴流試験も実施しています——印字された数字だけでなく、実際にどの試験が行われたかを供給元に確認してください。
</div>

<h2>IP65 が適している場合</h2>

<p>ドライバーが天候に曝され、水に浸からない場合、IP65 が最も経済的です：</p>

<ul>
<li><strong>看板と発光文字</strong>——ドライバーは密閉された看板箱内。</li>
<li><strong>広告塔とライトボックス</strong>——雨水は筐体を流れ、たまらない。</li>
<li><strong>屋根付き歩廊、ひさし、半屋外天井</strong>——湿気と粉塵はあるが乾燥。</li>
<li><strong>大電力 100-600W</strong>——通気口付き金属筐体は密閉ポッティング品よりはるかに放熱が良く、これが 600W に達する理由。</li>
</ul>

<p>上記のいずれかであれば、<a href="/products/ip65/">IP65 防雨ドライバー</a> はポッティング品より安く、温度も低くなります。ここで IP67 に余計な出費をするのは、単により熱いドライバーを買うだけです。</p>

<h2>IP67 に引き上げる必要がある場合</h2>

<p>水が筐体の周りにたまる、あるいは空気自体が腐食性の場合、完全ポッティングの <a href="/products/ip67/">IP67 防水ドライバー</a> を選択してください：</p>

<ul>
<li><strong>地上または地中設置</strong>——庭園灯、歩道灯、豪雨後に冠水するポール灯。</li>
<li><strong>噴水、プール、水景</strong>——飛沫と一時的浸漬は例外ではなく日常。</li>
<li><strong>沿岸・海洋施設</strong>——塩霧は通気口付き金属筐体を内側から腐食させる；シリコンポッティングと塩霧試験のみが耐久的な解決策。</li>
<li><strong>洗浄エリア</strong>——食品加工、洗車場、定期的に高圧洗浄されるトンネル。</li>
<li><strong>熱帯の豪雨</strong>——圧力を伴う大雨は噴流に近く、通り雨ではない。</li>
</ul>

<h2>仕様書に書かれないトレードオフ</h2>

<p>密閉は水を遮るが、熱も閉じ込めます。完全ポッティングの IP67 ユニットは筐体のみで放熱するため、同じ負荷では通気口付き IP65 筐体より高温になります。実際の影響：</p>

<ol>
<li><strong>余裕を大きく取る。</strong> IP67 を高温・密閉空間に置く場合、定格負荷の 70-80% で選定し、80-90% ではなく。</li>
<li><strong>通気のある場所に設置し、埋めない。</strong> 通気のない密閉ピットにポッティング品を入れれば、等級に関係なく焼き切れる。</li>
<li><strong>上限は短くなる。</strong> CHUGAO の IP67 ラインが 400W で止まり、通気口付き IP65 ラインが 600W に達するのは物理であり、マーケティングではない。</li>
</ol>

<h2>実際に支払うもの</h2>

<p>同仕様の 200W ユニットでは、ポッティングは材料と工程コストを増やします：シリコン材、真空ポッティング、長い硬化時間、100% 漏れ試験。実際にはユニットあたりわずかな上乗せ——しかし海辺の現場で故障したドライバーを交換に行く出張費用に比べれば、この上乗せはずっと安いです。本当に高いのはドライバーではなく「その出張」です。</p>

<h2>4 つの質問で決まる</h2>

<ol>
<li><strong>ドライバーの設置位置に水がたまるか？</strong> はい → IP67。いいえ → IP65 で十分。</li>
<li><strong>沿岸か、水洗いされるか？</strong> はい → 塩霧試験付き IP67。</li>
<li><strong>400W 以上必要か？</strong> はい → 通気口付き IP65 ラインを遮蔽場所に。</li>
<li><strong>ドライバーは密閉灯具や看板箱内か？</strong> はい → IP65 で十分、かつ低温。</li>
</ol>

<p>まだ迷うなら、設置場所の写真と負荷をお送りください。どちらのラインを買うべきか——より安い IP65 が正解の場合も含めて——正直にお答えします。当社が出荷するすべてのユニットは、どのラインでも CE と RoHS 認証を取得し、出荷前に 48 時間の全負荷エージングを経て、3 年保証、最小ロット 50 台、OEM/ODM 対応です。</p>

<div class="cta-box">
<h3>現場にどの等級が必要かまだ不明ですか？</h3>
<p>設置場所の写真と負荷（ワット数）をお送りください。より安い IP65 が正解の場合も含めて、どちらのラインを買うべきかお答えします。</p>
<a href="/#inquiry" class="btn">選定アドバイスを得る</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">テープライト、モジュール、サイン用のコンパクトな 12V/24V ユニット。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内用 LED ドライバー 50-400W</span><span class="pc-desc">アクティブ PFC 付き定電圧、吊り下げ灯やパネル灯用。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">完全ポッティング、塩水噴霧試験済み、潮湿・沿岸向け。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">通気口付き金属筐体、サイン・半屋外設置向け。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の違い</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで選ぶ正しい LED 電源</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深読み</span><span class="rel-title">LED ドライバーの寿命：MTBF・L70・実際のもち</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">購入ガイド</span><span class="rel-title">12V か 24V か：LED 電源の選び方</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビ"><a class="pn-prev" href="/blog-5/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">LED ドライバーの寿命：MTBF・L70・実際のもち</span></a><a class="pn-next" href="/blog-7/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">12V か 24V か：LED 電源の選び方</span></a></nav>
</main>"""

BLOG_BODY['ko']['blog-6'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>IP67 vs IP65: 어떤 방수 LED 구동장치를 선택해야 할까?</h1>
<div class="meta">기술 가이드 · 2026년 6월 · 약 9분 읽기</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="IP67 방수 LED 구동장치와 IP65 방우 구동장치 나란히" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>"방수"는 하나의 사양이 아니라 시험 결과입니다. IP65와 IP67 구동장치는 데이터시트상 거의 동일해 보이지만, 완전히 다른 환경을 견뎠냅니다. 잘못 고르는 것은 현장에서 가장 흔히 보는 옥외 초기 고장의 원인입니다.</p>

<p>이 가이드에서는 각 등급이 실제로 보호하는 것, 각각이 실패하는 지점, 그리고 필요 없는 보호에 돈을 쓰지 않고 결정하는 방법을 풉니다.</p>

<h2>두 자리 숫자의 의미</h2>

<p>모든 IP 코드는 두 자리 숫자입니다. 첫째는 고체(방진), 둘째는 액체(방수)입니다. LED 구동장치에서 첫째는 거의 항상 6(완전 방진)입니다. 진짜 차이는 둘째 자리에 있습니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">등급</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">통과해야 할 시험</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">견디는 상황</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">임의 방향 6.3 mm 수류 분사, 3분</td><td style="padding:10px 14px;border:1px solid var(--b)">비, 물튀김, 거리 둔 호스 세척, 분진</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">수심 1 m 30분 침지</td><td style="padding:10px 14px;border:1px solid var(--b)">일시적 침수, 고인 물, 세척, 염수 분무</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">지속 침지(수심은 제조사와 협의)</td><td style="padding:10px 14px;border:1px solid var(--b)">분수, 수영장, 지중 우물</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>중요:</strong> IP67이 IP65를 대체하는 것은 아닙니다. 구동장치는 침수 시험(IP67)에 합격해도, 제조사가 분사 시험을 한 경우에만 분사 등급이 "5"가 됩니다. 그래서 CHUGAO 방수 라인은 "IP67 / IP68"로 표기되고 추가로 분사 시험도 거칩니다—인쇄된 숫자만이 아니라 실제로 어떤 시험을 통과했는지 공급자에게 확인하세요.
</div>

<h2>IP65가 정답인 경우</h2>

<p>구동장치가 날씨에 노출되지만 물에 잠기지 않는다면 IP65가 가장 경제적입니다:</p>

<ul>
<li><strong>간판과 발광 글자</strong>——구동장치는 밀폐된 사인 박스 안.</li>
<li><strong>광고판과 라이트박스</strong>——빗물은 하우징을 타고 흐르고 고이지 않음.</li>
<li><strong>지붕 달린 보도, 캐노피, 반옥외 천장</strong>——습하고 먼지 많지만 건조.</li>
<li><strong>고출력 100-600W</strong>——통풍구 있는 금속 하우징이 밀봉 포팅형보다 훨씬 방열이 좋아 600W에 달하는 이유.</li>
</ul>

<p>위 중 하나라면 <a href="/products/ip65/">IP65 방우 구동장치</a>는 포팅 방식보다 저렴하고 온도도 낮습니다. 여기서 IP67에 돈을 더 쓰는 것은 더 뜨거운 구동장치를 사는 셈입니다.</p>

<h2>IP67로 올려야 하는 경우</h2>

<p>물이 하우징 주변에 고일 수 있거나 공기 자체가 부식성이라면 완전 포팅된 <a href="/products/ip67/">IP67 방수 구동장치</a>를 선택하세요:</p>

<ul>
<li><strong>지면 또는 지중 설치</strong>——정원등, 보도등, 폭우 후 침수되는 폴대등.</li>
<li><strong>분수, 수영장, 수경</strong>——물튀김과 일시적 침지는 예외가 아니라 일상.</li>
<li><strong>해안 및 해양 시설</strong>——염수 분무는 통풍구 있는 금속 하우징을 안쪽에서 부식시킴; 실리콘 포팅과 염수 분무 시험만이 유일한 내구적 해법.</li>
<li><strong>세척 구역</strong>——식품 가공, 세차장, 정기적으로 고압 세척되는 터널.</li>
<li><strong>열대성 호우</strong>——압력을 동반한 큰 비는 소나기가 아니라 분사에 가까움.</li>
</ul>

<h2>데이터시트에 적지 않는 트레이드오프</h2>

<p>밀봉은 물을 막지만 열도 가둡니다. 완전 포팅된 IP67 유닛은 하우징만으로 방열하므로 동일 부하에서 통풍구 있는 IP65 하우징보다 더 뜨거워집니다. 실제 결과:</p>

<ol>
<li><strong>여유를 더 남기세요.</strong> IP67을 더운 밀폐 공간에 두면 정격 부하의 70-80%로 선정, 80-90%가 아니라.</li>
<li><strong>통풍되는 곳에 설치하고 묻지 마세요.</strong> 통풍 없는 밀폐 피트에 포팅품을 넣으면 등급과 무관하게 익습니다.</li>
<li><strong>상한은 짧아집니다.</strong> CHUGAO IP67 라인이 400W에서 멈추고 통풍구 있는 IP65 라인이 600W에 이르는 것은 마케팅이 아니라 물리입니다.</li>
</ol>

<h2>실제로 지불하는 것</h2>

<p>동등 사양 200W 유닛에서 포팅은 재료와 공정 비용을 더합니다: 실리콘 소재, 진공 포팅, 긴 경화 시간, 100% 누수 검사. 실제로는 유닛당 약간의 프리미엄—하지만 해변 공사장에서 고장 난 구동장치를 교체하러 가는 출장 비용에 비하면 그 프리미엄은 훨씬 싸습니다. 진짜 비싼 것은 구동장치가 아니라 "그 출장"입니다.</p>

<h2>네 가지 질문으로 결정</h2>

<ol>
<li><strong>구동장치 설치 위치에 물이 고이나요?</strong> 예 → IP67. 아니요 → IP65면 충분.</li>
<li><strong>해안인가, 아니면 세척되나요?</strong> 예 → 염수 분무 시험을 거친 IP67.</li>
<li><strong>400W 이상 필요한가요?</strong> 예 → 통풍구 있는 IP65 라인을 차폐된 곳에.</li>
<li><strong>구동장치가 밀폐 조명이나 사인 박스 안인가요?</strong> 예 → IP65면 충분하고 더 시원함.</li>
</ol>

<p>여전히 망설이신다면 설치 위치 사진과 부하를 보내주세요. 어떤 라인을 사야 할지—더 저렴한 IP65가 정답인 경우도 포함해—정직하게 알려드리겠습니다. 당사가 출하하는 모든 유닛은 어떤 라인이든 CE와 RoHS 인증을 받았고, 출하 전 48시간 만부하 에이징을 거치며 3년 보증, 최소 주문 50대, OEM/ODM 지원입니다.</p>

<div class="cta-box">
<h3>현장에 어떤 등급이 필요한지 아직 모르시겠어요?</h3>
<p>설치 위치 사진과 부하(와트)를 보내주세요. 더 저렴한 IP65가 정답인 경우도 포함해 어떤 라인을 사야 할지 알려드리겠습니다.</p>
<a href="/#inquiry" class="btn">선정 조언 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 간판용 컴팩트 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내용 LED 구동장치 50-400W</span><span class="pc-desc">액티브 PFC 정전압, 펜던트·패널등용.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 구동장치 10-400W</span><span class="pc-desc">완전 포팅, 염수 분무 시험, 습윤·해안용.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 구동장치 100-600W</span><span class="pc-desc">통풍구 있는 금속 하우징, 간판·반옥외용.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">다른 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 비교</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 맞는 LED 전원 선택하기</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 구동장치 수명: MTBF, L70 그리고 실제 수명</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">구매 가이드</span><span class="rel-title">12V 또는 24V: LED 전원 어떻게 선택할까</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-5/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">LED 구동장치 수명: MTBF, L70 그리고 실제 수명</span></a><a class="pn-next" href="/blog-7/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">12V 또는 24V: LED 전원 어떻게 선택할까</span></a></nav>
</main>"""

BLOG_BODY['it']['blog-6'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; Torna alle Note dal Campo</a>

<h1>IP67 o IP65: quale driver LED impermeabile ti serve?</h1>
<div class="meta">Guida tecnica · Giugno 2026 · 9 min di lettura</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="Driver LED impermeabile IP67 accanto a un driver anti-pioggia IP65" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>"Impermeabile" non è una sola specifica — è un risultato di prova. Un driver IP65 e uno IP67 sembrano quasi identici sulla scheda tecnica, ma sopravvivono a compiti molto diversi, e scegliere quello sbagliato è la causa più comune di guasti precoci all'aperto che vediamo sul campo.</p>

<p>Questa guida spiega cosa protegge realmente ogni classe, dove cede ciascuna, e come decidere — senza pagare per una protezione di cui non hai bisogno.</p>

<h2>Cosa significano le due cifre</h2>

<p>Ogni codice IP ha due cifre. La prima è solidi (polveri), la seconda liquidi (acqua). Per i driver LED la prima è quasi sempre 6, cioè ermetico alla polvere. La vera differenza sta nella seconda cifra.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Classe</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Prova da superare</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Cosa sopravvive</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">Getto d'acqua da 6,3 mm da qualsiasi direzione, 3 minuti</td><td style="padding:10px 14px;border:1px solid var(--b)">Pioggia, spruzzi, lavaggio a distanza, polvere</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">Immersione in 1 m d'acqua per 30 minuti</td><td style="padding:10px 14px;border:1px solid var(--b)">Allagamenti temporanei, pozzanghere, lavaggio, nebbia salina</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">Immersione continua, profondità concordata con il costruttore</td><td style="padding:10px 14px;border:1px solid var(--b)">Fontane, piscine, pozzi interrati</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>Importante:</strong> IP67 non sostituisce IP65. Un driver può superare il test di immersione (IP67) e restare classificato solo "5" contro i getti se il costruttore lo ha testato così. Ecco perché la linea impermeabile CHUGAO è marcata "IP67 / IP68" ed è anche testata contro i getti — chiedi al fornitore quali test sono stati realmente eseguiti, non solo quale numero è stampato.
</div>

<h2>Dove IP65 è la scelta giusta</h2>

<p>IP65 è la soluzione conveniente ogni volta che il driver è esposto alle intemperie ma non rimane nell'acqua:</p>

<ul>
<li><strong>Insegne e lettere luminose</strong> — il driver è dentro una scatola segnaposto sigillata.</li>
<li><strong>Cartelloni e light box</strong> — la pioggia scorre sul contenitore, non ristagna.</li>
<li><strong>Passaggi coperti, pensiline, soffitti semi-estemi</strong> — umidi e polverosi, ma asciutti.</li>
<li><strong>Alta potenza, 100-600W</strong> — il contenitore metallico ventilato dissipa molto meglio di un'unità sigillata, ed è per questo che questa linea arriva a 600W.</li>
</ul>

<p>Se la tua installazione rientra in uno di questi casi, i nostri <a href="/products/ip65/">driver IP65 anti-pioggia</a> costano meno e girano più freschi di un equivalente sigillato. Pagare per IP67 qui non compra altro che un driver più caldo.</p>

<h2>Quando devi salire a IP67</h2>

<p>Scegli un driver <a href="/products/ip67/">IP67 impermeabile</a> completamente sigillato quando l'acqua può raccogliersi attorno alla scatola o l'aria stessa è aggressiva:</p>

<ul>
<li><strong>Installazioni a livello del suolo o interrate</strong> — luci da giardino, passerelle, pali che si allagano dopo forti piogge.</li>
<li><strong>Fontane, piscine, giochi d'acqua</strong> — spruzzi e immersioni temporanee sono la norma, non incidenti.</li>
<li><strong>Siti costieri e marini</strong> — la nebbia salina corrode da dentro un contenitore metallico ventilato; il potting in silicone più il test nebbia salina è l'unica risposta durevole.</li>
<li><strong>Aree di lavaggio</strong> — lavorazione alimentare, autolavaggi, tunnel lavati regolarmente.</li>
<li><strong>Piogge tropicali</strong> — la pioggia battente sotto pressione si comporta come un getto, non come un acquazzone.</li>
</ul>

<h2>Il compromesso che nessuno mette sulla scheda</h2>

<p>La tenuta trattiene l'acqua, ma trattiene anche il calore. Un'unità IP67 completamente sigillata dissipa solo attraverso la scatola, quindi gira più calda di un contenitore IP65 ventilato allo stesso carico. Conseguenze pratiche:</p>

<ol>
<li><strong>Lascia più margine.</strong> Dimensiona un IP67 al 70-80% del carico nominale, non 80-90%, se finisce in uno spazio caldo e sigillato.</li>
<li><strong>Montalo all'aria, non seppellito.</strong> Un driver sigillato in una buca ermetica senza flusso si cuoce indipendentemente dal suo grado IP.</li>
<li><strong>Aspetta una testa più bassa.</strong> Ecco perché la linea IP67 CHUGAO si ferma a 400W mentre la linea IP65 ventilata arriva a 600W — è fisica, non marketing.</li>
</ol>

<h2>Cosa paghi davvero</h2>

<p>Sulla stessa unità da 200W, il potting aggiunge costi di materiale e processo: composto siliconico, potting sottovuoto, tempo di cura più lungo e test di tenuta al 100%. Nella pratica è un premio modesto per unità — ed è molto più economico di un sopralluogo per sostituire driver guasti su un cantiere sul mare. Il vero costo non è il driver, è "quel sopralluogo".</p>

<h2>Quattro domande che risolvono</h2>

<ol>
<li><strong>L'acqua può ristagnare dove sta il driver?</strong> Sì → IP67. No → IP65 basta.</li>
<li><strong>È in zona costiera, o verrà lavato con getto?</strong> Sì → IP67 con test nebbia salina.</li>
<li><strong>Ti servono più di 400W?</strong> Sì → la linea IP65 ventilata, montata al riparo.</li>
<li><strong>Il driver è dentro una fixture o scatola segnaposto sigillata?</strong> Sì → IP65 basta, e girerà più fresco.</li>
</ol>

<p>Ancora indeciso? Inviaci una foto del luogo di installazione e il carico. Ti diremo onestamente quale linea comprare — anche quando la più economica IP65 è la risposta giusta. Ogni unità che spediamo, in entrambe le linee, è certificata CE e RoHS, esegue 48 ore di burn-in a pieno carico prima dell'imballaggio e ha 3 anni di garanzia, con ordine minimo 50 pz e opzioni OEM/ODM.</p>

<div class="cta-box">
<h3>Non sei sicuro di quale classe serve al tuo sito?</h3>
<p>Inviaci una foto del luogo e il carico in watt. Ti diremo quale linea comprare — anche quando la più economica IP65 è la risposta giusta.</p>
<a href="/#inquiry" class="btn">Ottieni una raccomandazione di classe</a>
</div>

<section class="product-crosslink" aria-label="Prodotti correlati"><h2 class="related-h">Esplora i prodotti CHUGAO</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">Adattatori LED 5-200W</span><span class="pc-desc">Unità compatte 12V/24V per strisce, moduli e insegne.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">Driver LED da interno 50-400W</span><span class="pc-desc">Tensione costante con PFC attivo per soffitti e pannelli.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">Driver impermeabili IP67 10-400W</span><span class="pc-desc">Completamente sigillati, test nebbia salina, per umido e coste.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">Driver anti-pioggia IP65 100-600W</span><span class="pc-desc">Contenitore metallico ventilato per insegne e semi-esterno.</span></a></div></section>

<section class="related" aria-label="Articoli correlati">
  <h2 class="related-h">Altre Note dal Campo</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">IP20 vs IP65 vs IP67 vs IP68</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">Tecnologia LED</span><span class="rel-title">Scegliere l'alimentatore LED giusto in 3 passi</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">Approfondimento</span><span class="rel-title">Durata dei driver LED: MTBF, L70 e quanto durano davvero</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">Guida all'acquisto</span><span class="rel-title">12V o 24V: come scegliere l'alimentatore LED</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="Navigazione articoli"><a class="pn-prev" href="/blog-5/" rel="prev"><span class="pn-lab">Articolo precedente</span><span class="pn-t">Durata dei driver LED: MTBF, L70 e quanto durano davvero</span></a><a class="pn-next" href="/blog-7/" rel="next"><span class="pn-lab">Articolo successivo</span><span class="pn-t">12V o 24V: come scegliere l'alimentatore LED</span></a></nav>
</main>"""

# ============================ blog-7 (12V vs 24V) ============================
BLOG_BODY['zh']['blog-7'] = """<main class="article">
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

BLOG_BODY['ja']['blog-7'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>12V か 24V か：LED 電源の選び方</h1>
<div class="meta">購入ガイド · 2026年7月 · 約8分</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-adapter.avif"><source type="image/webp" srcset="/images/product-adapter.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-adapter.jpg" alt="12V と 24V の LED 電源の並び" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>12V と 24V はどちらも LED ストリップを駆動できます。違いはケーブルの発熱として現れ、それがストリップ末端が暗くなる前に引ける距離を決めます。以下にその計算と、そこから導かれる簡単な法則を示します。</p>

<h2>電圧が実際に変えるもの</h2>

<p>同じワット数では、24V システムの電流は 12V システムの半分です：</p>

<div class="highlight">
<strong>電力 = 電圧 × 電流。</strong> 96W の負荷は 12V では 8A を引き、24V ではわずか 4A です。ケーブルの電圧降下は電流に比例するため、電流を半減させると損失は約 4 分の 1 に減り、同じ輝度低下でケーブル長を約 2 倍に引けます。
</div>

<h2>どれだけ引けるか</h2>

<p>恒圧 LED ストリップの目安：電圧降下を <strong>5%</strong> 未満（12V で 0.6V、24V で 1.2V）に保ちます。一端から給電する場合の実効的な単区間の長さ上限：</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">負荷</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">ケーブル</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">12V 最大長</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">24V 最大長</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">24 W（2 A / 1 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">1.5 mm²（16 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">約 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">約 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">48 W（4 A / 2 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">2.5 mm²（14 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">約 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">約 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">96 W（8 A / 4 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">4 mm²（12 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">約 7 m</td><td style="padding:10px 14px;border:1px solid var(--b)">約 14 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">192 W（16 A / 8 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">6 mm²（10 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">約 5 m</td><td style="padding:10px 14px;border:1px solid var(--b)">約 10 m</td></tr>
</tbody>
</table>

<p>これより長い場合？ストリップに両端から給電するか、同じドライバーでの並列区間に分割します。これらの工夫は 12V でも有効ですが、24V はほとんどの部屋でこの問題をそもそも解消します。</p>

<h2>12V が依然として正解の場合</h2>

<ul>
<li><strong>5 m 未満の短距離</strong>——キャビネット下、展示ケース、棚下照明、小さな看板。</li>
<li><strong>キャンピングカー、船舶、ソーラーシステム</strong>——システム全体が 12V バッテリーで動く。</li>
<li><strong>取替工事</strong>——既存のストリップとコントローラーが 12V；電圧変更は全再配線を意味する。</li>
<li><strong>極小負荷</strong>——単一展示用 15W アダプターは 12V の方が簡単で安い。</li>
</ul>

<p>当社の <a href="/products/adapters/">LED アダプター 5-200W</a> は単一の汎用 100-240V 入力で 12V/24V/36V/48V をカバーし、1 モデルでどの市場にも出荷できます。</p>

<h2>24V が勝つ場合</h2>

<ul>
<li><strong>5 m を超える距離</strong>、または両端から給電できない配線。</li>
<li><strong>商業用天井とリニア配線</strong>——1 台の 24V ドライバーで連続ラインを給電でき、12V なら 3 台必要。</li>
<li><strong>約 100W 以上</strong>——12V では電流が大きくなり、ケーブルコストとコネクタ発熱が問題に。</li>
<li><strong>建築案件</strong>——末端の可視的な輝度低下が許容できない。</li>
</ul>

<h2>私たちが絶えず見る 2 つの間違い</h2>

<ol>
<li><strong>1 つのドライバーで電圧を混用。</strong> 24V 電源の上の 12V ストリップは即座に焼損；通電前にストリップラベルを確認。</li>
<li><strong>ドライバーではなく配線でケーブルを選定。</strong> 問題はドライバー定格ではなく距離；上の表を使い、ケーブルが埋設または商用電源と束ねられている場合は太さを 1 段上げる。</li>
</ol>

<h2>定電圧と定電流</h2>

<p>12V と 24V のストリップはどちらも定電圧です：ドライバーが電圧を保持し、ストリップの抵抗が電流を決めます。高電力器具（ダウンライト、投光器）は通常定電流で、mA で指定されます。器具が 350 mA または 700 mA と表示されている場合は定電流ドライバーが必要で、12V/24V の問題は当てはまりません。器具の仕様をお知らせいただければ、当社が適合させます。</p>

<h2>クイック決定</h2>

<p><strong>距離 5 m 未満、バッテリーシステム、または同仕様の取替 &rarr; 12V。</strong><br>
<strong>距離 5 m 超、商業天井、または負荷 100W 超 &rarr; 24V。</strong></p>

<p>すべての CHUGAO ドライバーは CE と RoHS 認証を取得し、48 時間の全負荷エージングを経て、3 年保証付きです。最小ロット 50 台、ご仕様に応じた 12V/24V/36V/48V の OEM/ODM 生産也对応。</p>

<div class="cta-box">
<h3>配線長に合う電圧を決めたいですか？</h3>
<p>負荷、ケーブル配線長、ストリップの種類をお知らせください。12V か 24V か、および全てのメートルを満輝度に保つモデルを確認します。</p>
<a href="/#inquiry" class="btn">電圧アドバイスを得る</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">テープライト、モジュール、サイン用のコンパクトな 12V/24V ユニット。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内用 LED ドライバー 50-400W</span><span class="pc-desc">アクティブ PFC 付き定電圧、吊り下げ灯やパネル灯用。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">完全ポッティング、塩水噴霧試験済み、潮湿・沿岸向け。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">通気口付き金属筐体、サイン・半屋外設置向け。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで選ぶ正しい LED 電源</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP67 か IP65 か：どちらの防水 LED ドライバーが必要？</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技術ガイド</span><span class="rel-title">LED 電源の容量決め：ワット数・余裕・突入電流</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の違い</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビ"><a class="pn-prev" href="/blog-6/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">IP67 か IP65 か：どちらの防水 LED ドライバーが必要？</span></a><a class="pn-next" href="/blog-8/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">LED 電源の容量決め：ワット数・余裕・突入電流</span></a></nav>
</main>"""

BLOG_BODY['ko']['blog-7'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>12V 또는 24V: LED 전원 어떻게 선택할까</h1>
<div class="meta">구매 가이드 · 2026년 7월 · 약 8분</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-adapter.avif"><source type="image/webp" srcset="/images/product-adapter.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-adapter.jpg" alt="12V와 24V LED 전원 나란히" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>12V와 24V 모두 LED 스트립을 구동합니다. 차이는 케이블 발열로 나타나며, 이것이 스트립 끝이 어두워지기 전에 끌 수 있는 거리를 결정합니다. 그 수학과 그로부터 나온 간단한 법칙은 다음과 같습니다.</p>

<h2>전압이 실제로 바꾸는 것</h2>

<p>같은 와트에서는 24V 시스템의 전류가 12V 시스템의 절반입니다:</p>

<div class="highlight">
<strong>전력 = 전압 × 전류.</strong> 96W 부하는 12V에서 8A를 끌고, 24V에서는 단 4A입니다. 케이블 전압 강하는 전류에 비례하므로 전류를 반으로 줄이면 손실은 약 4분의 1로 줄고, 같은 휘도 손실로 케이블 길이를 약 2배로 늘릴 수 있습니다.
</div>

<h2>얼마나 끌 수 있나</h2>

<p>정전압 LED 스트립 기준: 전압 강하를 <strong>5%</strong> 미만(12V에서 0.6V, 24V에서 1.2V)으로 유지합니다. 한쪽 끝에서 급전할 때 실효 단일 구간 길이 상한:</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">부하</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">케이블</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">12V 최대 길이</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">24V 최대 길이</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">24 W（2 A / 1 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">1.5 mm²（16 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">약 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">약 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">48 W（4 A / 2 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">2.5 mm²（14 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">약 8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">약 16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">96 W（8 A / 4 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">4 mm²（12 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">약 7 m</td><td style="padding:10px 14px;border:1px solid var(--b)">약 14 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">192 W（16 A / 8 A）</td><td style="padding:10px 14px;border:1px solid var(--b)">6 mm²（10 AWG）</td><td style="padding:10px 14px;border:1px solid var(--b)">약 5 m</td><td style="padding:10px 14px;border:1px solid var(--b)">약 10 m</td></tr>
</tbody>
</table>

<p>이보다 길다면? 스트립에 양끝에서 급전하거나 같은 드라이버의 병렬 구간으로 나눕니다. 이 방법은 12V에서도 통하지만, 24V는 대부분의 방에서 이 문제를 애초에 없앱니다.</p>

<h2>12V가 여전히 정답인 경우</h2>

<ul>
<li><strong>5 m 미만 단거리</strong>——캐비닛 하단, 진열장, 선반 조명, 작은 간판.</li>
<li><strong>카라반, 선박, 태양광 시스템</strong>——시스템 전체가 12V 배터리로 동작.</li>
<li><strong>교체 공사</strong>——기존 스트립과 컨트롤러가 12V; 전압 변경은 전선 재시공 의미.</li>
<li><strong>극소 부하</strong>——단일 진열용 15W 어댑터는 12V가 더 간단하고 저렴.</li>
</ul>

<p>당사의 <a href="/products/adapters/">LED 어댑터 5-200W</a>는 단일 범용 100-240V 입력으로 12V/24V/36V/48V를 커버하여 하나의 모델로 어느 시장에도 출하됩니다.</p>

<h2>24V가 이기는 경우</h2>

<ul>
<li><strong>5 m 초과 거리</strong>, 또는 양끝 급전 불가 배선.</li>
<li><strong>상업용 천장과 리니어 배선</strong>——24V 드라이버 1대로 연속 라인 급전 가능, 12V는 3대 필요.</li>
<li><strong>약 100W 이상</strong>——12V에서는 전류가 커져 케이블 비용과 커넥터 발열이 문제.</li>
<li><strong>건축 프로젝트</strong>——말단 가시적 휘도 저하가 허용 안 됨.</li>
</ul>

<h2>늘 보는 두 가지 실수</h2>

<ol>
<li><strong>하나의 드라이버에 전압 혼용.</strong> 24V 전원 위 12V 스트립은 즉시 소손; 통전 전 스트립 라벨 확인.</li>
<li><strong>드라이버가 아닌 배선 기준으로 케이블 선정.</strong> 문제는 드라이버 정격이 아니라 거리; 위 표 사용, 케이블 매설 또는 상용전원과 묶일 때 굵기 1단계 상향.</li>
</ol>

<h2>정전압과 정전류</h2>

<p>12V와 24V 스트립은 모두 정전압입니다: 드라이버가 전압을 유지하고 스트립 저항이 전류를 결정합니다. 고출력 기기(다운라이트, 투광기)는 보통 정전류로 mA 지정됩니다. 기기가 350 mA 또는 700 mA로 표기되면 정전류 드라이버가 필요하며 12V/24V 문제는 해당하지 않습니다. 기기 사양을 알려주시면 당사가 맞춰드립니다.</p>

<h2>빠른 결정</h2>

<p><strong>거리 5 m 미만, 배터리 시스템, 또는 동일 사양 교체 &rarr; 12V.</strong><br>
<strong>거리 5 m 초과, 상업용 천장, 또는 부하 100W 초과 &rarr; 24V.</strong></p>

<p>모든 CHUGAO 드라이버는 CE와 RoHS 인증을 받고 48시간 만부하 에이징을 거치며 3년 보증입니다. 최소 주문 50대, 사양에 따른 12V/24V/36V/48V OEM/ODM 생산也对응.</p>

<div class="cta-box">
<h3>배선 길이에 맞는 전압을 정할까요?</h3>
<p>부하, 케이블 배선 길이, 스트립 종류를 알려주세요. 12V인지 24V인지, 그리고 모든 미터를 만휘도로 유지하는 모델을 확인합니다.</p>
<a href="/#inquiry" class="btn">전압 조언 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 간판용 컴팩트 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내용 LED 구동장치 50-400W</span><span class="pc-desc">액티브 PFC 정전압, 펜던트·패널등용.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 구동장치 10-400W</span><span class="pc-desc">완전 포팅, 염수 분무 시험, 습윤·해안용.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 구동장치 100-600W</span><span class="pc-desc">통풍구 있는 금속 하우징, 간판·반옥외용.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">다른 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 맞는 LED 전원 선택하기</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP67 vs IP65: 어떤 LED 구동장치가 필요한가</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">기술 가이드</span><span class="rel-title">LED 전원 용량 정하기: 와트·여유·돌입전류</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 비교</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-6/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">IP67 vs IP65: 어떤 LED 구동장치가 필요한가</span></a><a class="pn-next" href="/blog-8/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">LED 전원 용량 정하기: 와트·여유·돌입전류</span></a></nav>
</main>"""

BLOG_BODY['it']['blog-7'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; Torna alle Note dal Campo</a>

<h1>12V o 24V: come scegliere l'alimentatore LED</h1>
<div class="meta">Guida all'acquisto · Luglio 2026 · 8 min di lettura</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-adapter.avif"><source type="image/webp" srcset="/images/product-adapter.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-adapter.jpg" alt="Alimentatori LED 12V e 24V affiancati" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>Sia 12V che 24V alimentano strisce LED. La differenza emerge come calore nel cavo — e decide quanto puoi tirare prima che l'estremità della striscia si affievolisca. Ecco la matematica e la regola semplice che ne deriva.</p>

<h2>Cosa cambia davvero la tensione</h2>

<p>Alla stessa potenza, un sistema 24V assorbe metà della corrente di uno 12V:</p>

<div class="highlight">
<strong>Potenza = Tensione × Corrente.</strong> Un carico da 96W assorbe 8A a 12V, ma solo 4A a 24V. La caduta di tensione lungo un cavo è proporzionale alla corrente, quindi dimezzare la corrente riduce le perdite di circa un quarto — e permette di tirare il cavo circa il doppio per la stessa perdita di luminosità.
</div>

<h2>Quanto puoi tirare</h2>

<p>Regola pratica per strisce LED a tensione costante: mantieni la caduta di tensione sotto il 5% (0,6V a 12V, 1,2V a 24V). Limiti reali di tratta singola, alimentata da un capo:</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Carico</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Cavo</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Lunghezza max @12V</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Lunghezza max @24V</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">24 W (2 A / 1 A)</td><td style="padding:10px 14px;border:1px solid var(--b)">1,5 mm² (16 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">48 W (4 A / 2 A)</td><td style="padding:10px 14px;border:1px solid var(--b)">2,5 mm² (14 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~8 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~16 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">96 W (8 A / 4 A)</td><td style="padding:10px 14px;border:1px solid var(--b)">4 mm² (12 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~7 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~14 m</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">192 W (16 A / 8 A)</td><td style="padding:10px 14px;border:1px solid var(--b)">6 mm² (10 AWG)</td><td style="padding:10px 14px;border:1px solid var(--b)">~5 m</td><td style="padding:10px 14px;border:1px solid var(--b)">~10 m</td></tr>
</tbody>
</table>

<p>Più lungo di così? Alimenta la striscia da entrambi i capi, o dividila in tratte parallele dallo stesso driver. Entrambi i trucchi funzionano a 12V, ma 24V elimina il problema nella maggior parte delle stanze.</p>

<h2>Quando 12V è ancora la risposta</h2>

<ul>
<li><strong>Tratte corte sotto 5 m</strong> — sotto armadi, vetrine, illuminazione mensole, piccole insegne.</li>
<li><strong>Camper, barche e sistemi solari</strong> — tutto il sistema gira già a batteria 12V.</li>
<li><strong>Lavori di sostituzione</strong> — le strisce e i controlli esistenti sono 12V; cambiare tensione significa ricablaggio totale.</li>
<li><strong>Carichi molto piccoli</strong> — un adattatore da 15W per una singola vetrina è più semplice ed economico a 12V.</li>
</ul>

<p>I nostri <a href="/products/adapters/">adattatori LED 5-200W</a> coprono 12V/24V/36V/48V con un unico ingresso universale 100-240V, così un solo SKU parte per qualsiasi mercato.</p>

<h2>Quando vince 24V</h2>

<ul>
<li><strong>Tratte oltre 5 m</strong>, o qualsiasi tratta non alimentabile da entrambi i capi.</li>
<li><strong>Soffitti commerciali e tratte lineari</strong> — un driver 24V alimenta una linea continua che a 12V richiederebbe tre alimentazioni.</li>
<li><strong>Oltre ~100W</strong> — la corrente a 12V diventa abbastanza alta che costo cavo e riscaldamento connettori contano.</li>
<li><strong>Lavori architettonici</strong> dove l'attenuazione visibile all'estremità è inaccettabile.</li>
</ul>

<h2>Due errori che vediamo di continuo</h2>

<ol>
<li><strong>Mescolare tensioni su un driver.</strong> Una striscia 12V su alimentatore 24V muore all'istante. Controlla l'etichetta prima di energizzare.</li>
<li><strong>Dimensionare il cavo per il driver, non per la tratta.</strong> Il problema non è la corrente del driver — è la distanza. Usa la tabella, poi sali di una misura se il cavo è interrato o affiancato alla rete.</li>
</ol>

<h2>Tensione costante vs corrente costante</h2>

<p>Sia le strisce 12V che 24V sono a tensione costante: il driver mantiene la tensione, le resistenze della striscia fissano la corrente. Le armature ad alta potenza (downlight, proiettori) sono solitamente a corrente costante — specificate in mA, non volt. Se la tua armature dice 350 mA o 700 mA, ti serve un driver a corrente costante e la questione 12V/24V non si applica. Dicci le specifiche e abbineremo il driver.</p>

<h2>Decisione rapida</h2>

<p><strong>Tratte sotto 5 m, sistemi a batteria, o sostituzione equivalente &rarr; 12V.</strong><br>
<strong>Tratte oltre 5 m, soffitti commerciali, o carichi oltre 100W &rarr; 24V.</strong></p>

<p>Ogni driver CHUGAO è certificato CE e RoHS, esegue 48 ore di burn-in a pieno carico e ha 3 anni di garanzia. Ordine minimo 50 pz, e produciamo versioni 12V/24V/36V/48V su specifica in OEM/ODM.</p>

<div class="cta-box">
<h3>Ti serve la tensione giusta per la tua lunghezza di tratta?</h3>
<p>Dicci il carico, la lunghezza del cavo e il tipo di striscia. Confermeremo 12V o 24V e il modello che mantiene ogni metro a piena luminosità.</p>
<a href="/#inquiry" class="btn">Ottieni una raccomandazione di tensione</a>
</div>

<section class="product-crosslink" aria-label="Prodotti correlati"><h2 class="related-h">Esplora i prodotti CHUGAO</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">Adattatori LED 5-200W</span><span class="pc-desc">Unità compatte 12V/24V per strisce, moduli e insegne.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">Driver LED da interno 50-400W</span><span class="pc-desc">Tensione costante con PFC attivo per soffitti e pannelli.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">Driver impermeabili IP67 10-400W</span><span class="pc-desc">Completamente sigillati, test nebbia salina, per umido e coste.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">Driver anti-pioggia IP65 100-600W</span><span class="pc-desc">Contenitore metallico ventilato per insegne e semi-esterno.</span></a></div></section>

<section class="related" aria-label="Articoli correlati">
  <h2 class="related-h">Altre Note dal Campo</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">Tecnologia LED</span><span class="rel-title">Scegliere l'alimentatore LED giusto in 3 passi</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">IP67 o IP65: quale driver LED impermeabile ti serve?</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">Come dimensionare un alimentatore LED: watt, margine e inrush</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">IP20 vs IP65 vs IP67 vs IP68</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="Navigazione articoli"><a class="pn-prev" href="/blog-6/" rel="prev"><span class="pn-lab">Articolo precedente</span><span class="pn-t">IP67 o IP65: quale driver LED impermeabile ti serve?</span></a><a class="pn-next" href="/blog-8/" rel="next"><span class="pn-lab">Articolo successivo</span><span class="pn-t">Come dimensionare un alimentatore LED: watt, margine e inrush</span></a></nav>
</main>"""

# ============================ blog-8 (How to size) ============================
BLOG_BODY['zh']['blog-8'] = """<main class="article">
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

BLOG_BODY['ja']['blog-8'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>LED 電源の容量決め：ワット数・余裕・突入電流</h1>
<div class="meta">技術ガイド · 2026年8月 · 約7分</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="商業照明負荷に選定された屋内 LED ドライバー" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 電源を小さく選ぶと発熱し、早期に暗くなり、1 年で故障します。大きすぎると使わない容量にお金を払います。その間にあるのは、ほとんどの買い手が飛ばす 20 分の計算です。</p>

<h2>ステップ1：実負荷を合算</h2>

<p>ドライバーが給電する全器具のワット数を足します。器具の入力ワット数を使い、「相当」ではなく—「50W 相当」のダウンライトは 9W しか引かないことも。</p>

<ul>
<li>LED ストリップ：1 m あたりのワット数 × メートル数（ラベルを確認：4.8W/m、9.6W/m、14.4W/m が一般的）。</li>
<li>パネルとトロッファ：器具の銘板。</li>
<li>看板モジュール：モジュール数 × モジュールあたりのワット数。</li>
</ul>

<p>例：14.4W/m ストリップ 12 m = <strong>173W</strong>。</p>

<h2>ステップ2：20% の余裕を追加</h2>

<p>1.2 を掛けます。この 20% は無駄ではなく、駆動電源の寿命を縮める 3 つの事柄をカバーします：</p>

<ol>
<li><strong>熱。</strong> 40°C 天井で定格運転のドライバーは、同じものの 80% 負荷時よりずっと熱い。定格を 10°C 超えるごとにコンデンサ寿命は約半減。</li>
<li><strong>商用電源の変動。</strong> 電圧低下とサージは余裕があれば楽に吸収。</li>
<li><strong>将来の追加。</strong> 来年誰かが別のストリップを足す。</li>
</ol>

<p>173W × 1.2 = <strong>208W</strong> &rarr; 数値の上の標準定格である 240W または 250W を選択。</p>

<div class="highlight">
<strong>経験則：</strong> ドライバーを定格の 80% 以下で運転。60W から 100W への増額は数ドル。故障したドライバーを交換に技術者を派遣するコストはその百倍以上。
</div>

<h2>ステップ3：ブレーカーを選ぶ前に突入電流を確認</h2>

<p>スイッチング電源は通電時にごく短い大きなサージを引きます—通常 30-60 A、数ミリ秒、高電力ユニットではそれ以上の場合も。10 台のドライバーを同じスイッチや接触器に繋ぐとサージが加算され、初日でブレーカーが落ちたりリレーが溶着したりする可能性があります。</p>

<ul>
<li><strong>複数の小ドライバー？</strong> 時間遅れリレーで起動をずらすか、加算サージに合わせた定格の接触器を使用。</li>
<li><strong>単体の大ドライバー？</strong> B 型ではなく C 型または D 型ブレーカー。</li>
<li><strong>突入値を要求する</strong>—仕様書に載っている。提示できない供給元は推測している。</li>
</ul>

<h2>ステップ4：温度で降格</h2>

<p>ほとんどのドライバーは環境 40°C 以下で全出力です。それ以上は降格—通常 1°C あたり出力の 2-3%、但し機種の曲線を確認。実例：</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">設置</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">代表的環境温度</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">対策</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">オープン室内天井</td><td style="padding:10px 14px;border:1px solid var(--b)">25-35°C</td><td style="padding:10px 14px;border:1px solid var(--b)">標準の 20% 余裕で十分</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">密閉天井空隙</td><td style="padding:10px 14px;border:1px solid var(--b)">45-55°C</td><td style="padding:10px 14px;border:1px solid var(--b)">30-40% 余裕を追加、またはドライバーを通気のある場所へ</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">屋外直射日光</td><td style="padding:10px 14px;border:1px solid var(--b)">50-65°C</td><td style="padding:10px 14px;border:1px solid var(--b)">機器を日陰に、または 1 段大きくし灌封 <a href="/products/ip67/">IP67</a> を使用</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">密閉看板箱内</td><td style="padding:10px 14px;border:1px solid var(--b)">45-60°C</td><td style="padding:10px 14px;border:1px solid var(--b)">箱に通風を、または通気口付き <a href="/products/ip65/">IP65</a> 筐体を使用</td></tr>
</tbody>
</table>

<h2>算例：店先看板、8 モジュール</h2>

<p>看板モジュール：8 × 1.5W = 12W。ストリップ装飾：4 m × 9.6W/m = 38W。合計 = 50W。余裕 ×1.2 = 60W。夏に 50°C に達する密閉箱に設置 &rarr; さらに 30% 追加 &rarr; 78W。100W ユニットを選択。約半負荷で動作し、低温を保ち、看板自体より長持ちします。</p>

<h2>5 つの選定ミス</h2>

<ol>
<li><strong>「相当ワット数」を使う</strong>（実消費ではなく）。</li>
<li><strong>100% 負荷で選定</strong>（余裕なし）。</li>
<li><strong>密閉筐体内の環境温度を無視</strong>。</li>
<li><strong>10 台のドライバーを突入確認なしに 1 スイッチへ</strong>。</li>
<li><strong>将来を忘れる</strong>—余分なストリップ、2 つめの看板。</li>
</ol>

<h2>お客様に必要なもの</h2>

<p>負荷（ワット数）、出力電圧（12V または 24V）、設置場所とおおよその環境温度、必要台数をお送りください。適切な定格を推奨します—より小さく安いモデルで十分な場合も正直にお伝えします。</p>

<div class="cta-box">
<h3>選定を確認しましょうか？</h3>
<p>負荷、出力電圧、設置場所、台数をお送りください。適切な定格を確認します—またはより小さなモデルで十分な場合もお伝えします。</p>
<a href="/#inquiry" class="btn">選定確認を取得</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">テープライト、モジュール、サイン用のコンパクトな 12V/24V ユニット。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内用 LED ドライバー 50-400W</span><span class="pc-desc">アクティブ PFC 付き定電圧、吊り下げ灯やパネル灯用。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">完全ポッティング、塩水噴霧試験済み、潮湿・沿岸向け。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">通気口付き金属筐体、サイン・半屋外設置向け。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで選ぶ正しい LED 電源</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">購入ガイド</span><span class="rel-title">12V か 24V か：LED 電源の選び方</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP67 か IP65 か：どちらの防水 LED ドライバーが必要？</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深読み</span><span class="rel-title">LED ドライバーの寿命：MTBF・L70・実際のもち</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビ"><a class="pn-prev" href="/blog-7/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">12V か 24V か：LED 電源の選び方</span></a><a class="pn-next" href="/blog/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">現場ノート</span></a></nav>
</main>"""

BLOG_BODY['ko']['blog-8'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>LED 전원 용량 정하기: 와트·여유·돌입전류</h1>
<div class="meta">기술 가이드 · 2026년 8월 · 약 7분</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="상업 조명 부하에 선정된 실내 LED 구동장치" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 전원을 작게 고르면 발열하고 일찍 어두워지며 1년 안에 고장납니다. 너무 크면 쓰지 않는 용량에 돈을 씁니다. 그 사이에는 대부분의 구매자가 건너뛰는 20분 계산이 있습니다.</p>

<h2>1단계: 실제 부하 합산</h2>

<p>드라이버가 급전할 모든 기구의 와트수를 더합니다. 기구의 입력 와트수를 쓰되 "상당" 표기가 아니라—"50W 상당" 다운라이트는 9W만 쓸 수도 있습니다.</p>

<ul>
<li>LED 스트립: 미터당 와트 × 미터(라벨 확인: 4.8W/m, 9.6W/m, 14.4W/m 흔함).</li>
<li>패널과 트로퍼: 기구 명판.</li>
<li>간판 모듈: 모듈 수 × 모듈당 와트.</li>
</ul>

<p>예: 14.4W/m 스트립 12 m = <strong>173W</strong>.</p>

<h2>2단계: 20% 여유 추가</h2>

<p>1.2를 곱합니다. 이 20%는 여유가 아니라 구동장치 수명을 줄이는 세 가지를 커버합니다:</p>

<ol>
<li><strong>열.</strong> 40°C 천장에서 정격 운전 드라이버는 동일품 80% 부하보다 훨씬 뜨거움. 정격을 10°C 넘을 때마다 콘덴서 수명은 약 반감.</li>
<li><strong>상용전원 변동.</strong> 전압 강하와 서지는 여유가 있으면 편히 흡수.</li>
<li><strong>향후 증설.</strong> 내년에 누군가 스트립을 더 붙임.</li>
</ol>

<p>173W × 1.2 = <strong>208W</strong> &rarr; 수치 위 표준 정격인 240W 또는 250W 선택.</p>

<div class="highlight">
<strong>경험칙:</strong> 드라이버를 정격의 80% 이하로 운전. 60W에서 100W로 올리는 것은 몇 달러. 고장 난 드라이버 교체하러 기술자를 보내는 비용은 그 백배 이상.
</div>

<h2>3단계: 차단기 선택 전 돌입전류 확인</h2>

<p>스위칭 전원은 통전 시 매우 짧은 큰 서지를 끕니다—보통 30-60 A, 수 밀리초, 고출력 유닛은 그 이상인 경우도. 드라이버 10대를 같은 스위치나 접촉기에 연결하면 서지가 누적되어 첫날 차단기가 떨어지거나 릴레이가 용착될 수 있습니다.</p>

<ul>
<li><strong>여러 작은 드라이버?</strong> 시간 지연 릴레이로 기동을 어긋시키거나 누적 서지 정격 접촉기 사용.</li>
<li><strong>단일 대형 드라이버?</strong> B형이 아닌 C형 또는 D형 차단기.</li>
<li><strong>돌입값 요구</strong>—사양서에 있음. 제시 못 하는 공급자는 추측하는 것.</li>
</ul>

<h2>4단계: 온도로 감율</h2>

<p>대부분 드라이버는 환경 40°C 이하에서 전출력입니다. 그 이상은 감율—보통 1°C당 출력 2-3%, 단 기종 곡선 확인. 실례:</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">설치</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">대표 환경온도</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">대응</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">개방형 실내 천장</td><td style="padding:10px 14px;border:1px solid var(--b)">25-35°C</td><td style="padding:10px 14px;border:1px solid var(--b)">표준 20% 여유로 충분</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">밀폐 천장 공간</td><td style="padding:10px 14px;border:1px solid var(--b)">45-55°C</td><td style="padding:10px 14px;border:1px solid var(--b)">30-40% 여유 추가 또는 드라이버를 통풍처로</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">옥외 직사광</td><td style="padding:10px 14px;border:1px solid var(--b)">50-65°C</td><td style="padding:10px 14px;border:1px solid var(--b)">기기 그늘지게 하거나 1단 크게 하여 포팅 <a href="/products/ip67/">IP67</a> 사용</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">밀폐 간판함 내</td><td style="padding:10px 14px;border:1px solid var(--b)">45-60°C</td><td style="padding:10px 14px;border:1px solid var(--b)">함에 통풍을 주거나 통풍구 있는 <a href="/products/ip65/">IP65</a> 하우징 사용</td></tr>
</tbody>
</table>

<h2>산예: 상점 간판, 8 모듈</h2>

<p>간판 모듈: 8 × 1.5W = 12W. 스트립 장식: 4 m × 9.6W/m = 38W. 합계 = 50W. 여유 ×1.2 = 60W. 여름 50°C 도달 밀폐함 설치 &rarr; 30% 추가 &rarr; 78W. 100W 유닛 선택. 약 반부하로 동작해 저온 유지, 간판 그 자체보다 오래 감.</p>

<h2>5가지 선정 실수</h2>

<ol>
<li><strong>"상당 와트수" 사용</strong>(실소비 아님).</li>
<li><strong>100% 부하로 선정</strong>(여유 없음).</li>
<li><strong>밀폐 하우징 내 환경온도 무시</strong>.</li>
<li><strong>돌입 확인 없이 드라이버 10대를 1스위치에</strong>.</li>
<li><strong>미래 잊기</strong>(남는 스트립, 두 번째 간판).</li>
</ol>

<h2>필요한 것</h2>

<p>부하(와트), 출력 전압(12V 또는 24V), 설치 위치와 대략 환경온도, 필요 대수를 보내주세요. 적절한 정격을 추천합니다—더 작고 저렴한 모델로 충분한 경우도 정직히 알립니다.</p>

<div class="cta-box">
<h3>선정 확인해 드릴까요?</h3>
<p>부하, 출력 전압, 설치 위치, 대수를 보내주세요. 적절한 정격을 확인합니다—또는 더 작은 모델로 충분한 경우도 알립니다.</p>
<a href="/#inquiry" class="btn">선정 확인 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 간판용 컴팩트 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내용 LED 구동장치 50-400W</span><span class="pc-desc">액티브 PFC 정전압, 펜던트·패널등용.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 구동장치 10-400W</span><span class="pc-desc">완전 포팅, 염수 분무 시험, 습윤·해안용.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 구동장치 100-600W</span><span class="pc-desc">통풍구 있는 금속 하우징, 간판·반옥외용.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">다른 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 맞는 LED 전원 선택하기</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">구매 가이드</span><span class="rel-title">12V 또는 24V: LED 전원 어떻게 선택할까</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP67 vs IP65: 어떤 LED 구동장치가 필요한가</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 구동장치 수명: MTBF, L70 그리고 실제 수명</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-7/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">12V 또는 24V: LED 전원 어떻게 선택할까</span></a><a class="pn-next" href="/blog/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">현장 노트</span></a></nav>
</main>"""

BLOG_BODY['it']['blog-8'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; Torna alle Note dal Campo</a>

<h1>Come dimensionare un alimentatore LED: watt, margine e inrush</h1>
<div class="meta">Guida tecnica · Agosto 2026 · 7 min di lettura</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="Driver LED da interno dimensionato per un carico di illuminazione commerciale" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>Un alimentatore LED sottodimensionato scalda, si attenua presto e muore in un anno. Uno sovradimensionato paghi per capacità che non usi. In mezzo c'è un calcolo di 20 minuti che la maggior parte dei compratori salta.</p>

<h2>Passo 1: totalizza il carico reale</h2>

<p>Somma i watt di ogni apparato che il driver alimenterà. Usa i watt di ingresso dell'apparato, non la "equivalenza" — un downlight "equivalente 50W" può assorbire 9W.</p>

<ul>
<li>Striscia LED: watt per metro × metri (controlla l'etichetta: comuni 4,8W/m, 9,6W/m, 14,4W/m).</li>
<li>Pannelli e troffer: la targa dell'apparato.</li>
<li>Moduli insegna: moduli × watt per modulo.</li>
</ul>

<p>Esempio: striscia 14,4W/m per 12 m = <strong>173W</strong>.</p>

<h2>Passo 2: aggiungi il margine del 20%</h2>

<p>Moltiplica per 1,2. Quel 20% non è padding — copre tre cose che accorciano la vita del driver:</p>

<ol>
<li><strong>Calore.</strong> Un driver al 100% di carico in un soffitto a 40°C gira molto più caldo dello stesso a 80%; ogni 10°C oltre la classe dimezza circa la vita dei condensatori.</li>
<li><strong>Variazioni rete.</strong> Cadute e picchi si assorbono meglio con margine.</li>
<li><strong>Aggiunte future.</strong> La striscia che qualcuno aggiunge l'anno prossimo.</li>
</ol>

<p>173W × 1,2 = <strong>208W</strong> &rarr; scegli un modello da 240W o 250W, la classe standard sopra il tuo numero.</p>

<div class="highlight">
<strong>Regola pratica:</strong> fai girare il driver all'80% o meno della sua classe. Passare da 60W a 100W costa pochi dollari; mandare un tecnico a sostituire un driver guasto costa cento volte tanto.
</div>

<h2>Passo 3: controlla l'inrush prima di scegliere il magnetotermico</h2>

<p>Gli alimentatori switching assorbono un picco brevissimo ma intenso all'inserzione — tipicamente 30-60 A per pochi millisecondi, a volte più su unità ad alta potenza. Se metti dieci driver su un solo interruttore o contattore, i picchi si sommano e possono far scattare il magnetotermico o saldare il relè al primo giorno.</p>

<ul>
<li><strong>Molti driver piccoli?</strong> Scaglionali con un relè a ritardo, o usa un contattore rateizzato per l'inrush sommato.</li>
<li><strong>Un solo driver grande?</strong> Usa un magnetotermico tipo C o D, non tipo B.</li>
<li><strong>Chiedi il valore di inrush</strong> — è sulla scheda; un fornitore che non lo dà sta indovinando.</li>
</ul>

<h2>Passo 4: derate per temperatura</h2>

<p>La maggior parte dei driver è a pieno carico a 40°C ambiente o meno. Oltre, derate — tipicamente 2-3% di uscita per °C, ma controlla la curva del modello. Casi pratici:</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Installazione</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Temperatura ambiente tipica</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Cosa fare</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">Soffitto interno aperto</td><td style="padding:10px 14px;border:1px solid var(--b)">25-35°C</td><td style="padding:10px 14px;border:1px solid var(--b)">basta il margine standard 20%</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">Vano soffitto sigillato</td><td style="padding:10px 14px;border:1px solid var(--b)">45-55°C</td><td style="padding:10px 14px;border:1px solid var(--b)">aggiungi 30-40% di margine, o sposta il driver all'aperto</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">Esterno in pieno sole</td><td style="padding:10px 14px;border:1px solid var(--b)">50-65°C</td><td style="padding:10px 14px;border:1px solid var(--b)">ombreggia l'unità, o sali una taglia e usa un IP67 sigillato</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">Dentro scatola insegna sigillata</td><td style="padding:10px 14px;border:1px solid var(--b)">45-60°C</td><td style="padding:10px 14px;border:1px solid var(--b)">ventola la scatola, o usa un contenitore IP65 ventilato</td></tr>
</tbody>
</table>

<h2>Esempio: insegna vetrina, 8 moduli</h2>

<p>Moduli insegna: 8 × 1,5W = 12W. Accenti striscia: 4 m × 9,6W/m = 38W. Totale = 50W. Margine ×1,2 = 60W. In scatola sigillata che d'estate raggiunge 50°C &rarr; aggiungi un altro 30% &rarr; 78W. Scegli un'unità da 100W. Girerà a circa metà carico, resterà fresca e supererà la durata dell'insegna.</p>

<h2>Cinque errori di dimensionamento</h2>

<ol>
<li><strong>Usare i "watt equivalenti"</strong> invece del consumo reale.</li>
<li><strong>Dimensionare al 100% di carico senza margine</strong>.</li>
<li><strong>Ignorare la temperatura ambiente in un contenitore sigillato</strong>.</li>
<li><strong>Mettere dieci driver su un interruttore senza controllare l'inrush</strong>.</li>
<li><strong>Dimenticare il futuro</strong> — la striscia in più, la seconda insegna.</li>
</ol>

<h2>Cosa ci serve da te</h2>

<p>Inviaci il carico in watt, la tensione di uscita (12V o 24V), il luogo di installazione e la temperatura ambiente approssimativa, e quante unità ti servono. Ti raccomanderemo la classe giusta — e ti diremo quando un modello più piccolo e economico è davvero sufficiente.</p>

<div class="cta-box">
<h3>Vuoi che controlliamo il tuo dimensionamento?</h3>
<p>Inviaci carico, tensione di uscita, luogo di installazione e quantità. Confermeremo la classe giusta — o ti diremo che un modello più piccolo basta.</p>
<a href="/#inquiry" class="btn">Ottieni un controllo di dimensionamento</a>
</div>

<section class="product-crosslink" aria-label="Prodotti correlati"><h2 class="related-h">Esplora i prodotti CHUGAO</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">Adattatori LED 5-200W</span><span class="pc-desc">Unità compatte 12V/24V per strisce, moduli e insegne.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">Driver LED da interno 50-400W</span><span class="pc-desc">Tensione costante con PFC attivo per soffitti e pannelli.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">Driver impermeabili IP67 10-400W</span><span class="pc-desc">Completamente sigillati, test nebbia salina, per umido e coste.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">Driver anti-pioggia IP65 100-600W</span><span class="pc-desc">Contenitore metallico ventilato per insegne e semi-esterno.</span></a></div></section>

<section class="related" aria-label="Articoli correlati">
  <h2 class="related-h">Altre Note dal Campo</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">Tecnologia LED</span><span class="rel-title">Scegliere l'alimentatore LED giusto in 3 passi</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">Guida all'acquisto</span><span class="rel-title">12V o 24V: come scegliere l'alimentatore LED</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">IP67 o IP65: quale driver LED impermeabile ti serve?</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">Approfondimento</span><span class="rel-title">Durata dei driver LED: MTBF, L70 e quanto durano davvero</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="Navigazione articoli"><a class="pn-prev" href="/blog-7/" rel="prev"><span class="pn-lab">Articolo precedente</span><span class="pn-t">12V o 24V: come scegliere l'alimentatore LED</span></a><a class="pn-next" href="/blog/" rel="next"><span class="pn-lab">Articolo successivo</span><span class="pn-t">Note dal Campo</span></a></nav>
</main>"""
