# Workflow 05 — Fast Growth (Multiple SEEK Job Postings)
**Campaign:** #8 from campaign-strategy.md
**Signal:** Company has 3 or more active SEEK job postings across any department in the last 30 days
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 8–12
**Confidence:** High → auto-push

---

## Why This Works

Fast-growing businesses outgrow informal IT overnight. Every 10 new hires adds:
- More devices to manage
- More user accounts to provision
- More attack surface for phishing
- More demand on whoever is "handling IT" informally

Catching them mid-growth — before IT becomes a crisis — is the highest-value moment.

---

## Logic

```
SEEK scrape: companies with 3+ active postings in last 30 days
  → Filter: company headcount 5–80 (LinkedIn)
  → Filter: NOT an IT company / MSP
  → Extract: departments hiring + total role count
  → Find: most senior decision-maker
  → Email waterfall
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source: SEEK Company-Level Scrape

**Option A: Clay + Claygent**
```
Prompt:
Search SEEK for companies in Australia that have posted 3 or more job ads in the last 30 days.
Focus on companies with 10–80 employees (look for clues in the company description).
For each company extract:
- Company name
- Number of active SEEK postings
- Job categories being hired (e.g. Admin, Sales, Operations, Finance)
- Company location / suburb
- SEEK company profile URL
```

**Option B: Supplement from LinkedIn**
Use LinkedIn Sales Navigator to find companies that have recently posted multiple job openings. Filter by AU, 10–80 employees, non-IT industry.

**Input columns:**
- `company_name`
- `active_seek_postings_count`
- `departments_hiring` (e.g. "Admin, Sales, Finance")
- `company_suburb`
- `seek_company_url`

---

### Step 2 — Filter: 3+ Postings

Keep only `active_seek_postings_count` ≥ 3.

---

### Step 3 — Company Headcount + Industry Check (2–3 credits)

LinkedIn Company enrichment:
- `company_headcount_linkedin` → filter 5–80
- `company_industry` → exclude IT companies, MSPs, tech vendors

---

### Step 4 — Find Decision-Maker (2–3 credits)

```
Prompt:
At {{company_name}}, find the Business Owner, CEO, Director, or Operations Manager.
Return: first name, last name, job title, LinkedIn URL.
```

---

### Step 5 — Email Waterfall (2–4 credits)

---

### Step 6 — Auto-Push to Smartlead

**Campaign:** `ITT — Fast Growth Signal`

**Variables:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `contact_first_name` |
| `{{company_name}}` | `company_name` |
| `{{departments_hiring}}` | `departments_hiring` |
| `{{active_seek_postings_count}}` | `active_seek_postings_count` |
| `{{company_suburb}}` | `company_suburb` |

---

## Email Sequence

**Email #1 — Lead magnet: IT Health Check**
> Subject: `{{company_name}} is growing fast`
>
> Hey {{first_name}},
>
> I noticed {{company_name}} is hiring across {{departments_hiring}} — {{active_seek_postings_count}} open roles right now. That's impressive momentum.
>
> The one thing fast-growing businesses usually don't plan for is IT. Every 10 new hires adds significant complexity — more devices, accounts, and security exposure. It catches up fast.
>
> Happy to run a free IT health check so you're not caught off guard as the team scales.
>
> [Name], IT Together

**Email #2 (Day 4):**
> Subject: `IT keeping up with the growth?`
>
> Hey {{first_name}}, just following up.
>
> Free IT health check still on the table — useful to run before you're onboarding another wave of staff.
>
> [Name]

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| SEEK scrape (shared across leads) | 5–8 total |
| LinkedIn company + people search | 4–6/lead |
| Email waterfall | 2–4 |
| **Total** | **~8–12/lead** |

**Cadence:** Run every 2 weeks. Flag companies where hiring has slowed (< 3 postings) since last check — move to lower priority.
