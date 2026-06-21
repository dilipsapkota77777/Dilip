# Workflow 03 — SMSF Accountants
**Campaign:** #10 from campaign-strategy.md
**Signal:** Accounting firm's website mentions SMSF services
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 8–12
**Confidence level:** High → auto-push

---

## Logic

```
Source list (Prospeo — accountants, 1–50, AU)
  → Enrich: company website URL
  → Claygent: does website mention SMSF services?
  → Filter: YES → keep | NO → exclude
  → Enrich: email waterfall
  → Extract: SMSF service description for personalisation
  → Push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source the List (Prospeo)

**Prospeo search:**
```
job_titles: [Accountant, Senior Accountant, Tax Agent, CPA, Managing Partner, Partner, Principal Accountant]
industries: [Accounting, Financial Services]
headcount: 1–50
country: AU
```

**Import into Clay as base table.**

---

### Step 2 — Validate Website (1 credit/lead)

HTTP status check on `company_website`.
Filter: keep `website_live = TRUE` only.

---

### Step 3 — Claygent: SMSF Detection (8–12 credits/lead)

**Prompt:**
```
Visit {{company_website}} and check if this accounting firm offers SMSF (Self-Managed Super Fund) services.

Look for:
- A dedicated SMSF page or section
- "SMSF" mentioned in their services list
- Terms like "self-managed super", "LRBA", "limited recourse borrowing", "superannuation fund audit"

Return:
- has_smsf_service: YES or NO
- smsf_description: [1-sentence description of their SMSF offering, or "not found"]
- smsf_page_url: [direct URL to their SMSF page if exists, else "none"]
```

**Add columns:**
- `has_smsf_service` → YES / NO
- `smsf_description`
- `smsf_page_url`

**Filter:** Keep only `has_smsf_service = YES`

---

### Step 4 — Also Check: Investment Property / Negative Gearing Language (3–5 credits, optional)

*Run this on SMSF-confirmed leads only for richer personalisation.*

**Prompt:**
```
On {{company_website}}, check if they mention any of the following:
- Property investment advice
- Negative gearing
- Capital gains tax on property
- Property depreciation schedules
- Investment property tax returns

Return:
- has_property_language: YES or NO
- property_context: [1-sentence summary of what they say, or "not found"]
```

**Add columns:**
- `has_property_language`
- `property_context`

---

### Step 5 — Email Waterfall (2–4 credits/lead)

Order: Prospeo → Hunter → Apollo

**Filter:** Keep `email` found only.

---

### Step 6 — Auto-Push to Smartlead

**Trigger:** `has_smsf_service = YES` AND `email` found

**Variables passed:**
| Smartlead Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{smsf_description}}` | `smsf_description` |
| `{{property_context}}` | `property_context` |
| `{{company_website}}` | `company_website` |

---

## Email Copy Hook

**Subject:** `SMSF clients asking about property?`

**Opening line (uses `smsf_description`):**
> "I noticed {{company_name}} offers {{smsf_description}} — a lot of your SMSF clients are probably asking about buying property inside their fund. LRBA lending is a specialist area most brokers avoid. We handle it regularly and have a clean explainer I can send — no pitch, just useful context for when clients ask."

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Website validation | 1 |
| Claygent SMSF check | 8–12 |
| Property language check (optional) | 3–5 |
| Email waterfall | 2–4 |
| **Total** | **~14–22** |

**Starter plan tip:** This is the most credit-intensive workflow. Run on 50 leads/month max. Pre-filter using keyword tools (e.g. Google search `site:accountantwebsite.com.au SMSF`) before running Claygent.

---

## Pre-Filter Trick (Save Credits)

Before running Claygent, use a Clay HTTP enrichment to Google search:
```
site:{{company_website}} SMSF
```
If Google returns 0 results → skip Claygent. Only run Claygent on domains where Google confirms SMSF content exists.

**This can cut Claygent usage by 40–60% on this workflow.**
