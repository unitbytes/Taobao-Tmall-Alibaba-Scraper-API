#!/usr/bin/env python3
"""
Alibaba B2B Wholesale & Supplier Data — Real-Time Synchronous REST API Quickstart (RapidAPI Hub & Zyla API Hub)
RapidAPI Hub: https://rapidapi.com/unitbytes/api/alibaba-b2b-wholesale-and-supplier-data
Zyla API Hub: https://zylalabs.com/api-marketplace/commerce+%26+ecommerce/global+b2b+wholesale+and+supplier+data+api/14474
Docs & Schema: https://unitbytes.com/actors/alibaba-scraper/

Usage:
    pip install requests
    export RAPIDAPI_KEY="your_rapidapi_key"
    python examples/run_alibaba_rapidapi.py
"""

import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
if not RAPIDAPI_KEY or RAPIDAPI_KEY.startswith("YOUR_"):
    raise SystemExit("Please set your RapidAPI key: export RAPIDAPI_KEY='your_rapidapi_key'")

BASE_URL = "https://alibaba-b2b-wholesale-and-supplier-data.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-host": "alibaba-b2b-wholesale-and-supplier-data.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
}

# 1. Search Verified & Trade Assurance Alibaba B2B Suppliers in USD (GET /v1/alibaba/search)
resp = requests.get(
    f"{BASE_URL}/v1/alibaba/search",
    headers=HEADERS,
    params={
        "keyword": "wireless earbuds",
        "verified_only": "true",
        "trade_assurance_only": "true",
        "page": 1,
        "page_size": 5,
    },
    timeout=30,
)
resp.raise_for_status()
search_res = resp.json()

products = search_res.get("data", {}).get("items", [])
print(f"Found {len(products)} Alibaba B2B wholesale offers:")
for item in products[:3]:
    print(f" - [{item.get('productId')}] {item.get('title')} | ${item.get('price')} USD | MOQ: {item.get('minOrderQuantity')}")

# 2. Calculate USD FOB Volume Tier Cost & SKU Variations (GET /v1/alibaba/product/skus)
product_id = products[0]["productId"] if products else "1601659070533"
sku_resp = requests.get(
    f"{BASE_URL}/v1/alibaba/product/skus",
    headers=HEADERS,
    params={"product_id": product_id, "order_quantity": 500},
    timeout=30,
)
sku_resp.raise_for_status()
sku_res = sku_resp.json().get("data", {})

print(
    f"\nProduct {product_id} @ 500 units: "
    f"Active FOB Unit Price = ${sku_res.get('matchedTierUnitPriceUsd')} USD | "
    f"Estimated Order Total = ${sku_res.get('estimatedOrderTotalUsd')} USD"
)

# 3. Calculate FBA Packaging Weight, CBM Volume & Lead Time (GET /v1/alibaba/product/logistics)
log_resp = requests.get(
    f"{BASE_URL}/v1/alibaba/product/logistics",
    headers=HEADERS,
    params={"product_id": product_id, "order_quantity": 500},
    timeout=30,
)
log_resp.raise_for_status()
log_res = log_resp.json().get("data", {})

print(
    f"Logistics (500 units): "
    f"Gross Weight = {log_res.get('totalGrossWeightKg')} kg | "
    f"Sea Volume = {log_res.get('totalVolumeCbm')} CBM"
)
