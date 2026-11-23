"""
Contra Freelancers & Tech Talent Scraper - Client Runner
Calls the canonical Apify Actor 'moneygain/contra-freelancers-scraper' via Pay-Per-Event API.
"""

import os
import json
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
if not APIFY_TOKEN:
    raise ValueError("Missing APIFY_TOKEN in environment or .env file.")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "startUrls": ["https://contra.com/discover?roles=AI+Developer"],
    "roles": ["AI Developer", "Web Developer"],
    "onlyAvailableForInquiries": True,
    "maxItems": 10,
}

print(f"🚀 Calling moneygain/contra-freelancers-scraper with input: {json.dumps(run_input)}")
run = client.actor("moneygain/contra-freelancers-scraper").call(run_input=run_input)

print(f"✅ Actor run completed! Status: {run['status']}. Dataset ID: {run['defaultDatasetId']}")
dataset = client.dataset(run["defaultDatasetId"])

items = dataset.list_items().items
print(f"📊 Downloaded {len(items)} freelancer records:")
for item in items[:5]:
    print(f" - {item.get('fullName')} ({item.get('username')}): {item.get('title')} [{item.get('location')}] - Earnings: {item.get('platformEarningsBadge')}")
