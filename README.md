# Contra Freelancers & Tech Talent Scraper (Showcase Mirror)

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-orange.svg)](https://apify.com/moneygain/contra-freelancers-scraper)
[![Pricing](https://img.shields.io/badge/Pricing-Pay--Per--Event%20($0.005)-blue.svg)](https://apify.com/moneygain/contra-freelancers-scraper)
[![RAM](https://img.shields.io/badge/Memory-128%20MB-success.svg)](https://apify.com/moneygain/contra-freelancers-scraper)
[![Zero Browser](https://img.shields.io/badge/Zero--Browser-curl__cffi-brightgreen.svg)](https://apify.com/moneygain/contra-freelancers-scraper)

**Extract vetted Contra freelancers, top independent contractors, AI engineers, product designers, and web developers to structured JSON, CSV, or Excel in seconds without headless browser overhead.**

Run directly on [Apify Store](https://apify.com/moneygain/contra-freelancers-scraper) or call programmatically via the Python client wrapper in this repository.

---

## ⚡ Why Choose Our Contra Freelancers Scraper?

| Metric / Feature | Traditional Playwright / Puppeteer Scrapers | **Contra Freelancers Scraper (Our Actor)** |
| :--- | :--- | :--- |
| **Execution Speed** | 12 – 25 seconds per page | **< 0.5 seconds per page** (Direct SSR Extraction) |
| **Memory Footprint** | 4 GB – 8 GB RAM per run | **128 MB RAM** (Zero headless browser overhead) |
| **Pricing Model** | Expensive platform compute charges ($0.08+/run) | **Pay-Per-Event ($0.005 / record)** — Pay only for real data |
| **Reliability Score** | 60% – 75% (DOM selector shifts & timeouts) | **99.9%** (Direct Relay GraphQL cache parsing) |
| **AI / MCP Native** | Complex & slow | **Optimized for Cursor, Claude Desktop & n8n** |

---

## 📋 Sample JSON Output

```json
{
  "username": "NoorMtir",
  "fullName": "Noor Mtir",
  "firstName": "Noor",
  "lastName": "Mtir",
  "title": "Product Designer & Software Engineer",
  "location": "London, UK",
  "platformEarningsBadge": "$25k+",
  "hiredCount": 2,
  "followerCount": 98,
  "topIndependentStatus": "TOP_INDEPENDENT",
  "canReceiveInquiries": true,
  "isQuickResponder": true,
  "hasVerifiedEarnings": true,
  "profileUrl": "https://contra.com/noormtir",
  "avatarUrl": "https://media.contra.com/image/upload/qpm0sdqjqrrkgcw6fs",
  "scrapedAt": "2026-11-23T15:30:00.000Z"
}
```

---

## 🚀 Quick Start (Python Client)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Apify API Token:
```bash
export APIFY_TOKEN="your_apify_token_here"
```

3. Run extraction:
```bash
python run.py
```

---

## 🎯 Key Use Cases

1. **Tech Headhunting & Recruitment Pipelines**: Source pre-vetted AI engineers, Next.js developers, Framer specialists, and product designers directly into your applicant tracking system (ATS) or CRM.
2. **Competitor & Freelance Rate Intelligence**: Analyze platform earnings badges (`$50k+`, `$25k+`, `$10k+`) and hired frequency to benchmark contractor compensation across US, UK, and European markets.
3. **Agency Partnership Sourcing**: Find high-performing independent contractors available for immediate project subcontracting with verified client track records.
4. **AI Agents & Automated Workflow Feeds**: Supply real-time freelance contractor candidate data to automated sourcing bots, Claude MCP pipelines, and n8n workflows.

---

## 🤖 AI Agent & MCP Server Integration (Cursor / Claude)

You can call this Actor directly from your AI agents via the official Apify MCP Server:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

Prompt example:
> *"Find top 10 AI Developers on Contra who are currently available for client inquiries and have verified earnings badges. Return their names, titles, and profile links in a Markdown table."*

---

## ❓ Frequently Asked Questions (FAQ)

### Is scraping Contra data compliant?
Yes. This Actor strictly collects public contractor profile data displayed openly on Contra's discovery index. It operates without requiring user accounts or passwords and does not bypass paywalls.

### How much does this Actor cost?
We use a 100% transparent **Pay-Per-Event (PPE)** pricing model at **$0.005 per extracted freelancer record** ($5.00 per 1,000 records). You never pay for server idle time or empty results. Bronze, Silver, and Gold Apify subscription tiers receive automatic 10% to 20% discounts.

---

## 🔗 Official Links & Resources

- **Apify Actor Store**: [moneygain/contra-freelancers-scraper](https://apify.com/moneygain/contra-freelancers-scraper)
- **Developer Profile**: [Moneygain on Apify](https://apify.com/moneygain)
