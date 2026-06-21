# Workflow 02 — SEEK Hiring Signal
**Campaign:** #7 from campaign-strategy.md
**Signal:** Real estate agency has an active SEEK job posting for Sales Agent, Buyer's Agent, or Property Manager
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 5–8
**Confidence level:** High → auto-push

---

## Logic

```
Source: SEEK job board scrape (Clay HTTP or Claygent)
  → Filter: job title matches target list
  → Filter: company headcount 1–50 (LinkedIn enrichment)
  → Enrich: find principal/director contact at that company
  → Enrich: email waterfall
  → Filter: email found → push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source SEEK Job Postings

**Option A (Recommended): Clay HTTP Request to SEEK**

Set up a Clay HTTP integration to poll SEEK's job search:

```
URL: https://www.seek.com.au/api/chalice-search/v4/search?
  keywords=sales+agent+OR+buyer%27s+agent+OR+property+manager
  &classification=6281  (Real Estate & Property category)
  &worktype=242  (Full time)
  &daterange=7  (last 7 days)
  &country=AU
```

*Note: SEEK's public API has rate limits. Alternatively, use Claygent with Browserbase to scrape SEEK search results pages. Set this workflow to run weekly (Monday morning).*

**Option B (Manual): Paste SEEK URLs**
If API access is unavailable, do a manual SEEK search weekly and paste the results into Clay as a CSV import.

**Input columns from SEEK:**
- `job_title_posted` (e.g. "Sales Agent — Inner West Sydney")
- `company_name`
- `company_location`
- `job_posted_date`
- `seek_job_url`

---

### Step 2 — Filter by Job Title

**Filter condition:**
`job_title_posted` contains any of:
- "Sales Agent"
- "Buyer's Agent"
- "Buyer's Advocate"
- "Property Consultant"
- "Property Manager"
- "Real Estate Agent"

Drop anything that doesn't match.

---

### Step 3 — Company Headcount Check (2–3 credits/lead)

**Clay enrichment:** LinkedIn Company enrichment on `company_name`

**Add columns:**
- `company_headcount_linkedin`
- `company_linkedin_url`
- `company_industry`

**Filter:** Keep only `company_headcount_linkedin` between 1 and 50

---

### Step 4 — Find the Principal / Director (2–3 credits/lead)

**Clay enrichment:** LinkedIn People Search at the company

**Search prompt:**
```
At {{company_name}}, find the person with the most senior title — Principal, Director, Owner, or Managing Director.
Return: full name, LinkedIn URL, job title, start date in role.
```

**Add columns:**
- `contact_first_name`
- `contact_last_name`
- `contact_title`
- `contact_linkedin_url`
- `contact_start_date`

---

### Step 5 — Email Waterfall (2–4 credits/lead)

Run in order:
1. Prospeo name + domain lookup
2. Hunter.io
3. Apollo

**Add column:** `email`

**Filter:** Keep `email` found only.

---

### Step 6 — Extract Job Posting Details for Personalisation

**Add columns (from SEEK URL scrape, 2 credits):**
- `role_being_hired` — exact job title from posting (e.g. "Senior Sales Agent")
- `posting_suburb` — suburb from job location

---

### Step 7 — Auto-Push to Smartlead

**Trigger:** `email` found AND `job_posted_date` within last 14 days

**Variables passed:**
| Smartlead Variable | Clay Column |
|---|---|
| `{{first_name}}` | `contact_first_name` |
| `{{company_name}}` | `company_name` |
| `{{role_being_hired}}` | `role_being_hired` |
| `{{posting_suburb}}` | `posting_suburb` |
| `{{seek_job_url}}` | `seek_job_url` |

---

## Email Copy Hook

**Subject:** `{{company_name}} is growing`

**Opening line:**
> "I saw {{company_name}} is hiring a {{role_being_hired}} in {{posting_suburb}} — congrats on the growth. As your team expands, having a broker who pre-quals buyers in 24 hours makes a real difference to conversion. Happy to send our partner overview?"

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| LinkedIn company enrichment | 2–3 |
| LinkedIn people search | 2–3 |
| Email waterfall | 2–4 |
| SEEK posting detail scrape | 2 |
| **Total** | **~8–12** |

**Automation cadence:** Run every Monday. Flag posts older than 14 days as stale — do not send.

---

## Deduplication

Before pushing to Smartlead, check:
- `company_name` not already in Smartlead active campaign (use Smartlead webhook dedup or maintain a "contacted" Google Sheet)
- `email` not already in any active Smartlead sequence
