# Workflow 05 — New Principal / Director Signal
**Campaign:** #8 from campaign-strategy.md
**Signal:** Agency principal or accounting firm director started their role in the last 90 days
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 6–10
**Confidence level:** High → auto-push

---

## Logic

```
Source list (Prospeo — principals/directors, real estate + accounting, AU)
  → Enrich: LinkedIn profile for job start date
  → Filter: started role < 90 days ago
  → Enrich: previous company name
  → Enrich: email waterfall
  → Push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source the List (Prospeo)

**Prospeo search (narrow to senior titles only):**
```
job_titles: [Principal, Director, Managing Director, Owner, Partner, Managing Partner, Founder]
industries: [Real Estate, Accounting, Financial Services]
headcount: 1–50
country: AU
```

---

### Step 2 — LinkedIn Job Start Date Enrichment (3–5 credits/lead)

**Clay enrichment:** LinkedIn profile scrape via `linkedin_url`

**Add columns:**
- `current_role_start_date` — when they started in this specific role
- `previous_company_name` — their company before this one
- `previous_job_title` — role at previous company

**Filter:** Keep only where `current_role_start_date` is within the last 90 days.

*This is the core filter. Drop everyone else.*

---

### Step 3 — Calculate Days in Role

**Clay formula column:**
```
days_in_role = TODAY() - current_role_start_date
```

**Filter:** Keep `days_in_role` between 0 and 90.

---

### Step 4 — Email Waterfall (2–4 credits/lead)

Prospeo → Hunter → Apollo on work email.

---

### Step 5 — Auto-Push to Smartlead

**Trigger:** `days_in_role` ≤ 90 AND `email` found

**Variables passed:**
| Smartlead Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{job_title}}` | `job_title` |
| `{{previous_company}}` | `previous_company_name` |
| `{{days_in_role}}` | `days_in_role` |

---

## Email Copy Hook

**Subject:** `congrats on the new role`

**Opening line (uses `previous_company_name`):**
> "Congrats on the move to {{company_name}} — stepping up from {{previous_company}} is a big step. Most new principals I talk to are trying to convert more buyer enquiries into settled deals early on. We pre-qual buyers within 24 hours across 40+ lenders. Happy to send our partner overview?"

*If `previous_company_name` is not found, fall back to:*
> "Congrats on the new role at {{company_name}}. Most new principals I talk to are focused on one thing early on — converting more buyer enquiries into actual deals..."

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| LinkedIn job start date enrichment | 3–5 |
| Email waterfall | 2–4 |
| **Total** | **~5–9** |

**Automation cadence:** Run weekly. Leads where `days_in_role` has crossed 90 days since last run — exclude from future sends but flag for a "3-month check-in" sequence.

---

## Edge Case Handling

- **Founder of new company:** If `current_role_start_date` matches company founding date, treat as "new business" → route to Workflow 04 (New ABN) instead for the new business angle.
- **Multiple principals at same company:** Send to the most senior title only. De-duplicate by `company_name` and keep highest-ranking job title.
