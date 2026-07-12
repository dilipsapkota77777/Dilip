# IT Together — Clay Segmentation & Enrichment Formulas
Generated: 2026-07-12 | Framework: Clayscript (JavaScript) + Claygent prompts
Purpose: Route each contact to the correct campaign track and personalise at scale

---

## Table Setup Overview

### Columns Required (in order)

| Column Name | Type | Source | Credits |
|---|---|---|---|
| `first_name` | Text | Import / LinkedIn | 0 |
| `last_name` | Text | Import / LinkedIn | 0 |
| `job_title` | Text | Import / LinkedIn | 0 |
| `company_name` | Text | Import | 0 |
| `company_domain` | Text | Import / Clearbit | 0 |
| `company_linkedin_url` | Text | Import / LinkedIn | 0 |
| `headcount` | Number | Apollo / LinkedIn | 1–2 |
| `industry_raw` | Text | Apollo / LinkedIn | 1–2 |
| `industry_clean` | Formula | Clayscript | 0 |
| `segment` | Formula | Clayscript | 0 |
| `atl_btl` | Formula | Clayscript | 0 |
| `hiring_it_role` | Text | Claygent | 2–3 |
| `current_it_vendor` | Text | Claygent | 2–3 |
| `signal_tier` | Formula | Clayscript | 0 |
| `campaign_track` | Formula | Clayscript | 0 |
| `email_subject` | Formula | Clayscript | 0 |
| `personalized_opener` | Text | GPT-4 Mini via Clay | 1 |
| `email_1_body` | Formula | Clayscript | 0 |
| `work_email` | Text | Email waterfall | 3–5 |
| `email_verified` | Text | MillionVerifier | 1 |
| `send_ready` | Formula | Clayscript | 0 |

**Estimated total credits per row: 12–20**
**Run conditional formulas first — never run enrichment on empty or irrelevant rows.**

---

## Formula 1 — Industry Cleaner

**Column:** `industry_clean`
**Type:** Clayscript formula (0 credits)
**Purpose:** Normalises raw industry names into 6 clean segments for routing

```javascript
const raw = String({{industry_raw}} || "").toLowerCase().trim();

if (raw.includes("legal") || raw.includes("law firm") || raw.includes("solicitor")) return "Legal";
if (raw.includes("account") || raw.includes("bookkeep") || raw.includes("tax") || raw.includes("cpa")) return "Accounting";
if (raw.includes("financial") || raw.includes("finance") || raw.includes("insurance") || raw.includes("wealth") || raw.includes("investment")) return "Financial Services";
if (raw.includes("health") || raw.includes("medical") || raw.includes("clinic") || raw.includes("ndis") || raw.includes("aged care") || raw.includes("allied")) return "Healthcare";
if (raw.includes("construction") || raw.includes("building") || raw.includes("trade") || raw.includes("plumb") || raw.includes("electr") || raw.includes("civil")) return "Construction";
if (raw.includes("recruit") || raw.includes("staffing") || raw.includes("labour hire")) return "Recruitment";
if (raw.includes("real estate") || raw.includes("property") || raw.includes("convey")) return "Real Estate";
if (raw.includes("manufactur") || raw.includes("warehouse") || raw.includes("logistics") || raw.includes("supply chain")) return "Manufacturing";
if (raw.includes("retail") || raw.includes("ecommerce") || raw.includes("e-commerce")) return "Retail";
if (raw.includes("education") || raw.includes("training") || raw.includes("school") || raw.includes("university")) return "Education";
if (raw.includes("tech") || raw.includes("software") || raw.includes("saas") || raw.includes("it ") || raw.includes("digital")) return "Technology";

return "Professional Services";
```

---

## Formula 2 — Segment Router

**Column:** `segment`
**Type:** Clayscript formula (0 credits)
**Purpose:** Routes contact to CFO / CEO / IT_MANAGER / OPS_MANAGER / UNKNOWN

```javascript
const title = String({{job_title}} || "").toLowerCase().trim();

// CFO / Finance track
const cfoTerms = ["cfo", "chief financial", "finance director", "vp finance", "head of finance",
  "financial controller", "controller", "finance manager", "vp of finance", "director of finance"];
if (cfoTerms.some(t => title.includes(t))) return "CFO";

// IT Manager track
const itTerms = ["it manager", "head of it", "it director", "director of it", "it lead",
  "technology manager", "systems manager", "infrastructure manager", "head of technology",
  "chief technology", "cto", "it operations", "it operations manager"];
if (itTerms.some(t => title.includes(t))) return "IT_MANAGER";

// Operations Manager track
const opsTerms = ["operations manager", "head of operations", "ops manager", "vp operations",
  "director of operations", "chief operating", "coo", "general manager"];
if (opsTerms.some(t => title.includes(t))) return "OPS_MANAGER";

// CEO / MD / Founder track
const ceoTerms = ["ceo", "chief executive", "managing director", " md", "founder",
  "co-founder", "cofounder", "owner", "principal", "president", "managing partner", "partner"];
if (ceoTerms.some(t => title.includes(t))) return "CEO";

return "UNKNOWN";
```

---

## Formula 3 — ATL vs BTL Split

**Column:** `atl_btl`
**Type:** Clayscript formula (0 credits)
**Purpose:** Determines messaging tone — strategic (ATL) vs tactical (BTL)

```javascript
const segment = String({{segment}} || "");
const atl = ["CEO", "CFO"];
const btl = ["IT_MANAGER", "OPS_MANAGER"];

if (atl.includes(segment)) return "ATL";
if (btl.includes(segment)) return "BTL";
return "SKIP";
```

---

## Formula 4 — Signal Tier

**Column:** `signal_tier`
**Type:** Clayscript formula (0 credits) — depends on `hiring_it_role` and `current_it_vendor` columns
**Purpose:** Prioritises contacts for send order (Tier 1 = hottest, send first)

```javascript
const hiringIT = String({{hiring_it_role}} || "").toLowerCase();
const itVendor = String({{current_it_vendor}} || "").toLowerCase().trim();
const growth = parseInt({{headcount}} || 0);

const isHiringIT = hiringIT.includes("yes") || hiringIT.includes("true");
const noVendor = itVendor === "" || itVendor === "none" || itVendor === "n/a" || itVendor === "unknown";
const isGrowing = growth >= 25;

if (isHiringIT) return "Tier 1";          // Actively considering in-house IT = high intent
if (noVendor && isGrowing) return "Tier 1";  // No vendor + growing = urgent gap
if (noVendor) return "Tier 2";            // No vendor but smaller/stable
if (isGrowing) return "Tier 2";           // Growing but has vendor — intercept
return "Tier 3";                           // Cold, send last
```

---

## Formula 5 — Campaign Track Assignment

**Column:** `campaign_track`
**Type:** Clayscript formula (0 credits)
**Purpose:** Returns the Smartlead campaign name to enroll this contact in

```javascript
const segment = String({{segment}} || "");

const tracks = {
  "CFO": "IT-CFO-AUS",
  "CEO": "IT-CEO-AUS",
  "IT_MANAGER": "IT-OPS-AUS",
  "OPS_MANAGER": "IT-OPS-AUS"
};

return tracks[segment] || "SKIP";
```

**If `campaign_track` returns "SKIP" or `segment` = "UNKNOWN" — do not enroll. Move to manual review.**

---

## Formula 6 — Email Subject Auto-Selector

**Column:** `email_subject`
**Type:** Clayscript formula (0 credits)
**Purpose:** Pre-fills the correct subject line for Smartlead merge tag

```javascript
const segment = String({{segment}} || "");
const tier = String({{signal_tier}} || "");

// Tier 1 contacts (hiring IT signal) get urgency-adjacent subject
if (tier === "Tier 1") {
  const t1subjects = {
    "CFO": "it hire",
    "CEO": "it risk",
    "IT_MANAGER": "constant fires",
    "OPS_MANAGER": "it ceiling"
  };
  return t1subjects[segment] || "quick question";
}

// Tier 2 / 3 default subjects
const subjects = {
  "CFO": "it spend",
  "CEO": "it risk",
  "IT_MANAGER": "constant fires",
  "OPS_MANAGER": "it ceiling"
};

return subjects[segment] || "quick question";
```

---

## Formula 7 — Send Ready Gate

**Column:** `send_ready`
**Type:** Clayscript formula (0 credits)
**Purpose:** Final gate — only TRUE if all required fields are present and valid

```javascript
const email = String({{work_email}} || "").trim();
const verified = String({{email_verified}} || "").toLowerCase();
const segment = String({{segment}} || "");
const track = String({{campaign_track}} || "");
const firstName = String({{first_name}} || "").trim();
const company = String({{company_name}} || "").trim();

const hasEmail = email.includes("@") && email.includes(".");
const isVerified = verified === "valid" || verified === "catch-all";
const hasSegment = segment !== "UNKNOWN" && segment !== "";
const hasTrack = track !== "SKIP" && track !== "";
const hasName = firstName !== "" && firstName.length > 1;
const hasCompany = company !== "" && company.length > 1;

return (hasEmail && isVerified && hasSegment && hasTrack && hasName && hasCompany).toString();
```

**Only export rows where `send_ready` = "true" to Smartlead.**

---

## Claygent Prompts (Paid — Run Conditionally)

### Prompt A — Hiring IT Role Check

**Column:** `hiring_it_role`
**Model:** GPT-4 Mini
**Credits:** ~2–3 per row
**Run condition:** `=IF({{headcount}} >= 10, "run", "skip")` — only run for 10+ headcount companies

```
You are a research assistant. Visit the SEEK job board and search for IT-related job postings from {{company_name}} (domain: {{company_domain}}).

Look for any active job listings with titles like: IT Manager, IT Support, Systems Administrator, Network Engineer, Help Desk, IT Technician, Head of IT, Technology Manager, Cybersecurity.

Instructions:
- If you find an active IT job listing: return "Yes — [job title found]"
- If no IT jobs found: return "No"
- If unable to check: return "Unknown"

Return only one of those three responses. No explanation needed.
```

---

### Prompt B — Current IT Vendor Check

**Column:** `current_it_vendor`
**Model:** GPT-4 Mini
**Credits:** ~2–3 per row
**Run condition:** `=IF({{segment}} != "UNKNOWN", "run", "skip")` — only run for segmented contacts

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

---

### Prompt C — Personalised Opener (GPT-4 Mini)

**Column:** `personalized_opener`
**Model:** GPT-4 Mini
**Credits:** ~1 per row
**Run condition:** `=IF({{send_ready}} == "true", "run", "skip")` — only for send-ready contacts

**For CFO segment:**
```
Write the opening sentence of a cold email to {{first_name}}, {{job_title}} at {{company_name}}, a {{industry_clean}} business with approximately {{headcount}} staff.

The angle: IT costs are often the most overlooked overhead for finance leaders at businesses this size — usually because no one has run the numbers properly.

Rules:
- Under 20 words
- Conversational, not formal
- No compliments, no "I hope this finds you well"
- Lead with an observation about their situation, not about us
- Do NOT mention "AI", "managed IT", "IT Together", or any product
- Plain text, no punctuation tricks

Example output format:
"Most CFOs I speak to at {{headcount}}-person firms haven't run the actual numbers on their IT setup."
```

**For CEO segment:**
```
Write the opening sentence of a cold email to {{first_name}}, {{job_title}} at {{company_name}}, a {{industry_clean}} business with approximately {{headcount}} staff.

The angle: CEOs at growing businesses often don't think about IT until something breaks — by then it's already costing them.

Rules:
- Under 20 words
- Conversational, plain
- No compliments
- Lead with an observation about the business or their role — not a pitch
- Do NOT mention "IT Together", "managed IT", or any product name
- Avoid the word "IT" if possible — use "tech", "systems", or "setup" instead

Example output format:
"Most founders at this stage tell me their tech setup is fine — until it isn't."
```

**For IT Manager / Ops segment:**
```
Write the opening sentence of a cold email to {{first_name}}, {{job_title}} at {{company_name}}, a {{industry_clean}} business with approximately {{headcount}} staff.

The angle: IT managers at businesses this size spend most of their time reacting to problems rather than doing anything strategic.

Rules:
- Under 20 words
- Peer-to-peer tone — like one IT professional talking to another
- No compliments, no corporate language
- Lead with an observation about their day-to-day — not a pitch
- Do NOT mention any product name or company

Example output format:
"Quick question — how much of your week right now is reactive vs anything strategic?"
```

---

## Conditional Logic Stack (Run in this order)

```
Step 1:  Import CSV → populate: first_name, last_name, job_title, company_name, company_domain
Step 2:  Run formula: industry_clean (0 credits)
Step 3:  Run formula: segment (0 credits)
Step 4:  Run formula: atl_btl (0 credits)
Step 5:  Filter: remove rows where segment = "UNKNOWN" or atl_btl = "SKIP"
Step 6:  Run enrichment: headcount via Apollo (1–2 credits) — conditional: only if headcount is empty
Step 7:  Run Claygent: hiring_it_role (2–3 credits) — conditional: only if headcount >= 10
Step 8:  Run Claygent: current_it_vendor (2–3 credits) — conditional: only if segment != "UNKNOWN"
Step 9:  Run formula: signal_tier (0 credits) — depends on Steps 7–8
Step 10: Run email waterfall (3–5 credits) — conditional: only if signal_tier != "Tier 3" (skip cold)
Step 11: Run MillionVerifier (1 credit) — conditional: only if email is not empty
Step 12: Run formula: campaign_track (0 credits)
Step 13: Run formula: email_subject (0 credits)
Step 14: Run GPT-4 Mini: personalized_opener (1 credit) — conditional: only if send_ready = "true"
Step 15: Run formula: send_ready (0 credits)
Step 16: Export filter: send_ready = "true" → push to Smartlead
```

**Total credits per qualifying row (estimate):**
- Tier 1 (full enrichment + opener): ~12–18 credits
- Tier 2 (email + opener): ~8–12 credits
- Tier 3 (skip enrichment, no send): 2–4 credits (industry + segment formulas only)

---

## Clay Table View Setup

### Views to create:

| View name | Filter | Sort | Purpose |
|---|---|---|---|
| All Contacts | None | Import order | Master view |
| Tier 1 — Ready | signal_tier = Tier 1, send_ready = true | headcount DESC | First launch batch |
| Tier 2 — Ready | signal_tier = Tier 2, send_ready = true | company_name ASC | Second batch |
| CFO Track | segment = CFO | signal_tier ASC | Campaign-specific view |
| CEO Track | segment = CEO | signal_tier ASC | Campaign-specific view |
| IT Manager Track | segment = IT_MANAGER or OPS_MANAGER | signal_tier ASC | Campaign-specific view |
| Unknown / Review | segment = UNKNOWN or send_ready = false | — | Manual review queue |
| Email Issues | work_email is empty OR email_verified = invalid | — | Fix or remove |

---

## Smartlead Upload Mapping

When pushing from Clay to Smartlead, map these fields:

| Clay column | Smartlead field |
|---|---|
| `first_name` | firstName |
| `last_name` | lastName |
| `work_email` | email |
| `company_name` | companyName |
| `job_title` | title |
| `campaign_track` | campaignId (map to correct campaign) |
| `personalized_opener` | customVar1 (use as {{customVar1}} in email template) |
| `industry_clean` | customVar2 |
| `headcount` | customVar3 |
| `signal_tier` | customVar4 |

**In Smartlead email template, reference:**
- `{{firstName}}` — first name
- `{{companyName}}` — company name
- `{{customVar1}}` — personalized opener line (replaces generic opener)
- `{{customVar2}}` — industry (for "companies in {{industry}}" line)
- `{{customVar3}}` — headcount (for cost comparison personalisation)
