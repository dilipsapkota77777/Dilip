# IT Together — List Building Guide
Generated: 2026-07-12 | Framework: ColdIQ + List Building Master Skill
Target: Australian businesses, 10–250 headcount, needing managed IT
Campaign type: LinkedIn + Email | Multi-persona: CFO / CEO / IT Manager / Ops

---

## Target Universe (Australia)

| Segment | Estimated companies | Estimated contacts (per persona) |
|---|---|---|
| Professional Services 10–250 staff | ~85,000 | ~255,000 |
| Legal firms 10–250 staff | ~8,000 | ~24,000 |
| Accounting/Finance 10–250 staff | ~12,000 | ~36,000 |
| Healthcare/NDIS 10–250 staff | ~22,000 | ~66,000 |
| Construction 10–250 staff | ~30,000 | ~90,000 |
| Recruitment 10–250 staff | ~6,000 | ~18,000 |
| Real Estate agencies 10–250 staff | ~9,000 | ~27,000 |
| Manufacturing/Logistics 10–250 staff | ~14,000 | ~42,000 |
| **Total reachable universe** | **~186,000** | **~500,000+** |

**Practical starting list size:** 2,000–5,000 contacts for first campaign run.
**Sweet spot headcount:** 20–100 employees (in-house IT is too expensive, managed IT is ideal fit).

---

## Signal Priority — Build in This Order

| Tier | Signal | Why | Est. contacts |
|---|---|---|---|
| **Tier 1** | Company posting IT role on SEEK | In-market: considering hiring in-house IT — intercept with managed IT pitch | 200–500/month |
| **Tier 1** | Company with no IT vendor mentioned on website/LinkedIn | Gap to fill immediately | Variable |
| **Tier 2** | Company headcount grew 20%+ in 12 months | IT strain is imminent | Thousands |
| **Tier 2** | CFO or Operations Manager recently appointed | New leader reviewing vendor stack | Hundreds/month |
| **Tier 3** | No signal — cold ICP match only | Firmographic fit only | Unlimited |

**Run Tier 1 first, Tier 2 second, Tier 3 only after testing Tier 1/2.**

---

## Source 1 — SEEK Job Signals (Tier 1 — Highest Priority)

**Why:** Companies posting IT roles are actively considering hiring in-house IT. This is the highest-intent signal for managed IT outreach — intercept them *before* they hire.

### SEEK Search Strategy

Go to seek.com.au and run these searches to find in-market companies:

| Search query | Signal meaning | CTA angle |
|---|---|---|
| "IT Manager" + Australia | Considering $90k+ IT hire — show cost comparison | CFO/CEO email, Do the Math |
| "IT Support" + Australia | Scaling IT needs, ad-hoc is breaking | CFO/CEO email |
| "Systems Administrator" + Australia | Growing IT infrastructure burden | IT Manager email |
| "Help Desk" OR "Helpdesk" + Australia | Volume of support tickets overwhelming | Ops Manager email |
| "Network Engineer" + Australia | Scaling network needs | IT Manager/CEO email |
| "Cybersecurity" + Australia | Proactive security focus — upsell angle | CEO email |

### SEEK Scraping Workflow

**Tool:** Apify SEEK scraper ($5–15/run) or Instant Data Scraper (free Chrome extension)

```
Step 1: Run SEEK search for target IT role
Step 2: Scrape job listings — extract: company name, company size (if shown), location, post date
Step 3: Export CSV → import to Clay
Step 4: Clay enrichment — find company domain (Clearbit/Apollo)
Step 5: Claygent — confirm it's an IT role posting (not internal IT company)
Step 6: Find CFO/CEO contact via Sales Navigator or Apollo
Step 7: Tag signal_tier = "Tier 1" + signal_source = "SEEK_IT_HIRE"
Step 8: Load into IT-CFO-AUS or IT-CEO-AUS Smartlead campaign
```

**Volume estimate:** 50–200 new companies/month posting IT roles in Australia.
**Conversion expectation:** 3–5x higher reply rate vs cold Tier 3 contacts.

---

## Source 2 — LinkedIn Sales Navigator

**Best for:** Finding the right *person* at each target company, persona filtering, Australian professional market.

### Account Search Filters (Find Target Companies First)

```
Geography: Australia
Headcount: 11–250
Industry: [See list below]
Exclude: Information Technology, Telecommunications, Government Administration, Military
```

**Industries to include:**
- Legal Services
- Accounting
- Financial Services
- Hospital & Health Care
- Construction
- Real Estate
- Staffing & Recruiting
- Logistics & Supply Chain
- Education Management
- Insurance
- Retail
- Facilities Services

### People Search Boolean Formulas (per persona)

**Persona A — CFO / Finance Director**
```
Title boolean:
("CFO" OR "Chief Financial Officer" OR "Finance Director" OR "VP Finance" OR "Head of Finance" OR "Financial Controller" OR "Controller" OR "Director of Finance") NOT (intern OR student OR assistant OR "non-executive")

Filters:
- Geography: Australia
- Headcount: 11–250
- Seniority: Director, VP, CXO, Partner, Owner
- Industries: [exclude IT/Telco/Gov]
```

**Persona B — CEO / Managing Director / Founder**
```
Title boolean:
("CEO" OR "Chief Executive" OR "Managing Director" OR "Founder" OR "Co-Founder" OR "Owner" OR "Principal" OR "Managing Partner") NOT (intern OR student OR "non-executive" OR "board member")

Filters:
- Geography: Australia
- Headcount: 11–100 (CEOs at 100–250 are harder to reach, deprioritise)
- Seniority: Owner, Partner, CXO
```

**Persona C — IT Manager / Head of IT**
```
Title boolean:
("IT Manager" OR "Head of IT" OR "IT Director" OR "Director of IT" OR "Technology Manager" OR "Systems Manager" OR "Infrastructure Manager" OR "Head of Technology" OR "CTO" OR "Chief Technology Officer" OR "IT Lead") NOT (intern OR student OR analyst)

Filters:
- Geography: Australia
- Headcount: 20–250 (smaller companies won't have dedicated IT Manager)
- Seniority: Manager, Director, CXO
```

**Persona D — Operations Manager**
```
Title boolean:
("Operations Manager" OR "Head of Operations" OR "General Manager" OR "Director of Operations" OR "VP Operations" OR "COO" OR "Chief Operating Officer") NOT (intern OR student OR assistant)

Filters:
- Geography: Australia
- Headcount: 15–250
- Seniority: Manager, Director, VP, CXO
```

### Bypassing the 2,500 Results Cap

If any search exceeds 2,500 results, segment by:

1. **State** — NSW / VIC / QLD / WA / SA / ACT / NT / TAS (run 8 separate searches)
2. **Industry** — Split into 4 industry groups and run separately
3. **Headcount** — 11–50 / 51–150 / 151–250

### Export Tool

**Recommended:** Evaboot ($29–99/month)
- Clean Sales Nav export with email enrichment
- Removes job changers automatically
- Better data quality than PhantomBuster for Australian contacts

**Alternative:** Apollo.io (if already subscribed — cross-reference with Sales Nav)

---

## Source 3 — Apollo.io (Volume + Email Discovery)

**Best for:** Broad Australian company discovery, email finding, supplementing Sales Nav gaps.

### Apollo Search Setup

```
Filters:
- Country: Australia
- Employees: 10–250
- Titles: [same boolean terms as Sales Nav, adapted for Apollo filters]
- Exclude industries: Information Technology, Telecommunications, Government
- Has email: Yes
- Email status: Verified or Likely valid
```

### Apollo Workflow

```
Step 1: Run search with filters above
Step 2: Sort by "Last updated" (freshest data first)
Step 3: Export in batches of 500 (better quality than bulk export)
Step 4: Import to Clay for enrichment
Step 5: Run MillionVerifier on all emails before sending
Step 6: Merge with Sales Nav list — deduplicate on email + LinkedIn URL
```

**Volume estimate:** 5,000–20,000 Australian contacts matching ICP filters.
**Email find rate:** ~60–70% (supplement with waterfall for remaining 30%).

---

## Source 4 — Australian Business Directories (Supplementary)

### Yellow Pages Australia (yellowpages.com.au)

**Best for:** Finding SMBs with 10–50 staff that aren't well-represented on LinkedIn/Apollo.

```
Search: [Industry keyword] + [City/State]
Scrape: Instant Data Scraper (Chrome extension, free)
Extract: Business name, phone, website, address
Import: CSV → Clay → find contacts via Clay Find People
```

**Target categories:**
- Accountants → find CFO/Partner
- Law firms → find Managing Partner/Operations Manager
- Construction companies → find GM/Operations Manager
- Medical centres → find Practice Manager/GM

### ABN Lookup (abn.business.gov.au)

**Best for:** Verifying Australian company legitimacy, finding ABN, registered business name.

```
Use in Clay Claygent:
"Look up the ABN for {{company_name}} on abn.business.gov.au.
Return: ABN, entity type (Pty Ltd / Trust / Partnership), registration state, active/cancelled status.
If not found, return 'Not found'."
```

**Use case:** Validate that contact's company is a real, active Australian business before spending credits.

### Industry Associations (Australia-specific)

| Association | Members | Relevance |
|---|---|---|
| Law Institute of Victoria | Victorian law firms | Legal segment |
| NSW Law Society | NSW legal | Legal segment |
| CPA Australia | Accounting firms | Accounting segment |
| RCSA (Recruitment industry) | Staffing/recruitment | Recruitment segment |
| HIA (Housing Industry Assoc.) | Construction/builders | Construction segment |
| Master Builders Australia | Construction companies | Construction segment |
| AIIA (Australian IT Industry) | Tech companies | Exclude — IT competitors |
| Property Council of Australia | Real estate firms | Real estate segment |

**Access:** Most publish member directories (some require membership, some are public). Scrape public-facing directories with Instant Data Scraper.

---

## Source 5 — Google Maps (Local + SMB Discovery)

**Best for:** Finding local professional services businesses not captured in LinkedIn/Apollo.

### Apify Google Maps Scraper

**Tool:** Apify Google Maps Reviews Scraper (~$5/run for 1,000 businesses)

```
Search queries to run:
- "accounting firm" + "Sydney" / "Melbourne" / "Brisbane" / "Perth"
- "law firm" + [major Australian cities]
- "recruitment agency" + [cities]
- "construction company" + [cities]
- "medical centre" + [cities]

Extract: Business name, website, phone, address, rating, review count, category
Import: CSV → Clay → enrich with headcount + find contacts
```

**Filter after scraping:**
- Remove: 1–2 star rating (distressed businesses, harder close)
- Keep: 10+ Google reviews (established, with budget)
- Headcount filter: Check if company has 10–250 employees via Clay enrichment

---

## Source 6 — SEEK Company Pages (Headcount Signal)

**Why underused:** SEEK shows company headcount on company profile pages — free data, no scraping needed.

```
Manual workflow:
1. Go to seek.com.au/companies
2. Search by industry
3. Filter: company size 11–200
4. Extract: company name, size, industry, website
5. Import to Clay → find decision maker contacts

Or: Use Apify SEEK Company Scraper (automated)
```

---

## Full Clay Workflow — Step by Step

### Table Setup

```
Column order:
1. company_name (Text)
2. company_domain (Text)
3. company_linkedin_url (Text)
4. source (Text) — track where each row came from
5. signal (Text) — SEEK_IT_HIRE / NO_VENDOR / GROWTH / COLD
6. first_name (Text)
7. last_name (Text)
8. job_title (Text)
9. contact_linkedin_url (Text)
10. headcount (Number)
11. industry_raw (Text)
12. industry_clean (Formula — from clay-segmentation.md)
13. segment (Formula — from clay-segmentation.md)
14. signal_tier (Formula — from clay-segmentation.md)
15. hiring_it_role (Claygent)
16. current_it_vendor (Claygent)
17. work_email (Waterfall)
18. email_verified (MillionVerifier)
19. personalized_opener (GPT-4 Mini)
20. campaign_track (Formula)
21. send_ready (Formula)
```

### Run Order (credit-safe)

```
Step 1:  Import CSV from Apollo/Sales Nav/SEEK — populate company + contact basics
Step 2:  Run industry_clean formula (0 credits)
Step 3:  Run segment formula (0 credits)
Step 4:  STOP — manual review: remove segment = UNKNOWN, remove IT companies
Step 5:  Enrich headcount if empty — Apollo ($1–2/row, conditional: only if headcount is blank)
Step 6:  Run hiring_it_role Claygent ($2–3/row, conditional: headcount >= 10 AND source != "SEEK")
         [Skip if source = "SEEK_IT_HIRE" — you already know they're hiring IT]
Step 7:  Run current_it_vendor Claygent ($2–3/row, conditional: segment != UNKNOWN)
Step 8:  Run signal_tier formula (0 credits)
Step 9:  STOP — filter: remove signal_tier = Tier 3 before running email waterfall
Step 10: Email waterfall (Prospeo → Apollo → Hunter → RocketReach) — ($3–5/row, Tier 1+2 only)
Step 11: MillionVerifier ($0.001/row, conditional: work_email is not empty)
Step 12: Run personalized_opener GPT-4 Mini ($1/row, conditional: email_verified = valid)
Step 13: Run send_ready formula (0 credits)
Step 14: Export: send_ready = true → Smartlead upload
```

### Credit Budget Estimate

| List size | Tier 1 + 2 (full enrichment) | Tier 3 (skipped) | Total spend est. |
|---|---|---|---|
| 500 contacts | 300 × 15 credits = 4,500 | 200 × 3 = 600 | ~5,100 credits |
| 2,000 contacts | 1,200 × 15 = 18,000 | 800 × 3 = 2,400 | ~20,400 credits |
| 5,000 contacts | 3,000 × 15 = 45,000 | 2,000 × 3 = 6,000 | ~51,000 credits |

**Clay plan recommendation:** Starter ($149/mo) for first run. Scale to Explorer ($349/mo) once workflow is confirmed.

---

## Email Waterfall Setup (in Clay)

Run providers in this order — cheapest first, most expensive last:

| Order | Provider | Cost | Coverage |
|---|---|---|---|
| 1 | Prospeo | ~$0.01/email | 40–50% hit rate |
| 2 | Apollo | ~$0.05–0.10/email | +15–20% |
| 3 | Hunter.io | ~$0.05/email | +5–10% |
| 4 | RocketReach | ~$0.10–0.20/email | +5% |
| 5 | Datagma | ~$0.05/email | +3–5% |

**Conditional formula for waterfall:**
```javascript
// Run Prospeo first
// If Prospeo email is empty, run Apollo
// If Apollo email is empty, run Hunter
// etc.
const prospeo = String({{prospeo_email}} || "").trim();
const apollo = String({{apollo_email}} || "").trim();
const hunter = String({{hunter_email}} || "").trim();

if (prospeo.includes("@")) return prospeo;
if (apollo.includes("@")) return apollo;
if (hunter.includes("@")) return hunter;
return "";
```

**Target coverage:** 75–85% email find rate with 4-provider waterfall.

---

## Deduplication Rules

When merging Apollo + Sales Nav + SEEK sources:

| Dedup rule | Field to match on |
|---|---|
| Primary | `contact_linkedin_url` (most reliable unique ID) |
| Secondary | `work_email` (if LinkedIn URL missing) |
| Fallback | `first_name` + `last_name` + `company_domain` |

**In Clay:** Use the deduplication column feature (Settings → Deduplicate rows).
**Field priority when merging:** LinkedIn URL > Apollo ID > SEEK source.

---

## Volume & Timeline Plan

### Month 1 — Test Run (500 contacts)

| Week | Action | Output |
|---|---|---|
| Week 1 | SEEK scrape — find 50 companies posting IT roles | 50 companies |
| Week 1 | Find CFO/CEO contact for each via Sales Nav | 50 contacts (Tier 1) |
| Week 2 | Apollo pull — 450 Australian contacts, ICP filtered | 450 contacts (Tier 2/3) |
| Week 2 | Run Clay enrichment on all 500 | Enriched list |
| Week 3 | Email waterfall + verify | ~375 sendable emails (75%) |
| Week 3 | Upload to Smartlead — start sending 40/day | Campaign live |
| Week 4 | Review replies, optimise subject lines | Data to improve |

**Expected output from 500 contacts:**
- Sendable: ~375
- Opens (55%): ~206
- Replies (5%): ~19
- Positive replies (2%): ~8
- Meetings booked: 3–5

---

### Month 2–3 — Scale (2,000+ contacts)

```
Source breakdown:
- SEEK IT hiring signals: 100–200/month ongoing
- Sales Navigator (by state): 500/month
- Apollo ICP pull: 1,000/month
- Australian directories (Yellow Pages / industry assoc): 200–300/month

Total monthly volume: ~1,800–2,500 new contacts
```

---

## Quality Gates — What to Remove Before Sending

Remove any contact where:

| Condition | Action |
|---|---|
| `email_verified` = invalid or risky | Remove — never send to invalid emails |
| `segment` = UNKNOWN | Move to manual review or discard |
| `headcount` < 10 | Remove — too small for managed IT |
| `headcount` > 250 | Move to separate enterprise track |
| `industry_clean` = Technology | Remove — likely IT companies (competitors/irrelevant) |
| `company_domain` contains ittogether | Remove — own company |
| `work_email` is empty after waterfall | Move to LinkedIn-only outreach |
| `first_name` is empty or = "Unknown" | Remove — can't personalise |

---

## LinkedIn-Only Track (No Email Found)

For contacts where the email waterfall returns empty — route to LinkedIn-only:

```
Step 1: Send connection request (personalised note from campaign-strategy.md)
Step 2: Wait for acceptance
Step 3: DM sequence (3 DMs over 20 days — from campaign-strategy.md)
Step 4: If no reply after DM 3 — remove from active outreach
```

**Volume expectation:** ~15–25% of list will be LinkedIn-only (no verified email found).

---

## Tools Summary

| Tool | Purpose | Cost |
|---|---|---|
| LinkedIn Sales Navigator | Boolean contact search | $99–150/mo |
| Evaboot | Sales Nav export | $29–99/mo |
| Apollo.io | Company + contact database | Free–$119/mo |
| Clay | Enrichment + segmentation + AI | $149–349/mo |
| Apify | SEEK + Google Maps scraping | $5–50/run |
| Instant Data Scraper | Free Chrome scraper | Free |
| Prospeo | Email finding (waterfall #1) | Pay-per-use |
| Hunter.io | Email finding (waterfall #3) | $49–99/mo |
| MillionVerifier | Email verification | $50 per 50k |
| Smartlead | Sending + sequencing | $59–149/mo |

**Minimum viable stack (Month 1):**
Apollo ($49/mo) + Clay Starter ($149/mo) + MillionVerifier ($50 one-time) + Smartlead ($59/mo) = **~$307/mo** to run the first campaign end-to-end.
