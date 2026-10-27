#!/usr/bin/env python3
"""
Taobao & Tmall 淘宝 Product Scraper — Products, Seller Shops, Reviews, DSR & Prices — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/taobao-tmall-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/taobao-tmall-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/taobao-tmall-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_taobao_tmall_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "queries": ["手机壳", "wireless earbuds"],
    "shopUrls": ["https://world.taobao.com/dianpu/100000001.htm"],
    "itemUrls": ["https://detail.tmall.com/item.htm?id=100000000001"],
    "scrapeDetails": True,
    "maxItems": 50,
    "sortBy": "sales"
}

run = client.actor("unitbytes/taobao-tmall-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("reviewCount"), item.get("dsrDescription"), item.get("shopName"))
