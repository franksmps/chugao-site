# -*- coding: utf-8 -*-
"""Italian body copy for blog-1..5 and blog-9..14.

Extends the 'it' sub-dict declared in blog_body_zh.py (blog-6/7/8). Only NEW
keys -- never re-declare BLOG_BODY['it'] = {}.
AI translation pending native review.
"""


BLOG_BODY['it']['blog-1'] = """<main class="article">
<a href="/blog/" class="back-link">&larr; Torna alle note dal campo</a>

<h1>Scegliere l'alimentatore LED giusto in 3 passi</h1>
<div class="meta">Tecnologia LED &middot; marzo 2026 &middot; 6 min di lettura</div>

<div class="hero-img">
<picture><source type="image/avif" srcset="/images/blog-1-led-power-supply-md.avif 1200w, /images/blog-1-led-power-supply.avif 1024w">
<source type="image/webp" srcset="/images/blog-1-led-power-supply-md.webp 1200w, /images/blog-1-led-power-supply.webp 1024w" sizes="(max-width:768px) 100vw, 800px">
<img src="/images/blog-1-led-power-supply.jpg" alt="Guida alla scelta dell'alimentatore LED" loading="lazy" style="width:100%;aspect-ratio:4/3">
</picture>
</div>

<p>Scegliere un alimentatore LED sembra tecnico, ma si riduce a tre cose: <strong>wattaggio</strong>, <strong>grado IP</strong> e <strong>tensione di ingresso</strong>. Azzecca questi tre e avrai eliminato il 90% dei resi e dei guasti sul campo.</p>

<p>Questa guida spiega esattamente cosa controllare prima di ordinare — scritta dal nostro team tecnico, non da un reparto marketing.</p>

<h2>Passo 1: Abbinare il wattaggio</h2>

<p>L'errore più comune è sottodimensionare. Ecco la regola empirica che usiamo in CHUGAO:</p>

<div class="highlight">
<strong>Wattaggio del carico &times; 1,25 = potenza minima del driver.</strong><br>
Lascia sempre almeno il 25% di margine. Far lavorare un driver al 100% della capacit&agrave; ne accorcia la vita e lo fa scaldare di pi&ugrave;.
</div>

<h3>Esempio</h3>
<p>Se la tua striscia LED assorbe 80W, non comprare un driver da 80W. Compra un'unit&agrave; da 100W (o superiore). La capacit&agrave; extra mantiene l'uscita stabile, riduce il calore e allunga la durata da circa 3 anni a oltre 5.</p>

<h3>Perch&eacute; il margine conta</h3>
<ul>
<li><strong>Temperatura:</strong> i driver lavorano pi&ugrave; freschi sotto il carico nominale. Ogni riduzione di 10&deg;C raddoppia all'incirca la vita dei condensatori.</li>
<li><strong>Tolleranza ai picchi:</strong> le strisce LED possono assorbire brevi picchi all'avvio. Il margine li assorbe senza far scattare le protezioni.</li>
<li><strong>Stabilit&agrave; di tensione:</strong> un driver poco caricato mantiene la tensione d'uscita pi&ugrave; stabile, e quindi una luminosit&agrave; pi&ugrave; costante.</li>
</ul>

<h2>Passo 2: Scegliere il grado IP giusto</h2>

<p>Il codice IP (Ingress Protection) indica quanto il driver resiste a polvere e acqua. &Egrave; qui che la maggior parte dei progetti sbaglia — si risparmiano 2 dollari sul driver e poi lo si sostituisce dopo un temporale.</p>

<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<thead><tr style="background:var(--bg)"><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Grado IP</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Polvere</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Acqua</th><th style="padding:10px 14px;text-align:left;border:1px solid var(--b)">Caso d'uso</th></tr></thead>
<tbody>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP20</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">Nessuna protezione</td><td style="padding:10px 14px;border:1px solid var(--b)">Nessuna protezione dall'acqua</td><td style="padding:10px 14px;border:1px solid var(--b)">Solo interni asciutti</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP65</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">A tenuta di polvere</td><td style="padding:10px 14px;border:1px solid var(--b)">Getto d'acqua (qualsiasi direzione)</td><td style="padding:10px 14px;border:1px solid var(--b)">Esterni esposti, aree lavabili</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP67</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">A tenuta di polvere</td><td style="padding:10px 14px;border:1px solid var(--b)">Immersione fino a 1 m</td><td style="padding:10px 14px;border:1px solid var(--b)">Immersione temporanea, rischio allagamento</td></tr>
<tr><td style="padding:10px 14px;border:1px solid var(--b)"><strong>IP68</strong></td><td style="padding:10px 14px;border:1px solid var(--b)">A tenuta di polvere</td><td style="padding:10px 14px;border:1px solid var(--b)">Immersione continua</td><td style="padding:10px 14px;border:1px solid var(--b)">Apparecchi subacquei, immersione profonda</td></tr>
</tbody>
</table>

<p>Se non sei sicuro, sali di un livello rispetto a quello che pensi ti serva. La differenza di costo tra IP20 e IP65 su un driver da 100W &egrave; di norma inferiore a 3 dollari al prezzo diretto di fabbrica.</p>

<h2>Passo 3: Verificare la compatibilit&agrave; della tensione di ingresso</h2>

<p>Questo &egrave; facile da trascurare ma causa il tasso di reso pi&ugrave; alto:</p>

<ul>
<li><strong>Nord America, Giappone, Taiwan (Cina), Cina continentale:</strong> 110V AC / 60Hz</li>
<li><strong>Europa, Cina continentale, gran parte dell'Asia, Africa:</strong> 220–240V AC / 50Hz</li>
<li><strong>Brasile:</strong> ibrido 127V/220V (verifica la presa locale)</li>
<li><strong>Industriale / marino:</strong> spesso 277V, 380V o 480V trifase</li>
</ul>

<p>I range di ingresso variano per linea. Gli adattatori coprono 100–240V AC; i modelli indoor, IP65 e IP67 coprono 190–264V (IP67 fino a 340V). Controlla il range esatto del tuo modello nella nostra <a href="/#specs">tabella specifiche</a> e verifica che corrisponda alla tensione di rete di destinazione.</p>

<h2>Checklist di riferimento rapido</h2>

<ol>
<li>Somma i watt totali del carico LED &rarr; moltiplica per 1,25 &rarr; arrotonda al formato driver standard pi&ugrave; vicino.</li>
<li>Controlla l'ambiente d'installazione &rarr; interno (IP20), esterno/pioggia (IP65) o rischio immersione (IP67/IP68).</li>
<li>Conferma la tensione di rete del paese di destinazione &rarr; area 110V o area 220V.</li>
<li>Opzionale: ti serve la dimmerazione? (0-10V, PWM, DALI o Triac — specificalo in ordine)</li>
<li>Opzionale: serve la certificazione UL? (aumenta il costo, 2–3 settimane di lead time per modello)</li>
</ol>

<div class="cta-box">
<h3>Non sai quale modello fa per te?</h3>
<p>Inviaci le tue specifiche — wattaggio, quantit&agrave;, porto di destinazione e mercato target. Rispondiamo entro 1 ora negli orari lavorativi con datasheet e preventivo.</p>
<a href="/#inquiry" class="btn">Richiedi un preventivo</a>
</div>


<section class="product-crosslink" aria-label="Prodotti correlati"><h2 class="related-h">Scopri i prodotti CHUGAO</h2><div class="pc-grid"><a class="pc-card" href="/products/adapters/"><span class="pc-title">Adattatori LED 5-200W</span><span class="pc-desc">Adattatori a spina e da tavolo a ingresso universale per insegne e strisce.</span></a><a class="pc-card" href="/products/indoor/"><span class="pc-title">Driver LED indoor 50-400W</span><span class="pc-desc">Driver ad alta efficienza per pannelli, faretti e apparecchi commerciali.</span></a><a class="pc-card" href="/products/ip67/"><span class="pc-title">Driver waterproof IP67 10-400W</span><span class="pc-desc">Alimentatori subacquei per progetti esterni e paesaggistici.</span></a></div></section>

<section class="related" aria-label="Articoli correlati">
  <h2 class="related-h">Altre note dal campo</h2>
  <div class="rel-grid">
  <a class="rel-card" href="/blog-2/"><span class="rel-cat">Guida tecnica</span><span class="rel-title">IP20 vs IP65 vs IP67 vs IP68</span></a>
  <a class="rel-card" href="/blog-3/"><span class="rel-cat">Tendenze di settore</span><span class="rel-title">Mercato LED 2026: cosa stiamo vedendo</span></a>
  <a class="rel-card" href="/blog-4/"><span class="rel-cat">Normativa</span><span class="rel-title">Certificazione BIS per driver LED: guida all'import in India</span></a>
  <a class="rel-card" href="/blog-5/"><span class="rel-cat">Approfondimento</span><span class="rel-title">Durata dei driver LED: MTBF, L70 e vita reale</span></a>
  </div>
</section>

<nav class="post-nav" aria-label="Navigazione articolo"><a class="pn-prev" href="/blog/"><span class="pn-lab">Tutti gli articoli</span><span class="pn-t">Note dal campo</span></a><a class="pn-next" href="/blog-2/" rel="next"><span class="pn-lab">Articolo successivo</span><span class="pn-t">IP20 vs IP65 vs IP67 vs IP68</span></a></nav>
</main>"""
