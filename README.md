# 🛍️ Taobao, Tmall & Alibaba B2B Wholesale Scraper API — Details, Reviews, DSR, SKUs & Factory Tiers (淘宝 / 天猫 / 阿里巴巴)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Zero Login](https://img.shields.io/badge/Account_Required-None-blue?style=for-the-badge)](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba)

**The fastest, cheapest zero-login Taobao (淘宝), Tmall (天猫) & Alibaba.com B2B Wholesale Scraper API suite on Apify ($1.50 / 1,000 items). Dual-Catalog Engine (taobao_retail + mainland_wholesale) extracting 50+ full product detail fields, real customer reviews (with buyer videos), 3-axis Seller DSR ratings, SKU matrices, multi-currency prices (CNY, SGD, HKD, TWD), wholesale tier discounts, and permanent HD photos.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 22 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-taobao-tmall-search-product-catalog-scraper-banner.jpg" alt="🛍️ Taobao, Tmall & Alibaba B2B Wholesale Scraper API — Details, Reviews, DSR, SKUs & Factory Tiers (淘宝 / 天猫 / 阿里巴巴)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's $5 free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, **1-click n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **Taobao & Tmall 淘宝 Product Scraper — Details, Reviews, Prices, SKUs & HD Photos**<br><sub>[`unitbytes/taobao-tmall-scraper`](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba) • [Full Schema](https://unitbytes.com/actors/taobao-tmall-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/how-to-scrape-taobao-tmall-products-prices-reviews-guide/)</sub> | [`examples/run_taobao_tmall_scraper.py`](examples/run_taobao_tmall_scraper.py) | [`n8n/taobao-tmall-scraper-n8n-workflow.json`](n8n/taobao-tmall-scraper-n8n-workflow.json) | [`JSON`](samples/taobao-tmall-scraper-sample.json) · [`CSV`](samples/taobao-tmall-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba) |
| **Alibaba Scraper: Wholesale Products & Factory Finder**<br><sub>[`unitbytes/alibaba-scraper`](https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba) • [Full Schema](https://unitbytes.com/actors/alibaba-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/how-to-scrape-1688-without-account-sourcing-guide/)</sub> | [`examples/run_alibaba_scraper.py`](examples/run_alibaba_scraper.py) | [`n8n/alibaba-scraper-n8n-workflow.json`](n8n/alibaba-scraper-n8n-workflow.json) | [`JSON`](samples/alibaba-scraper-sample.json) · [`CSV`](samples/alibaba-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba) |

- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 22 pre-built scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbook:** Read **[Taobao & Tmall API Pricing in 2026 ($1.50/1K vs. $99/mo RapidAPI & Open.Taobao Limits)](https://unitbytes.com/blog/how-to-scrape-taobao-tmall-products-prices-reviews-guide/)** or browse all scraping & automation guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **Find Products on Alibaba: Wholesale Sourcing Engine** | Search millions of products on Alibaba.com. Extract tiered wholesale volume pricing, MOQ, lead times, and factory audit credentials. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-products-on-alibaba?fpr=939u3w&fp_sid=web_tasks) |
| **Find Verified Suppliers on Alibaba: Factory Audits & B2B Leads** | Extract TÜV Rheinland & SGS audited Verified Suppliers on Alibaba with Trade Assurance, Gold Supplier tenure, and direct contacts. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-verified-suppliers-on-alibaba?fpr=939u3w&fp_sid=web_tasks) |
| **Find Low MOQ Products on Alibaba: Small Batch & Dropshipping** | Discover wholesale items with low minimum order quantities (MOQ ≤ 5) for dropshipping, sample orders, and small-batch private labeling. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-low-moq-products-on-alibaba?fpr=939u3w&fp_sid=web_tasks) |
| **Scrape Alibaba Product URLs: Deep Specs & Volume Pricing** | Deep scrape specific Alibaba.com product URLs to extract tiered volume pricing ladders, full packaging specs, and certified supplier details. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/scrape-alibaba-product-urls?fpr=939u3w&fp_sid=web_tasks) |
| **Find Trending Products on Alibaba: Best Match & High Reviews** | Extract top-rated, trending products on Alibaba.com sorted by customer reviews, supplier credibility, and high-demand wholesale niches. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-trending-products-on-alibaba?fpr=939u3w&fp_sid=web_tasks) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 Taobao & Tmall 淘宝 Product Scraper — Details, Reviews, Prices, SKUs & HD Photos (`unitbytes/taobao-tmall-scraper`)

The fastest, cheapest, and most complete Taobao & Tmall product scraper on Apify ($1.50 / 1,000 items). Extract 50+ full product detail fields, real customer reviews (with buyer videos), 3-axis Seller DSR ratings, SKU matrices, dual-currency prices (CNY, SGD, HKD, TWD), wholesale tier discounts (taobao_retail + mainland_wholesale), and permanent HD photos from Taobao (淘宝) and Tmall (天猫) — Zero Login, Zero Cookies & Zero Chinese Phone Number Required.

- **Pricing:** `$0.0015 / item` ($1.50 per 1,000 items ($0.0015/item) — 3,330+ products free/month with Apify's $5 credit, $0.00 empty-run protection)
- **Cloud Console:** [https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/taobao-tmall-scraper/](https://unitbytes.com/actors/taobao-tmall-scraper/)
- **n8n Workflow File:** [`n8n/taobao-tmall-scraper-n8n-workflow.json`](n8n/taobao-tmall-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Taobao & Tmall API Pricing in 2026 ($1.50/1K vs. $99/mo RapidAPI & Open.Taobao Limits)](https://unitbytes.com/blog/how-to-scrape-taobao-tmall-products-prices-reviews-guide/)

#### Key Capabilities
- **Dual-Catalog Engine (taobao_retail + mainland_wholesale):** Switch between official retail Taobao & Tmall Flagship shops via world.taobao.com (50+ full detail fields with scrapeDetails: true and 100% itemUrls compatibility) and high-speed Mainland Factory Wholesale (~30 items/sec, up to 10,000 items/run with tierPricing, repurchaseRate, businessType, and isSuperFactory).
- **Real Customer Reviews, Buyer Videos & Sentiment Tags:** Extract real customer reviews (buyer comments, dates, purchased SKU variant, user avatars, and buyer video proofs) plus crowd-sourced buyer sentiment tags (reviewTags) and 3-axis Seller DSR ratings (dsrDescription, dsrService, dsrDelivery).
- **Direct Product URL / ID Scraping (itemUrls) & SKU Matrices:** Paste Taobao (item.taobao.com), Tmall (detail.tmall.com), or World Taobao (world.taobao.com) product links or numeric IDs directly into itemUrls, extracting full SKU price/stock matrices (skus, skuCount) and category breadcrumbs (categoryPath).
- **Multi-Currency Pricing & Permanent Shopify-Ready HD Photos:** Automatic cross-border retail pricing (CNY, SGD, HKD, TWD) and unblocked master-resolution image galleries (img.alicdn.com) that never expire or return 403 Forbidden in Shopify, WooCommerce, or Excel.
- **Cheapest Full-Detail Pricing ($0.0015 / item — $1.50 / 1K):** 3x to 10x cheaper than competing scrapers. Extract 3,330+ products completely free every month with Apify's $5 credit, with 100% cross-page deduplication and $0.00 charged on empty runs or unavailable items.

### 🔥 Taobao & Tmall Dual-Catalog Engine (`taobao_retail` + `mainland_wholesale`) & 50+ Field Schema

> 💰 **Cheapest Full-Detail Taobao & Tmall Scraper on Apify Store**: Only **$1.50 per 1,000 items** (`$0.0015/item`) — **3,330+ products free every month** with Apify's $5 credit.

Choose your target catalog directly via the **`catalogSource`** parameter on [`unitbytes/taobao-tmall-scraper`](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba):
- **`taobao_retail` (Default — Taobao & Tmall Retail via `world.taobao.com`)**: Official retail Taobao & Tmall Flagship shops. Supports **Full 50+ Field Detail Extraction (`scrapeDetails: true`, Default)**—including **3-axis Seller DSR Scores** (`dsrDescription`, `dsrService`, `dsrDelivery`), **Real Customer Reviews** (`reviews` with buyer comments, dates, purchased SKU, and buyer video proofs), **Buyer Sentiment Tags** (`reviewTags`), **Category Breadcrumbs** (`categoryPath`), **Full HD Image Galleries** (`images`), and **Multi-Currency Pricing** (`CNY`, `SGD`, `HKD`, `TWD`)—plus **Fast Retail Summary (`scrapeDetails: false`)** (~1s/page). Every `itemId` scraped in retail mode is 100% compatible with **`itemUrls`**.
- **`mainland_wholesale` (Mainland Factory & Wholesale Catalog)**: Ultra-fast, high-volume Mainland factory & B2B search (~30 items/second, up to 10,000 items/run). Extracts 28+ supplier & bulk-sourcing fields in a single pass (`tierPricing` volume discounts, `repurchaseRate`, `isSuperFactory`, `businessType`, `shopAgeYears`, and permanent HD photos).

#### 📊 Key Extracted Columns (`taobao-tmall-scraper`)

| Column Name | Sample Value | What It Tells You |
| :--- | :--- | :--- |
| **`itemId` & `platform`** | `978797368275` (`tmall` / `taobao`) | Unique numeric product ID and marketplace indicator (`tmall` Flagship vs `taobao`). |
| **`price` / `originalPrice`** | `168.0` / `198.0` (`CNY`) | Current promotion price and original list price in Chinese Yuan (`¥ CNY`). |
| **`priceLocal` / `priceHkd` / `priceTwd`** | `31.39` (`SGD`) / `182.5` (`HKD`) / `756.0` (`TWD`) | Automatic multi-currency cross-border retail pricing (`SGD`, `HKD`, `TWD`). |
| **`dsrDescription` / `dsrService` / `dsrDelivery`** | `4.8` / `4.8` / `4.8` | **3-Axis Seller DSR Scores:** Official rating across Description Match, Seller Service, and Shipping Speed. |
| **`reviewCount` / `ratingGoodPercent`** | `200` / `99%` | Total buyer review volume and positive rating percentage. |
| **`reviews`** | `[{"rating": 5, "content": "手機殼質感非常好...", "sku": "...", "videos": []}]` | **Real Customer Reviews:** Buyer comments, dates, purchased SKU variant, user handles, and buyer video proofs. |
| **`reviewTags`** | `[{"tag": "摸起來順手", "count": 40}, {"tag": "質感很高端", "count": 29}]` | **Buyer Sentiment Tags:** Crowd-sourced product pros & cons with buyer vote counts. |
| **`categoryPath`** | `首頁 > 阿裏B2C商城 > 手機及配件 > 保護套/矽膠套` | Full category breadcrumb hierarchy for taxonomy mapping. |
| **`skus` / `skuCount`** | `[{"skuId": "sku_1", "name": "適用iPhone16ProMax...", "price": 168.0, "stock": 999}]` | Extracted SKU variations, option names, variant pricing, and inventory stock. |
| **`tierPricing` & `repurchaseRate`** | `1~199 @ ¥15.0, ≥3000 @ ¥13.5` / `54%` | **Wholesale Mode (`mainland_wholesale`):** Bulk volume discount breaks, buyer repeat rate (`回头率`), `businessType` (`生产加工`), and `isSuperFactory`. |

#### 🏭 Mainland Factory & Wholesale Sample Output (`catalogSource: "mainland_wholesale"`)
```json
{
  "itemId": "1043802302596",
  "title": "适用苹果18ProMax科技布织物手机壳磁吸i phone 17相机按键保护套16",
  "platform": "taobao",
  "url": "https://item.taobao.com/item.htm?id=1043802302596",
  "price": 15.0,
  "currency": "CNY",
  "salesCount": "544",
  "shopName": "深圳市罗湖区洪星电子商行",
  "sellerNick": "深圳洪星生产",
  "shopAgeYears": 5,
  "businessType": "生产加工",
  "isSuperFactory": true,
  "location": "深圳市",
  "mainImage": "https://img.alicdn.com/img/ibank/O1CN01txLhMd1gezw9SFwuB_!!2212690464168-0-cib.jpg",
  "repurchaseRate": "54%",
  "tierPricing": [
    { "quantity": "1~199个", "price": 15.0 },
    { "quantity": "200~2999个", "price": 14.5 },
    { "quantity": "≥3000个", "price": 13.5 }
  ],
  "scrapedAt": "2026-10-18T17:35:00+00:00",
  "searchQuery": "phone case",
  "detailLevel": "full"
}
```


#### Python SDK Quickstart (`examples/run_taobao_tmall_scraper.py`)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
    "queries": ["phone case", "wireless earbuds"],
    "itemUrls": ["https://world.taobao.com/item/978797368275.htm"],
    "catalogSource": "taobao_retail",
    "scrapeDetails": True,
    "maxItems": 50,
    "sortBy": "sales"
}

run = client.actor("unitbytes/taobao-tmall-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("reviewCount"), item.get("dsrDescription"), item.get("shopName"))
```

#### Sample Output Schema (`samples/taobao-tmall-scraper-sample.json`)
```json
{
  "itemId": "978797368275",
  "title": "適用新款17pro iPhone手機殼case磁吸深藍色18promax蘋果手機殼橙色16全包15防",
  "platform": "tmall",
  "url": "https://world.taobao.com/item/978797368275.htm",
  "taobaoUrl": "https://detail.tmall.com/item.htm?id=978797368275",
  "price": 168.0,
  "originalPrice": 198.0,
  "promotionPrice": 168.0,
  "currency": "CNY",
  "priceLocal": 31.39,
  "localCurrency": "SGD",
  "priceHkd": 182.5,
  "priceTwd": 756.0,
  "discountType": "官方立減",
  "shopId": "539281742",
  "sellerUserId": "2214958201928",
  "shopName": "芒殼旗艦店",
  "sellerNick": "芒殼旗艦店",
  "sellerType": "B",
  "sellerTypeLabel": "Tmall Flagship Store",
  "shopItemCount": 142,
  "shopNewItemCount": 18,
  "shopUrl": "https://shop539281742.world.taobao.com",
  "taobaoShopUrl": "https://shop539281742.taobao.com",
  "dsrDescription": 4.8,
  "dsrService": 4.8,
  "dsrDelivery": 4.8,
  "ratingGoodPercent": 99,
  "ratingGoodCount": "200+",
  "reviewCount": 200,
  "reviewTags": [
    {
      "tag": "摸起來順手",
      "count": 40
    },
    {
      "tag": "質感很高端",
      "count": 29
    },
    {
      "tag": "外形外觀好看",
      "count": 26
    },
    {
      "tag": "很貼合",
      "count": 15
    }
  ],
  "reviews": [
    {
      "rating": 5,
      "content": "手機殼質感非常好，磁吸很穩，按鍵反饋清脆！",
      "date": "2026-10-12",
      "sku": "適用iPhone16ProMax【深海藍-磁吸款】",
      "user": "t***8",
      "videos": []
    }
  ],
  "categoryId": "50015056",
  "rootCategoryId": "1512",
  "categoryPath": "首頁 > 阿裏B2C商城 > 手機及配件 > 手機配件 > 保護套/矽膠套",
  "location": "廣東深圳",
  "freeShipping": true,
  "mainImage": "https://img.alicdn.com/imgextra/i3/2214958201928/O1CN01ENie9321XlZreIJor_!!2214958201928.jpg",
  "images": [
    "https://img.alicdn.com/imgextra/i3/2214958201928/O1CN01ENie9321XlZreIJor_!!2214958201928.jpg",
    "https://img.alicdn.com/imgextra/i1/2214958201928/O1CN01aBcDeF21XlZreIJor_!!2214958201928.jpg"
  ],
  "skuCount": 4,
  "skus": [
    {
      "skuId": "sku_1",
      "name": "適用iPhone16ProMax【深海藍-磁吸款】",
      "price": 168.0,
      "stock": 999
    }
  ],
  "scrapedAt": "2026-10-18T17:35:00+00:00",
  "searchQuery": "phone case",
  "detailLevel": "full"
}
```

#### Frequently Asked Questions
**Q: Do I need a Taobao account, Alipay, or a Chinese phone number?**
No, absolutely not. The actor operates 100% cookieless and anonymously. You never have to register an account, scan QR codes, or verify SMS codes.

**Q: What is the difference between taobao_retail and mainland_wholesale in catalogSource?**
taobao_retail (Default — Taobao & Tmall Retail via world.taobao.com) searches official retail Taobao & Tmall consumer shops and supports scrapeDetails: true (50+ full detail fields including 3-axis DSR scores, real customer reviews with buyer videos, reviewTags, full HD image galleries, categoryPath, and multi-currency CNY/SGD/HKD/TWD pricing) as well as itemUrls. mainland_wholesale searches the Mainland factory & B2B wholesale supply chain at ~30 items/sec (up to 10,000 items/run), returning tierPricing volume discounts, repurchaseRate, isSuperFactory, and verified manufacturer profiles.

**Q: Can I scrape a list of direct product links (itemUrls)?**
Yes! Paste any Taobao (item.taobao.com), Tmall (detail.tmall.com), or World Taobao (world.taobao.com) product URLs or numeric item IDs into itemUrls or startUrls. Products listed on Taobao's global export catalog return full 50+ field details; offline or mainland-only restricted items return a clean status notice (UNAVAILABLE) at $0.00 charged.

**Q: Will the product photo links expire or break in Shopify / WooCommerce?**
No. Our actor automatically unblocks and converts all image URLs to permanent, master-resolution links on img.alicdn.com so they work reliably in Shopify, WooCommerce, Excel, and WordPress without 403 Forbidden errors.

**Q: How many products can I scrape for free?**
With Apify's default $5.00 free monthly credit, you can extract over 3,330 products completely free every month at $0.0015/item ($1.50 per 1,000 items).

---

### 🚀 Alibaba Scraper: Wholesale Products & Factory Finder (`unitbytes/alibaba-scraper`)

The ultimate supplier intelligence engine for Alibaba.com. Extract global manufacturer product catalogs, FOB tiered pricing brackets, verified factory audit certifications, and Trade Assurance status.

- **Pricing:** `$0.005 / item` (Pay-Per-Event — $0.005 search product listing, $0.01 full b2b product detail & supplier audit (volume tiers from $0.0009))
- **Cloud Console:** [https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba](https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/alibaba-scraper/](https://unitbytes.com/actors/alibaba-scraper/)
- **n8n Workflow File:** [`n8n/alibaba-scraper-n8n-workflow.json`](n8n/alibaba-scraper-n8n-workflow.json)
- **Engineering Playbook:** [1688 vs. Alibaba Direct Factory Sourcing & Price Extraction Playbook](https://unitbytes.com/blog/how-to-scrape-1688-without-account-sourcing-guide/)

#### Key Capabilities
- **FOB Tiered Price Brackets:** Captures unit prices across volume tiers (e.g., 500-1000 pcs, 1000-5000 pcs, 10,000+ pcs) in USD.
- **Verified Factory Credentials:** Audits ISO/CE/RoHS certifications, on-site inspection reports, floor space, and factory staff count.
- **Supplier Response & On-Time Delivery:** Extracts verified historical transaction scores, buyer review percentages, and average dispatch times.
- **Customization & OEM Capabilities:** Identifies custom logo minimums, custom packaging thresholds, and graphic design lead times.

#### Python SDK Quickstart (`examples/run_alibaba_scraper.py`)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
    "keyword": "wireless earbuds",
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}

run = client.actor("unitbytes/alibaba-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("priceMin"))
```

#### Sample Output Schema (`samples/alibaba-scraper-sample.json`)
```json
{
  "id": "1601918386232",
  "offerId": "1601918386232",
  "productId": "1601918386232",
  "title": "Premium Crystal Clear TPU PC Case for iPhone 17 18 Pro Max Strong Magnetic Charging Shockproof Transparent Phone Cover",
  "url": "https://www.alibaba.com/product-detail/Premium-Crystal-Clear-TPU-PC-Case_1601918386232.html",
  "productUrl": "https://www.alibaba.com/product-detail/Premium-Crystal-Clear-TPU-PC-Case_1601918386232.html",
  "price": 0.68,
  "priceMin": 0.7251,
  "priceMax": 0.9667,
  "currency": "USD",
  "minOrderQuantity": "Min. order: 200 pieces",
  "soldOrder": "300 sold",
  "tieredPrices": [
    {
      "minQuantity": 200,
      "maxQuantity": 2999,
      "price": 0.68,
      "unit": "piece"
    },
    {
      "minQuantity": 3000,
      "maxQuantity": 29999,
      "price": 0.65,
      "unit": "piece"
    },
    {
      "minQuantity": 30000,
      "maxQuantity": null,
      "price": 0.51,
      "unit": "piece"
    }
  ],
  "supplier": {
    "name": "Guangzhou Ruite Electronic Technology Co., Ltd.",
    "country": "CN",
    "yearsActive": "9 yrs",
    "isVerified": true,
    "tradeAssurance": true,
    "rating": 4.7,
    "reviewCount": 99,
    "storeUrl": "https://ruitetec.en.alibaba.com/company_profile.html"
  },
  "mainImage": "https://sc04.alicdn.com/kf/He0c23016d3854f688506c3d7090724e8a.png",
  "pictureUrl": "https://sc04.alicdn.com/kf/He0c23016d3854f688506c3d7090724e8a.png",
  "images": [
    "https://sc04.alicdn.com/kf/He0c23016d3854f688506c3d7090724e8a.png",
    "https://sc04.alicdn.com/kf/H0905779a61dc41c7a3122237ebd3af61u.jpg"
  ],
  "leadTime": {
    "ladderPeriodList": [
      {
        "minQuantity": 1,
        "maxQuantity": 100,
        "processPeriod": 8
      },
      {
        "minQuantity": 101,
        "maxQuantity": 1000,
        "processPeriod": 12
      },
      {
        "minQuantity": 1001,
        "maxQuantity": 5000,
        "processPeriod": 16
      }
    ]
  },
  "specifications": {
    "compatible brand": "For iPhone, For Samsung",
    "design style": "Transparent",
    "material": "TPU+PC",
    "feature": "360 protection, Anti-Fingerprint, Magnetic, Shockproof",
    "OEM/ODM": "Warmly Welcomed"
  },
  "detailLevel": "full",
  "page": 1,
  "position": 1,
  "nextPage": 2,
  "resumptionToken": "gAAAAABqs8yqOTyY..."
}
```

#### Frequently Asked Questions
**Q: Can I filter for only Verified Suppliers or Trade Assurance sellers?**
Yes. Filter toggles allow you to restrict results to Verified Gold Suppliers with Trade Assurance protection.

**Q: How does this differ from the 1688 Scraper?**
Alibaba.com focuses on international export with USD pricing and English documentation. 1688.com is China domestic wholesale market with CNY pricing (often 30-50% cheaper, but domestic-focused).

**Q: Can I scrape direct product detail URLs?**
Yes, input either search keywords or arrays of specific product detail URLs.

**Q: Does it extract sample order pricing?**
Yes, sample prices and lead times are parsed into dedicated fields when provided by the vendor.


---

## ⚡ Quick Installation & Local Usage

### 1. Run with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API.git
cd Taobao-Tmall-Alibaba-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_taobao_tmall_scraper.py
```

### 2. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Paste your Apify API Token into Node `1. Set Apify Token & Input` and click **Test Workflow**.

### 3. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 22 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
