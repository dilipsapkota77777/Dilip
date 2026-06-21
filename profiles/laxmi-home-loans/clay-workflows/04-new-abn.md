# Workflow 04 — New ABN (Business < 12 Months Old)
**Campaign:** #6 from campaign-strategy.md
**Signal:** Business registered ABN within the last 12 months
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 5–8
**Confidence level:** High → auto-push

---

## Logic

```
Source: ABN Lookup bulk data OR Claygent ABN search
  → Filter: registration date < 12 months ago
  → Filter: industry = Real Estate OR Accounting
  → Filter: state = NSW / VIC / QLD (priority markets)
  → Enrich: find principal contact via LinkedIn
  → Enrich: email waterfall
  → Push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source New ABNs

**Option A (Best): ABN Bulk Extract**
The Australian Business Register publishes bulk ABN data for download at:
`data.gov.au/dataset/ds-dga-abn-bulk`

Download monthly. Filter in Clay or Excel first:
- `EntityTypeCode` = IND (individual) or PRV (private company)
- `ABNStatusEffectiveFrom` = within last 12 months
- `MainBusinessPhysicalAddressStateCode` = NSW, VIC, QLD, WA, SA
- `GST status` = registered (indicates active business)

Import filtered list into Clay.

**Option B (Lighter): Claygent ABN Search**
For smaller batches, Claygent can search ABN Lookup by industry keywords:
```
Search ABN Lookup (abn.business.gov.au) for businesses:
- Registered in the last 12 months
- Trading name contains: "real estate" OR "property" OR "accounting" OR "financial"
- State: NSW or VIC or QLD
Return: ABN, entity name, registration date, address
```

---

### Step 2 — Enrich: Company Website

**Clay enrichment:** Clearbit / Apollo company lookup by business name

**Add column:** `company_website`

**Filter:** Keep only leads where website is found and live.

---

### Step 3 — Filter: Verify Industry (2 credits/lead)

**Clay enrichment:** Claygent quick check on website

**Prompt (short = cheap):**
```
Visit {{company_website}}. In ONE word, what industry is this business in?
Options: RealEstate, Accounting, Finance, Other
```

**Filter:** Keep only `RealEstate`, `Accounting`, or `Finance`

---

### Step 4 — Find Principal / Director Contact (2–3 credits/lead)

**LinkedIn People Search:**
```
At {{company_name}}, find the most senior person (Owner, Principal, Director, or Founder).
Return: first name, last name, LinkedIn URL, job title.
```

---

### Step 5 — Email Waterfall (2–4 credits/lead)

Prospeo → Hunter → Apollo

---

### Step 6 — Auto-Push to Smartlead

**Trigger:** `abn_age_months` < 12 AND `email` found AND industry confirmed

**Variables passed:**
| Smartlead Variable | Clay Column |
|---|---|
| `{{first_name}}` | `contact_first_name` |
| `{{company_name}}` | `company_name` |
| `{{company_state}}` | `state` |
| `{{months_since_launch}}` | `abn_age_months` |

---

## Email Copy Hook

**Subject:** `congrats on the launch, {{first_name}}`

**Opening line:**
> "Congrats on launching {{company_name}} — I saw you recently registered. Most new agencies and firms are still building their referral network at this stage, and a reliable mortgage broker is usually near the top of the list. We pre-qual buyers within 24 hours across 40+ lenders. Happy to send our partner overview?"

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Website enrichment | 1 |
| Industry check (Claygent) | 2–3 |
| LinkedIn people search | 2–3 |
| Email waterfall | 2–4 |
| **Total** | **~7–11** |

**Automation cadence:** Run monthly on new ABN data. Flag leads where `abn_age_months` > 12 as expired — do not send.
