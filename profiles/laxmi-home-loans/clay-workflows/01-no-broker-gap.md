# Workflow 01 — No Broker Partner Gap
**Campaign:** #4 from campaign-strategy.md
**Signal:** Real estate agency or accounting firm has no mortgage broker/finance partner mentioned on their website
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 7–10
**Confidence level:** High → auto-push

---

## Logic

```
Source list (Prospeo)
  → Enrich: company website URL
  → Filter: is website live? (drop dead sites)
  → Claygent: does website mention a broker/finance partner?
  → Filter: NO → keep | YES → exclude
  → Enrich: contact email (waterfall)
  → Filter: email found? → push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source the List (Prospeo)

**Input columns:**
- `first_name`
- `last_name`
- `email` (may be empty — waterfall later)
- `job_title`
- `company_name`
- `company_website`
- `linkedin_url`
- `company_headcount`
- `industry`
- `country`

**Prospeo search parameters:**
```
job_titles: [Real Estate Agent, Sales Agent, Buyer's Agent, Principal, Director, Accountant, Tax Agent, CPA, Financial Planner, Financial Adviser]
industries: [Real Estate, Accounting, Financial Services]
headcount: 1–50
country: AU
```

---

### Step 2 — Validate Website (1 credit/lead)

**Clay enrichment:** HTTP status check on `company_website`

**Add column:** `website_live` → TRUE / FALSE

**Filter:** Keep only `website_live = TRUE`

*Drop dead sites here — don't waste Claygent credits on them.*

---

### Step 3 — Claygent: Broker Partner Check (8–12 credits/lead)

**Prompt for Claygent:**
```
Visit {{company_website}} and look for any mention of:
- A preferred mortgage broker or finance partner
- A "finance" page or "home loans" referral partner section
- Any named broker or lending company they recommend to clients
- Any text like "our preferred broker", "finance partner", "mortgage referral"

Return:
- has_broker_partner: YES or NO
- broker_partner_name: [name if found, else "none"]
- evidence: [exact quote or URL where found, or "not found"]
```

**Add columns:**
- `has_broker_partner` → YES / NO
- `broker_partner_name`
- `broker_evidence`

**Filter:** Keep only `has_broker_partner = NO`

*This is where Starter plan credits go. Run in batches of 50 max per day to stay within limits.*

---

### Step 4 — Email Waterfall (2–4 credits/lead)

Run email enrichment in this order (stop when found):
1. **Prospeo** email lookup by name + domain
2. **Hunter.io** email finder
3. **Apollo** email enrichment

**Add column:** `email_verified` → found / not found

**Filter:** Keep only `email_verified = found`

---

### Step 5 — Extract Personalization Variables

**Add columns (Claygent pull from website, 2–3 credits):**
- `company_suburb` — primary suburb/area they operate in
- `specialisation` — e.g. "residential sales", "buyer advocacy", "SMSF accounting"
- `years_operating` — if mentioned on website (About page)

---

### Step 6 — Push to Smartlead (Auto)

**Smartlead webhook trigger:** When `email_verified = found` AND `has_broker_partner = NO`

**Variables passed to Smartlead:**
| Smartlead Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{job_title}}` | `job_title` |
| `{{company_suburb}}` | `company_suburb` |
| `{{specialisation}}` | `specialisation` |
| `{{company_website}}` | `company_website` |

---

## Email Copy Hooks (from campaign-strategy.md #4)

**Subject line options:**
- `quick question, {{first_name}}`
- `{{company_name}} — mortgage partner?`
- `noticed something on your site`

**Opening line (uses `company_suburb` + `specialisation`):**
> "I was looking at {{company_name}}'s site and noticed you don't have a preferred mortgage broker listed — pretty common for {{specialisation}} firms in {{company_suburb}}, but worth fixing."

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Prospeo source | ~0.5 (bulk export) |
| Website validation | 1 |
| Claygent broker check | 8–12 |
| Email waterfall | 2–4 |
| Personalization pull | 2–3 |
| **Total** | **~14–20** |

**Starter plan tip:** Run this workflow on a filtered list of 75–100 leads/month max to stay within credits. Prioritise suburbs with most active agencies first (Sydney, Melbourne, Brisbane).

---

## Exclusion Logic

Before running Claygent, filter out:
- `company_website` contains: `raywhite.com`, `ljhooker.com`, `anz.com.au`, `commbank.com.au`, `nab.com.au`, `westpac.com.au`
- `company_name` contains: "Ray White HQ", "LJ Hooker HQ"
- Any domain matching `excluded_domains` list in `client-profile.yaml`
