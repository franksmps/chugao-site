# CHUGAO 网站内容与格式审查报告
日期：2026-07-31
范围：`index.html` + `blog-1~5.html`（对照 `main.js` i18n、`style.css`/`blog.css`、图片资源）
本轮重点：**内容准确性 + 文案/格式一致性**（前几轮已处理 SEO/性能/ accessibility/ 安全头等）。

---

## 一、内容准确性问题（事实冲突，最该先改）

### P0-1 功率区间在「规格表」与「产品卡片/JSON-LD/首页/表单」互相打架 ⚠️
同一产品线在不同位置给出的功率范围不一致，买家会看到矛盾数字，直接损害报价与信任：

| 产品线 | 产品卡片 / JSON-LD / 首页 Hero / 表单 | 规格表（#specs）< | 冲突 |
|---|---|---|---|
| Indoor 室内驱动 | **50W–400W** | **15W–1000W** | 严重冲突 |
| IP67 防水 | **10W–400W** | **24W–400W** | 下沿不一致 |
| IP65 防雨 | **100W–600W** | **400W–1000W** | 严重冲突 |
| Adapters 适配器 | 5W–200W | 5W–200W | 一致 ✓ |

**额外矛盾**：产品卡片里的 SKU 列表也超出标称区间——
- Indoor 标称 50–400W，但列出 `C-500W`（超上限）；
- IP65 标称 100–600W，但列出 `FYG-1000W`（超上限）。

**建议**：以真实产品目录为准，选定每条线**唯一权威区间**，同步改 6 处：规格表、产品卡片正文、产品卡片 `.pt2` 标签、JSON-LD ItemList、首页 Hero 副标题、询单表单下拉项，并裁剪 SKU 列表使其落在区间内。

### P1-1 「12 years in business」与「since 2008」矛盾（文案过时）
- 首页 Hero 统计：`12 years in business`
- Twitter 描述：`12 years, 42 countries`
- 但标题/OG/JSON-LD/foundingDate 均写 `since 2008`（2026−2008 = **18 年**）。

「12 年」看起来是 2020 年写的旧文案没更新。**建议**：统一改为真实年数（目前应为 18，或按实际口径表述）。同时检查全站是否还有其它 «12 years» 残留。

### P1-2 Blog-1 防水等级表：IP20 描述技术错误
Blog-1 的 IP 对照表里写：
> IP20 — Dripping water (vertical)（滴水和垂直落水）

IP20 的第二个数字 «0» = **无防水保护**（第一个数字才是防固体）。能防垂直滴水的是 **IP21**。当前写法会误导买家在潮湿环境用错型号。
**建议**：IP20 改为 «No water protection — indoor dry locations only»（或简写 «Indoor only»）。

### P1-3 Blog-1 电压宣称与规格表冲突
Blog-1 写道：
> «All CHUGAO drivers are available in both 110V and 220V wide-range inputs (typically **90–305V AC universal**).»

但规格表：Indoor 为 `AC 190-264V`、IP67 为 `AC 190-340V`、IP65 为 `AC 190-264V`、Adapters 为 `AC 100-240V`。«90–305V 通用» 比规格表宽得多，前后矛盾。
**建议**：统一措辞——要么规格表改为宽压范围，要么 Blog 改为 «per the specs table for each line»，避免给出无法兑现的通用承诺。

### P2-1 「42 个国家」与 JSON-LD areaServed 仅列 31 个不一致
首页/信任条反复强调 «42 countries shipped to»，但 Organization 结构化数据 `areaServed` 只列了 31 个 ISO 代码。
**建议**：二选一——把 `areaServed` 补全到 42 个，或把文案改为 «30+ countries» 等可核实表述。

### P1-合规 Blog-1 将 Taiwan 作为并列区域列出
Blog-1 第 96 行：
> «North America, Japan, **Taiwan**: 110V AC / 60Hz»

按中国网站表述规范，台湾/香港/澳门应写作 «Taiwan, China» / «中国台湾»，不应作为与主权国家并列的独立区域。
**建议**：改为 «Taiwan, China»，或并入 «most of Asia» 一并说明 220–240V。

---

## 二、格式 / 一致性问题

### P1-格式 博客页仍走 jsDelivr CDN 加载 Twemoji，与首页自托管不一致
- `index.html` 已自托管：`./vendor/twemoji/twemoji.min.js`（commit 8ecb639 的优化）
- 但 `blog-1~5.html` 第 192 行仍写：
  `https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js`

**问题**：① 与首页不一致；② 引入外部依赖，离线/CDN 故障时国旗渲染失败；③ 博客正文无国旗 emoji，那段 `twemoji.parse(document.body)` 其实多余。
**建议**：博客页改为同首页的本地自托管写法（或直接删掉，因为博客正文不需要国旗）。

### P2-格式 规格表有 3 个表头未做国际化
规格表 `<thead>` 里 `Protection`、`Dimming`、`Temp` 三列**没有** `data-i18n`，切换语言时其它列会翻译、这三列保持英文，体验割裂。
**建议**：补 `data-i18n` 并在 `main.js` 的 `T` 里加对应 11 语言文案。

### P2-格式 博客 OG:image 用的是首页工厂图，不是文章配图
`blog-1~5.html` 的 `og:image` 全是 `images/factory.jpg.webp`（首页 Hero），而不是各篇自己的 `blog-N-*.webp`。社交分享（WhatsApp/FB/LinkedIn）缩略图会显示错图。
**建议**：每篇 `og:image` 改为该篇 hero 图（如 `images/blog-1-led-power-supply.webp`）。

### P3-格式 博客内联样式表格，未抽到 blog.css
Blog-1/2 的表格用内联 `style="...border:1px solid var(--b)..."`。功能正常，但不利于统一维护。
**建议**：在 `blog.css` 增加 `.blog-table` 类，正文改用类名。

---

## 三、内容与结构优化建议（增量）

### P2-内容 产品线缺少独立详情页（薄内容）
四条产品线只有首页卡片 + 一句简介，没有独立页面。这也是之前提到的 P2-A（可索引 URL 太少）。
**建议**：新增 `products/adapters.html`、`/indoor.html`、`/ip67.html`、`/ip65.html`，每页含参数表、型号清单、认证、应用场景、询单 CTA，既能丰富内容又利于 SEO。

### P2-内容 Hero 统计 «68 active SKUs» 不可核实
建议在改 P0-1 时一并核对真实在产 SKU 数，避免虚高。

### P3-内容 博客间互链已就位，但可加「本文结论/要点」小结
Blog-1 结尾有 CTA 框，但缺一段 2–3 句的结论性小结，读者扫读时抓不住重点。各篇可加一句 Summary。

---

## 四、执行优先级汇总

| 编号 | 问题 | 优先级 | 影响 |
|---|---|---|---|
| P0-1 | 功率区间全站矛盾 | **P0** | 报价/信任/退换货 |
| P1-1 | 12 年 vs 2008 过时 | P1 | 文案可信度 |
| P1-2 | IP20 技术描述错误 | P1 | 选型误导 |
| P1-3 | 电压 90–305V 与规格表冲突 | P1 | 选型误导 |
| P1-合规 | Taiwan 并列区域 | P1 | 合规 |
| P1-格式 | 博客 Twemoji 仍用 CDN | P1 | 一致性/可用性 |
| P2-1 | 42 国 vs areaServed 31 | P2 | 数据一致 |
| P2-格式 | 规格表 3 列表头未翻译 | P2 | i18n 体验 |
| P2-格式 | 博客 og:image 用错图 | P2 | 社媒分享 |
| P2-内容 | 缺产品独立页 | P2 | SEO/内容 |
| P3 | 博客内联表格 / 缺小结 | P3 | 维护/体验 |

---

## 五、可立即动手的清单（待你确认后我执行）
1. **P0-1**：统一功率区间（需你提供真实产品目录口径，或授权我按现有信息取交集/并集）。
2. **P1-1 / P1-2 / P1-3 / P1-合规 / P2-1**：文案修正（纯文本改动，风险低）。
3. **P1-格式**：博客页 Twemoji 改自托管 / 删除。
4. **P2-格式**：规格表表头补 i18n；博客 og:image 改各自配图。
5. **P2-内容 / P3**：产品独立页、博客小结（工作量较大，建议单独排期）。

> 注：本轮为**审查 + 建议**，未改动任何文件。你确认后我可分批实施；P0-1 需你拍板功率口径。
