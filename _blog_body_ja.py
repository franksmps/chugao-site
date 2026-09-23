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
