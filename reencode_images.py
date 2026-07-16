# -*- coding: utf-8 -*-
from PIL import Image
import os, glob

base = "images"
# png source -> clean jpg target
mapping = {
    "factory.jpg.png": "factory.jpg",
    "product-adapter.png": "product-adapter.jpg",
    "product-indoor.png": "product-indoor.jpg",
    "product-waterproof.png": "product-waterproof.jpg",
    "product-rainproof.png": "product-rainproof.jpg",
    "blog-1-led-power-supply.png": "blog-1-led-power-supply.jpg",
    "blog-2-ip-rating.png": "blog-2-ip-rating.jpg",
    "blog-3-led-market.png": "blog-3-led-market.jpg",
}

total_before = total_after = 0
for src, dst in mapping.items():
    sp = os.path.join(base, src)
    dp = os.path.join(base, dst)
    if not os.path.exists(sp):
        print("SKIP (missing):", sp)
        continue
    im = Image.open(sp).convert("RGB")
    im.save(dp, "JPEG", quality=82, optimize=True, progressive=True)
    sb = os.path.getsize(sp); db = os.path.getsize(dp)
    total_before += sb; total_after += db
    print("  %-34s %6.1f KB -> %6.1f KB" % (dst, sb/1024, db/1024))
    os.remove(sp)  # delete original PNG

print("Total PNG: %.1f KB -> JPG: %.1f KB (saved %.1f KB)" % (
    total_before/1024, total_after/1024, (total_before-total_after)/1024))
print("Remaining .png files:", [os.path.basename(f) for f in glob.glob(base + "/*.png")])
