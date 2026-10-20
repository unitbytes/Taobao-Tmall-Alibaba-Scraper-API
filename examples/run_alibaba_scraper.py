#!/usr/bin/env python3
"""
Alibaba Scraper: Wholesale Products & Factory Finder — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/alibaba-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/alibaba-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/alibaba-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_alibaba_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "keyword": "wireless earbuds",
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}

run = client.actor("unitbytes/alibaba-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("priceMin"))
