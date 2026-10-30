#!/usr/bin/env python3
"""
Taobao & Tmall Seller Catalog & Shop Scraper (淘宝店铺) — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/taobao-seller-shop-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/taobao-seller-shop-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/taobao-seller-shop-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_taobao_seller_shop_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "shopUrls": ["https://world.taobao.com/dianpu/63978904.htm"],
    "maxItems": 30,
    "startPage": 1,
    "scrapeDetails": True,
    "sortBy": "default"
}

run = client.actor("unitbytes/taobao-seller-shop-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("shopName"), item.get("searchQuery"))
