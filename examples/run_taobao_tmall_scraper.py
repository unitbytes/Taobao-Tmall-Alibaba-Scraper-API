#!/usr/bin/env python3
"""
Taobao & Tmall 淘宝 Product Scraper — Details, Reviews, Prices, SKUs & HD Photos — Official Python SDK Quickstart
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

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

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
