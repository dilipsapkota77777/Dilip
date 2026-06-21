# Workflow 04 — New CEO / Operations Manager / Practice Manager
**Campaign:** #9 from campaign-strategy.md
**Signal:** CEO, Director, Operations Manager, or Practice Manager started role in last 90 days
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 6–10
**Confidence:** High → auto-push

---

## Logic

```
Source list (Prospeo — senior titles, 5–100, AU)
  → Enrich: LinkedIn profile for job start date
  → Filter: started role < 90 days ago
  → Enrich: previous company name
  → Enrich: email waterfall
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source (Prospeo)

```
job_titles: [CEO, Managing Director, Director, Operations Manager,
             Office Manager, Practice Manager, General Manager]
headcount: 5–100
country: AU
state: NSW (primary)
```

Ensure `linkedin_url` is populated.

---

### Step 2 — LinkedIn Start Date Enrichment (3–5 credits)

**Clay enrichment:** LinkedIn profile scrape via `linkedin_url`

**Add columns:**
- `current_role_start_date`
- `days_in_role` = TODAY() - `current_role_start_date`
- `previous_company_name`
- `previous_job_title`

**Filter:** Keep `days_in_role` between 0 and 90.

---

### Step 3 — Email Waterfall (2–4 credits)

---

### Step 4 — Auto-Push to Smartlead

**Campaign:** `ITT — New Leader Welcome`

**Variables:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{job_title}}` | `job_title` |
| `{{previous_company}}` | `previous_company_name` |
| `{{days_in_role}}` | `days_in_role` |

---

## Email Sequence

**Email #1 — Lead magnet: IT Health Check**
> Subject: `congrats on the new role, {{first_name}}`
>
> Hey {{first_name}},
>
> Congrats on the move to {{company_name}} — stepping up from {{previous_company}} is exciting.
>
> Most new ops leaders I talk to inherit an IT situation they didn't create. A free IT health check is a quick way to know exactly what you're working with from day one — before something breaks and you're scrambling.
>
> Happy to run one for {{company_name}} — no commitment, just useful context.
>
> [Name], IT Together

**Email #2 (Day 5):**
> Subject: `the IT health check offer`
>
> Still happy to run that free IT health check for {{company_name}} — takes 20 minutes, I'll send a one-page report.
>
> Useful to have early in a new role.
>
> [Name]

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| LinkedIn start date enrichment | 3–5 |
| Email waterfall | 2–4 |
| **Total** | **~5–9** |

**Cadence:** Run weekly. Exclude leads where `days_in_role` > 90.
