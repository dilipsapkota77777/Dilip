# Workflow 06 — Facebook Ads Running (Real Estate Agents)
**Campaign:** #9 from campaign-strategy.md
**Signal:** Real estate agent or agency has active Facebook/Instagram ads running
**Output:** Manual review → CSV export → Smartlead upload
**Est. credits per lead:** 10–15
**Confidence level:** Medium → manual review before sending

---

## Logic

```
Source: Facebook Ad Library scrape (Claygent + Browserbase)
  → Filter: advertiser is a real estate agency (AU)
  → Filter: ad is active and in Real Estate category
  → Enrich: find principal/agent contact at that agency
  → Enrich: extract ad details for personalisation
  → Enrich: email waterfall
  → Export to CSV → manual review → Smartlead
```

---

## Clay Table Setup

### Step 1 — Source from Facebook Ad Library

**Facebook Ad Library URL pattern:**
```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AU&q=real+estate&search_type=keyword_unordered&media_type=all
```

**Option A: Claygent + Browserbase scrape**

Set up a Claygent workflow to browse the Facebook Ad Library:

```
Prompt:
Go to https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AU&q=[suburb]+real+estate&search_type=keyword_unordered

For each active advertiser on the page, extract:
- Page name (advertiser name)
- Ad headline / primary text (first 100 chars)
- Ad type (image/video/carousel)
- Page URL
- Number of active ads

Return as a JSON list.
```

Run this for each target suburb cluster (e.g. "Sydney real estate", "Melbourne real estate", "Brisbane real estate").

*Note: Facebook Ad Library has rate limits and anti-scrape measures. Run with delays between requests. Expect 2–3 successful scrapes per Claygent session.*

**Option B: Manual scraping (credit-free)**

For Starter plan, consider manually browsing Facebook Ad Library for top target suburbs weekly and pasting results into Clay as a CSV. This saves all Claygent credits for the downstream enrichments.

---

### Step 2 — Filter: Real Estate Agencies Only

**Clay formula filter:**
`page_name` does NOT contain: bank, lender, mortgage, insurance, Ray White Corporate, LJ Hooker Corporate

**Claygent quick check (2–3 credits):**
```
Is "{{page_name}}" a real estate agency (not a bank, insurer, or mortgage broker)?
Return YES or NO only.
```

Keep `YES` only.

---

### Step 3 — Find Agency Website + Contact (3–4 credits/lead)

**Claygent:**
```
Find the official website for a real estate agency called "{{page_name}}" in Australia.
Also find the principal or director's name and LinkedIn URL if available.
Return: website_url, contact_name, contact_linkedin_url
```

---

### Step 4 — Extract Ad Details for Personalisation (3–4 credits/lead)

**Claygent:**
```
Visit {{facebook_page_url}}/ads to see their active Facebook ads.
Extract:
- The suburb or area being advertised
- The property type (residential, commercial, investment)
- Approximate number of active ads
Return: ad_suburb, ad_property_type, active_ad_count
```

**Add columns:**
- `ad_suburb`
- `ad_property_type`
- `active_ad_count`

---

### Step 5 — Email Waterfall (2–4 credits/lead)

Prospeo → Hunter → Apollo by name + domain.

---

### Step 6 — Export to CSV (Manual Review)

**Columns for review sheet:**
- `contact_name`
- `email`
- `page_name` (agency)
- `ad_suburb`
- `ad_property_type`
- `active_ad_count`
- `facebook_page_url`

**Review criteria before uploading:**
- [ ] Does the agency look legitimate (website live, reviews exist)?
- [ ] Is the ad clearly for property listings (not rentals or commercial only)?
- [ ] Is the contact a principal/director (not just an agent)?

---

## Email Copy Hook

**Subject:** `converting your {{ad_suburb}} ad traffic`

**Opening line:**
> "I saw {{page_name}} is running ads for {{ad_suburb}} properties — nice work on the creative. A lot of agents running paid ads find they're getting buyer enquiries from people who aren't finance-ready yet. We pre-qual buyers within 24 hours so you're only spending time on serious ones. Happy to send our partner overview?"

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Claygent Ad Library scrape | 8–12 (shared across multiple leads from one scrape) |
| Agency/contact lookup | 3–4 |
| Ad detail extraction | 3–4 |
| Email waterfall | 2–4 |
| **Total** | **~10–15** |

**Starter plan recommendation:** Run this workflow manually once per fortnight. Target 20–30 leads per run. Reserve full Claygent usage for the high-value enrichment steps only.
