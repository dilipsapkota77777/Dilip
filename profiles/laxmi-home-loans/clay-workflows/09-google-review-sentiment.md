# Workflow 09 — Google Review Sentiment (Settlement Delay Signal)
**Campaign:** #23 from campaign-strategy.md
**Signal:** Agency or accounting firm has Google reviews mentioning finance delays, settlement issues, or broker problems
**Output:** Manual review → Smartlead (high-priority personalised send)
**Est. credits per lead:** 10–15
**Confidence level:** Medium-High → manual review (sensitive topic)

---

## Logic

```
Source list (Prospeo — agents + accountants with 20+ Google reviews)
  → Enrich: Google Maps business data (reviews, rating, review count)
  → Claygent: scan recent reviews for settlement/finance/broker pain keywords
  → Filter: pain keyword found → keep
  → Extract: pain context for personalisation
  → Enrich: email waterfall
  → Manual review → Smartlead
```

---

## Why This Works

Prospects who have experienced the specific pain you solve (slow/unreliable broker = fallen-through settlements) are 3–5x more likely to engage with a message that references that pain. This workflow finds them at scale.

**Caution:** Never name the reviewer or quote the review in your email. Reference the pattern only ("I noticed a few reviews mentioning..."). This keeps it useful without feeling invasive.

---

## Clay Table Setup

### Step 1 — Source List (Prospeo)

```
job_titles: [Principal, Director, Real Estate Agent, Sales Agent, Accountant]
industries: [Real Estate, Accounting]
headcount: 1–50
country: AU
```

---

### Step 2 — Google Maps Enrichment (2–3 credits/lead)

**Clay enrichment:** Google Places API lookup by business name + location

**Add columns:**
- `google_rating` — average star rating
- `google_review_count` — total number of reviews
- `google_maps_url` — direct link to their listing

**Filter:** Keep only `google_review_count` ≥ 20

*Businesses with fewer than 20 reviews don't have enough data to detect a pattern.*

---

### Step 3 — Claygent: Review Sentiment Scan (8–12 credits/lead)

**Prompt:**
```
Go to this Google Maps listing: {{google_maps_url}}

Read through the most recent 20–30 reviews. Look for any reviews that mention:
- Delays with settlement or finance
- Issues with a mortgage broker or lender
- Deals falling through due to finance
- Slow pre-approval or loan processing
- Problems with the buyer's finance

Return:
- has_finance_pain: YES or NO
- pain_summary: [1-sentence summary of the pattern found, or "none"]
- pain_review_count: [approximate number of reviews mentioning this, or 0]
- example_keyword: [one key phrase from a review, do NOT include reviewer name, e.g. "settlement delayed due to broker" — or "none"]
```

**Add columns:**
- `has_finance_pain` → YES / NO
- `pain_summary`
- `pain_review_count`
- `example_keyword`

**Filter:** Keep only `has_finance_pain = YES`

---

### Step 4 — Email Waterfall (2–4 credits/lead)

---

### Step 5 — Manual Review Before Sending

This is a sensitive workflow. Before sending, the reviewer must confirm:
- [ ] The pain pattern is genuine (not a one-off complaint about something unrelated)
- [ ] The email references the pain pattern — NOT any specific reviewer
- [ ] The tone is empathetic, not accusatory

---

## Email Copy Hook

**Subject:** `finance delays hurting {{company_name}}?`

**Opening line (uses `pain_summary`, `example_keyword`):**
> "I was looking at {{company_name}}'s Google reviews and noticed a few mentions of {{example_keyword}} — that's usually a broker reliability problem, not a you problem. We turn pre-quals around in 24 hours and have a clean track record on settlement. Happy to chat about how we work?"

**Alternative opener (if pain is less explicit):**
> "I noticed a pattern in {{company_name}}'s reviews that made me think — a few clients mentioned finance-related delays. That's almost always fixable with the right broker partner. We pre-qual buyers in 24 hours across 40+ lenders. Worth a look?"

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Google Maps enrichment | 2–3 |
| Claygent review scan | 8–12 |
| Email waterfall | 2–4 |
| **Total** | **~12–19** |

**Starter plan tip:** Run this on high-value targets only (agencies with 50+ reviews in target suburbs). Aim for 15–20 leads/month maximum.

---

## Review Pain Keywords to Detect

Train Claygent to look for these patterns:

| Category | Keywords |
|---|---|
| Finance/broker pain | "broker", "lender", "pre-approval", "loan", "finance fell through", "not finance approved" |
| Settlement delay | "settlement", "delayed", "extended", "fell through", "unconditional" |
| Slow process | "slow", "weeks", "waited", "took forever", "dragged out" |
| Blame signals | "not their fault but", "outside their control", "let down by", "disappointed" |

Keywords that are NOT relevant (filter these out):
- "Great broker they recommended" (positive — already has a broker)
- "Their broker sorted everything" (positive — already partnered)
