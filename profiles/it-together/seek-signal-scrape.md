# IT Together — SEEK Signal Scrape Playbook
Generated: 2026-07-12 | Signal type: Hiring (Tier 1)
Framework: Signal Sourcer — Hiring Sub-Skill
Logic: Companies posting IT roles are in-market. Intercept before they hire.

---

## Why This Signal Works

A company posting an IT Manager role on SEEK has already made two decisions:
1. They need dedicated IT support
2. They have budget allocated for it

They haven't decided *how* to solve it yet — hire in-house or outsource.

**Your window:** The moment the job goes live to ~30 days later (before they shortlist).
**Your angle:** Show them managed IT covers the same need at 30–50% less cost than a full-time hire.
**Rule:** Never say "I saw your job posting." Say "noticed you're scaling" — reference the growth challenge, not the listing.

**Signal score:** 40 points (Tier 1 for IT Together — highest buying intent signal available)

---

## Step 1 — SEEK Searches to Run

Run each search at **seek.com.au/jobs** with these exact queries:

### Primary IT Role Searches (highest signal)

| Search query | What it means | Campaign to route to |
|---|---|---|
| `IT Manager` | Considering $85–110k hire — perfect cost comparison target | IT-CFO-AUS |
| `IT Support Officer` | Volume of tickets has hit a wall | IT-CEO-AUS |
| `Systems Administrator` | Infrastructure is growing beyond ad-hoc management | IT-CEO-AUS |
| `Help Desk Technician` | Team size has hit IT tipping point | IT-CEO-AUS |
| `Network Administrator` | Network complexity growing | IT-CEO-AUS |
| `IT Coordinator` | Smaller org, first dedicated IT role | IT-CEO-AUS |
| `Head of IT` OR `IT Director` | More senior — likely 50+ staff, mature IT need | IT-CFO-AUS |

### Secondary Searches (cybersecurity angle — AI Operations upsell)

| Search query | Angle | Campaign |
|---|---|---|
| `Cybersecurity Analyst` | Security becoming a priority — perfect for bundled pitch | IT-CEO-AUS |
| `Information Security` | Compliance-driven IT need | IT-CFO-AUS |
| `Cloud Engineer` | Moving to cloud = need managed support | IT-CEO-AUS |

### Filters to apply on SEEK (every search)

```
Location: All Australia
Date posted: Last 30 days (run weekly to catch new postings)
Work type: Full time (avoid casual/contract — signals committed headcount spend)
Classification: Information & Communication Technology
```

---

## Step 2 — Extract the Data

### Option A — Apify SEEK Scraper (Recommended, ~$2–5/run)

1. Go to **apify.com** → Search "SEEK Jobs Scraper"
2. Actor: `misceres/seek-scraper` or `apify/seek-jobs-scraper`
3. Input configuration:

```json
{
  "searchQuery": "IT Manager",
  "location": "Australia",
  "datePosted": "30",
  "maxItems": 200,
  "proxy": "RESIDENTIAL"
}
```

4. Run for each search query separately (8–10 runs total)
5. Export as CSV from Apify → download

**Fields Apify returns:**
- `job_title` — the actual role posted
- `company_name` — company posting the role
- `company_url` — sometimes direct company URL
- `location` — city/state
- `posted_date` — when it went live
- `job_description` — full text (use to extract headcount clues)

### Option B — Instant Data Scraper (Free, manual)

1. Install **Instant Data Scraper** Chrome extension (free)
2. Go to seek.com.au/jobs → run your search
3. Click Instant Data Scraper → it auto-detects the job listing table
4. Click "Start crawling" — let it page through all results
5. Export CSV when done

**Limitation:** Manual per search, slower, but free. Good for first test run.

### Option C — Manual Copy-Paste (Zero cost, 30 min)

1. Run each SEEK search
2. Open each job listing → copy company name + location
3. Paste into Google Sheet
4. This works fine for the first 50 companies before you automate

---

## Step 3 — Clean the Raw Data

Before importing to Clay, clean the CSV:

### Remove these rows

| Remove if... | Why |
|---|---|
| Company is an IT/MSP company itself | They're a competitor, not a prospect |
| Company is a recruiter posting on behalf of client | Fake company name, can't enrich |
| Role is listed as "contract" or "casual" | Lower intent signal |
| Same company appears 3+ times | Likely a recruiter or IT company |
| Company name is blank or "Confidential" | Can't find contact |

### Add these columns manually (or Clay formula)

```
signal_source = "SEEK_IT_HIRE"
signal_date = [date you scraped]
job_title_signal = [the IT role they posted, e.g. "IT Manager"]
signal_tier = "Tier 1"
```

### Deduplicate

If running multiple SEEK searches, same company may appear from different queries.
Dedup on `company_name` — keep the row with the most senior IT role posted (IT Manager > IT Support > Help Desk).

---

## Step 4 — Import to Clay & Enrich

### Clay Table Setup for SEEK Signal

Create a new Clay table: **"IT Together — SEEK Signal — [Month Year]"**

Import your cleaned CSV. Then run these enrichments in order:

```
Step 1: Enrich company domain
  → Use: Clay "Find Company" (input: company_name + location)
  → Or: Apollo company search by name
  → Output: company_domain, company_linkedin_url
  → Cost: 1–2 credits/row
  → Conditional: only run if company_domain is empty

Step 2: Validate company size (headcount)
  → Use: Apollo or LinkedIn enrichment
  → Filter: keep 10–250 employees
  → Remove: <10 (too small) and >250 (enterprise, separate track)
  → Cost: 1–2 credits/row
  → Conditional: only if headcount is empty

Step 3: Confirm it's NOT an IT company
  → Use: Claygent prompt (see below)
  → Cost: 2 credits/row

Step 4: Find the right contact
  → Use: Clay "Find People" (input: company_domain, titles: see below)
  → Output: first_name, last_name, job_title, contact_linkedin_url
  → Cost: 2–3 credits/row

Step 5: Apply segment formula
  → Formula from clay-segmentation.md
  → 0 credits

Step 6: Email waterfall
  → Prospeo → Apollo → Hunter
  → Cost: 3–5 credits/row
  → Conditional: only if contact found

Step 7: MillionVerifier
  → Cost: ~0.001 credits/email
  → Conditional: only if email found

Step 8: Personalized opener (GPT-4 Mini)
  → SEEK-specific prompt (see below)
  → Cost: 1 credit/row
  → Conditional: only if email verified = valid
```

---

## Step 5 — Claygent Prompts for SEEK Enrichment

### Prompt A — Confirm Not an IT Company

**Column:** `is_it_company`
**Run condition:** Always (cheap gate before spending credits)
**Model:** GPT-4 Mini | Cost: ~1 credit

```
Visit the website {{company_domain}} and their LinkedIn page {{company_linkedin_url}}.

Determine if this company is primarily an IT services, managed IT, cybersecurity, or technology services company that sells IT support to other businesses.

Return ONLY one of:
- "Yes" — if they sell IT services/support to other businesses
- "No" — if they are a regular business that uses IT (not sells it)
- "Unknown" — if you cannot determine

Do not explain. Return one word only.
```

**Filter:** Remove rows where `is_it_company` = "Yes" before spending more credits.

---

### Prompt B — Find the Right Contact Title

**Column:** `contact_title_to_find`
**Run condition:** After confirming not IT company
**Model:** GPT-4 Mini | Cost: ~1 credit

```
The company {{company_name}} ({{company_domain}}) posted a job for "{{job_title_signal}}" on SEEK.

Based on their company size (~{{headcount}} employees) and the role they are hiring for, which of these titles is most likely to make the decision to use managed IT instead of hiring in-house?

Choose ONE from this list:
- CFO (if headcount > 20 and finance leader likely exists)
- CEO (if headcount < 20 or finance function is small)
- Operations Manager (if headcount > 50 and ops role likely exists)

Return ONLY the title. No explanation.
```

---

### Prompt C — SEEK-Specific Personalised Opener

**Column:** `personalized_opener`
**Run condition:** Only if `send_ready` = true
**Model:** GPT-4 Mini | Cost: ~1 credit

```
Write the opening line of a cold email to {{first_name}}, {{job_title}} at {{company_name}}.

Context: This company is scaling (approximately {{headcount}} staff) and is at the stage where IT support is becoming a real need.

The angle: At {{headcount}} employees, IT usually hits a tipping point where ad-hoc support isn't enough anymore. Most businesses at this stage face the choice between hiring in-house or outsourcing.

Rules:
- Under 20 words
- Do NOT mention "SEEK", "job posting", "hiring", or "we saw your ad"
- Do NOT mention "IT Together" or any product name
- Reference their growth/size as the natural trigger, not the job ad
- Conversational, peer-to-peer tone
- No compliments

Good example: "At {{headcount}} staff, IT usually starts becoming a real overhead — curious how {{company_name}} is handling it."
Bad example: "I noticed you posted an IT Manager role on SEEK."
```

---

## Step 6 — Find the Right Contact in Clay

Use **Clay Find People** with these title inputs depending on `contact_title_to_find`:

### If targeting CFO
```
Job titles to search:
CFO, Chief Financial Officer, Finance Director, Financial Controller, Head of Finance, VP Finance

Company: {{company_domain}}
Location: Australia
```

### If targeting CEO
```
Job titles to search:
CEO, Managing Director, Founder, Co-Founder, Owner, Director, Principal

Company: {{company_domain}}
Location: Australia
```

### If targeting Operations Manager
```
Job titles to search:
Operations Manager, General Manager, Head of Operations, COO, Director of Operations

Company: {{company_domain}}
Location: Australia
```

**If Clay Find People returns no result:**
→ Fallback to LinkedIn manual search
→ Or skip and route to LinkedIn-only DM track

---

## Step 7 — Email Template (SEEK Signal Version)

This replaces the generic Email 1 from campaign-strategy.md for SEEK-signal contacts.
The opener never mentions the job posting — it references the growth challenge instead.

### CFO Version (SEEK Signal)

```
Subject: it hire

{{first_name}},

{{personalized_opener}}

A full-time IT hire in Australia runs $90k–$110k + super + tools + leave cover — roughly $120k all-in before you factor in the gap when they're sick or on leave.

Managed IT typically covers the same scope at 30–50% less, with 24/7 monitoring included.

Worth running the actual numbers for {{company_name}}'s setup before committing?
```

### CEO Version (SEEK Signal)

```
Subject: it ceiling

{{first_name}},

{{personalized_opener}}

Most businesses hit the same fork: hire in-house or outsource. The hire path locks you into $90k+ salary + super + gaps in cover.

We run proactive managed IT for businesses at exactly this stage — typically less than the cost of the hire, with better coverage.

Worth a quick look at what that looks like for {{company_name}}?
```

---

## Step 8 — LinkedIn Outreach (Same Signal, Different Channel)

Run LinkedIn outreach in parallel with email. Send connection request the same day as Email 1.

### Connection Request Note (SEEK Signal)

```
{{first_name}}, saw {{company_name}} is growing — at your stage IT usually starts becoming a real pressure point. Work with businesses in this situation. Worth connecting?
```

*(Under 300 chars. No mention of SEEK or IT job posting.)*

### DM 1 (after connection accepted)

```
Hey {{first_name}}, thanks for connecting.

Quick one — at {{company_name}}'s current size, are you handling IT with an in-house person or external support?

Asking because we work with a lot of {{industry}} businesses at this stage and the answer usually shapes what makes sense for them.
```

---

## Step 9 — Ongoing Monitoring (Weekly Cadence)

Don't do this once — run it every week to keep a fresh Tier 1 pipeline flowing.

### Weekly SEEK Signal Workflow

```
Monday: Run all 8 SEEK searches (new listings from past 7 days only)
Monday: Export from Apify / Instant Data Scraper
Tuesday: Import to Clay, run enrichment (Steps 3–7)
Wednesday: Review send_ready contacts, upload to Smartlead
Wednesday: Send LinkedIn connection requests
Thursday–Friday: First emails go out (20–30/day per inbox)
Following week: Email 2 follows up automatically via Smartlead sequence
```

**Monthly volume estimate:** 50–150 new Tier 1 contacts/month from SEEK signal alone.

### Clay Auto-Update Option (Advanced)

Set up a Zapier or Make webhook:
```
Trigger: New Apify run completes (schedule: every Monday 8am)
Action: Auto-import CSV to Clay SEEK Signal table
Action: Clay auto-runs enrichment columns (if auto-update is ON)
```

This makes the whole signal flow automatic — zero manual imports after setup.

---

## Step 10 — Smartlead Campaign Upload

**Campaign:** IT-CFO-AUS or IT-CEO-AUS (determined by `campaign_track` formula)

**Upload mapping:**

| Clay column | Smartlead field |
|---|---|
| `first_name` | firstName |
| `last_name` | lastName |
| `work_email` | email |
| `company_name` | companyName |
| `job_title` | title |
| `personalized_opener` | customVar1 |
| `industry_clean` | customVar2 |
| `headcount` | customVar3 |
| `job_title_signal` | customVar4 (the IT role they posted) |

**In Smartlead email template:**
- `{{customVar1}}` = the personalised opener line
- `{{customVar4}}` = available if you ever want to reference role type (use carefully — don't say "IT Manager role")

---

## Expected Results — SEEK Signal Contacts

| Metric | SEEK Tier 1 | Cold Tier 3 |
|---|---|---|
| Open rate | 60–70% | 40–50% |
| Reply rate | 8–12% | 3–5% |
| Positive reply rate | 4–6% | 1–2% |
| Meetings per 100 contacts | 5–8 | 1–3 |

**Why:** These contacts are already in the buying decision. You're not creating demand — you're entering an existing conversation at the right moment.

---

## Quick Start Checklist

```
[ ] Install Instant Data Scraper (Chrome extension) — free, 5 min
[ ] Run first SEEK search: "IT Manager" + Australia + last 30 days
[ ] Export results (100–200 listings)
[ ] Clean CSV: remove IT companies, recruiters, blank names
[ ] Import to Clay
[ ] Run Steps 1–8 in clay-segmentation.md (conditional run order)
[ ] Upload first batch to Smartlead (aim for 50 send-ready contacts)
[ ] Send LinkedIn connection requests same day
[ ] Check replies after 48–72 hours
[ ] Repeat next Monday
```
