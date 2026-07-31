// extract_i18n.cjs
// Reads main.js and extracts the i18n dictionary (T) and META map into i18n.json
// so the Python build script can translate pages without fragile regex on JS.
const fs = require('fs');

const mainJs = process.argv[2] || 'main.js';
const out = process.argv[3] || 'i18n.json';
const src = fs.readFileSync(mainJs, 'utf8');

// Brace-counting object extractor (string-safe)
function extractObject(s, startIdx) {
  let i = startIdx, depth = 0, inStr = false, strCh = '', esc = false;
  for (; i < s.length; i++) {
    const c = s[i];
    if (inStr) {
      if (esc) esc = false;
      else if (c === '\\') esc = true;
      else if (c === strCh) inStr = false;
      continue;
    }
    if (c === '"' || c === "'") { inStr = true; strCh = c; continue; }
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) return s.slice(startIdx, i + 1); }
  }
  return null;
}

const LANGS = ['en','zh','es','fr','de','pt','ru','ja','ko','ar','it'];
const T = {};
for (const lang of LANGS) {
  const re = new RegExp('T\\.' + lang + '\\s*=\\s*\\{');
  const m = re.exec(src);
  if (!m) { console.error('WARN: T.' + lang + ' not found'); continue; }
  const objText = extractObject(src, m.index + m[0].indexOf('{'));
  if (!objText) { console.error('WARN: could not extract T.' + lang); continue; }
  try { T[lang] = eval('(' + objText + ')'); }
  catch (e) { console.error('ERR eval T.' + lang + ': ' + e.message); }
}

// META
const META = {};
const mm = /var\s+META\s*=\s*\{/.exec(src);
if (mm) {
  const metaText = extractObject(src, mm.index + mm[0].indexOf('{'));
  if (metaText) { try { Object.assign(META, eval('(' + metaText + ')')); } catch(e){ console.error('ERR eval META: '+e.message);} }
}

const result = { langs: LANGS, T, META };
fs.writeFileSync(out, JSON.stringify(result, null, 1));
console.log('Extracted', Object.keys(T).length, 'languages, META keys:', Object.keys(META).length);
