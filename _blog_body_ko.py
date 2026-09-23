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
