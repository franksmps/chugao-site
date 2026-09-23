# -*- coding: utf-8 -*-
"""Japanese body copy for blog-1..5 and blog-9..14.

Extends the 'ja' sub-dict declared in blog_body_zh.py (blog-6/7/8). Only NEW
keys -- never re-declare BLOG_BODY['ja'] = {}.
AI translation pending native review.
"""


BLOG_BODY['ja']['blog-1'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>3 ステップで正しい LED 電源を選ぶ</h1>
<div class="meta">LED 技術 &middot; 2026 年 3 月 &middot; 約 6 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-1-led-power-supply-md.avif 1200w, /images/blog-1-led-power-supply.avif 1024w">
<source type="image/webp" srcset="/images/blog-1-led-power-supply-md.webp 1200w, /images/blog-1-led-power-supply.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-1-led-power-supply.jpg" alt="LED 電源の選定ガイド" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>LED 電源の選定は難しそうに聞こえますが、突き詰めれば 3 点です——<strong>ワット数</strong>、<strong>IP 保護等級</strong>、<strong>入力電圧</strong>。この 3 点を正しく押さえれば、返品と現場故障の 90% を排除できます。</p>

<p>本ガイドは、発注前に確認すべき点を順に解説します。マーケティング部門ではなく、当社のエンジニアリングチームが執筆しています。</p>

<h2>ステップ 1：ワット数を合わせる</h2>

<p>最も多いミスは容量不足です。CHUGAO で使っている目安は次のとおりです。</p>

<div class="highlight">
<strong>負荷ワット数 &times; 1.25 = ドライバーの最低定格。</strong><br>
常に少なくとも 25% の余裕を確保してください。ドライバーを 100% の容量で運転すると寿命が縮み、温度も高くなります。
</div>

<h3>例</h3>
<p>LED テープが 80W を消費するなら、80W のドライバーを買ってはいけません。100W（またはそれ以上）を選んでください。余分な容量は出力を安定させ、発熱を抑え、寿命を約 3 年から 5 年以上へ延ばします。</p>

<h3>余裕が重要な理由</h3>
<ul>
<li><strong>温度：</strong>ドライバーは定格負荷以下でより低温で動作します。温度が 10&deg;C 下がるごとに、コンデンサの寿命はおよそ 2 倍になります。</li>
<li><strong>サージ耐性：</strong>LED テープは起動時に一時的なスパイクを引くことがあります。余裕があれば保護が作動せずに吸収できます。</li>
<li><strong>電圧安定性：</strong>軽負荷のドライバーは出力電圧をより厳密に保ち、明るさがより安定します。</li>
</ul>

<h2>ステップ 2：正しい IP 保護等級を選ぶ</h2>

<p>IP（保護等級）コードは、ドライバーが粉塵と水にどれだけ耐えるかを示します。多くのプロジェクトがここで失敗します——ドライバーで 2 ドル節約し、一度の雨で交換することになるのです。</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">IP 等級</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">粉塵</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">水</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">用途</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP20</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">保護なし</td><td style="padding:10px 14px;border:1px solid var(--b)">水保護なし</td><td style="padding:10px 14px;border:1px solid var(--b)">屋内の乾燥場所のみ</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">粉塵密閉</td><td style="padding:10px 14px;border:1px solid var(--b)">ウォータージェット（全方向）</td><td style="padding:10px 14px;border:1px solid var(--b)">屋外露出・洗浄エリア</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">粉塵密閉</td><td style="padding:10px 14px;border:1px solid var(--b)">1m までの浸水</td><td style="padding:10px 14px;border:1px solid var(--b)">一時的な水没・浸水リスク</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">粉塵密閉</td><td style="padding:10px 14px;border:1px solid var(--b)">連続浸水</td><td style="padding:10px 14px;border:1px solid var(--b)">水中器具・深い水没</td></tr>
</tbody>
</table>

<p>迷ったら、必要と思うより 1 段階上を選んでください。100W ドライバーでの IP20 と IP65 の価格差は、工場直販価格で通常 3 ドル未満です。</p>

<h2>ステップ 3：入力電圧の互換性を確認する</h2>

<p>これは見落としやすい一方、最も高い返品率を招きます。</p>

<ul>
<li><strong>北米・日本・中国台湾・中国大陸：</strong>110V AC / 60Hz</li>
<li><strong>欧州・中国大陸・アジアの大部分・アフリカ：</strong>220–240V AC / 50Hz</li>
<li><strong>ブラジル：</strong>127V/220V ハイブリッド（現地のコンセントを確認）</li>
<li><strong>産業／船舶：</strong>多くの場合 277V、380V、または 480V 三相</li>
</ul>

<p>入力範囲は製品ラインによって異なります。アダプターは 100–240V AC、屋内・IP65・IP67 モデルは 190–264V（IP67 は最大 340V）に対応します。お使いのモデルの正確な入力範囲は<a href="/#specs">仕様表</a>で確認し、仕向地の系統電圧と一致することを確かめてください。</p>

<h2>クイック確認チェックリスト</h2>

<ol>
<li>LED 総負荷ワット数を合計 &rarr; 1.25 を掛ける &rarr; 最も近い標準ドライバーサイズに切り上げる。</li>
<li>設置環境を確認 &rarr; 屋内（IP20）、屋外／防雨（IP65）、または水没リスク（IP67/IP68）。</li>
<li>仕向国の系統電圧を確認 &rarr; 110V 地域か 220V 地域か。</li>
<li>任意：調光が必要ですか？（0-10V、PWM、DALI、Triac——発注時に指定）</li>
<li>任意：UL 認証が必要ですか？（コスト増、モデルごとに 2〜3 週間のリードタイム）</li>
</ol>

<div class="cta-box">
<h3>どのモデルが合うかわからない？</h3>
<p>仕様をお送りください——ワット数、数量、仕向港、ターゲット市場。営業時間内は 1 時間以内に、データシートと見積もりを返信します。</p>
<a href="/#inquiry" class="btn">見積もりを依頼</a>
</div>


<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">看板やテープ照明向けの広入力・コンセント／デスクトップ型アダプター。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内 LED ドライバー 50-400W</span><span class="pc-desc">パネル・ダウンライト・商業器具向けの高効率ドライバー。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">屋外・景観プロジェクト向けの水没対応電源。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の選び方</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">業界動向</span><span class="rel-title">2026 年の LED 市場：私たちが見ているもの</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">規制</span><span class="rel-title">LED ドライバーの BIS 認証：インド輸入ガイド</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深掘り</span><span class="rel-title">LED ドライバーの寿命：MTBF、L70、実際の使用年数</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog/"><span class="pn-lab">すべての記事</span><span class="pn-t">現場ノート</span></a><a class="pn-next" href="/blog-2/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">IP20・IP65・IP67・IP68 の選び方</span></a></nav>
</main>"""


BLOG_BODY['ja']['blog-2'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>IP20・IP65・IP67・IP68 の比較</h1>
<div class="meta">技術ガイド &middot; 2026 年 2 月 &middot; 約 7 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-2-ip-rating-md.avif 1200w, /images/blog-2-ip-rating.avif 1024w">
<source type="image/webp" srcset="/images/blog-2-ip-rating-md.webp 1200w, /images/blog-2-ip-rating.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-2-ip-rating.jpg" alt="IP 等級の比較チャート" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>すべての LED 電源には IP 等級があります。2 桁で構成され、1 桁目が<strong>粉塵／固体粒子からの保護</strong>、2 桁目が<strong>水からの保護</strong>です。数値が大きいほど密封性が高くなります。</p>

<p>本ガイドでは、一般的な各 IP 等級が実世界で何を意味するのかを分解し、過剰な出費も仕様不足も避けられるようにします。</p>

<h2>2 桁システムの読み方</h2>

<table class="ip-table">
<thead><tr><th>桁</th><th>測定対象</th><th>スケール</th></tr></thead>
<tbody>
<tr><td><strong>1 桁目（0〜6）</strong></td><td>固体／粉塵</td><td>0 = 保護なし &rarr; 6 = 粉塵密閉</td></tr>
<tr><td><strong>2 桁目（0〜8）</strong></td><td>液体／水</td><td>0 = 保護なし &rarr; 8 = 連続浸水</td></tr>
</tbody>
</table>

<h2>1 桁目：粉塵保護</h2>

<ul>
<li><strong>IPx0：</strong>保護なし。商用 LED ドライバーでは使われません。</li>
<li><strong>IPx3 – IPx4：</strong>電線・ネジ・指の侵入を防ぎます。基本的な安全保護。</li>
<li><strong>IPx5：</strong>粉塵の侵入が限定的。微細な粉塵は入りますが動作に支障はありません。</li>
<li><strong>IPx6：</strong>粉塵密閉。粉塵の侵入ゼロ。屋外仕様ドライバーの標準です。</li>
</ul>

<p>実際には、有意な防水等級（2 桁目が 4 以上）を持つ当社の全ドライバーは、すでに粉塵は IPx6 を満たしています。この桁を個別に気にする必要はほとんどありません。</p>

<h2>2 桁目：水保護——ここで判断が分かれる</h2>

<h3>IP20 / IP21 — 屋内専用</h3>
<p>垂直方向からの水滴は無影響（IP20）。垂直から 15&deg; 以内の水滴も無影響（IP21）。</p>
<ul>
<li>用途：屋内シーリング器具、密閉型ルミナリエ、乾燥場所</li>
<li>避ける：窓・浴室・厨房・空調吹き出し口の近く</li>
<li>コスト：最下位クラス</li>
</ul>

<h3>IP44 — 防沫</h3>
<p>あらゆる方向からの水はねでも損傷しません。</p>
<ul>
<li>用途：洗面所のミラー灯、キャビネット下テープ、厨房の作業照明</li>
<li>直接の雨曝露や洗浄には不向き</li>
</ul>

<h3>IP54 — 粉塵＋防沫</h3>
<p>限定的な粉塵侵入＋全方向の防沫。</p>
<ul>
<li>用途：小売ディスプレイ、展示ブース、半屋外の屋根付きエリア</li>
</ul>

<h3>IP65 — 全方向からのウォータージェット</h3>
<p>屋外 LED 設置の主力です。</p>
<div class="highlight">
<strong>IP65 = 完全粉塵密閉 + 全方向からの低圧ウォータージェットに耐性（6.3mm ノズル、12.5 L/min）。</strong>
</div>
<ul>
<li>用途：屋外看板、ファサード照明、街路灯、駐車場器具、ホース洗浄のある食品加工エリア</li>
<li>屋外 LED ドライバー需要の 70% 以上をカバー</li>
<li>CHUGAO で数量ベース最も売れているカテゴリ</li>
</ul>

<h3>IP67 — 1m までの一時的な浸水</h3>
<p>IP65 と同じ粉塵密閉性に加え、1m の水深に 30 分間浸かっても耐えます。</p>
<ul>
<li>用途：池やプール付近の景観照明、トンネル照明、地中埋込器具、浸水しやすい設置点</li>
<li>注：浸水深度は筐体の底面から測ります（上面ではありません）</li>
</ul>

<h3>IP68 — 1m を超える連続浸水</h3>
<p>最高規格。メーカー指定の深さ（通常 1m〜10m）で長期の水中動作に対応します。</p>
<ul>
<li>用途：プール照明、噴水器具、水槽照明、水中の建築的演出、海洋用途</li>
<li>これらは専用のポッティングとシーリングが必要——コストは IP67 よりかなり高くなります</li>
</ul>

<div class="warn">
<strong>よくある間違い：</strong> 溜まり水や浸水リスクのある用途（例：地中埋込器具）に IP65 を使うこと。IP67 へ引き上げるための 1 台あたり 2〜4 ドルの追加で、高くつく保証返品を防げます。
</div>

<h2>CHUGAO での試験方法</h2>

<ol>
<li><strong>組立：</strong>ドライバーは密閉されたアルミまたは樹脂筐体内で PU 樹脂によりポッティングされます。</li>
<li><strong>IP 試験：</strong>全ロットを IEC 60529 に基づき、校正済みのウォータージェットと粉塵チャンバーで抜き取り試験します。</li>
<li><strong>エージング試験：</strong>IP シーリング後に 40&deg;C 環境で 48 時間の全負荷運転を行い、潜在不良を検出します。</li>
</ol>

<h2>どれを発注すべきか？</h2>

<table class="ip-table">
<thead><tr><th>用途</th><th>最低 IP 等級</th><th>推奨</th></tr></thead>
<tbody>
<tr><td>屋内シーリング／壁付け</td><td>IP20</td><td>IP20</td></tr>
<tr><td>浴室／厨房</td><td>IP44</td><td>IP44</td></tr>
<tr><td>屋外看板／建物ファサード</td><td>IP65</td><td>IP65</td></tr>
<tr><td>トンネル／駐車場</td><td>IP65</td><td>IP67</td></tr>
<tr><td>水辺の景観</td><td>IP67</td><td>IP67</td></tr>
<tr><td>プール／噴水／水中</td><td>IP68</td><td>IP68</td></tr>
</tbody>
</table>

<div class="cta-box">
<h3>IP 等級をプロジェクトに合わせるのに迷っていますか？</h3>
<p>設置環境をお知らせください。適切な IP レベルと型番をご提案します。データシートも無料でお付けします。</p>
<a href="/#inquiry" class="btn">おすすめを聞く</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">建物ファサードや看板向けの粉塵密閉・耐ジェット電源。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">トンネル・プール・浸水しやすいエリア向けの一時浸水保護。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで正しい LED 電源を選ぶ</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">業界動向</span><span class="rel-title">2026 年の LED 市場：私たちが見ているもの</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">規制</span><span class="rel-title">LED ドライバーの BIS 認証：インド輸入ガイド</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深掘り</span><span class="rel-title">LED ドライバーの寿命：MTBF、L70、実際の使用年数</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog-1/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">3 ステップで正しい LED 電源を選ぶ</span></a><a class="pn-next" href="/blog-3/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">2026 年の LED 市場：私たちが見ているもの</span></a></nav>
</main>"""


BLOG_BODY['ja']['blog-3'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>2026 年の LED 市場：私たちが見ているもの</h1>
<div class="meta">業界動向 &middot; 2026 年 1 月 &middot; 約 8 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-3-led-market-md.avif 1200w, /images/blog-3-led-market.avif 1024w">
<source type="image/webp" srcset="/images/blog-3-led-market-md.webp 1200w, /images/blog-3-led-market.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-3-led-market.jpg" alt="2026 年 世界 LED 市場の概観" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>これは CHUGAO 中山工場の生産現場からの観察です——アナリストレポートでも市場調査論文でもありません。2025 年にお客様が実際に発注した内容と、2026 年に入って何を尋ねているかです。</p>

<h2>数字（当社の受注状況）</h2>

<div class="stat-grid">
<div class="stat-card"><div class="stat-num">+34%</div><div class="stat-label">受注量の前年比成長<br>（2025 対 2024）</div></div>
<div class="stat-card"><div class="stat-num">47%</div><div class="stat-label">新規受注がスマート／調光<br>機能を指定</div></div>
<div class="stat-card"><div class="stat-num">#1</div><div class="stat-label">成長市場：<br>中東／GCC 地域</div></div>
<div class="stat-card"><div class="stat-num">100W–200W</div><div class="stat-label">最も要望の多い<br>ワット数帯</div></div>
</div>

<h2>トレンド 1：IP67 が既定の要求に</h2>

<p>3 年前、屋外の標準仕様は IP65 でした。2025 年には、<strong>屋外ドライバー受注の 62% が IP67 を指定</strong>しました。100W で価格差は 1 台 1〜3 ドルまで縮まり、お客様は保証クレームに対応するより、浸水の余裕を選んでいます。</p>

<p>これは特に次の分野で顕著です。</p>
<ul>
<li><strong>景観照明の施工業者</strong>——一度の大雨で、週末を費やしてドライバーを交換することになります</li>
<li><strong>看板メーカー</strong>——取付点に結露がたまり、IP65 では完全に対応できません</li>
<li><strong>インフラプロジェクト</strong>（駐車場、トンネル、交通）——仕様策定者は今や既定で IP67 を書きます</li>
</ul>

<h2>トレンド 2：スマート／調光ドライバーが急成長</h2>

<p>新規問い合わせのほぼ半数が調光機能を尋ねます。実際に発注される内容の内訳：</p>

<ul>
<li><strong>DALI：</strong>商業ビルプロジェクト（オフィス、小売）。安定しているが 1 案件あたりの量は小さい。</li>
<li><strong>0-10V：</strong>依然として北米の数量王者。シンプル、安価、あらゆるものと互換。</li>
<li><strong>PWM 調光：</strong>精密な制御が重要な園芸照明や建築照明で急成長。</li>
<li><strong>Zigbee／WiFi／Bluetooth：</strong>関心は高いが実際の受注はまだ少ない（調光受注の約 8%）。ほとんどのお客様は別体のスマートコントローラーを好み、ドライバーはシンプルなままにしています。</li>
</ul>

<div class="highlight">
<strong>当社の見解：</strong> 2026 年に新製品ラインを立ち上げるなら、0-10V + オプションの DALI を軸に設計してください。これで現在の調光需要の 85% 以上をカバーでき、過剰設計にもなりません。
</div>

<h2>トレンド 3：地域シフト</h2>

<h3>中東／GCC——最も成長している地域</h3>
<p>サウジアラビア（ビジョン 2030 プロジェクト）、UAE（万博の遺産建設）、カタールが積極的に発注しています。主な特徴：</p>
<ul>
<li>屋外はすべて = 最低 IP67、噴水／プール工事では IP68 が多い</li>
<li>220V グリッド、50Hz——当社にとって標準</li>
<li>リードタイム感度が高い：在庫品は 7 日で出荷、カスタム OEM は 25 日</li>
<li>認証の重点：CE/RoHS に加えて SASO（サウジ）、ESMA（UAE）</li>
</ul>

<h3>欧州——安定、価格に敏感</h3>
<p>EU の受注は数量ベースで前年比横ばいですが、平均受注額はわずかに増えました。お客様はサプライヤーを集約しています（SKU を減らし、バッチを拡大）。エネルギー効率要件（ErP／エコデザイン）が、より高効率なドライバー（全負荷で &ge;90%）の需要を押し上げています。</p>

<h3>東南アジア——数量増、平均単価は低め</h3>
<p>ベトナム、タイ、インドネシア、フィリピンが急成長しています。ほとんどが屋内アダプターと IP20 ドライバーの受注——単価は低いが数量は多い。ここは価格競争が激しく、工場直販価格が不可欠です。</p>

<h3>米州——北米は安定、中南米が新興</h3>
<p>北米（米／加／墨）は売上高で当社最大の単一市場であり続けています。110V 入力、恒久設置に入るものは UL 認証が必要です。中南米（ブラジル、コロンビア、チリ）が新興——220V、街路照明と商業改修の需要が伸びています。</p>

<h2>トレンド 4：2026 年の仕様書の姿</h2>

<p>3 年前と比べ、入ってくる RFQ（見積依頼）は最初からより詳細な情報を求めています。今日最もよく要求される仕様：</p>

<ol>
<li><strong>50% 負荷で効率 &ge;88%</strong>（以前は全負荷効率のみ）</li>
<li><strong>50% 負荷で力率 &ge;0.9</strong></li>
<li><strong>THD &lt;15%</strong>（全高調波歪——系統運用者による要求が増加）</li>
<li><strong>動作温度範囲 -20&deg;C〜+50&deg;C</strong>（従来は -10&deg;C〜+40&deg;C）</li>
<li><strong>サージ保護 2kV ライン-ニュートラル</strong>（雷の多い市場で要求が増加）</li>
<li><strong>保証は最低 3 年</strong>、5 年を求める例も増加</li>
</ol>

<h2>トレンド 5：価格圧力と品質への影響</h2>

<p>率直に言います。Alibaba には常にもっと安い相手がいます。LED ドライバーを市場価格より 30% 安く買うと、次のものを得ます。</p>

<ul>
<li>より細い PCB 配線（連続負荷で過熱）</li>
<li>より小さい、またはノーブランドのコンデンサ（3〜5 年ではなく 12〜18 か月で故障）</li>
<li>本物のポッティングなし（IP 等級を謳うが未試験——数か月で水が浸入）</li>
<li>温度が上がると出力電圧が仕様外にドリフト（LED の明るさが不均一になるか早期故障）</li>
</ul>

<div class="highlight">
<strong>当社の立場：</strong> 当社は絶対的な最安値ではなく、信頼性とリードタイムで競います。1 台 0.80 ドル高いが 18 か月ではなく 5 年もつドライバーは、総所有コストで見れば安価です——返送費、再設置の工数、現場故障による評判の損害を考慮すればなおさらです。
</div>

<h2>2026 年後半の見通し</h2>

<ul>
<li><strong>GCC のインフラ支出</strong>は年末まで続く（ワールドカップ後の関連プロジェクト）。</li>
<li><strong>園芸用 LED ドライバー</strong>は、欧州と北米で制御環境農業が拡大するにつれ成長。</li>
<li><strong>USB-C / PD（Power Delivery）</strong>ドライバーがニッチ用途（家具組み込み、ポータブル器具）に現れ始める。今は少量だが注視に値する。</li>
<li><strong>バッテリーバックアップ／非常用ドライバー</strong>は、いくつかの国で建築基準が非常照明の適合を要求するため、関心が再燃。</li>
</ul>

<div class="cta-box">
<h3>2026 年の調達を計画中ですか？</h3>
<p>部品表または製品コンセプトをお送りください。見積もり、リードタイムの見積もり、条件を満たすプロジェクトには無料サンプルを提供します。</p>
<a href="/#inquiry" class="btn">問い合わせを始める</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">屋外・景観照明向けで最も成長している輸出ライン。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">看板筐体やファサード照明向けの大量生産主力。</span></a><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">世界の小売・住宅プロジェクト向けのコンパクトなアダプター。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで正しい LED 電源を選ぶ</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の選び方</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">規制</span><span class="rel-title">LED ドライバーの BIS 認証：インド輸入ガイド</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深掘り</span><span class="rel-title">LED ドライバーの寿命：MTBF、L70、実際の使用年数</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog-2/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">IP20・IP65・IP67・IP68 の選び方</span></a><a class="pn-next" href="/blog-4/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">LED ドライバーの BIS 認証：インド輸入ガイド</span></a></nav>
</main>"""


BLOG_BODY['ja']['blog-4'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>LED ドライバーの BIS 認証：インド輸入者が知っておくべきこと</h1>
<div class="meta">規制 &middot; 2026 年 5 月 &middot; 約 7 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof-md.avif 1200w, /images/product-waterproof.avif 1024w">
<source type="image/webp" srcset="/images/product-waterproof-md.webp 1200w, /images/product-waterproof.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-waterproof.jpg" alt="インド市場向け BIS 認証 LED 電源" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>2018 年以来、インドは電子製品に対する強制的な <strong>BIS（インド標準局）</strong>登録要件を段階的に拡大してきました。LED 電源をインドへ輸入する者にとって、BIS はもはや任意ではなく、通関の関門です。</p>

<p>本ガイドでは、BIS があなたの注文にとって何を意味するか、手続きの流れ、なぜスケジュールに影響するか、そして CHUGAO のような BIS 認証工場と組むことで数週間分の書類作業をどう省けるかを説明します。</p>

<h2>BIS とは？</h2>

<p>BIS はインドの国家標準機関です。強制登録制度（CRS）の下、対象カテゴリの製品はインドで輸入・販売する前に BIS 登録マークを付ける必要があります。</p>

<p>LED スイッチング電源に適用される規格は <strong>IS 13252（Part 1）：情報技術機器——安全——一般要求事項</strong>で、以下を対象とします。</p>
<ul>
<li>電気安全と絶縁</li>
<li>温度上昇限界</li>
<li>感電保護</li>
<li>防火筐体要件</li>
<li>部品の安全定格</li>
</ul>

<div class="highlight">
<strong>要点：</strong> LED ドライバーに BIS 登録がなければ、インド税関は貨物を拒否し、通関を遅延させ、またはあなたの費用で再輸出を求めることができます。
</div>

<h2>BIS 対 CE / RoHS</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">項目</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">CE / RoHS</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">BIS（インド）</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>所管機関</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">EU 委員会／自己宣言</td><td style="padding:10px 14px;border:1px solid var(--b)">インド政府（BIS）</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>強制か？</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">EU 市場では必須</td><td style="padding:10px 14px;border:1px solid var(--b)">インド輸入では必須</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>試験場所</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">工場ラボまたは第三者</td><td style="padding:10px 14px;border:1px solid var(--b)">インド国内の BIS 認定ラボ</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>標準的な期間</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">モデルあたり 2〜4 週間</td><td style="padding:10px 14px;border:1px solid var(--b)">モデルあたり 4〜8 週間</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>有効性</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">期限なし（自己宣言）</td><td style="padding:10px 14px;border:1px solid var(--b)">2 年、更新可能</td></tr>
</tbody>
</table>

<h2>BIS 手続きの流れ</h2>

<ol>
<li><strong>申請：</strong>製造者（またはその認定代理人）がポータルを通じて BIS にオンライン申請し、技術文書と認定ラボの試験報告書を添付します。</li>
<li><strong>工場検査：</strong>BIS は品質システムと生産の一貫性を確認するため、製造施設を監査することがあります。</li>
<li><strong>試験：</strong>サンプルは IS 13252（Part 1）に基づき試験されます。絶縁耐力、温度、湿度、機械的ストレス試験を含みます。</li>
<li><strong>ライセンスの付与：</strong>合格すると、BIS は製品ラベルと包装に表示される登録番号を発行します。</li>
<li><strong>サーベイランス：</strong>登録後、BIS は継続的な適合を確認するため定期的なフォローアップ監査を行います。</li>
</ol>

<h2>なぜこれがスケジュールに影響するか</h2>

<p>インド市場向けに LED ドライバーを発注する場合、二つの道があります。</p>

<ul>
<li><strong>パス A——BIS 非取得工場から発注：</strong>BIS は自分で対応します。出荷前に試験＋申請で 4〜8 週間を見込んでください。さらにラボ費用（複雑さに応じてモデルあたり 500〜2000 ドル）。</li>
<li><strong>パス B——BIS 認証工場から発注：</strong>工場がすでにそのモデルシリーズの BIS ライセンスを保有しています。注文はすぐに出荷されます。BIS 証明書のコピーを出荷書類とともに受け取ります。</li>
</ul>

<p>CHUGAO は中核 LED ドライバーモデルの BIS 登録を保有しています。インド向け注文をいただくと、BIS 証明書 PDF を出荷書類に同梱します——追加の待ち時間はありません。</p>

<h2>インドの買い手向け実務のヒント</h2>

<ul>
<li><strong>BIS の適用範囲を早めに確認。</strong>すべてのモデルが登録されているとは限りません。SKU リストを確定する前に、どの SKU が有効な BIS 状態かをお尋ねください。</li>
<li><strong>HS コードの分類を確認。</strong>LED 電源は通常 HS 8504.40（電子バラスト／変換器）に分類されます。規則は変わるため、通関ブローカーに確認してください。</li>
<li><strong>インドの港での BIS 書類審査に 2〜3 日余分に見込む。</strong>書類が正しくても、一部の港では電子機器の貨物を抜き取り検査します。</li>
<li><strong>ラベル要件：</strong>BIS 登録製品は、本体と外箱に BIS 標準マークを表示する必要があります。ご注文で「インド向け」とご指定いただければ、当社がこの表示を処理します。</li>
</ul>

<div class="cta-box">
<h3>インド市場向けに LED ドライバーを調達中ですか？</h3>
<p>対象モデル、数量、仕向港をお知らせください。1 時間以内に BIS 状態を確認し、すべての証明書を出荷に同梱します。</p>
<a href="/#inquiry" class="btn">インド対応の見積もりを依頼</a>
</div>


<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">インド向け出荷に対応した BIS 登録モデル。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">インド準拠のラベルを備えた BIS 適用電源。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで正しい LED 電源を選ぶ</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の選び方</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">業界動向</span><span class="rel-title">2026 年の LED 市場：私たちが見ているもの</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">技術深掘り</span><span class="rel-title">LED ドライバーの寿命：MTBF、L70、実際の使用年数</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog-3/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">2026 年の LED 市場：私たちが見ているもの</span></a><a class="pn-next" href="/blog-5/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">LED ドライバーの寿命：MTBF、L70、実際の使用年数</span></a></nav>
</main>"""


BLOG_BODY['ja']['blog-5'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>LED ドライバーの寿命：MTBF、L70、そして実際の使用年数</h1>
<div class="meta">技術深掘り &middot; 2026 年 4 月 &middot; 約 8 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor-md.avif 1200w, /images/product-indoor.avif 1024w">
<source type="image/webp" srcset="/images/product-indoor-md.webp 1200w, /images/product-indoor.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-indoor.jpg" alt="長寿命の屋内 LED ドライバー" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>データシートには「50,000 時間」とあります。計算すると連続運転で <strong>5.7 年</strong>です。ではなぜ、わずか 2〜3 年でドライバーを交換しなければならない設置があるのでしょうか？</p>

<p>答えは、定格寿命と実使用寿命は別物だということです。本記事では、これらの数字が実際に何を意味するのか、何がドライバーを早く壊すのか、そしてプロジェクトの想定供用寿命に合った仕様の選び方を説明します。</p>

<h2>重要な 3 つの指標</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">指標</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">測定対象</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">典型的な値</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>MTBF</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">平均故障間隔——母集団における故障間の統計的平均時間</td><td style="padding:10px 14px;border:1px solid var(--b)">50,000〜100,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>L70 / L80</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">出力が初期値の 70% または 80% まで低下するまでの時間</td><td style="padding:10px 14px;border:1px solid var(--b)">30,000〜50,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>保証期間</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">欠陥に対するメーカー保証</td><td style="padding:10px 14px;border:1px solid var(--b)">2〜5 年</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>重要な洞察：</strong> 50,000 時間の L70 定格は、試験条件下で 50,000 時間後にドライバーが初期出力の少なくとも 70% を維持することを意味します。すべての個体が故障するまで 50,000 時間動くという意味ではありません。
</div>

<h2>ドライバーが早期に故障する理由</h2>

<h3>1. 熱が最大の要因</h3>
<p>定格動作温度より 10&deg;C 高いごとに、電解コンデンサの寿命はおよそ半分になります。密閉灯具内に取り付けた IP20 屋内ドライバーは、周囲より 20&deg;C 高温で動作することも珍しくありません。周囲が 35&deg;C（夏によくある）なら、内部部品温度は 75〜85&deg;C に達し、典型的な設計点 60&deg;C を大きく超えます。</p>

<ul>
<li><strong>IP67 防水モデル：</strong>金属ケース＋シリコンポッティングで放熱性が向上。-30〜+60&deg;C 対応。典型的な寿命：50,000h。</li>
<li><strong>IP20 屋内モデル：</strong>灯具の通気に依存。密閉筐体では定格より 40〜60% 短い寿命を見込んでください。</li>
<li><strong>アダプター：</strong>樹脂筐体が熱をため込みやすい。典型的な寿命：30,000h。</li>
</ul>

<h3>2. 電圧スパイクとサージ</h3>
<p>系統電圧の変動（特に新興市場）は入力コンデンサと MOV にストレスを与えます。AC 190-264V 定格のドライバーは 280V の過渡を 1〜2 回なら耐えるかもしれませんが、繰り返しのサージは通常の摩耗より速く部品を劣化させます。</p>

<h3>3. 定格負荷近くでの運転</h3>
<p>定格負荷の 90〜100% では、出力コンデンサを通るリップル電流が増加します。これがより多くの熱を生み、劣化を早めます。CHUGAO が推奨する目安：</p>

<div class="highlight">
<strong>負荷ワット数 &times; 1.25 = ドライバーの最低定格。</strong><br>
ドライバーを 95% ではなく 70〜80% の容量で運転すると、実効寿命を 30〜50% 延ばせます。
</div>

<h2>用途ごとに必要なもの</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">用途</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">推奨ドライバー</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">想定供用寿命</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">理由</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">小売看板（1 日 8〜12 時間）</td><td style="padding:10px 14px;border:1px solid var(--b)">アダプター／屋内 IP20</td><td style="padding:10px 14px;border:1px solid var(--b)">8〜12 年</td><td style="padding:10px 14px;border:1px solid var(--b)">1 日の稼働時間が短く、単体寿命の短さを相殺</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">屋外ファサード照明（1 日 12 時間以上）</td><td style="padding:10px 14px;border:1px solid var(--b)">IP67 防水</td><td style="padding:10px 14px;border:1px solid var(--b)">10〜14 年</td><td style="padding:10px 14px;border:1px solid var(--b)">密閉ポッティングが湿度と温度変化に対応</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">産業 24/7（倉庫）</td><td style="padding:10px 14px;border:1px solid var(--b)">IP65 防雨または産業用 CGS</td><td style="padding:10px 14px;border:1px solid var(--b)">5〜7 年</td><td style="padding:10px 14px;border:1px solid var(--b)">連続高温運転が摩耗を加速</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">海洋／噴水</td><td style="padding:10px 14px;border:1px solid var(--b)">IP68 定格モデル</td><td style="padding:10px 14px;border:1px solid var(--b)">8〜12 年</td><td style="padding:10px 14px;border:1px solid var(--b)">完全浸水定格、塩水噴霧試験済み</td></tr>
</tbody>
</table>

<h2>CHUGAO での試験方法</h2>

<p>すべての CHUGAO ドライバーは出荷前に <strong>48 時間のバーンイン試験</strong>を行います。不合格品は廃棄され、工場から出ることはありません。この出荷前スクリーニングが初期故障（バスタブ曲線の早期故障部分）を捉えます。</p>

<p>500 個を超える OEM 注文では、発注書に指定いただければ追加費用なしで延長バーンイン（72〜168 時間）を提供します。</p>

<h2>クイック意思決定ガイド</h2>

<ol>
<li><strong>1 日の稼働時間？</strong>小売の 8 時間と産業の 24 時間では大きく変わります。目標プロジェクト寿命に 1 日の時間を掛けて総時間要件を求めてください。</li>
<li><strong>周囲温度？</strong>40&deg;C を超えて 10&deg;C ごとに寿命は約 50% 短くなります。モデル選定に織り込んでください。</li>
<li><strong>通気？</strong>密閉器具は IP67 以上が必要。通気のある筐体は IP20/65 で可。</li>
<li><strong>余裕？</strong>常に 25% を加えてください。故障品交換のための現場訪問に比べれば、60W と 100W のドライバーの価格差はわずかです。</li>
<li><strong>予備在庫？</strong>24/7 設置では 5〜10% の予備ドライバーを確保してください。緊急輸送より安くつきます。</li>
</ol>

<div class="cta-box">
<h3>どのドライバーが寿命要件に合うかわからない？</h3>
<p>用途、1 日の稼働時間、周囲条件をお知らせください。あなたの設置に合ったシリーズと、現実的な期待寿命をご提案します。</p>
<a href="/#inquiry" class="btn">寿命に合わせたおすすめを依頼</a>
</div>


<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">すべての定格に MTBF データを備えた長寿命アダプター。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内 LED ドライバー 50-400W</span><span class="pc-desc">商業・建築器具向けの L70 定格ドライバー。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">屋外での長い供用寿命のためのポッティング密閉。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">50,000 時間以上の屋外運転向けに設計された堅牢なドライバー。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで正しい LED 電源を選ぶ</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">技術ガイド</span><span class="rel-title">IP20・IP65・IP67・IP68 の選び方</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">業界動向</span><span class="rel-title">2026 年の LED 市場：私たちが見ているもの</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">規制</span><span class="rel-title">LED ドライバーの BIS 認証：インド輸入ガイド</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog-4/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">LED ドライバーの BIS 認証：インド輸入ガイド</span></a><a class="pn-next" href="/blog-6/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">IP67 と IP65 の LED ドライバー：どちらの等級が必要？</span></a></nav>
</main>"""


BLOG_BODY['ja']['blog-9'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 現場ノートに戻る</a>

<h1>定電圧か定電流か：どちらの LED ドライバーが必要ですか？</h1>
<div class="meta">技術ガイド &middot; 2026 年 9 月 &middot; 約 8 分で読めます</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="定電圧と定電流の LED ドライバーを並べた写真" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 器具がそもそも点くかどうかを決める 2 つの言葉があります——<strong>定電圧</strong>と<strong>定電流</strong>。取り違えると、LED は点かないか、数日で焼き切れます。しかし多くの買い手は器具が故障して初めてこの用語に出会います。そこで、すべての仕様書が最初に印刷してほしいと思う短い説明をここに示します。</p>

<h2>「定電圧」とは</h2>

<p>定電圧（CV）ドライバーは出力電圧を一定に保ちます——通常 12V、24V、36V、48V——どのくらいの電流を引くかは器具側が決めます。LED テープ、看板モジュール、そしてほとんどの「12V/24V」製品は自ら電流制限抵抗を備えているため、固定電圧の供給を必要とします。装飾・建築・看板工事の大半にとって、これが既定です。</p>

<div class="highlight">
<strong>目安：</strong> 製品ラベルに <strong>12V</strong> または <strong>24V</strong> とあれば、定電圧ドライバーが必要です。電圧はドライバーが決め、電流はテープが決めます。
</div>

<h2>「定電流」とは</h2>

<p>定電流（CC）ドライバーは電流を一定に保ちます——通常 350mA、500mA、700mA、1050mA、1500mA——LED の順方向電圧が温度で変化してもその電流を一定に保つよう電圧を変えます。素の大出力 LED（ダウンライト、投光器、街路灯、ハイベイモジュール）には基板上の安定化がなく、固定電圧源につなぐと暴走電流を引いて自らを焼きます。CC ドライバーが必要です。</p>

<p>ラベルに <strong>350 mA</strong> または <strong>700 mA</strong> とあれば、定電流が必要です。器具の仕様をお知らせいただければ適合させます。</p>

<h2>両者を並べて比較</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">特性</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">定電圧</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">定電流</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">保持する出力</td><td style="padding:10px 14px;border:1px solid var(--b)">電圧（12/24/36/48V）</td><td style="padding:10px 14px;border:1px solid var(--b)">電流（350-1500mA）</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">駆動対象</td><td style="padding:10px 14px;border:1px solid var(--b)">テープ、モジュール、看板</td><td style="padding:10px 14px;border:1px solid var(--b)">素の大出力 LED、ダウンライト</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">基板上の安定化</td><td style="padding:10px 14px;border:1px solid var(--b)">LED 製品側</td><td style="padding:10px 14px;border:1px solid var(--b)">ドライバー側</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">CHUGAO の代表ライン</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/adapters/">アダプター 5-200W</a>、<a href="/products/indoor/">屋内 50-400W</a></td><td style="padding:10px 14px;border:1px solid var(--b)">屋内／IP67（要望に応じて）</td></tr>
</tbody>
</table>

<h2>混用すると器具が壊れる理由</h2>

<ol>
<li><strong>定電圧ドライバーを定電流 LED に</strong>——LED は引けるだけの電流を引き、発熱し、壊れます。最も多いのは、12V テープ用電源を 350mA ダウンライトに流用するケースです。</li>
<li><strong>定電流ドライバーを定電圧テープに</strong>——ドライバーはテープの抵抗では制限できない電流を流し込み、テープは過熱するかドライバーが故障します。いずれにせよ点きません。</li>
</ol>

<p>通電前に必ず器具のラベルを読んでください。少しでも不明なら、ラベルの写真をお送りいただければ、どちらのタイプが必要かお答えします。</p>

<h2>1 台で両方できる？</h2>

<p>一部のプログラマブルまたは「デュアルモード」ドライバーは固定出力で CV または CC に設定できますが、高価で、必要とされることはまれです。標準的な設置では、正しいタイプを一度選べば現場への手戻りを避けられます。当社の <a href="/products/indoor/">屋内ドライバー</a> と <a href="/products/ip67/">IP67 ドライバー</a> は、大出力器具向けに 100W 以上の定電流版をご用意しています。</p>

<h2>ご提供いただきたい情報</h2>

<p>器具ラベル（ボルト表示の電圧、またはミリアンペア表示の電流）、総ワット数、設置場所、数量をお送りください。定電圧か定電流かを確認し、正確な型番をお見積もりします——そして、より安価な既製品で本当に十分な場合もお伝えします。</p>

<div class="cta-box">
<h3>あなたの器具が CV か CC かわからない？</h3>
<p>LED ラベルの写真をお送りください——ボルト表示の電圧、またはミリアンペア表示の電流。タイプを確認し、正確な型番をお見積もりします。</p>
<a href="/#inquiry" class="btn">CV か CC かを確認</a>
</div>

<section class="product-crosslink" aria-label="関連製品"><h2 class="related-h">CHUGAO 製品を見る</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED アダプター 5-200W</span><span class="pc-desc">テープ、モジュール、看板向けのコンパクトな 12V/24V ユニット。</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">屋内 LED ドライバー 50-400W</span><span class="pc-desc">シーリングやパネル灯向けのアクティブ PFC 付き定電圧。</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 防水ドライバー 10-400W</span><span class="pc-desc">湿潤・沿岸地向けの完全ポッティング、塩水噴霧試験済み。</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 防雨ドライバー 100-600W</span><span class="pc-desc">看板や半屋外設置向けの通気金属ケース。</span></a></div></section>

<section class="related" aria-label="関連記事">
  <h2 class="related-h">その他の現場ノート</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 技術</span><span class="rel-title">3 ステップで正しい LED 電源を選ぶ</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">購入ガイド</span><span class="rel-title">12V か 24V か：LED 電源の選び方</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">技術ガイド</span><span class="rel-title">LED 電源の容量決め：ワット数・余裕・突入電流</span></a><a class="rel-card" href="/blog-10/"><span class="rel-cat">技術ガイド</span><span class="rel-title">LED ドライバーの調光を解説：0-10V、PWM、DALI、TRIAC</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="記事ナビゲーション"><a class="pn-prev" href="/blog-8/" rel="prev"><span class="pn-lab">前の記事</span><span class="pn-t">LED 電源の容量決め：ワット数・余裕・突入電流</span></a><a class="pn-next" href="/blog-10/" rel="next"><span class="pn-lab">次の記事</span><span class="pn-t">LED ドライバーの調光を解説：0-10V、PWM、DALI、TRIAC</span></a></nav>
</main>"""
