# Workflow 02 — No IT Provider on Website
**Campaign:** #4 from campaign-strategy.md
**Signal:** Business has no MSP, IT company, or tech partner mentioned on their website
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 10–15
**Confidence:** High → auto-push

---

## Logic

```
Source list (Prospeo — business owners + ops managers, 5–100, AU)
  → Validate: website live
  → Pre-filter: Google search "site:domain IT support OR managed" returns 0 results (credit-saving trick)
  → Claygent: confirm no IT provider mentioned on website
  → Filter: NO provider → keep
  → Enrich: industry + suburb for personalisation
  → Email waterfall
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source List (Prospeo)

```
job_titles: [Business Owner, Director, Managing Director, CEO, Founder,
             Operations Manager, Office Manager, Practice Manager]
headcount: 5–100
country: AU
state: NSW (primary run), then VIC, QLD
```

---

### Step 2 — Website Validation (1 credit)

HTTP check on `company_website`. Keep `website_live = TRUE` only.

---

### Step 3 — Pre-filter: Google Site Search (1–2 credits)

Before running Claygent, do a cheap Google search to see if the website mentions IT:

```
Clay HTTP enrichment:
Search Google for: site:{{company_website}} "IT support" OR "managed IT" OR "technology partner" OR "IT provider"

If results > 0 → likely has IT provider → skip Claygent, mark as EXCLUDED
If results = 0 → run Claygent
```

**This cuts Claygent usage by ~50% on this workflow.**

---

### Step 4 — Claygent: IT Provider Confirmation (8–12 credits)

Run only on leads that passed Step 3.

```
Prompt:
Visit {{company_website}} and check every page you can access.

Look for any mention of:
- A named IT company, MSP, or technology partner
- "Managed IT", "IT support", "technology support", "helpdesk"
- Any IT vendor logos or partner badges
- A "technology" or "IT" section listing their provider

Return:
- has_it_provider: YES or NO
- provider_name: [name if found, else "none"]
- evidence: [exact quote or URL, or "not found"]
```

**Filter:** Keep `has_it_provider = NO`

---

### Step 5 — Extract Personalisation Variables (2–3 credits)

```
Prompt (run on filtered list only):
Visit {{company_website}} and extract:
- company_suburb: primary suburb or area they operate in
- company_industry: one word (e.g. Accounting, Legal, Healthcare, Construction, Retail)
- team_size_signal: any mention of team size or number of staff on the website
- pain_signal: any mention of tech, IT, computers, systems, or digital tools (quote if found)
```

---

### Step 6 — Email Waterfall (2–4 credits)

Prospeo → Hunter → Apollo.

---

### Step 7 — Auto-Push to Smartlead

**Campaign:** `ITT — No IT Provider Gap`

**Variables:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{company_suburb}}` | `company_suburb` |
| `{{company_industry}}` | `company_industry` |
| `{{pain_signal}}` | `pain_signal` |

---

## Email Sequence

**Email #1 — Lead magnet: IT Health Check**
> Subject: `noticed something about {{company_name}}`
>
> Hey {{first_name}},
>
> I was looking at {{company_name}}'s website and couldn't find a preferred IT provider listed.
>
> A lot of {{company_industry}} businesses your size are managing IT ad hoc — which usually means expensive emergency callouts when something breaks and no backup coverage when it matters.
>
> Happy to run a free IT health check and report back on where the gaps are. No commitment, no sales call required.
>
> [Name], IT Together

**Email #2 (Day 4):**
> Subject: `free IT health check for {{company_name}}`
>
> Still happy to run that free IT health check — takes me 20 minutes, no cost to you.
>
> Most businesses are surprised by what comes up. Worth knowing before something breaks.
>
> [Name]

**Email #3 (Day 9):**
> Subject: `last one`
>
> Last message — if IT isn't a priority right now, no worries.
>
> But if you ever want a second opinion on your setup, the offer stands.
>
> [Name], IT Together

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| Website validation | 1 |
| Google pre-filter | 1–2 |
| Claygent IT check | 8–12 |
| Personalisation variables | 2–3 |
| Email waterfall | 2–4 |
| **Total** | **~14–22** |

**Starter plan tip:** Run 25 leads/week. Prioritise Sydney CBD, Inner West, North Shore first.
