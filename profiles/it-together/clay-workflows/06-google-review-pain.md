# Workflow 06 — Negative Google Reviews (Tech Issues)
**Campaign:** #10 from campaign-strategy.md
**Signal:** Company has Google reviews mentioning IT problems, tech issues, computer outages, or connectivity failures
**Output:** Manual review → Smartlead
**Est. credits per lead:** 10–15
**Confidence:** Medium → manual review

---

## Logic

```
Source list (Prospeo — business owners + ops managers, 5–100, AU)
  → Enrich: Google Maps data (review count, rating)
  → Filter: 20+ reviews (enough data)
  → Claygent: scan reviews for tech/IT pain keywords
  → Filter: tech pain found → keep
  → Extract: pain theme for personalisation
  → Email waterfall
  → Manual review → Smartlead
```

---

## Clay Table Setup

### Step 1 — Source List (Prospeo)

Same base list as WF02. Cross-reference to avoid duplicate outreach.

---

### Step 2 — Google Maps Enrichment (2–3 credits)

**Clay enrichment:** Google Places API

**Add columns:**
- `google_rating`
- `google_review_count`
- `google_maps_url`

**Filter:** Keep `google_review_count` ≥ 20

---

### Step 3 — Claygent: Review Tech Pain Scan (8–12 credits)

```
Prompt:
Go to this Google Maps listing: {{google_maps_url}}

Read through the 20–30 most recent reviews. Look for any that mention:
- IT, computers, technology, systems
- Outages, downtime, crashes, slow systems
- Internet, connectivity, Wi-Fi issues
- Emails not working, email problems
- "Couldn't access", "system went down", "computers were down"
- Staff "couldn't help because the system was down"

Return:
- has_tech_pain: YES or NO
- pain_theme: [1-sentence summary, e.g. "multiple reviews mention system outages affecting service"]
- pain_keyword: [one representative phrase from reviews, e.g. "system was down all morning" — do NOT include reviewer name]
- pain_review_count: [approximate count]
```

**Filter:** Keep `has_tech_pain = YES`

---

### Step 4 — Email Waterfall (2–4 credits)

---

### Step 5 — Manual Review

Before sending, confirm:
- [ ] Tech pain is genuine and recurring (not a one-off)
- [ ] Email references the pain pattern, not any specific reviewer
- [ ] Tone is empathetic, not condescending

---

## Email Sequence

**Email #1 — Lead magnet: Dark Web Scan or IT Health Check**
> Subject: `noticed something in {{company_name}}'s reviews`
>
> Hey {{first_name}},
>
> I was looking at {{company_name}}'s Google reviews and noticed a few mentions of {{pain_theme}} — that's almost always an IT infrastructure problem rather than a people problem.
>
> We work with businesses your size to make sure that stops happening. Happy to run a free IT health check and show you exactly where the gaps are?
>
> [Name], IT Together

---

## Tech Pain Keywords to Detect

| Category | Keywords |
|---|---|
| System outages | "system down", "computers down", "outage", "couldn't access", "system crashed" |
| Connectivity | "internet", "Wi-Fi", "network", "offline", "disconnected" |
| Email issues | "email not working", "didn't receive", "email problems" |
| Slow systems | "slow", "freezing", "loading forever", "crashed" |
| Staff impact | "couldn't help", "manual", "had to write it down", "waiting for system" |

**NOT relevant (exclude):**
- Reviews praising their technology or IT setup
- One-off complaints about an unrelated technical product they sell

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| Google Maps enrichment | 2–3 |
| Claygent review scan | 8–12 |
| Email waterfall | 2–4 |
| **Total** | **~12–19** |

**Volume:** 15–20 leads/month on Starter plan.
