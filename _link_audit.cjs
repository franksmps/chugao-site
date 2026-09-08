const fs = require('fs'), path = require('path');
const SKIP = new Set(['src', '.git', '__pycache__', 'images', 'node_modules']);
function walk(d, acc = []) {
  for (const f of fs.readdirSync(d)) {
    if (SKIP.has(f)) continue;
    const p = path.join(d, f);
    const s = fs.statSync(p);
    if (s.isDirectory()) walk(p, acc);
    else if (f.endsWith('.html')) acc.push(p);
  }
  return acc;
}
const files = walk('.');
const LANGS = new Set(['zh','es','pt','ru','fr','de','ar','ja','ko','it']);
const en = files.filter(f => {
  const rel = path.relative('.', f).split(path.sep);
  return !(rel.length > 1 && LANGS.has(rel[0]));
});
const inbound = {}, words = {};
for (const f of en) {
  const h = fs.readFileSync(f, 'utf8');
  for (const m of h.matchAll(/href="\/([a-z0-9\-\/]*)\/?"/g)) {
    const l = m[1] || '/';
    if (l.includes('.')) continue;
    inbound[l] = (inbound[l] || 0) + 1;
  }
  const body = h
    .replace(/<script[\s\S]*?<\/script>/g, '')
    .replace(/<style[\s\S]*?<\/style>/g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  words[path.relative('.', f).replace(/\\/g, '/')] = body.split(' ').length;
}
console.log('=== 英文版 内链指向次数（Top 18）===');
Object.entries(inbound).sort((a, b) => b[1] - a[1]).slice(0, 18)
  .forEach(([k, v]) => console.log(String(v).padStart(4), '/' + k));
console.log('内链目标种类:', Object.keys(inbound).length);
console.log('\n=== 英文版 各页正文字数 ===');
Object.entries(words).sort((a, b) => b[1] - a[1])
  .forEach(([k, v]) => console.log(String(v).padStart(6), k));
