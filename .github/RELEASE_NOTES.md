### 🚀 v1.1.0 Release Notes — 🛍️ Taobao, Tmall & Alibaba B2B Wholesale Scraper API — Products, Seller Shops, Reviews, DSR, SKUs & Factory Tiers (淘宝 / 天猫 / 阿里巴巴)

The fastest, cheapest zero-login Taobao (淘宝), Tmall (天猫) & Alibaba.com B2B Wholesale Scraper & Synchronous REST API suite (`$1.50 / 1,000 items`). Extract official Mainland Taobao & Tmall products, seller shop catalogs (`shopUrls`), 50+ full detail fields, customer reviews (with buyer videos), 3-axis Seller DSR ratings, purchased SKU attributes, multi-currency prices (CNY, SGD, HKD, TWD), Alibaba B2B wholesale tiers, and permanent HD photos.

- 📓 **1-Click Interactive Google Colab Notebook:** [**Open `notebooks/quickstart.ipynb` in Colab**](https://colab.research.google.com/github/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/notebooks/quickstart.ipynb)
- ⚡ **Synchronous REST API on RapidAPI Hub (`<500ms` GET, Free Tier):** [https://rapidapi.com/unitbytes/api/alibaba-b2b-wholesale-and-supplier-data](https://rapidapi.com/unitbytes/api/alibaba-b2b-wholesale-and-supplier-data)
- ⚡ **Synchronous REST API on Zyla API Hub (7-Day Free Trial):** [https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/global+b2b+wholesale+and+supplier+data+api/14474](https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/global+b2b+wholesale+and+supplier+data+api/14474)
- 🤖 **AI Coding Agent MCP Ready:** Includes `.cursor/mcp.json` for Cursor, Windsurf, and Claude Code.
- 🔧 **9-Node n8n Automation Workflows:** Ready-to-import `.json` templates under `n8n/` and at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.

## 🛠️ Included Extraction Engines & SDK Quickstarts

| Extraction Engine | Pricing (PPE) | Python SDK & n8n Template | Cloud Console & Docs |
| :--- | :---: | :--- | :---: |
| **Taobao & Tmall 淘宝 Product Scraper — Products, Seller Shops, Reviews, DSR & Prices** | `$0.0015 / item` | [`examples/run_taobao_tmall_scraper.py`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/examples/run_taobao_tmall_scraper.py) · [`n8n/taobao-tmall-scraper-n8n-workflow.json`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/n8n/taobao-tmall-scraper-n8n-workflow.json) | [⚡ **Run on Apify**](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) · [Schema](https://unitbytes.com/actors/taobao-tmall-scraper/) |
| **Taobao & Tmall Seller Catalog & Shop Scraper (淘宝店铺)** | `$0.0015 / item` | [`examples/run_taobao_seller_shop_scraper.py`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/examples/run_taobao_seller_shop_scraper.py) · [`n8n/taobao-seller-shop-scraper-n8n-workflow.json`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/n8n/taobao-seller-shop-scraper-n8n-workflow.json) | [⚡ **Run on Apify**](https://apify.com/unitbytes/taobao-seller-shop-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) · [Schema](https://unitbytes.com/actors/taobao-seller-shop-scraper/) |
| **Alibaba Scraper: Wholesale Products & Factory Finder** | `$0.0015 / item` | [`examples/run_alibaba_scraper.py`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/examples/run_alibaba_scraper.py) · [`n8n/alibaba-scraper-n8n-workflow.json`](https://github.com/unitbytes/Taobao-Tmall-Alibaba-Scraper-API/blob/main/n8n/alibaba-scraper-n8n-workflow.json) | [⚡ **Run on Apify**](https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) · [Schema](https://unitbytes.com/actors/alibaba-scraper/) |

## ⚡ Pre-Configured 1-Click Task Presets

| Task Preset | Target Use Case | Direct Cloud Launch |
| :--- | :--- | :---: |
| **Scrape Taobao & Tmall Product Prices, SKUs & 3-Axis DSR Scores** | Extract Taobao and Tmall product catalogs, full SKU price matrices, monthly sales volume, and merchant DSR ratings without login cookies. | [⚡ Run Task Preset](https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |
| **Audit Taobao & Tmall Seller Storefronts, Full Catalogs & Reviews** | Extract a Taobao or Tmall merchant's full product inventory, 3-axis DSR ratings, crown credit level, and verified buyer reviews. | [⚡ Run Task Preset](https://apify.com/unitbytes/taobao-seller-shop-scraper?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |
| **Find Products on Alibaba: Wholesale Sourcing Engine** | Search millions of products on Alibaba.com. Extract tiered wholesale volume pricing, MOQ, lead times, and factory audit credentials. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-products-on-alibaba?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |
| **Find Verified Suppliers on Alibaba: Factory Audits & B2B Leads** | Extract TÜV Rheinland & SGS audited Verified Suppliers on Alibaba with Trade Assurance, Gold Supplier tenure, and direct contacts. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-verified-suppliers-on-alibaba?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |
| **Find Low MOQ Products on Alibaba: Small Batch & Dropshipping** | Discover wholesale items with low minimum order quantities (MOQ ≤ 5) for dropshipping, sample orders, and small-batch private labeling. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/find-low-moq-products-on-alibaba?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |
| **Scrape Alibaba Product URLs: Deep Specs & Volume Pricing** | Deep scrape specific Alibaba.com product URLs to extract tiered volume pricing ladders, full packaging specs, and certified supplier details. | [⚡ Run Task Preset](https://apify.com/unitbytes/alibaba-scraper/examples/scrape-alibaba-product-urls?fpr=939u3w&fp_sid=gh_taobao_alibaba_rel) |

---

### 🛡️ Core Engineering Guarantees
- **Zero Login or Cookies Required:** Operates 100% anonymously without personal accounts or session tokens.
- **Clean Flat Schemas:** Export directly to Excel, CSV, Google Sheets, Pandas, or AI agents with zero `[object Object]` nesting errors.
- **Permanent Media CDNs:** High-resolution image and video links that never expire or return 403 Forbidden.
- **Enterprise Support & Custom Feeds:** [contact@unitbytes.com](mailto:contact@unitbytes.com) • [https://unitbytes.com](https://unitbytes.com)
