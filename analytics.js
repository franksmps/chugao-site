// CHUGAO conversion tracking — GA4 events (decoupled; no build-step dependency)
// Loaded with `defer` after main.min.js on every page.
// Tracks: successful Formspree inquiry submissions (generate_lead) and
// WhatsApp / Email contact-channel clicks (contact_click).
(function () {
  "use strict";
  if (typeof window.gtag !== "function") return;

  // --- Successful inquiry form submission -> GA4 lead -----------------------
  // handleInquiry() in main.min.js posts to Formspree via window.fetch.
  // We wrap fetch globally and inspect Formspree responses, so we never
  // touch the minified handler and stay robust to handler internals.
  if (typeof window.fetch === "function") {
    var _fetch = window.fetch.bind(window);
    window.fetch = function (input, init) {
      var p = _fetch(input, init);
      try {
        var url = typeof input === "string" ? input : (input && input.url) || "";
        if (/formspree\.io|formspree\.com/.test(url)) {
          p.then(function (r) {
            if (r && r.ok) {
              window.gtag("event", "generate_lead", {
                method: "inquiry_form",
                event_category: "lead",
                event_label: "inquiry_form_success"
              });
            }
          }).catch(function () {});
        }
      } catch (e) {}
      return p;
    };
  }

  // --- Contact-channel clicks (WhatsApp / Email) ----------------------------
  document.addEventListener("click", function (e) {
    var t = e.target;
    var a = t && typeof t.closest === "function" ? t.closest("a") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (/wa\.me|web\.whatsapp/.test(href)) {
      window.gtag("event", "contact_click", { method: "whatsapp" });
    } else if (/^mailto:/i.test(href)) {
      window.gtag("event", "contact_click", { method: "email" });
    }
  });
})();
