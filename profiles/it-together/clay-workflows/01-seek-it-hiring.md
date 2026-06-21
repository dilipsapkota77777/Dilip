# Workflow 01 — SEEK IT Hiring Signal
**Campaign:** #2 from campaign-strategy.md
**Signal:** Company has active SEEK job posting for IT Support, Helpdesk, IT Admin, Systems Administrator, or IT Coordinator
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 8–12
**Confidence:** High → auto-push

---

## Why This Is the #1 Signal

Companies posting IT roles on SEEK have already:
1. Decided they need IT help (pain confirmed)
2. Chosen the expensive path (hiring in-house)
3. Not yet committed (still posting)

This is the perfect intercept moment. MSP is faster, cheaper, and available same-week. The email writes itself.

---

## Logic

```
SEEK scrape (IT roles, AU)
  → Filter: job title matches IT Support / Helpdesk / Admin / SysAdmin
  → Filter: company headcount 5–100 (LinkedIn enrichment)
  → Find: most senior decision-maker at that company (Owner/Director/Ops Manager)
  → Enrich: email waterfall
  → Extract: job title + suburb from posting
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source SEEK Job Postings

**Option A: Clay HTTP Request (weekly automation)**
```
URL: https://www.seek.com.au/api/chalice-search/v4/search?
  keywords=IT+support+OR+helpdesk+OR+IT+administrator+OR+systems+administrator+OR+IT+coordinator
  &country=AU
  &daterange=7
```

**Option B: Claygent scrape of SEEK search page**
```
Prompt:
Go to https://www.seek.com.au/IT-support-jobs/in-Sydney-NSW and list all job postings on the first 2 pages.
For each posting extract:
- Job title
- Company name
- Suburb/location
- Date posted
- SEEK job URL
Return as a list.
```

Set to run every Monday.

**Input columns:**
- `job_title_posted`
- `company_name`
- `job_suburb`
- `job_posted_date`
- `seek_job_url`

---

### Step 2 — Filter: IT Role Confirmation

Keep postings where `job_title_posted` contains:
- "IT Support", "Helpdesk", "Help Desk", "IT Administrator", "IT Admin"
- "Systems Administrator", "SysAdmin", "IT Coordinator", "IT Technician"
- "Desktop Support", "Level 1 Support", "Level 2 Support"

Exclude:
- "Senior IT Manager", "IT Director", "CTO", "Chief Technology" (too senior — already have IT leadership)
- "Software Developer", "Developer", "Engineer" (not IT support roles)

---

### Step 3 — Company Headcount Check (2–3 credits)

**Clay enrichment:** LinkedIn Company lookup on `company_name`

**Add columns:**
- `company_headcount_linkedin`
- `company_industry`
- `company_linkedin_url`

**Filter:** Keep `company_headcount_linkedin` between 5 and 100

---

### Step 4 — Find Decision-Maker (2–3 credits)

**Clay enrichment:** LinkedIn People Search at company

```
Prompt:
At {{company_name}}, find the most senior non-IT decision-maker:
Business Owner, Director, Managing Director, CEO, Operations Manager, or Office Manager.
(Not the IT Manager or IT person — we want the business decision-maker.)
Return: first name, last name, job title, LinkedIn URL.
```

**Add columns:**
- `contact_first_name`
- `contact_last_name`
- `contact_title`
- `contact_linkedin_url`

---

### Step 5 — Email Waterfall (2–4 credits)

Order: Prospeo → Hunter → Apollo

**Filter:** Keep `email` found only.

---

### Step 6 — Auto-Push to Smartlead

**Trigger:** `email` found AND `job_posted_date` within last 14 days AND headcount 5–100

**Smartlead campaign:** `ITT — SEEK IT Hiring Signal`

**Variables passed:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `contact_first_name` |
| `{{company_name}}` | `company_name` |
| `{{it_role}}` | `job_title_posted` |
| `{{job_suburb}}` | `job_suburb` |
| `{{seek_job_url}}` | `seek_job_url` |
| `{{company_headcount}}` | `company_headcount_linkedin` |

---

## Email Sequence

**Email #1 — Lead magnet: Hiring vs MSP Calculator**
> Subject: `{{company_name}} — hiring {{it_role}}?`
>
> Hey {{first_name}},
>
> I saw {{company_name}} is hiring a {{it_role}} in {{job_suburb}}.
>
> Before you commit to a $65–80k salary + super + recruitment time, it's worth seeing the numbers. We manage IT for businesses your size for a fraction of that cost — and we're available same-week, not after a 6-week hiring process.
>
> Reply and I'll send a quick cost comparison. Most businesses save 40–60%.
>
> [Name], IT Together

**Email #2 (Day 4) — Follow-up**
> Subject: `re: the {{it_role}} role`
>
> Just following up — did the cost comparison idea make sense?
>
> Happy to jump on a 15-min call and show you exactly how we work vs. a hire.
>
> [Name]

**Email #3 (Day 8) — Soft close**
> Subject: `last one from me`
>
> Not going to keep following up — but if you're still weighing up hiring vs. managed IT, the offer stands.
>
> Free 30-min session where I walk through exactly what we'd cover for {{company_name}}. No commitment.
>
> [Name]

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| LinkedIn company lookup | 2–3 |
| LinkedIn people search | 2–3 |
| Email waterfall | 2–4 |
| **Total** | **~6–10** |

**Cadence:** Run every Monday. Discard postings older than 14 days.
