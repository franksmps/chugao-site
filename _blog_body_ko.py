# -*- coding: utf-8 -*-
"""Korean body copy for blog-1..5 and blog-9..14.

Extends the 'ko' sub-dict declared in blog_body_zh.py (blog-6/7/8). Only NEW
keys -- never re-declare BLOG_BODY['ko'] = {}.
AI translation pending native review.
"""


BLOG_BODY['ko']['blog-1'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>3단계로 올바른 LED 전원 고르기</h1>
<div class="meta">LED 기술 &middot; 2026년 3월 &middot; 약 6분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-1-led-power-supply-md.avif 1200w, /images/blog-1-led-power-supply.avif 1024w">
<source type="image/webp" srcset="/images/blog-1-led-power-supply-md.webp 1200w, /images/blog-1-led-power-supply.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-1-led-power-supply.jpg" alt="LED 전원 선택 가이드" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>LED 전원을 고르는 일은 기술적으로 들리지만, 결국 세 가지로 귀결됩니다: <strong>와트수</strong>, <strong>IP 등급</strong>, <strong>입력 전압</strong>. 이 세 가지만 제대로 맞추면 반품과 현장 고장의 90%를 없앨 수 있습니다.</p>

<p>이 가이드는 주문 전에 확인해야 할 점을 정확히 짚어 줍니다. 마케팅 부서가 아니라 당사 엔지니어링 팀이 작성했습니다.</p>

<h2>1단계: 와트수 맞추기</h2>

<p>가장 흔한 실수는 용량을 작게 잡는 것입니다. CHUGAO에서 사용하는 경험 법칙은 다음과 같습니다.</p>

<div class="highlight">
<strong>부하 와트수 &times; 1.25 = 드라이버 최소 정격.</strong><br>
항상 최소 25%의 여유를 두십시오. 드라이버를 100% 용량으로 운전하면 수명이 짧아지고 더 뜨거워집니다.
</div>

<h3>예시</h3>
<p>LED 스트립이 80W를 소비한다면 80W 드라이버를 사지 마십시오. 100W(또는 그 이상)를 사십시오. 여분의 용량은 출력을 안정적으로 유지하고 발열을 줄이며 수명을 약 3년에서 5년 이상으로 늘립니다.</p>

<h3>여유가 중요한 이유</h3>
<ul>
<li><strong>온도:</strong> 드라이버는 정격 부하 이하에서 더 시원하게 작동합니다. 온도가 10&deg;C 낮아질 때마다 커패시터 수명은 대략 두 배가 됩니다.</li>
<li><strong>서지 내성:</strong> LED 스트립은 시동 시 짧은 스파이크를 끌어올 수 있습니다. 여유가 있으면 보호 회로가 작동하지 않고 이를 흡수합니다.</li>
<li><strong>전압 안정성:</strong> 가볍게 부하된 드라이버는 출력 전압을 더 엄격하게 유지하므로 밝기가 더 일정합니다.</li>
</ul>

<h2>2단계: 올바른 IP 등급 선택</h2>

<p>IP(침입 보호) 코드는 드라이버가 먼지와 물을 얼마나 잘 견디는지 알려 줍니다. 대부분의 프로젝트가 여기서 잘못됩니다——드라이버에서 2달러를 아끼고 한 번의 폭우 후에 교체하게 됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">IP 등급</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">먼지</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">물</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">사용 사례</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP20</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">보호 없음</td><td style="padding:10px 14px;border:1px solid var(--b)">방수 없음</td><td style="padding:10px 14px;border:1px solid var(--b)">실내 건조 장소 전용</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">먼지 밀폐</td><td style="padding:10px 14px;border:1px solid var(--b)">워터 제트(모든 방향)</td><td style="padding:10px 14px;border:1px solid var(--b)">옥외 노출, 세척 구역</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">먼지 밀폐</td><td style="padding:10px 14px;border:1px solid var(--b)">1m까지 침수</td><td style="padding:10px 14px;border:1px solid var(--b)">일시적 침수, 침수 위험</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">먼지 밀폐</td><td style="padding:10px 14px;border:1px solid var(--b)">연속 침수</td><td style="padding:10px 14px;border:1px solid var(--b)">수중 기구, 깊은 침수</td></tr>
</tbody>
</table>

<p>확실하지 않다면 필요하다고 생각하는 것보다 한 단계 높게 선택하십시오. 100W 드라이버에서 IP20과 IP65의 가격 차이는 공장 직거래 가격으로 보통 3달러 미만입니다.</p>

<h2>3단계: 입력 전압 호환성 확인</h2>

<p>이 항목은 간과하기 쉽지만 가장 높은 반품률을 유발합니다.</p>

<ul>
<li><strong>북미·일본·중국 대만·중국 본토:</strong> 110V AC / 60Hz</li>
<li><strong>유럽·중국 본토·아시아 대부분·아프리카:</strong> 220–240V AC / 50Hz</li>
<li><strong>브라질:</strong> 127V/220V 혼합(현지 콘센트 확인)</li>
<li><strong>산업／선박:</strong> 흔히 277V, 380V 또는 480V 3상</li>
</ul>

<p>입력 범위는 제품 라인마다 다릅니다. 어댑터는 100–240V AC, 실내·IP65·IP67 모델은 190–264V(IP67은 최대 340V)를 지원합니다. 사용 중인 모델의 정확한 입력 범위를 <a href="/#specs">사양표</a>에서 확인하고 목적지 전력망 전압과 일치하는지 확인하십시오.</p>

<h2>빠른 확인 체크리스트</h2>

<ol>
<li>LED 총 부하 와트수를 합산 &rarr; 1.25를 곱함 &rarr; 가장 가까운 표준 드라이버 크기로 올림.</li>
<li>설치 환경 확인 &rarr; 실내(IP20), 옥외／방우(IP65), 또는 침수 위험(IP67/IP68).</li>
<li>목적지 국가의 전력망 전압 확인 &rarr; 110V 지역 또는 220V 지역.</li>
<li>선택: 조광이 필요하십니까? (0-10V, PWM, DALI 또는 Triac——주문 시 지정)</li>
<li>선택: UL 인증이 필요하십니까? (비용 증가, 모델당 2~3주 리드타임)</li>
</ol>

<div class="cta-box">
<h3>어떤 모델이 맞는지 모르시겠습니까?</h3>
<p>사양을 보내 주십시오——와트수, 수량, 목적지 항구, 목표 시장. 영업시간 중 1시간 이내에 데이터시트와 견적으로 회신합니다.</p>
<a href="/#inquiry" class="btn">견적 요청</a>
</div>


<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">사인과 스트립 조명용 광입력 콘센트／데스크톱 어댑터.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">패널·다운라이트·상업용 기구용 고효율 드라이버.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">옥외 및 조경 프로젝트용 침수 등급 전원.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 선택법</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">업계 동향</span><span class="rel-title">2026 LED 시장: 우리가 보고 있는 것</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">규제</span><span class="rel-title">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog/"><span class="pn-lab">모든 글</span><span class="pn-t">현장 노트</span></a><a class="pn-next" href="/blog-2/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">IP20·IP65·IP67·IP68 선택법</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-2'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>IP20 vs IP65 vs IP67 vs IP68</h1>
<div class="meta">기술 가이드 &middot; 2026년 2월 &middot; 약 7분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-2-ip-rating-md.avif 1200w, /images/blog-2-ip-rating.avif 1024w">
<source type="image/webp" srcset="/images/blog-2-ip-rating-md.webp 1200w, /images/blog-2-ip-rating.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-2-ip-rating.jpg" alt="IP 등급 비교 차트" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>모든 LED 전원에는 IP 등급이 있습니다. 두 자리로 구성되며, 첫째 자리는 <strong>먼지／고체 입자 보호</strong>, 둘째 자리는 <strong>물 보호</strong>를 나타냅니다. 숫자가 높을수록 밀봉이 우수합니다.</p>

<p>이 가이드는 일반적인 각 IP 등급이 실제로 무엇을 의미하는지 분해하여, 과지출도 사양 미달도 피할 수 있게 합니다.</p>

<h2>두 자리 시스템 이해하기</h2>

<table class="ip-table">
<thead><tr><th>자리</th><th>측정 대상</th><th>척도</th></tr></thead>
<tbody>
<tr><td><strong>첫째 자리(0–6)</strong></td><td>고체／먼지</td><td>0 = 보호 없음 &rarr; 6 = 먼지 밀폐</td></tr>
<tr><td><strong>둘째 자리(0–8)</strong></td><td>액체／물</td><td>0 = 보호 없음 &rarr; 8 = 연속 침수</td></tr>
</tbody>
</table>

<h2>첫째 자리: 먼지 보호</h2>

<ul>
<li><strong>IPx0:</strong> 보호 없음. 어떤 상업용 LED 드라이버에도 사용되지 않습니다.</li>
<li><strong>IPx3 – IPx4:</strong> 전선, 나사, 손가락 침입 방지. 기본 안전 보호.</li>
<li><strong>IPx5:</strong> 제한적 먼지 침입. 미세 먼지가 일부 들어오지만 작동에 지장이 없습니다.</li>
<li><strong>IPx6:</strong> 먼지 밀폐. 먼지 침입 제로. 모든 옥외용 드라이버의 표준입니다.</li>
</ul>

<p>실제로 유의미한 방수 등급(둘째 자리 4 이상)을 가진 당사 모든 드라이버는 이미 먼지 기준 IPx6을 충족합니다. 이 자리는 따로 걱정할 필요가 거의 없습니다.</p>

<h2>둘째 자리: 물 보호 — 결정이 이루어지는 곳</h2>

<h3>IP20 / IP21 — 실내 전용</h3>
<p>수직 방향의 물방울은 무영향(IP20). 수직에서 15&deg; 이내의 물방울도 무영향(IP21).</p>
<ul>
<li>용도: 실내 천장 기구, 밀폐형 등기구, 건조 장소</li>
<li>회피: 창문, 욕실, 주방, 공조 송풍구 근처</li>
<li>비용: 최저 등급</li>
</ul>

<h3>IP44 — 비말 보호</h3>
<p>모든 방향의 물튀김에도 손상되지 않습니다.</p>
<ul>
<li>용도: 욕실 거울등, 캐비닛 하부 스트립, 주방 작업 조명</li>
<li>직접적인 비 노출이나 세척에는 부적합</li>
</ul>

<h3>IP54 — 먼지 + 비말 보호</h3>
<p>제한적 먼지 침입 + 전 방향 비말 보호.</p>
<ul>
<li>용도: 소매 디스플레이, 전시 부스, 반옥외 지붕 있는 구역</li>
</ul>

<h3>IP65 — 모든 방향의 워터 제트</h3>
<p>옥외 LED 설치의 주력입니다.</p>
<div class="highlight">
<strong>IP65 = 완전 먼지 밀폐 + 모든 방향의 저압 워터 제트에 대한 보호(6.3mm 노즐, 12.5 L/min).</strong>
</div>
<ul>
<li>용도: 옥외 사인, 파사드 조명, 가로등, 주차장 기구, 호스 세척이 있는 식품 가공 구역</li>
<li>옥외 LED 드라이버 수요의 70% 이상을 커버</li>
<li>CHUGAO에서 수량 기준 가장 많이 팔리는 카테고리</li>
</ul>

<h3>IP67 — 1m까지 일시적 침수</h3>
<p>IP65와 동일한 먼지 밀폐성에 더해, 1m 수심에 30분간 잠겨도 견딥니다.</p>
<ul>
<li>용도: 연못이나 수영장 근처의 조경 조명, 터널 조명, 지중 매립 기구, 침수되기 쉬운 설치 지점</li>
<li>참고: 침수 깊이는 인클로저의 바닥에서 측정합니다(상단이 아님)</li>
</ul>

<h3>IP68 — 1m를 초과하는 연속 침수</h3>
<p>최고 등급. 제조사가 지정한 깊이(보통 1m~10m)에서 장기 수중 작동에 적합합니다.</p>
<ul>
<li>용도: 수영장 조명, 분수 기구, 수족관 조명, 수중 건축 연출, 해양 용도</li>
<li>이들은 특수 포팅과 실링이 필요합니다——비용이 IP67보다 상당히 높습니다</li>
</ul>

<div class="warn">
<strong>흔한 실수:</strong> 고인 물이나 침수 위험이 있는 용도(예: 지중 매립 기구)에 IP65를 사용하는 것. IP67로 올리기 위한 대당 2~4달러의 추가 비용으로 값비싼 보증 반품을 막을 수 있습니다.
</div>

<h2>CHUGAO의 시험 방식</h2>

<ol>
<li><strong>조립:</strong> 드라이버는 밀봉된 알루미늄 또는 플라스틱 인클로저 내부에서 PU 수지로 포팅됩니다.</li>
<li><strong>IP 시험:</strong> 모든 배치를 IEC 60529 기준으로 교정된 워터 제트와 먼지 챔버 장비로 샘플 시험합니다.</li>
<li><strong>에이징 시험:</strong> IP 실링 후 40&deg;C 환경에서 48시간 전부하 운전을 하여 잠재 결함을 검출합니다.</li>
</ol>

<h2>어느 것을 주문해야 합니까?</h2>

<table class="ip-table">
<thead><tr><th>용도</th><th>최소 IP 등급</th><th>권장</th></tr></thead>
<tbody>
<tr><td>실내 천장／벽 부착</td><td>IP20</td><td>IP20</td></tr>
<tr><td>욕실／주방</td><td>IP44</td><td>IP44</td></tr>
<tr><td>옥외 사인／건물 파사드</td><td>IP65</td><td>IP65</td></tr>
<tr><td>터널／주차장</td><td>IP65</td><td>IP67</td></tr>
<tr><td>물가 조경</td><td>IP67</td><td>IP67</td></tr>
<tr><td>수영장／분수／수중</td><td>IP68</td><td>IP68</td></tr>
</tbody>
</table>

<div class="cta-box">
<h3>IP 등급을 프로젝트에 맞추는 데 도움이 필요하십니까?</h3>
<p>설치 환경을 알려 주시면 적합한 IP 레벨과 모델명을 추천해 드립니다. 데이터시트도 무료로 제공합니다.</p>
<a href="/#inquiry" class="btn">추천 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">건물 파사드와 사인용 먼지 밀폐·제트 방수 전원.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">터널·수영장·침수 위험 지역용 일시적 침수 보호.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">업계 동향</span><span class="rel-title">2026 LED 시장: 우리가 보고 있는 것</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">규제</span><span class="rel-title">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-1/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">3단계로 올바른 LED 전원 고르기</span></a><a class="pn-next" href="/blog-3/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">2026 LED 시장: 우리가 보고 있는 것</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-3'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>2026 LED 시장: 우리가 보고 있는 것</h1>
<div class="meta">업계 동향 &middot; 2026년 1월 &middot; 약 8분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-3-led-market-md.avif 1200w, /images/blog-3-led-market.avif 1024w">
<source type="image/webp" srcset="/images/blog-3-led-market-md.webp 1200w, /images/blog-3-led-market.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-3-led-market.jpg" alt="2026 글로벌 LED 시장 개요" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>이것은 CHUGAO 중산 공장 생산 현장에서의 관찰입니다——애널리스트 보고서나 시장 조사 논문이 아닙니다. 2025년에 고객이 실제로 주문한 내용과 2026년으로 넘어가며 무엇을 묻고 있는지입니다.</p>

<h2>숫자(당사 수주 현황)</h2>

<div class="stat-grid">
<div class="stat-card"><div class="stat-num">+34%</div><div class="stat-label">수주량 전년 대비 성장<br>(2025 대 2024)</div></div>
<div class="stat-card"><div class="stat-num">47%</div><div class="stat-label">신규 주문이 스마트／조광<br>기능을 지정</div></div>
<div class="stat-card"><div class="stat-num">#1</div><div class="stat-label">성장 시장:<br>중동／GCC 지역</div></div>
<div class="stat-card"><div class="stat-num">100W–200W</div><div class="stat-label">가장 많이 요청되는<br>와트수 대역</div></div>
</div>

<h2>트렌드 1: IP67이 이제 기본 요구</h2>

<p>3년 전만 해도 옥외 표준 사양은 IP65였습니다. 2025년에는 <strong>옥외 드라이버 주문의 62%가 IP67을 지정</strong>했습니다. 100W에서 가격 차이는 대당 1~3달러로 좁혀졌고, 고객은 보증 클레임을 처리하느니 침수 여유를 택합니다.</p>

<p>이는 특히 다음 분야에서 두드러집니다.</p>
<ul>
<li><strong>조경 조명 시공사</strong>——한 번의 폭우로 주말을 들여 드라이버를 교체해야 합니다</li>
<li><strong>사인 제조사</strong>——설치 지점에 결로가 고여 IP65로는 완전히 감당할 수 없습니다</li>
<li><strong>인프라 프로젝트</strong>(주차, 터널, 교통)——사양 작성자가 이제 기본적으로 IP67을 씁니다</li>
</ul>

<h2>트렌드 2: 스마트／조광 드라이버의 빠른 성장</h2>

<p>신규 문의의 거의 절반이 조광 기능을 묻습니다. 실제로 주문되는 내용의 구성:</p>

<ul>
<li><strong>DALI:</strong> 상업용 빌딩 프로젝트(사무실, 소매). 안정적이지만 프로젝트당 물량은 작습니다.</li>
<li><strong>0-10V:</strong> 여전히 북미의 물량 왕. 단순하고 저렴하며 모든 것과 호환됩니다.</li>
<li><strong>PWM 조광:</strong> 정밀 제어가 중요한 원예 조명과 건축 조명에서 빠르게 성장.</li>
<li><strong>Zigbee／WiFi／블루투스:</strong> 관심은 높지만 실제 주문은 아직 적습니다(조광 주문의 약 8%). 대부분의 고객은 별도의 스마트 컨트롤러를 선호하고 드라이버는 단순하게 둡니다.</li>
</ul>

<div class="highlight">
<strong>당사 견해:</strong> 2026년에 신제품 라인을 출시한다면 0-10V + 선택적 DALI를 중심으로 설계하십시오. 이는 현재 조광 수요의 85% 이상을 커버하면서 과잉 설계가 되지 않습니다.
</div>

<h2>트렌드 3: 지역별 변화</h2>

<h3>중동／GCC——가장 빠르게 성장하는 지역</h3>
<p>사우디아라비아(비전 2030 프로젝트), UAE(엑스포 이후 건설), 카타르가 적극적으로 주문하고 있습니다. 주요 특징:</p>
<ul>
<li>옥외는 모두 = 최소 IP67, 분수／수영장 공사에는 흔히 IP68</li>
<li>220V 그리드, 50Hz——당사에 표준</li>
<li>리드타임 민감도: 재고품은 7일 출하, 맞춤 OEM은 25일</li>
<li>인증 중시: CE/RoHS 외에 SASO(사우디), ESMA(UAE)</li>
</ul>

<h3>유럽——안정적, 가격 민감</h3>
<p>EU 주문은 물량 기준 전년 대비 보합이지만 평균 주문 금액은 소폭 상승했습니다. 고객은 공급사를 통합하고 있습니다(SKU 감소, 배치 확대). 에너지 효율 요건(ErP／에코디자인)이 더 높은 효율의 드라이버(전부하 &ge;90%) 수요를 밀어 올리고 있습니다.</p>

<h3>동남아시아——물량 증가, 평균 단가 낮음</h3>
<p>베트남, 태국, 인도네시아, 필리핀이 빠르게 성장하고 있습니다. 대부분 실내 어댑터와 IP20 드라이버 주문——단가는 낮지만 수량이 많습니다. 여기서는 가격 경쟁이 치열하며, 공장 직거래 가격이 필수입니다.</p>

<h3>아메리카——북미 안정, 중남미 신흥</h3>
<p>북미(미／캐／멕)는 매출 기준 당사 최대 단일 시장으로 남아 있습니다. 110V 입력, 영구 설치에 들어가는 모든 제품은 UL 인증이 필요합니다. 중남미(브라질, 콜롬비아, 칠레)가 신흥——220V, 가로등과 상업 리모델링 수요가 성장하고 있습니다.</p>

<h2>트렌드 4: 2026년 사양서의 모습</h2>

<p>3년 전과 비교해 들어오는 RFQ(견적 요청)는 처음부터 더 자세한 정보를 요구합니다. 오늘 가장 자주 요구되는 사양:</p>

<ol>
<li><strong>50% 부하에서 효율 &ge;88%</strong>(예전에는 전부하 효율만)</li>
<li><strong>50% 부하에서 역률 &ge;0.9</strong></li>
<li><strong>THD &lt;15%</strong>(총 고조파 왜곡——전력망 운영자의 요구 증가)</li>
<li><strong>동작 온도 범위 -20&deg;C ~ +50&deg;C</strong>(과거에는 -10&deg;C ~ +40&deg;C)</li>
<li><strong>서지 보호 2kV 라인-뉴트럴</strong>(낙뢰가 잦은 시장에서 요구 증가)</li>
<li><strong>보증 최소 3년</strong>, 5년을 요구하는 경우도 증가</li>
</ol>

<h2>트렌드 5: 가격 압력과 품질에 미치는 영향</h2>

<p>솔직히 말씀드립니다. 알리바바에는 항상 더 싼 상대가 있습니다. LED 드라이버를 시장가보다 30% 낮게 살 때 얻게 되는 것:</p>

<ul>
<li>더 얇은 PCB 배선(연속 부하에서 과열)</li>
<li>더 작거나 무브랜드 커패시터(3~5년이 아니라 12~18개월 만에 고장)</li>
<li>진짜 포팅 없음(IP 등급을 표방하지만 미시험——수개월 내 물이 침투)</li>
<li>온도가 오르면 출력 전압이 사양을 벗어남(LED 밝기가 불균일하거나 조기 고장)</li>
</ul>

<div class="highlight">
<strong>당사 입장:</strong> 당사는 절대적 최저가가 아니라 신뢰성과 리드타임으로 경쟁합니다. 대당 0.80달러 더 비싸지만 18개월이 아니라 5년을 가는 드라이버가 총소유비용에서 더 저렴합니다——반송비, 재설치 인건비, 현장 고장으로 인한 평판 손실을 고려하면 더욱 그렇습니다.
</div>

<h2>2026년 하반기 전망</h2>

<ul>
<li><strong>GCC 인프라 지출</strong>은 연말까지 지속(월드컵 후속 프로젝트).</li>
<li><strong>원예용 LED 드라이버</strong>는 유럽과 북미에서 제어환경농업이 확대됨에 따라 성장.</li>
<li><strong>USB-C / PD(Power Delivery)</strong> 드라이버가 틈새 용도(가구 일체형, 휴대용 기구)에 등장하기 시작. 지금은 소량이지만 주목할 가치가 있습니다.</li>
<li><strong>배터리 백업／비상용 드라이버</strong>는 여러 국가의 건축 기준이 비상 조명 준수를 요구하면서 관심이 다시 높아지고 있습니다.</li>
</ul>

<div class="cta-box">
<h3>2026년 조달을 계획 중이십니까?</h3>
<p>자재 명세서나 제품 콘셉트를 보내 주십시오. 견적, 리드타임 추정, 조건을 충족하는 프로젝트에는 무료 샘플을 제공합니다.</p>
<a href="/#inquiry" class="btn">문의 시작하기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">옥외 및 조경 조명용으로 가장 빠르게 성장하는 수출 라인.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">사인 캐비닛과 파사드 조명용 대량 주력 제품.</span></a><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">전 세계 소매 및 주거 프로젝트용 소형 어댑터.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 선택법</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">규제</span><span class="rel-title">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-2/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">IP20·IP65·IP67·IP68 선택법</span></a><a class="pn-next" href="/blog-4/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-4'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>LED 드라이버 BIS 인증: 인도 수입업자가 알아야 할 것</h1>
<div class="meta">규제 &middot; 2026년 5월 &middot; 약 7분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof-md.avif 1200w, /images/product-waterproof.avif 1024w">
<source type="image/webp" srcset="/images/product-waterproof-md.webp 1200w, /images/product-waterproof.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-waterproof.jpg" alt="인도 시장용 BIS 인증 LED 전원" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>2018년부터 인도는 전자 제품에 대한 의무 <strong>BIS(인도표준국)</strong> 등록 요건을 점진적으로 확대해 왔습니다. LED 전원을 인도로 수입하는 사람에게 BIS는 더 이상 선택이 아니라 세관 관문입니다.</p>

<p>이 가이드는 BIS가 주문에 무엇을 의미하는지, 절차가 어떻게 진행되는지, 왜 일정에 영향을 미치는지, 그리고 CHUGAO처럼 BIS 인증을 받은 공장과 협력하면 수주 분의 서류 작업을 어떻게 절약할 수 있는지 설명합니다.</p>

<h2>BIS란?</h2>

<p>BIS는 인도의 국가표준기구입니다. 의무등록제도(CRS)에 따라 대상 카테고리 제품은 인도에서 수입 또는 판매되기 전에 BIS 등록 마크를 부착해야 합니다.</p>

<p>LED 스위칭 전원에 적용되는 표준은 <strong>IS 13252(Part 1): 정보기술기기——안전——일반 요구사항</strong>이며, 다음을 포함합니다.</p>
<ul>
<li>전기 안전 및 절연</li>
<li>온도 상승 한계</li>
<li>감전 보호</li>
<li>방화 인클로저 요구사항</li>
<li>부품 안전 정격</li>
</ul>

<div class="highlight">
<strong>핵심:</strong> LED 드라이버에 BIS 등록이 없으면 인도 세관은 화물을 거부하거나 통관을 지연시키거나, 귀하의 비용으로 재수출을 요구할 수 있습니다.
</div>

<h2>BIS 대 CE / RoHS</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">항목</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">CE / RoHS</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">BIS(인도)</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>관리 기관</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">EU 집행위／자기 선언</td><td style="padding:10px 14px;border:1px solid var(--b)">인도 정부(BIS)</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>의무인가?</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">EU 시장에서 필수</td><td style="padding:10px 14px;border:1px solid var(--b)">인도 수입 시 필수</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>시험 장소</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">공장 실험실 또는 제3자</td><td style="padding:10px 14px;border:1px solid var(--b)">인도 내 BIS 인정 실험실</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>일반 기간</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">모델당 2-4주</td><td style="padding:10px 14px;border:1px solid var(--b)">모델당 4-8주</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>유효성</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">만료 없음(자기 선언)</td><td style="padding:10px 14px;border:1px solid var(--b)">2년, 갱신 가능</td></tr>
</tbody>
</table>

<h2>BIS 절차</h2>

<ol>
<li><strong>신청:</strong> 제조사(또는 권한을 위임받은 대리인)가 포털을 통해 BIS에 온라인 신청하며, 기술 문서와 인정 실험실의 시험 성적서를 첨부합니다.</li>
<li><strong>공장 심사:</strong> BIS는 품질 시스템과 생산 일관성을 검증하기 위해 제조 시설을 감사할 수 있습니다.</li>
<li><strong>시험:</strong> 샘플은 IS 13252(Part 1)에 따라 시험됩니다. 절연 내력, 온도, 습도, 기계적 스트레스 시험이 포함됩니다.</li>
<li><strong>라이선스 부여:</strong> 통과하면 BIS는 제품 라벨과 포장에 표시되는 등록 번호를 발급합니다.</li>
<li><strong>사후 감독:</strong> 등록 후 BIS는 지속적 준수를 확인하기 위해 정기적인 후속 감사를 실시합니다.</li>
</ol>

<h2>이것이 일정에 영향을 주는 이유</h2>

<p>인도 시장용 LED 드라이버를 주문한다면 두 가지 길이 있습니다.</p>

<ul>
<li><strong>경로 A——BIS 미인증 공장에서 주문:</strong> BIS를 직접 처리합니다. 화물이 출하되기 전에 4-8주 시험 + 신청 기간을 예상하십시오. 또한 실험실 비용(복잡도에 따라 모델당 500-2000달러).</li>
<li><strong>경로 B——BIS 인증 공장에서 주문:</strong> 공장이 이미 해당 모델 시리즈의 BIS 라이선스를 보유하고 있습니다. 주문은 즉시 출하됩니다. BIS 인증서 사본을 선적 서류와 함께 받습니다.</li>
</ul>

<p>CHUGAO는 핵심 LED 드라이버 모델에 대한 BIS 등록을 보유하고 있습니다. 인도행 주문을 하시면 BIS 인증서 PDF를 선적 서류에 포함합니다——추가 대기 없음.</p>

<h2>인도 구매자를 위한 실무 팁</h2>

<ul>
<li><strong>BIS 적용 범위를 일찍 확인하십시오.</strong> 모든 모델이 등록되어 있지는 않습니다. SKU 목록을 확정하기 전에 어떤 SKU가 유효한 BIS 상태인지 문의하십시오.</li>
<li><strong>HS 코드 분류를 확인하십시오.</strong> LED 전원은 일반적으로 HS 8504.40(전자 안정기／변환기)에 분류됩니다. 규칙이 바뀌므로 관세사와 확인하십시오.</li>
<li><strong>인도 항구의 BIS 서류 심사에 2-3일을 추가로 확보하십시오.</strong> 서류가 정확해도 일부 항구는 전자 제품 화물을 표본 검사합니다.</li>
<li><strong>라벨 요건:</strong> BIS 등록 제품은 본체와 외부 카톤에 BIS 표준 마크를 표시해야 합니다. 주문에 “인도 목적지”를 명시하시면 당사가 이 라벨링을 처리합니다.</li>
</ul>

<div class="cta-box">
<h3>인도 시장용 LED 드라이버를 조달 중이십니까?</h3>
<p>대상 모델, 수량, 목적지 항구를 알려 주십시오. 1시간 이내에 BIS 상태를 확인하고 모든 인증서를 선적에 포함합니다.</p>
<a href="/#inquiry" class="btn">인도 대응 견적 요청</a>
</div>


<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">인도행 선적 준비가 된 BIS 등록 모델.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">인도 라벨 요건을 충족하는 BIS 적용 전원.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 선택법</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">업계 동향</span><span class="rel-title">2026 LED 시장: 우리가 보고 있는 것</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-3/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">2026 LED 시장: 우리가 보고 있는 것</span></a><a class="pn-next" href="/blog-5/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-5'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>LED 드라이버 수명: MTBF, L70 및 실제 수명</h1>
<div class="meta">기술 심층 &middot; 2026년 4월 &middot; 약 8분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor-md.avif 1200w, /images/product-indoor.avif 1024w">
<source type="image/webp" srcset="/images/product-indoor-md.webp 1200w, /images/product-indoor.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/product-indoor.jpg" alt="긴 수명의 실내 LED 드라이버" loading="lazy" style="width:100%;aspect-ratio:1/1">
</picture>
</div>

<p>데이터시트에는 “50,000시간”이라고 적혀 있습니다. 계산해 보면 연속 운전으로 <strong>5.7년</strong>입니다. 그런데 왜 어떤 설치 현장은 2-3년 만에 드라이버를 교체해야 할까요?</p>

<p>답은 정격 수명과 실제 수명은 다르다는 것입니다. 이 글은 그 숫자들이 실제로 무엇을 의미하는지, 무엇이 드라이버를 일찍 고장내는지, 프로젝트의 예상 사용 수명에 맞는 사양을 어떻게 고를지 설명합니다.</p>

<h2>중요한 세 가지 지표</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">지표</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">측정 대상</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">일반적인 값</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>MTBF</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">평균 고장 간격——모집단에서 고장 사이의 통계적 평균 시간</td><td style="padding:10px 14px;border:1px solid var(--b)">50,000-100,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>L70 / L80</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">출력이 초기값의 70% 또는 80%로 떨어지는 시간</td><td style="padding:10px 14px;border:1px solid var(--b)">30,000-50,000h</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>보증 기간</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">결함에 대한 제조사 보증</td><td style="padding:10px 14px;border:1px solid var(--b)">2-5년</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>핵심 통찰:</strong> 50,000시간의 L70 정격은 시험 조건에서 50,000시간 후에도 드라이버가 초기 출력의 최소 70%를 유지한다는 뜻입니다. 모든 개체가 고장 나기까지 50,000시간을 간다는 뜻은 아닙니다.
</div>

<h2>드라이버가 조기 고장하는 이유</h2>

<h3>1. 열이 최대 원인</h3>
<p>정격 동작 온도보다 10&deg;C 높을 때마다 전해 커패시터 수명은 대략 절반이 됩니다. 밀폐 등기구 내부에 장착한 IP20 실내 드라이버는 주변보다 20&deg;C 더 뜨겁게 동작하기 쉽습니다. 주변이 35&deg;C(여름에 흔함)라면 내부 부품 온도는 75-85&deg;C에 달해 일반적인 설계점 60&deg;C를 훨씬 웃돕니다.</p>

<ul>
<li><strong>IP67 방수 모델:</strong> 금속 케이스 + 실리콘 포팅으로 방열이 우수합니다. -30 ~ +60&deg;C 정격. 일반적인 수명: 50,000h.</li>
<li><strong>IP20 실내 모델:</strong> 등기구 통기에 의존합니다. 밀폐 하우징에서는 정격보다 40-60% 짧은 수명을 예상하십시오.</li>
<li><strong>어댑터:</strong> 플라스틱 인클로저가 열을 더 가둡니다. 일반적인 수명: 30,000h.</li>
</ul>

<h3>2. 전압 스파이크와 서지</h3>
<p>계통 전압 변동(특히 신흥 시장)은 입력 커패시터와 MOV에 스트레스를 줍니다. AC 190-264V 정격 드라이버는 280V 과도 현상을 한두 번은 견딜 수 있지만, 반복되는 서지는 정상 마모보다 빠르게 부품을 열화시킵니다.</p>

<h3>3. 정격 부하 근처 운전</h3>
<p>정격 부하의 90-100%에서 출력 커패시터를 통과하는 리플 전류가 증가합니다. 이는 더 많은 열을 발생시키고 노화를 가속합니다. CHUGAO에서 권장하는 규칙:</p>

<div class="highlight">
<strong>부하 와트수 &times; 1.25 = 드라이버 최소 정격.</strong><br>
드라이버를 95%가 아니라 70-80% 용량으로 운전하면 실효 수명을 30-50% 늘릴 수 있습니다.
</div>

<h2>용도별로 필요한 것</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">용도</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">권장 드라이버</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">예상 사용 수명</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">이유</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">소매 사인(1일 8-12시간)</td><td style="padding:10px 14px;border:1px solid var(--b)">어댑터／실내 IP20</td><td style="padding:10px 14px;border:1px solid var(--b)">8-12년</td><td style="padding:10px 14px;border:1px solid var(--b)">하루 가동 시간이 짧아 단위 수명의 짧음을 상쇄</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">옥외 파사드 조명(1일 12시간 이상)</td><td style="padding:10px 14px;border:1px solid var(--b)">IP67 방수</td><td style="padding:10px 14px;border:1px solid var(--b)">10-14년</td><td style="padding:10px 14px;border:1px solid var(--b)">밀봉 포팅이 습도와 온도 변화를 감당</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">산업 24/7(창고)</td><td style="padding:10px 14px;border:1px solid var(--b)">IP65 방우 또는 산업용 CGS</td><td style="padding:10px 14px;border:1px solid var(--b)">5-7년</td><td style="padding:10px 14px;border:1px solid var(--b)">연속 고온 운전이 마모를 가속</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">해양／분수</td><td style="padding:10px 14px;border:1px solid var(--b)">IP68 등급 모델</td><td style="padding:10px 14px;border:1px solid var(--b)">8-12년</td><td style="padding:10px 14px;border:1px solid var(--b)">완전 침수 등급, 염수 분무 시험 완료</td></tr>
</tbody>
</table>

<h2>CHUGAO의 시험 방식</h2>

<p>모든 CHUGAO 드라이버는 출하 전 <strong>48시간 번인 시험</strong>을 거칩니다. 불합격품은 폐기되며 공장을 떠나지 않습니다. 이 출하 전 스크리닝이 초기 고장(욕조 곡선의 조기 고장 구간)을 잡아냅니다.</p>

<p>500개를 초과하는 OEM 주문의 경우, 발주서에 명시하면 추가 비용 없이 연장 번인(72-168시간) 옵션을 제공합니다.</p>

<h2>빠른 결정 가이드</h2>

<ol>
<li><strong>하루 가동 시간?</strong> 소매 8시간과 산업 24시간은 전혀 다릅니다. 목표 프로젝트 수명에 하루 시간을 곱해 총 시간 요구량을 구하십시오.</li>
<li><strong>주변 온도?</strong> 40&deg;C를 초과해 10&deg;C마다 수명이 약 50% 줄어듭니다. 모델 선정에 반영하십시오.</li>
<li><strong>통기?</strong> 밀폐 기구는 IP67 이상이 필요합니다. 통기되는 하우징은 IP20/65로 가능합니다.</li>
<li><strong>여유?</strong> 항상 25%를 더하십시오. 고장품 교체를 위한 현장 방문에 비하면 60W와 100W 드라이버의 가격 차이는 미미합니다.</li>
<li><strong>예비 재고?</strong> 24/7 설치에는 5-10%의 예비 드라이버를 보유하십시오. 긴급 배송보다 저렴합니다.</li>
</ol>

<div class="cta-box">
<h3>어떤 드라이버가 수명 요구에 맞는지 모르시겠습니까?</h3>
<p>용도, 하루 가동 시간, 주변 조건을 알려 주십시오. 설치에 맞는 시리즈와 현실적인 기대 수명을 추천해 드립니다.</p>
<a href="/#inquiry" class="btn">수명 맞춤 추천 받기</a>
</div>


<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">모든 정격에 MTBF 데이터를 제공하는 장수명 어댑터.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">상업 및 건축 기구용 L70 등급 드라이버.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">옥외 사용 수명 연장을 위한 포팅 밀봉.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">50,000시간 이상 옥외 운전을 위해 설계된 견고한 드라이버.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a>
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20·IP65·IP67·IP68 선택법</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">업계 동향</span><span class="rel-title">2026 LED 시장: 우리가 보고 있는 것</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">규제</span><span class="rel-title">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-4/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">LED 드라이버 BIS 인증: 인도 수입 가이드</span></a><a class="pn-next" href="/blog-6/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">IP67 vs IP65 LED 드라이버: 어떤 등급이 필요하십니까?</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-9'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>정전압 vs 정전류 LED 드라이버: 어느 것이 필요하십니까?</h1>
<div class="meta">기술 가이드 &middot; 2026년 9월 &middot; 약 8분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="정전압 및 정전류 LED 드라이버를 나란히 놓은 사진" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 기구가 아예 켜지느냐를 결정하는 두 단어가 있습니다——<strong>정전압</strong>과 <strong>정전류</strong>. 이 둘을 바꿔 쓰면 LED는 켜지지 않거나 며칠 만에 타 버립니다. 그런데 대부분의 구매자는 기구가 고장 난 뒤에야 이 용어를 접합니다. 그래서 모든 사양서 맨 앞에 인쇄되었으면 하는 짧은 설명을 여기 정리합니다.</p>

<h2>“정전압”의 의미</h2>

<p>정전압(CV) 드라이버는 출력 전압을 일정하게 유지하며——보통 12V, 24V, 36V, 48V——얼마의 전류를 끌어올지는 기구가 결정합니다. LED 스트립, 사인 모듈, 그리고 대부분의 “12V/24V” 제품은 자체 전류 제한 저항을 갖고 있어 고정 전압 공급이 필요합니다. 장식·건축·사인 작업의 대다수에서 이것이 기본입니다.</p>

<div class="highlight">
<strong>경험 법칙:</strong> 제품 라벨에 <strong>12V</strong> 또는 <strong>24V</strong>라고 되어 있으면 정전압 드라이버가 필요합니다. 전압은 드라이버가 정하고, 전류는 스트립이 정합니다.
</div>

<h2>“정전류”의 의미</h2>

<p>정전류(CC) 드라이버는 전류를 일정하게 유지하며——보통 350mA, 500mA, 700mA, 1050mA, 1500mA——LED의 순방향 전압이 온도에 따라 변해도 그 전류를 일정하게 유지하도록 전압을 바꿉니다. 나전 고출력 LED(다운라이트, 투광등, 가로등, 하이베이 모듈)는 기판상 안정화가 없어 고정 전압원에 연결하면 폭주 전류를 끌어와 스스로를 태웁니다. CC 드라이버가 필요합니다.</p>

<p>라벨에 <strong>350 mA</strong> 또는 <strong>700 mA</strong>라고 되어 있으면 정전류가 필요합니다. 기구 사양을 알려 주시면 맞춰 드립니다.</p>

<h2>두 가지 나란히 비교</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">속성</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">정전압</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">정전류</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">유지하는 출력</td><td style="padding:10px 14px;border:1px solid var(--b)">전압(12/24/36/48V)</td><td style="padding:10px 14px;border:1px solid var(--b)">전류(350-1500mA)</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">구동 대상</td><td style="padding:10px 14px;border:1px solid var(--b)">스트립, 모듈, 사인</td><td style="padding:10px 14px;border:1px solid var(--b)">나전 고출력 LED, 다운라이트</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">기판상 안정화</td><td style="padding:10px 14px;border:1px solid var(--b)">LED 제품 쪽</td><td style="padding:10px 14px;border:1px solid var(--b)">드라이버 쪽</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">CHUGAO 대표 라인</td><td style="padding:10px 14px;border:1px solid var(--b)"><a href="/products/adapters/">어댑터 5-200W</a>, <a href="/products/indoor/">실내 50-400W</a></td><td style="padding:10px 14px;border:1px solid var(--b)">실내／IP67(요청 시)</td></tr>
</tbody>
</table>

<h2>혼용하면 기구가 망가지는 이유</h2>

<ol>
<li><strong>정전압 드라이버를 정전류 LED에</strong>——LED는 끌어올 수 있는 만큼 전류를 끌어와 발열하고 타 버립니다. 가장 흔한 것은 12V 스트립용 전원을 350mA 다운라이트에 재사용하는 경우입니다.</li>
<li><strong>정전류 드라이버를 정전압 스트립에</strong>——드라이버는 스트립의 저항으로 제한할 수 없는 전류를 밀어 넣어, 스트립이 과열되거나 드라이버가 고장 납니다. 어느 쪽이든 불이 들어오지 않습니다.</li>
</ol>

<p>무엇이든 전원을 넣기 전에 반드시 기구 라벨을 읽으십시오. 조금이라도 의문이 있으면 라벨 사진을 보내 주시면 어떤 타입이 필요한지 알려 드립니다.</p>

<h2>드라이버 하나로 둘 다 가능합니까?</h2>

<p>일부 프로그래머블 또는 “듀얼 모드” 드라이버는 고정 출력에서 CV 또는 CC로 설정할 수 있지만, 더 비싸고 거의 필요하지 않습니다. 표준 설치에서는 올바른 타입을 한 번 고르면 현장 재방문을 피할 수 있습니다. 당사의 <a href="/products/indoor/">실내 드라이버</a>와 <a href="/products/ip67/">IP67 드라이버</a>는 고출력 기구 작업용으로 100W부터 정전류 버전을 제공합니다.</p>

<h2>필요한 정보</h2>

<p>기구 라벨(볼트 단위 전압 또는 밀리암페어 단위 전류), 총 와트수, 설치 위치, 수량을 보내 주십시오. 정전압인지 정전류인지 확인하고 정확한 모델을 견적해 드립니다——그리고 더 저렴한 기성품으로 정말 충분한 경우도 알려 드립니다.</p>

<div class="cta-box">
<h3>기구가 CV인지 CC인지 확실하지 않으십니까?</h3>
<p>LED 라벨 사진을 보내 주십시오——볼트 단위 전압 또는 밀리암페어 단위 전류. 타입을 확인하고 정확한 모델을 견적해 드립니다.</p>
<a href="/#inquiry" class="btn">CV인지 CC인지 확인</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 사인용 소형 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">천장등과 패널등용 액티브 PFC 정전압.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">습윤·해안 현장용 완전 포팅, 염수 분무 시험 완료.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">사인과 반옥외 설치용 통기 금속 케이스.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a><a class="rel-card" href="/blog-7/"><span class="rel-cat">구매 가이드</span><span class="rel-title">12V 또는 24V: LED 전원 어떻게 선택할까</span></a><a class="rel-card" href="/blog-8/"><span class="rel-cat">기술 가이드</span><span class="rel-title">LED 전원 용량 정하기: 와트·여유·돌입전류</span></a><a class="rel-card" href="/blog-10/"><span class="rel-cat">기술 가이드</span><span class="rel-title">LED 드라이버 조광 설명: 0-10V, PWM, DALI &amp; TRIAC</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-8/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">LED 전원 용량 정하기: 와트·여유·돌입전류</span></a><a class="pn-next" href="/blog-10/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">LED 드라이버 조광 설명: 0-10V, PWM, DALI &amp; TRIAC</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-10'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>LED 드라이버 조광 설명: 0-10V, PWM, DALI &amp; TRIAC</h1>
<div class="meta">기술 가이드 &middot; 2026년 9월 &middot; 약 9분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="LED 드라이버 조광 표준 비교" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>LED 설치의 조광은 설정이어야지 연구 프로젝트여서는 안 됩니다. 실제로 잘못되는 이유는 네 가지 조광 표준이 같은 배선을 공유하는데 어느 것도 호환되지 않기 때문입니다. 각각이 무엇이고, 제어가 실제로 조광되도록 무엇을 지정해야 하는지 설명합니다.</p>

<h2>네 가지 표준, 알기 쉽게</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">표준</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">작동 방식</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">최적 용도</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>0-10V</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">별도의 저전압 제어 쌍이 10V에서 100%, 0V에서 약 10%까지 설정</td><td style="padding:10px 14px;border:1px solid var(--b)">상업용 천장, 신축</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>PWM</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">DC 측 펄스폭 변조. 매우 매끄럽고 색 이동 없음</td><td style="padding:10px 14px;border:1px solid var(--b)">사인, 카메라에 민감한 현장</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>DALI</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">디지털 어드레서블 버스. 각 기구를 주소 지정하고 기록</td><td style="padding:10px 14px;border:1px solid var(--b)">대형 스마트 빌딩</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>TRIAC</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">위상 제어. 기존 상용 조광기를 활용(리딩/트레일링 에지)</td><td style="padding:10px 14px;border:1px solid var(--b)">리모델링, 기존 벽면 조광기</td></tr>
</tbody>
</table>

<h2>0-10V: 상업용 기본</h2>

<p>0-10V는 신축 상업 인테리어에서 가장 흔한 사양입니다. 배선이 간단하고 저렴하기 때문입니다——저전압 도체 2가닥이 추가될 뿐 데이터는 필요 없습니다. 문제는 약 10%까지만 조광되고 완전 소등은 되지 않는다는 점입니다(“오프”를 위해 상용 릴레이를 추가하지 않는 한). 진정한 소등이 필요하면 사양에 명시하십시오.</p>

<h2>PWM: 가장 매끄럽고 사인에 최적</h2>

<p>PWM 조광은 DC 출력을 고주파로 잘게 자릅니다. 전류 레벨을 바꾸지 않으므로 조광해도 색온도 이동이 없습니다——<a href="/products/ip65/">사인</a>과 플리커가 허용되지 않는 카메라·방송 환경에서 중요합니다. PWM은 DC 측에 있으므로 정전압 드라이버와 짝을 이룹니다.</p>

<h2>DALI: 어드레서블 빌딩 제어</h2>

<p>DALI는 각 기구를 고유 주소를 가진 2선 디지털 버스에 올리므로, 빌딩 관리 시스템이 구역 조광, 고장 기록, 장면 호출을 할 수 있습니다. 드라이버와 시운전 비용은 더 들지만, 20층 사무실이라면 인건비로 회수됩니다. 당사는 <a href="/products/indoor/">실내 드라이버</a>에서 100W부터 DALI 버전을 공급합니다.</p>

<h2>TRIAC: 재배선 없는 리모델링</h2>

<p>TRIAC(위상 제어) 조광은 LED 드라이버가 기존 상용 벽면 조광기를 활용하게 해주므로, 리모델링에서 새 제어 케이블을 끌 필요가 없습니다. 함정은 모든 LED 드라이버가 TRIAC 호환인 것은 아니며, 저렴한 조광기는 저역에서 웅웅거리거나 떨어진다는 점입니다. 트레일링 에지(ELV) 조광기와, 명시적으로 호환 정격인 드라이버를 사용하십시오.</p>

<div class="highlight">
<strong>호환성 우선:</strong> “조광 가능 LED”는 <em>드라이버</em>가 조광기의 언어를 말할 때만 조광됩니다. 사용하는 조광기 또는 제어 시스템을 알려 주시면 주문 전에 호환성을 확인합니다——일부 실내 및 IP67 모델은 100W부터 0-10V, PWM, TRIAC을 지원합니다. 가장 작은 어댑터는 조광되지 않습니다.
</div>

<h2>우리가 보는 세 가지 실수</h2>

<ol>
<li><strong>“조광 가능” 스트립과 비조광 드라이버를 산다.</strong>조광은 드라이버가 하며 스트립이 아닙니다.</li>
<li><strong>TRIAC 조광기와 0-10V 드라이버를 혼용한다.</strong>같은 시스템이 아니며, 결과는 플리커 또는 무조광입니다.</li>
<li><strong>제어 케이블을 잊는다.</strong>0-10V와 DALI는 설치 시 전용 한 쌍을 끌어야 하며 나중에는 안 됩니다.</li>
</ol>

<h2>필요한 정보</h2>

<p>조광기 또는 제어 시스템 모델, 부하 와트수, 출력 전압, 그리고 현장이 신축인지 리모델링인지 보내 주십시오. 조광 표준과 적합한 모델(0-10V, PWM, DALI 또는 TRIAC)을 확인합니다.</p>

<div class="cta-box">
<h3>실제로 조광되는 드라이버가 필요하십니까?</h3>
<p>조광기 또는 제어 시스템, 부하, 전압을 알려 주십시오. 조광 표준과 적합한 모델을 확인합니다.</p>
<a href="/#inquiry" class="btn">조광 타입 확인</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 사인용 소형 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">천장등과 패널등용 액티브 PFC 정전압.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">습윤·해안 현장용 완전 포팅, 염수 분무 시험 완료.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">사인과 반옥외 설치용 통기 금속 케이스.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-11/"><span class="rel-cat">구매 가이드</span><span class="rel-title">역률 보정 및 플리커 프리 LED 드라이버</span></a><a class="rel-card" href="/blog-9/"><span class="rel-cat">기술 가이드</span><span class="rel-title">정전압 vs 정전류 LED 드라이버: 어느 것이 필요하십니까?</span></a><a class="rel-card" href="/blog-6/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP67 vs IP65: 어떤 방수 LED 구동장치를 선택해야 할까?</span></a><a class="rel-card" href="/blog-1/"><span class="rel-cat">LED 기술</span><span class="rel-title">3단계로 올바른 LED 전원 고르기</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-9/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">정전압 vs 정전류 LED 드라이버: 어느 것이 필요하십니까?</span></a><a class="pn-next" href="/blog-11/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">역률 보정 및 플리커 프리 LED 드라이버</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-11'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>역률 보정 및 플리커 프리 LED 드라이버</h1>
<div class="meta">구매 가이드 &middot; 2026년 9월 &middot; 약 7분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-indoor.avif"><source type="image/webp" srcset="/images/product-indoor.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-indoor.jpg" alt="역률 및 플리커 프리 LED 드라이버 사양" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>“역률”과 “플리커”는 소매 박스에는 절대 나오지 않지만 설치가 검사를 통과할지, 사람에게 두통을 줄지를 결정하는 두 가지 사양입니다. 둘 다 드라이버 단계에서 정해지므로, 구매자가 실제로 요구해야 할 것을 정리합니다.</p>

<h2>역률: 전력회사가 신경 쓰는 이유</h2>

<p>역률(PF)은 사용하는 유효 전력과 계통에서 끌어오는 총 전력의 비율입니다. PF 0.5의 저렴한 드라이버는 필요한 전류의 두 배를 끌어와 배선을 과부하시키고 상업용 빌딩에서 한계를 초과하게 합니다. 많은 지역에서 이제 5W 이상에서 PF 0.9 이상을 요구하며, EN 61000-3-2는 바로 이 이유로 고조파 한계를 정합니다.</p>

<div class="highlight">
<strong>액티브 PFC 대 패시브:</strong> 당사의 <a href="/products/indoor/">실내 드라이버</a>는 <strong>액티브 PFC</strong>를 사용하여 부하 범위 전반에서 PF 0.95+에 도달합니다——전부하에서만 도움이 되는 패시브 “역률 보정” 스티커가 아닙니다. 200대 천장에서는 이것이 깨끗한 분전반과 차단기가 떨어지는 것의 차이입니다.
</div>

<h2>플리커: 사람이 신경 쓰는 이유</h2>

<p>LED 플리커는 드라이버의 DC 출력 리플에서 발생합니다. 저렴한 드라이버는 리플을 20-30%까지 허용하는데, 육안으로는 못 잡을 수 있지만 카메라, 센서, 그리고 일부 사람은 확실히 느낍니다——영상의 띠, CCTV의 스트로브, 사무실의 눈 피로로 나타납니다. 양질의 드라이버는 리플을 5-8% 미만으로 유지하고 “플리커 프리”로 표기됩니다.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">증상</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">원인</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">해결</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">카메라／CCTV 띠</td><td style="padding:10px 14px;border:1px solid var(--b)">출력 리플 과다</td><td style="padding:10px 14px;border:1px solid var(--b)">플리커 프리, 리플 &lt;8%</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">부하 시 차단기 트립</td><td style="padding:10px 14px;border:1px solid var(--b)">낮은 역률</td><td style="padding:10px 14px;border:1px solid var(--b)">액티브 PFC, PF 0.95+</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">조광 시 웅웅거림</td><td style="padding:10px 14px;border:1px solid var(--b)">조광 불일치</td><td style="padding:10px 14px;border:1px solid var(--b)">일치하는 조광 표준(조광 가이드 참조)</td></tr>
</tbody>
</table>

<h2>플리커 프리가 타협 불가인 곳</h2>

<ul>
<li><strong>사무실과 학교</strong>——종일 노출. 열등한 드라이버는 피로 불만을 유발합니다.</li>
<li><strong>소매와 박물관</strong>——플리커는 제품 색과 촬영을 망칩니다.</li>
<li><strong>CCTV와 교통 허브</strong>——띠가 번호판과 얼굴을 판독 불가로 만듭니다.</li>
<li><strong>카메라가 비추는 모든 현장</strong>——휴대폰으로 찍는다면 플리커 프리를 지정하십시오.</li>
</ul>

<h2>데이터시트 읽는 법</h2>

<ol>
<li><strong>PF:</strong> 100%에서만이 아니라 부하 전반의 수치를 요구하십시오. 액티브 PFC는 높게 유지하고 패시브는 못 합니다.</li>
<li><strong>리플／플리커 비율:</strong> 대부분의 사양 작성자가 쓰는 SVM 지표로 8% 미만이 “플리커 프리”.</li>
<li><strong>THD</strong>(총 고조파 왜곡): 낮을수록 공급 측이 깨끗합니다. 액티브 PFC 드라이버는 EN 61000-3-2 한계를 크게 밑돕니다.</li>
</ol>

<p>모든 CHUGAO 실내 및 IP67 드라이버는 PF 0.95+와 플리커 프리 출력을 유료 옵션이 아니라 표준으로 제조됩니다. 귀하의 시장에 특정 고조파 한계가 있으면 알려 주십시오. 배치에 시험 성적서를 첨부해 공급합니다.</p>

<h2>필요한 정보</h2>

<p>현장 유형(사무실, 소매, CCTV 설치), 와트수와 전압, 그리고 현지 PF／고조파 한계를 보내 주십시오. 이를 통과하는 드라이버를 확인하고 주문 전에 보고서를 보내 드립니다.</p>

<div class="cta-box">
<h3>사무실이나 카메라 현장용 사양입니까?</h3>
<p>현장 유형, 와트수, 현지 PF／고조파 한계를 보내 주십시오. 플리커 프리 고PF 드라이버를 확인하고 시험 성적서를 제공합니다.</p>
<a href="/#inquiry" class="btn">깨끗한 드라이버 사양 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 사인용 소형 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">천장등과 패널등용 액티브 PFC 정전압.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">습윤·해안 현장용 완전 포팅, 염수 분무 시험 완료.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">사인과 반옥외 설치용 통기 금속 케이스.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-10/"><span class="rel-cat">기술 가이드</span><span class="rel-title">LED 드라이버 조광 설명: 0-10V, PWM, DALI &amp; TRIAC</span></a><a class="rel-card" href="/blog-5/"><span class="rel-cat">기술 심층</span><span class="rel-title">LED 드라이버 수명: MTBF, L70 및 실제 수명</span></a><a class="rel-card" href="/blog-9/"><span class="rel-cat">기술 가이드</span><span class="rel-title">정전압 vs 정전류 LED 드라이버: 어느 것이 필요하십니까?</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20 vs IP65 vs IP67 vs IP68</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-10/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">LED 드라이버 조광 설명: 0-10V, PWM, DALI &amp; TRIAC</span></a><a class="pn-next" href="/blog-12/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">LED 드라이버 서지 보호: 낙뢰와 과도 현상</span></a></nav>
</main>"""


BLOG_BODY['ko']['blog-12'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; 현장 노트로 돌아가기</a>

<h1>LED 드라이버 서지 보호: 낙뢰와 과도 현상</h1>
<div class="meta">기술 가이드 &middot; 2026년 9월 &middot; 약 7분 소요</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/product-waterproof.avif"><source type="image/webp" srcset="/images/product-waterproof.webp" sizes="(max-width:768px) 100vw, 800px"><img src="/images/product-waterproof.jpg" alt="서지 보호 기능이 있는 IP67 방수 LED 드라이버" loading="lazy" style="width:100%;aspect-ratio:4/3"></picture>
</div>


<p>세 블록 떨어진 낙뢰가 멀쩡한 LED 드라이버를 죽일 수 있습니다. 서지 보호는 드라이버가 폭풍을 견디느냐 전자 폐기물이 되느냐를 가르는 차이입니다——그리고 "품질" 탓으로 돌려지는 대부분의 고장은 사실 보호되지 않은 입력단일 뿐입니다. 무엇이 실제로 드라이버를 지키는지 정리합니다.</p>

<h2>서지는 어디서 오는가</h2>

<ul>
<li><strong>낙뢰</strong>——직격이 아니어도 긴 옥외 배선에 수 킬로볼트 스파이크를 유도합니다.</li>
<li><strong>개폐 동작</strong>——접촉기, 엘리베이터, 대형 모터가 같은 피더에 과도 현상을 쏟아냅니다.</li>
<li><strong>유도성 킥</strong>——릴레이 하나가 열려도 수백 볼트 스파이크가 생깁니다.</li>
</ul>

<p>깨끗한 건물 전원에 연결된 실내 드라이버는 이를 거의 겪지 않습니다. 긴 케이블의 옥외·<a href="/products/ip67/">습윤 현장 드라이버</a>는 끊임없이 겪습니다. 그래서 서지 정격은 IP 이야기의 일부이지, 별개가 아닙니다.</p>

<h2>중요한 두 계층</h2>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">계층</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">역할</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">일반 정격</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">내장 MOV</td><td style="padding:10px 14px;border:1px solid var(--b)">드라이버 내부에서 소형 과도를 클램프</td><td style="padding:10px 14px;border:1px solid var(--b)">2-4 kV 차동</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)">외부 SPD</td><td style="padding:10px 14px;border:1px solid var(--b)">인입점에서 큰 낙뢰를 흡수</td><td style="padding:10px 14px;border:1px solid var(--b)">10-20 kV, IEC 61643 기준</td></tr>
</tbody>
</table>

<div class="highlight">
<strong>핵심:</strong> 드라이버 내부 서지 클램프는 일상적인 노이즈를 처리합니다. 실제 낙뢰에는 공급 인입부의 <strong>외부 서지 보호 장치(SPD)</strong>가 필요합니다. 방열과 비용에 맞춰 설계된 드라이버 중 수천 암페어 낙뢰를 혼자 감당할 수 있는 것은 없기 때문입니다.
</div>

<h2>뇌우가 잦은 현장을 위한 사양</h2>

<ol>
<li><strong>옥외·해안 배선에는 포팅 IP67 드라이버</strong>를 선택하십시오——밀폐 케이스는 습기로 인한 고장의 첫 방어선이기도 합니다.</li>
<li><strong>인입부에 SPD 추가</strong>——조명에 전원을 공급하는 분전반에 Type 2 서지 어레스터를.</li>
<li><strong>케이블을 지면에서 띄우고</strong> 가능하면 전원선에서 멀리 두십시오. 평행 배선은 유도 스파이크를 부릅니다.</li>
<li><strong>함체를 확실히 접지하십시오</strong>. 접지되지 않은 드라이버는 낙뢰를 안전하게 배출할 수 없습니다.</li>
</ol>

<h2>흔한 서지 오해</h2>

<ul>
<li><strong>"IP67이면 서지도 막아 준다."</strong> 아닙니다——IP는 물의 문제이고 볼트의 문제가 아닙니다. 별개의 사양이므로 둘 다 사야 합니다.</li>
<li><strong>"드라이버 하나를 보호하면 열 전체가 보호된다."</strong> 낙뢰는 케이블을 타고 이동합니다. 한 대가 아니라 인입부를 보호하십시오.</li>
<li><strong>"실내는 안전하다."</strong> 엘리베이터나 압축기와 같은 피더를 쓰는 실내 드라이버도 개폐 스파이크를 겪습니다——내장 클램프 정격을 확인하십시오.</li>
</ul>

<p>당사의 <a href="/products/ip67/">IP67 방수 드라이버</a>와 <a href="/products/ip65/">IP65 방우 드라이버</a>는 내부 서지 클램프를 표준으로 갖추고 있습니다. 노출된 현장에서는 공급부의 외부 SPD를 권장하며 함께 선정해 드립니다.</p>

<h2>필요한 정보</h2>

<p>현장(옥상, 해안, 내륙), 케이블 길이, 그리고 분전반에 SPD가 이미 있는지 알려 주십시오. 드라이버 서지 정격과 추가해야 할 외부 보호를 확인해 드립니다.</p>

<div class="cta-box">
<h3>옥외나 해안 현장을 보호하십니까?</h3>
<p>현장, 케이블 길이, 분전반의 SPD 유무를 보내 주십시오. 서지 정격과 추가할 외부 보호를 확인해 드립니다.</p>
<a href="/#inquiry" class="btn">서지 계획 받기</a>
</div>

<section class="product-crosslink" aria-label="관련 제품"><h2 class="related-h">CHUGAO 제품 살펴보기</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">LED 어댑터 5-200W</span><span class="pc-desc">스트립, 모듈, 사인용 소형 12V/24V 유닛.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">실내 LED 드라이버 50-400W</span><span class="pc-desc">천장등과 패널등용 액티브 PFC 정전압.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">IP67 방수 드라이버 10-400W</span><span class="pc-desc">습윤·해안 현장용 완전 포팅, 염수 분무 시험 완료.</span></a><a class="pc-card" href="/products/ip65/"><span class="pc-title">IP65 방우 드라이버 100-600W</span><span class="pc-desc">사인과 반옥외 설치용 통기 금속 케이스.</span></a></div></section>

<section class="related" aria-label="관련 글">
  <h2 class="related-h">더 많은 현장 노트</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-6/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP67 vs IP65: 어떤 방수 LED 구동장치를 선택해야 할까?</span></a><a class="rel-card" href="/blog-13/"><span class="rel-cat">구매 가이드</span><span class="rel-title">옥외 및 혹독한 현장용 LED 전원 선택</span></a><a class="rel-card" href="/blog-2/"><span class="rel-cat">기술 가이드</span><span class="rel-title">IP20 vs IP65 vs IP67 vs IP68</span></a><a class="rel-card" href="/blog-11/"><span class="rel-cat">구매 가이드</span><span class="rel-title">역률 보정 및 플리커 프리 LED 드라이버</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="글 탐색"><a class="pn-prev" href="/blog-11/" rel="prev"><span class="pn-lab">이전 글</span><span class="pn-t">역률 보정 및 플리커 프리 LED 드라이버</span></a><a class="pn-next" href="/blog-13/" rel="next"><span class="pn-lab">다음 글</span><span class="pn-t">옥외 및 혹독한 현장용 LED 전원 선택</span></a></nav>
</main>"""
