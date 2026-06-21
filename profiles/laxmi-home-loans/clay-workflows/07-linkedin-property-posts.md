# Workflow 07 — LinkedIn Property Content Posts (Accountants)
**Campaign:** #11 from campaign-strategy.md
**Signal:** Accountant posted about property investment, negative gearing, or tax depreciation on LinkedIn in the last 60 days
**Output:** Manual review → CSV export → Smartlead
**Est. credits per lead:** 8–12
**Confidence level:** Medium → manual review

---

## Logic

```
Source: LinkedIn search for accountants in AU (Prospeo or Sales Nav)
  → Claygent: check LinkedIn activity for property-related posts in last 60 days
  → Filter: has recent property post → keep
  → Extract: post topic for personalisation
  → Enrich: email waterfall
  → Export to CSV → manual review → Smartlead
```

---

## Clay Table Setup

### Step 1 — Source Accountants List (Prospeo)

```
job_titles: [Accountant, Tax Agent, CPA, Senior Accountant, Partner, Director (Accounting)]
industries: [Accounting, Financial Services]
headcount: 1–50
country: AU
```

Ensure `linkedin_url` is populated for each contact.

---

### Step 2 — Claygent: LinkedIn Post Scan (8–12 credits/lead)

*This is the most expensive step — run only after cheaper pre-filters.*

**Pre-filter before running Claygent:**
- `linkedin_url` must be populated
- `job_title` must confirm accounting focus (not finance/banking)

**Prompt:**
```
Go to this LinkedIn profile: {{linkedin_url}}

Check their recent posts (last 60 days). Look for any posts about:
- Property investment
- Negative gearing
- Capital gains tax on property
- Tax depreciation for investment properties
- SMSF property strategies
- Real estate market commentary

Return:
- has_property_post: YES or NO
- post_topic: [brief description of what the post was about, or "none"]
- post_date: [approximate date, or "none"]
- post_excerpt: [first 50 chars of the post, or "none"]
```

**Add columns:**
- `has_property_post` → YES / NO
- `post_topic`
- `post_date`
- `post_excerpt`

**Filter:** Keep only `has_property_post = YES`

---

### Step 3 — Email Waterfall (2–4 credits/lead)

Prospeo → Hunter → Apollo.

---

### Step 4 — Export to CSV (Manual Review)

**Review before sending:**
- [ ] Is the post genuinely about property (not just a reshare)?
- [ ] Is the post recent enough (< 60 days)?
- [ ] Does the contact look like a decision-maker (partner/director)?

---

## Email Copy Hook

**Subject:** `re: your post on {{post_topic}}`

**Opening line (never quote the post directly — use neutral reference):**
> "I came across your recent post on {{post_topic}} — good take. A few accountants I work with have similar clients asking about the financing side alongside the tax angle. We handle the mortgage piece and refer back to the accountant for structuring. Happy to explain how it works if useful."

*Note: Never reference the post verbatim in the email — Australian privacy norms make this feel surveillance-like. Keep it to "I came across your post on [topic]" not "you wrote on 14 June that..."*

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| LinkedIn post scan (Claygent) | 8–12 |
| Email waterfall | 2–4 |
| **Total** | **~10–16** |

**Starter plan tip:** This workflow is expensive per lead. Run on 20–30 leads/month max. Prioritise accountants who ALSO have SMSF services (cross-reference with Workflow 03 for double-signal leads).

---

## Double Signal Upgrade

If a lead matches BOTH Workflow 03 (SMSF Accountant) AND Workflow 07 (Property Post), they get the highest-priority personalisation:

> "I saw your recent post on {{post_topic}} and noticed {{company_name}} also offers SMSF services. We work with a few accounting practices as their referred SMSF broker — we handle the LRBA complexity and refer back to the accountant for tax structuring. I have a short explainer on SMSF lending mistakes if you'd like it."

Route double-signal leads to auto-push (bypass manual review).
