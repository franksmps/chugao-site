// make_avif.cjs -- convert every raster image in images/ to AVIF.
// Run: NODE_PATH=<node-workspace>/node_modules node make_avif.cjs
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const DIR = 'images';
const SRC_EXT = ['.webp', '.jpg', '.jpeg', '.png'];

(async () => {
  const files = fs.readdirSync(DIR).filter(f => SRC_EXT.includes(path.extname(f).toLowerCase()));
  let totalBefore = 0, totalAfter = 0, n = 0;
  for (const f of files) {
    const src = path.join(DIR, f);
    const dst = path.join(DIR, path.basename(f, path.extname(f)) + '.avif');
    if (fs.existsSync(dst)) continue;            // avoid duplicate-base overwrite
    const before = fs.statSync(src).size;
    const buf = fs.readFileSync(src);
    await sharp(buf).avif({ quality: 55, effort: 4 }).toFile(dst);
    const after = fs.statSync(dst).size;
    totalBefore += before; totalAfter += after; n++;
    console.log(`${f.padEnd(34)} ${(before/1024).toFixed(1)}KB -> ${(after/1024).toFixed(1)}KB`);
  }
  console.log(`Converted ${n} images; ${(totalBefore/1024).toFixed(1)}KB -> ${(totalAfter/1024).toFixed(1)}KB (saved ${(100*(totalBefore-totalAfter)/Math.max(1,totalBefore)).toFixed(0)}%)`);
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
