import os

# 25 generated files that still have 2-3 non-lazy <img> each
files = [
    "ar/index.html", "de/index.html", "es/index.html", "fr/index.html",
    "it/index.html", "ja/index.html", "ko/index.html", "pt/index.html",
    "ru/index.html", "zh/index.html", "index.html",
    "blog-1.html", "blog-2.html", "blog-3.html", "blog-4.html", "blog-5.html",
    "products/adapters/index.html", "products/indoor/index.html",
    "products/ip65/index.html", "products/ip67/index.html",
    "src/index.html", "src/products/adapters.html", "src/products/indoor.html",
    "src/products/ip65.html", "src/products/ip67.html",
]

for f in files:
    with open(f, encoding="utf-8") as fh:
        lines = fh.readlines()
    out = []
    for line in lines:
        if "<img" in line and "loading=" not in line:
            line = line.replace("<img", '<img loading="lazy"', 1)
        out.append(line)
    with open(f, "w", encoding="utf-8") as fh:
        fh.writelines(out)
    print("patched", f)
