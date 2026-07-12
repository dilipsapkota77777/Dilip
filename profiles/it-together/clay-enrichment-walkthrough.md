# IT Together — Clay Enrichment Walkthrough
# SEEK Signal → Smartlead (33 companies, July 2026)
Generated: 2026-07-12 | Input: seek_signal_sendable.csv

---

## Overview

You have 33 clean companies from the SEEK signal scrape.
These are already Tier 1 — they are actively hiring IT staff, which means they are in-market.

**Goal:** Find the right decision-maker at each company, get their verified email, write a personalised opener, and push to Smartlead.

**Campaign split from CSV:**
- 9 rows → `IT-CFO-AUS` (IT Manager job postings → contact the CFO about cost)
- 24 rows → `IT-CEO-AUS` (IT Support / Sysadmin / Help Desk / Network / Coordinator / Head of IT / Cyber → contact the CEO about risk and productivity)

**Credit estimate for 33 rows:** ~250–420 Clay credits (~$5–$8)

---

## Step 0 — Create the Clay Table

1. Log in to Clay → click **New Workbook**
2. Name it: `IT Together — SEEK Signal — Jul 2026`
3. Click **Import** → **Upload CSV** → select `seek_signal_sendable.csv`
4. Map columns: all 11 columns auto-map (job_title, company_name, location, date_posted, search_query, signal, campaign_track, signal_source, signal_tier, exclude, exclude_reason)
5. Click **Import** — 33 rows loaded

> The `campaign_track` column from the CSV tells you which campaign to send to — **do not overwrite it**.

---

## Step 1 — Find Company Domain

**Enrichment:** Clay — Find Company (built-in)
**Credits:** 1–2 per row
**Input:** `company_name` + `location` (city)

**Setup:**
1. Click **Add Enrichment** → search **"Find Company"** → select Clay's native Find Company
2. Input: Company Name = `{{company_name}}`, Location = `{{location}}`
3. Map output: `company_domain`, `company_linkedin_url`
4. **No conditional needed** — all rows need a domain

**Expected output:** ~30/33 rows get a domain (a few small companies may not resolve)

---

## Step 2 — Company Enrichment via Apollo

**Enrichment:** Apollo — Enrich Company
**Credits:** 1–2 per row
**Input:** `company_domain`

**Setup:**
1. Click **Add Enrichment** → search **"Apollo"** → select **Enrich Company**
2. Input: Domain = `{{company_domain}}`
3. **Conditional run:** `{{company_domain}}` is not empty
4. Map outputs:
   - `headcount` ← Apollo Employee Count
   - `industry_raw` ← Apollo Industry
   - `apollo_revenue` ← Apollo Annual Revenue (optional)

**Expected:** ~27/33 rows get headcount. Small private firms (Bartley Cohen Legal, Talbot Family Law) may return nothing — that's fine.

---

## Step 3 — Add Formula Columns (0 credits, run immediately)

Add these as **Clayscript** formula columns. All are free.

### 3a — Industry Clean

**Column name:** `industry_clean`

```javascript
const raw = String({{industry_raw}} || "").toLowerCase().trim();

if (raw.includes("legal") || raw.includes("law firm") || raw.includes("solicitor")) return "Legal";
if (raw.includes("account") || raw.includes("bookkeep") || raw.includes("tax") || raw.includes("cpa")) return "Accounting";
if (raw.includes("financial") || raw.includes("finance") || raw.includes("insurance") || raw.includes("wealth") || raw.includes("investment")) return "Financial Services";
if (raw.includes("health") || raw.includes("medical") || raw.includes("clinic") || raw.includes("ndis") || raw.includes("aged care") || raw.includes("allied")) return "Healthcare";
if (raw.includes("construction") || raw.includes("building") || raw.includes("trade") || raw.includes("civil") || raw.includes("roof") || raw.includes("mining")) return "Construction & Resources";
if (raw.includes("real estate") || raw.includes("property") || raw.includes("reit")) return "Real Estate";
if (raw.includes("manufactur") || raw.includes("warehouse") || raw.includes("logistics") || raw.includes("supply chain") || raw.includes("ports")) return "Logistics & Industrial";
if (raw.includes("education") || raw.includes("school") || raw.includes("college")) return "Education";

return "Professional Services";
```

### 3b — Headcount Bucket

**Column name:** `headcount_bucket`

```javascript
const n = parseInt({{headcount}} || 0);
if (n === 0) return "Unknown";
if (n <= 10) return "1–10";
if (n <= 50) return "11–50";
if (n <= 100) return "51–100";
if (n <= 250) return "101–250";
return "250+";
```

### 3c — ICP Pass Gate

**Column name:** `icp_pass`
**Purpose:** Flags companies outside the 10–250 headcount ICP

```javascript
const n = parseInt({{headcount}} || 0);
if (n === 0) return "Unknown — check manually";
if (n < 10) return "Too small — skip";
if (n > 250) return "Too large — skip";
return "Pass";
```

> Filter out rows where `icp_pass` = "Too small — skip" or "Too large — skip" before continuing.
> "Unknown" rows: keep and continue — many smaller firms don't publish headcount.

---

## Step 4 — Find the Right Contact

This is the most important step. The contact to find depends on `campaign_track`.

| campaign_track | Who to find | Title keywords |
|---|---|---|
| `IT-CFO-AUS` | CFO / Finance lead | CFO, Chief Financial Officer, Finance Director, Financial Controller, Head of Finance |
| `IT-CEO-AUS` | CEO / owner | CEO, Managing Director, Founder, Co-Founder, Owner, Principal, Director |

**Enrichment:** Clay — Find People (or LinkedIn People Search)
**Credits:** 2–3 per row

**Setup — two separate enrichment columns:**

### Column A: CFO Contact (for IT-CFO-AUS rows only)

**Conditional run formula:**
```javascript
{{campaign_track}} === "IT-CFO-AUS" && {{company_domain}} !== ""
```

- Enrichment: **Clay Find People** or **Apollo Find People**
- Input: Company = `{{company_domain}}`, Title = "CFO OR Chief Financial Officer OR Finance Director OR Financial Controller OR Head of Finance"
- Output: `cfo_first_name`, `cfo_last_name`, `cfo_title`, `cfo_linkedin_url`
- Result limit: 1 person (top result)

### Column B: CEO Contact (for IT-CEO-AUS rows only)

**Conditional run formula:**
```javascript
{{campaign_track}} === "IT-CEO-AUS" && {{company_domain}} !== ""
```

- Enrichment: **Clay Find People** or **Apollo Find People**
- Input: Company = `{{company_domain}}`, Title = "CEO OR Managing Director OR Founder OR Owner OR General Manager"
- Output: `ceo_first_name`, `ceo_last_name`, `ceo_title`, `ceo_linkedin_url`
- Result limit: 1 person (top result)

### Column C: Merge Contact Fields (formula, 0 credits)

**Column name:** `contact_first_name`
```javascript
{{cfo_first_name}} || {{ceo_first_name}} || ""
```

**Column name:** `contact_last_name`
```javascript
{{cfo_last_name}} || {{ceo_last_name}} || ""
```

**Column name:** `contact_title`
```javascript
{{cfo_title}} || {{ceo_title}} || ""
```

**Column name:** `contact_linkedin_url`
```javascript
{{cfo_linkedin_url}} || {{ceo_linkedin_url}} || ""
```

**Column name:** `first_name` (cleaned)
```javascript
String({{contact_first_name}} || "").replace(/[^a-zA-Z- ]/g, "").trim().split(' ')[0]
```

---

## Step 5 — Email Waterfall

**Enrichment:** Work Email Waterfall (4 providers)
**Credits:** avg 4–8 per row (pay only until found)
**Expected coverage:** ~70–80% of rows with a known contact

**Setup:**
1. Click **Add Enrichment** → search **"Work Email"** → select **Find Work Email (Waterfall)**
2. Provider order (cheapest first):
   - **Provider 1:** LeadMagic (2 credits)
   - **Provider 2:** Prospeo (2 credits)
   - **Provider 3:** Hunter (2 credits)
   - **Provider 4:** Apollo (3 credits)
3. Inputs:
   - First Name = `{{first_name}}`
   - Last Name = `{{contact_last_name}}`
   - Company Domain = `{{company_domain}}`
   - LinkedIn URL = `{{contact_linkedin_url}}` (improves precision)
4. **Conditional run:** `{{first_name}}` is not empty AND `{{company_domain}}` is not empty
5. Output: `leadmagic_email`, `prospeo_email`, `hunter_email`, `apollo_email`

### Email Waterfall Merge (formula, 0 credits)

**Column name:** `work_email`
```javascript
{{leadmagic_email}} || {{prospeo_email}} || {{hunter_email}} || {{apollo_email}} || ""
```

---

## Step 6 — Email Verification (MillionVerifier)

**Enrichment:** MillionVerifier — Verify Email
**Credits:** 1 per row
**Conditional run:** `{{work_email}}` is not empty

**Setup:**
1. Click **Add Enrichment** → search **"MillionVerifier"**
2. Input: Email = `{{work_email}}`
3. Output: `email_verified` (returns: valid / catch-all / invalid / unknown)

**Disposition:**
- `valid` → send
- `catch-all` → send (most Australian SME domains are catch-all)
- `invalid` → do not send, mark for removal
- `unknown` → hold, try again or skip

---

## Step 7 — Current IT Vendor Check (Claygent, optional)

**Column:** `current_it_vendor`
**Credits:** 2–3 per row
**Conditional run:** `{{company_domain}}` is not empty AND `{{icp_pass}}` = "Pass"

This is optional but valuable — if they already have IT Together as a vendor, skip them.
If they have a known competitor (Brennan IT, Macquarie Cloud, etc.), note it for the email angle.

```
You are a research assistant. Visit the website {{company_domain}} and their LinkedIn company page.

Look for any mention of their current IT provider, managed IT company, technology partner, or IT support vendor.

Check:
1. Website footer or "partners" / "technology" page
2. LinkedIn company posts or "about" section
3. Any case studies or testimonials mentioning IT providers

Instructions:
- If you find a named IT vendor: return the vendor name (e.g., "Brennan IT", "Macquarie Cloud")
- If no IT vendor mentioned: return "None found"
- If unable to check: return "Unknown"

Return only the vendor name, "None found", or "Unknown". No explanation.
```

**Post-run filter:** Remove any row where `current_it_vendor` = "IT Together" (existing client, do not send).

---

## Step 8 — Personalized Opener (GPT-4 Mini)

**Column:** `personalized_opener`
**Model:** GPT-4 Mini (not GPT-4 — 10x cheaper, same quality for one-liners)
**Credits:** ~1 per row
**Conditional run:** `{{work_email}}` is not empty AND `{{email_verified}}` != "invalid"

Use a **branching Claygent** — run the CFO prompt for IT-CFO-AUS rows, CEO prompt for IT-CEO-AUS rows.

The simplest way: add two separate Claygent columns with conditional runs, then merge.

### Column: `opener_cfo` (conditional: campaign_track = IT-CFO-AUS)

```
Write one opening sentence for a cold email to {{first_name}}, {{contact_title}} at {{company_name}}, a {{industry_clean}} business with approximately {{headcount}} staff.

Context: They just posted an IT Manager or Head of IT job on SEEK — meaning they're about to take on a new IT hire.

Angle: For a finance leader at a {{headcount}}-person firm, that hire will cost $90–130k/yr in salary alone before laptop, software, and downtime. Most CFOs don't realise managed IT at this headcount runs $24–60k/yr for the same or better coverage.

Rules:
- Under 20 words
- Conversational, not formal
- Do NOT mention "SEEK", "job posting", "recruitment", or "AI"
- Do NOT mention "IT Together", "managed IT", or any product
- Lead with an observation about their situation — not a pitch
- Plain text, no punctuation tricks

Example: "Most CFOs I speak to at firms this size haven't run the actual numbers on their IT setup."
```

### Column: `opener_ceo` (conditional: campaign_track = IT-CEO-AUS)

```
Write one opening sentence for a cold email to {{first_name}}, {{contact_title}} at {{company_name}}, a {{industry_clean}} business with approximately {{headcount}} staff.

Context: They just posted an IT support or systems role on SEEK — meaning they're about to try solving their IT problems by hiring internally.

Angle: At {{headcount}} staff, IT usually becomes a real overhead — a full-time person costs $70–90k and still can't cover after-hours, cybersecurity, or infrastructure without outside help.

Rules:
- Under 20 words
- Conversational, plain
- Do NOT mention "SEEK", "job posting", or "recruitment"
- Do NOT mention "IT Together", "managed IT", or any product name
- Lead with an observation about business growth or operations — not a pitch
- Avoid the word "IT" if possible — use "tech", "systems", or "setup" instead

Example: "Most founders at this stage tell me their tech setup is fine — until it isn't."
```

### Merge Opener (formula, 0 credits)

**Column:** `personalized_opener`
```javascript
{{opener_cfo}} || {{opener_ceo}} || ""
```

---

## Step 9 — Send Ready Gate (formula, 0 credits)

**Column:** `send_ready`

```javascript
const email = String({{work_email}} || "").trim();
const verified = String({{email_verified}} || "").toLowerCase();
const track = String({{campaign_track}} || "");
const firstName = String({{first_name}} || "").trim();
const company = String({{company_name}} || "").trim();
const opener = String({{personalized_opener}} || "").trim();

const hasEmail = email.includes("@") && email.includes(".");
const isVerified = verified === "valid" || verified === "catch-all";
const hasTrack = track !== "SKIP" && track !== "" && track !== "undefined";
const hasName = firstName.length > 1;
const hasCompany = company.length > 1;
const hasOpener = opener.length > 5;

return (hasEmail && isVerified && hasTrack && hasName && hasCompany && hasOpener).toString();
```

---

## Step 10 — Table Views to Create

| View name | Filter | Purpose |
|---|---|---|
| All Companies | None | Master view |
| CFO Track | campaign_track = IT-CFO-AUS | Review the 9 CFO rows |
| CEO Track | campaign_track = IT-CEO-AUS | Review the 24 CEO rows |
| Send Ready | send_ready = true | Export batch |
| Email Issues | work_email is empty | Fix or skip |
| Outside ICP | icp_pass contains "skip" | Remove before send |

---

## Step 11 — Export to Smartlead

**Filter:** `send_ready` = "true"

**Clay → Smartlead Push (native integration):**
1. Click **Add Enrichment** → search **"Smartlead"** → select **Add Lead to Campaign**
2. Conditional run: `{{send_ready}}` = "true"
3. Field mapping:

| Clay column | Smartlead field |
|---|---|
| `first_name` | firstName |
| `contact_last_name` | lastName |
| `work_email` | email |
| `company_name` | companyName |
| `contact_title` | title |
| `campaign_track` | → Map to campaign ID (see below) |
| `personalized_opener` | customVariable1 |
| `industry_clean` | customVariable2 |
| `headcount` | customVariable3 |
| `signal_tier` | customVariable4 |
| `signal` | customVariable5 |

**Campaign ID mapping:**
- `IT-CFO-AUS` → your Smartlead campaign ID for the CFO track
- `IT-CEO-AUS` → your Smartlead campaign ID for the CEO track

**In your Smartlead email templates, reference:**
- `{{firstName}}` — their first name
- `{{companyName}}` — company
- `{{customVariable1}}` — the personalized opener line (first sentence of email 1)
- `{{customVariable2}}` — industry ("companies in {{customVariable2}}")
- `{{customVariable3}}` — headcount (for cost comparison personalisation)

---

## Credit Budget (33 rows)

| Step | Provider | Credits/row | Rows | Total |
|---|---|---|---|---|
| Find Company Domain | Clay native | 1–2 | 33 | 33–66 |
| Apollo Company Enrich | Apollo | 1–2 | 33 | 33–66 |
| Find CFO Contact | Apollo/Clay People | 2–3 | 9 | 18–27 |
| Find CEO Contact | Apollo/Clay People | 2–3 | 24 | 48–72 |
| Email Waterfall (4 providers) | LM/Prospeo/Hunter/Apollo | avg 5 | ~30 | 150 |
| MillionVerifier | MillionVerifier | 1 | ~25 | 25 |
| IT Vendor Claygent (optional) | GPT-4 Mini | 2–3 | 30 | 60–90 |
| Opener GPT-4 Mini | GPT-4 Mini | 1 | ~22 | 22 |
| **Total** | | | | **~389–518 credits** |

At typical Clay pricing (~$0.01–$0.02/credit): **~$4–$10 for the full 33-row run**

---

## Run Order Summary

```
1.  Import seek_signal_sendable.csv → 33 rows
2.  Add formula columns: industry_clean, headcount_bucket, icp_pass (all 0 credits)
3.  Run: Find Company Domain (conditional: always)
4.  Run: Apollo Company Enrich (conditional: domain not empty)
5.  Filter view: remove icp_pass = "Too small" or "Too large"
6.  Run: Find CFO Contact (conditional: campaign_track = IT-CFO-AUS)
7.  Run: Find CEO Contact (conditional: campaign_track = IT-CEO-AUS)
8.  Add formula: contact_first_name, contact_last_name, contact_title, first_name (merged + cleaned)
9.  Run: Email Waterfall (conditional: first_name not empty AND domain not empty)
10. Add formula: work_email (merge waterfall outputs)
11. Run: MillionVerifier (conditional: work_email not empty)
12. [Optional] Run: Claygent IT Vendor (conditional: domain not empty)
13. Run: opener_cfo Claygent (conditional: campaign_track = IT-CFO-AUS AND email not empty)
14. Run: opener_ceo Claygent (conditional: campaign_track = IT-CEO-AUS AND email not empty)
15. Add formula: personalized_opener (merge opener_cfo + opener_ceo)
16. Add formula: send_ready
17. Filter to send_ready = true → export or push to Smartlead
```

**Expected final output:** ~18–25 send-ready contacts from 33 companies
