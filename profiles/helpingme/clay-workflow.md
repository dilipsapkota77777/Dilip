# Helpingme — Clay Enrichment Workflow
# NDIS Provider Referral Partner Outreach
# Input: NDISOWner CSV (LinkedIn export, pre-qualified)
Generated: 2026-07-24

---

## What You Already Have (CSV Columns)

| Column | Quality | Use |
|---|---|---|
| `first_name`, `last_name` | ✅ Clean | Merge tag |
| `headline` | ✅ Rich | Personalization hook source |
| `current_company` | ✅ Clean | Merge tag |
| `Domain` | ✅ Most filled | Email waterfall + Claygent input |
| `profile_url` | ✅ All filled | LinkedIn outreach |
| `Position Tier` | ✅ All filled | Tier A (CEO/Founder) vs Tier B (MD/Ops) |
| `Employee Count` | ⚠️ Partial | ICP filter |
| `Years in Business` | ✅ Most filled | Signal tier scoring |
| `Annual Revenue` | ✅ Most filled | ICP filter |
| `Qualification Status` | ✅ All filled | Filter first (keep "qualify" only) |
| `Work Email` | ⚠️ ~40% filled | Run waterfall for the rest |
| `summary` | ✅ Rich | Deep personalization context |
| `Description` | ✅ Rich | Service type extraction |
| `Locality` | ✅ All filled | Geographic segmentation |
| `Size` | ✅ All filled | ICP bucket |

---

## Step 0 — Pre-Import Filters (Before Clay)

Apply these filters in Excel / Google Sheets BEFORE importing:

1. `Qualification Status` = "qualify" → keep
2. `NDIS Status` = "yes" → keep
3. Remove rows where `first_name` is blank
4. Remove rows where `Domain` is blank AND `Work Email` is blank (no way to reach them)
5. Remove `Position Tier` = "Tier C" or below if any exist

**Expected rows after filter:** ~70–80% of original

---

## Step 1 — Import to Clay

1. Clay → New Workbook → name: `Helpingme — NDIS Referral Partners — Jul 2026`
2. Import → Upload CSV → select the NDIS Owner export
3. Map all columns (auto-map should work — 55+ columns)
4. Do NOT delete any columns yet — you'll use `headline`, `summary`, `Description` for Claygent

---

## Step 2 — Formula Columns (Add Immediately, 0 Credits)

Add these Clayscript columns before running any paid enrichment.

### 2a — Clean First Name

**Column:** `clean_first_name`
```javascript
String({{first_name}} || "")
  .replace(/[^a-zA-Z\- ]/g, "")
  .trim()
  .split(' ')[0]
  .replace(/^\w/, c => c.toUpperCase())
```

### 2b — Signal Tier (from existing data)

**Column:** `signal_tier`
**Purpose:** Heat score using the data you already have. No credits needed.

```javascript
const years = String({{Years in Business}} || "").toLowerCase();
const revenue = String({{Annual Revenue}} || "");
const headline = String({{headline}} || "").toLowerCase();

// Signals from headline — partnership intent
const wantsPartner = headline.includes("collaborat") ||
                     headline.includes("partner") ||
                     headline.includes("together") ||
                     headline.includes("network") ||
                     headline.includes("referral");

// Revenue check — established enough to be worth partnering
const revenueNum = parseInt(revenue.replace(/[^0-9]/g,'')) || 0;
const isEstablishedRevenue = revenue.includes("5M") || revenue.includes("10M") ||
                              revenue.includes("25M") || revenue.includes("75M") ||
                              revenueNum >= 5000000;

// Business maturity
const isGrowing = years.includes("growing") || years.includes("2-5");
const isEstablished = years.includes("established") || years.includes("5-10");

// Tier logic — stack signals
if (wantsPartner && isGrowing && isEstablishedRevenue) return "Tier 1 — Hot";
if (wantsPartner && isEstablishedRevenue) return "Tier 1 — Hot";
if (isGrowing && isEstablishedRevenue) return "Tier 2 — Warm";
if (wantsPartner || isEstablishedRevenue) return "Tier 2 — Warm";
return "Tier 3 — Cold";
```

### 2c — Service Type Extract (from headline, 0 credits)

**Column:** `service_type_raw`
**Purpose:** Extract NDIS service category from their LinkedIn headline — no Claygent needed for most rows.

```javascript
const h = String({{headline}} || "").toLowerCase();
const d = String({{Description}} || "").toLowerCase();
const combined = h + " " + d;

const services = [];
if (combined.includes("support coord")) services.push("Support Coordination");
if (combined.includes("sil") || combined.includes("supported independent")) services.push("SIL");
if (combined.includes("sda") || combined.includes("specialist disability accom")) services.push("SDA");
if (combined.includes("personal care") || combined.includes("daily activit") || combined.includes("daily living")) services.push("Core Supports");
if (combined.includes("community access") || combined.includes("community particip")) services.push("Community Participation");
if (combined.includes("allied health") || combined.includes("occupational therap") || combined.includes("speech pathol") || combined.includes("physiother")) services.push("Allied Health");
if (combined.includes("behaviour support") || combined.includes("positive behaviour") || combined.includes("pbs")) services.push("Behaviour Support");
if (combined.includes("plan manag")) services.push("Plan Management");
if (combined.includes("psychosocial") || combined.includes("mental health") || combined.includes("recovery coach")) services.push("Psychosocial");
if (combined.includes("nursing") || combined.includes("high intensit") || combined.includes("complex care")) services.push("High Intensity / Nursing");
if (combined.includes("early childhood") || combined.includes("ecei") || combined.includes("child")) services.push("Early Childhood");

return services.length > 0 ? services.join(", ") : "General NDIS";
```

### 2d — Participant Specialisation Extract (from headline, 0 credits)

**Column:** `participant_type_raw`

```javascript
const h = String({{headline}} || "").toLowerCase();
const d = String({{Description}} || "").toLowerCase();
const combined = h + " " + d;

const types = [];
if (combined.includes("autism") || combined.includes("asd")) types.push("Autism");
if (combined.includes("adhd") || combined.includes("neurodiver")) types.push("Neurodivergence");
if (combined.includes("psychosocial") || combined.includes("mental health")) types.push("Psychosocial");
if (combined.includes("physical disabil") || combined.includes("neurological")) types.push("Physical");
if (combined.includes("intellectual disabil")) types.push("Intellectual Disability");
if (combined.includes("brain injur") || combined.includes("abi") || combined.includes("acquired")) types.push("ABI");
if (combined.includes("aged care") || combined.includes("elderly")) types.push("Aged Care crossover");
if (combined.includes("first nation") || combined.includes("indigenous") || combined.includes("aboriginal")) types.push("First Nations");
if (combined.includes("complex") || combined.includes("high intensit")) types.push("Complex / High Intensity");

return types.length > 0 ? types.join(", ") : "General";
```

### 2e — Geography State Extract

**Column:** `state`

```javascript
const loc = String({{Locality}} || {{location_name}} || "").toLowerCase();

if (loc.includes("sydney") || loc.includes("nsw") || loc.includes("new south wales")) return "NSW";
if (loc.includes("melbourne") || loc.includes("vic") || loc.includes("victoria")) return "VIC";
if (loc.includes("brisbane") || loc.includes("qld") || loc.includes("queensland") || loc.includes("gold coast") || loc.includes("sunshine coast")) return "QLD";
if (loc.includes("perth") || loc.includes("wa") || loc.includes("western australia")) return "WA";
if (loc.includes("adelaide") || loc.includes("sa") || loc.includes("south australia")) return "SA";
if (loc.includes("canberra") || loc.includes("act") || loc.includes("australian capital")) return "ACT";
if (loc.includes("darwin") || loc.includes("nt") || loc.includes("northern territory")) return "NT";
if (loc.includes("hobart") || loc.includes("tas") || loc.includes("tasmania")) return "TAS";
return "AU";
```

### 2f — Final Email Merge

**Column:** `final_email`
**Add AFTER waterfall runs (Step 4)**

```javascript
{{Work Email}} || {{leadmagic_email}} || {{prospeo_email}} || {{hunter_email}} || {{apollo_email}} || ""
```

### 2g — Campaign Track

**Column:** `campaign_track`

```javascript
const tier = String({{Position Tier}} || "");
if (tier === "Tier A") return "NDIS-FOUNDER";
if (tier === "Tier B") return "NDIS-DIRECTOR";
return "NDIS-GENERAL";
```

### 2i — Email 3 Subject Line (Clayscript, 0 credits)

**Column:** `subject_email3`
**Purpose:** Personal, ultra-short subject for the day-9 call offer email. Different pattern for Tier A vs Tier B.

```javascript
const firstName = String({{clean_first_name}} || "").trim().toLowerCase();
const company = String({{current_company}} || "").trim();
const tier = String({{Position Tier}} || "").trim();
const variant = String({{email_variant}} || "A");

const shortCo = company.length > 15 ? company.split(/[\s,&]+/)[0] : company;
const co = shortCo.toLowerCase().replace(/[^a-z0-9]/g, "");

const patternsA_tierA = [`15 mins, ${firstName}?`, `worth it?`, `${firstName} — quick`, `one question`];
const patternsA_tierB = [`15 mins?`, `worth a call?`, `quick one`, `one thing`];
const patternsB = [`${co}?`, `${firstName} — worth it?`, `15 min this week?`, `following up`];

const isTierA = tier === "Tier A";
const basePatterns = isTierA ? patternsA_tierA : patternsA_tierB;
const patterns = variant === "B" ? patternsB : basePatterns;

const hash = company.split("").reduce((sum, c) => sum + c.charCodeAt(0), 0);
return patterns[hash % patterns.length];
```

**Note on Email 2:** Email 2 does NOT get a subject column. In Smartlead, tick "Reply in thread" on Email 2's step — it automatically sends as `RE: [Email 1 subject]`. This keeps the conversation thread intact.

---

### 2j — Email A/B Variant Assignment

**Column:** `email_variant`
**Purpose:** Deterministically splits contacts 50/50 for Smartlead A/B testing — no randomness, reproducible.

```javascript
// Hash first + last name to get stable A/B assignment
const name = String({{first_name}} || "") + String({{last_name}} || "");
const seed = name.split("").reduce((acc, c) => acc + c.charCodeAt(0), 0);
return seed % 2 === 0 ? "A" : "B";
```

**How to use in Smartlead:** Create two subject line variants per email. Filter your export — Variant A contacts go into Variant A campaign sequence, Variant B into Variant B. Or use Smartlead's native A/B test and use this column only for tracking which contacts got which variant.

---

### 2k — Send Ready Gate

**Column:** `send_ready`
**Add LAST — after all enrichments complete**

```javascript
const email = String({{final_email}} || "").trim();
const verified = String({{email_verified}} || "").toLowerCase();
const name = String({{clean_first_name}} || "").trim();
const company = String({{current_company}} || "").trim();
const opener = String({{personalized_opener}} || "").trim();
const tier = String({{signal_tier}} || "");

const hasEmail = email.includes("@") && email.includes(".");
const isVerified = verified === "valid" || verified === "catch-all";
const hasName = name.length > 1;
const hasCompany = company.length > 1;
const hasOpener = opener.length > 10;
const notCold = tier !== "Tier 3 — Cold";

return (hasEmail && isVerified && hasName && hasCompany && hasOpener && notCold).toString();
```

---

## Step 3 — Claygent Prompts (Paid — Run Conditionally)

Run these ONLY after formula columns are done. Model: GPT-4 Mini for all three.

### Prompt 0 — Email 1 Subject Line (Two-Word Formula)

**Column:** `subject_email1`
**Credits:** ~1 per row
**Conditional:** `{{current_company}}` is not empty
**Run first** — before openers, before hooks. Subject line needs to be in Smartlead before any email body variables matter.

```
Write a two-word email subject line for a cold email to {{current_company}}, an NDIS provider.

Their services: {{service_type_raw}}
Their state: {{state}}

Rules:
- MUST be exactly 2 words
- All lowercase, no punctuation
- Relevant to participant acquisition, referral partnerships, or support coordinator relationships in NDIS
- Creates mild curiosity — does NOT reveal what the email is about
- No sales or buzz words: never use "sales", "outreach", "marketing", "partnership", "collaboration", "system", "solution", "services", "growth", "strategy"
- Should feel like it was typed by someone who knows their sector

Good examples:
"participant flow" — relevant to what every NDIS provider cares about, reveals nothing
"coordinator pipeline" — insider language
"referral gap" — implies a problem, names nothing
"care pipeline" — service-relevant but vague
"allied pipeline" — for allied health providers specifically
"sil waitlist" — hyper-relevant for SIL providers

Never write:
"referral system" — reveals the pitch
"quick question" — massively overused cliché
"more participants" — sounds like advertising
"ndis outreach" — banned word

Return ONLY the two-word subject line. Nothing else.
```

---

### Prompt A — LinkedIn Headline Hook

**Column:** `headline_hook`
**Credits:** ~1 per row
**Conditional:** `{{headline}}` is not empty
**Purpose:** Extract a personalization hook from their own headline — this becomes the PS line in Email 1

```
You are a B2B copywriter specialising in NDIS sector outreach.

The person's LinkedIn headline is: "{{headline}}"
Their company is: {{current_company}}
Their role is: {{Title}}

Write ONE short sentence (under 15 words) that:
- References something specific from their headline — their focus, mission, or value they emphasise
- Does NOT sound like a compliment or flattery
- Reads like an observation, not a pitch
- Does NOT mention Helpingme, managed services, or any product

Examples of good hooks:
- "Your focus on high-intensity NDIS care stands out — those participants are often the hardest to place."
- "Noticed you're building collaborative NDIS supports — that's a different approach from most providers."
- "A psychosocial focus in the NDIS space is a niche that most providers avoid."

Return ONLY the hook sentence. Nothing else.
```

### Prompt B — Services Deep Check (for rows where service_type_raw = "General NDIS")

**Column:** `services_confirmed`
**Credits:** ~2 per row
**Conditional:** `{{service_type_raw}}` = "General NDIS" AND `{{Domain}}` is not empty

```
Visit the website {{Domain}} and their LinkedIn page at {{profile_url}}.

Find out which NDIS support categories {{current_company}} provides. Look for:
- Core Supports (personal care, daily activities, community access)
- Capacity Building (support coordination, therapy, life skills)
- SDA (Specialist Disability Accommodation)
- SIL (Supported Independent Living)
- Allied Health (OT, speech pathology, psychology, physio)
- Behaviour Support / PBS
- Plan Management
- High Intensity / Nursing Care

Return a comma-separated list of their services.
If you cannot determine: return "Unknown"
No explanation needed.
```

### Prompt C — Referral Fit Check

**Column:** `referral_fit`
**Credits:** ~2 per row
**Conditional:** `{{signal_tier}}` is not "Tier 3 — Cold" AND `{{Domain}}` is not empty

**IMPORTANT: Fill in [HELPINGME_SERVICES] before activating this prompt**

```
Helpingme is an NDIS registered provider offering: [HELPINGME_SERVICES — e.g., Support Coordination, Community Participation, Daily Activities].

Based on what {{current_company}} offers ({{service_type_raw}}) and who they serve ({{participant_type_raw}}):

Classify the relationship:
- "Partner" — they offer different/complementary services (ideal referral relationship)
- "Competitor" — they offer the same services as Helpingme
- "Overlap" — some services match, some complement
- "Unknown" — cannot determine

Return ONE word: Partner, Competitor, Overlap, or Unknown.
```

**Post-run filter:** Remove rows where `referral_fit` = "Competitor"

---

## Step 4 — Email Waterfall (For Rows With No Work Email)

**Conditional:** `{{Work Email}}` is empty AND `{{signal_tier}}` is not "Tier 3 — Cold"

**Provider order (cheapest first):**
1. LeadMagic (2 credits) → output: `leadmagic_email`
2. Prospeo (2 credits) → output: `prospeo_email`
3. Hunter (2 credits) → output: `hunter_email`
4. Apollo (3 credits) → output: `apollo_email`

**Inputs for each provider:**
- First Name = `{{clean_first_name}}`
- Last Name = `{{last_name}}`
- Company Domain = `{{Domain}}`
- LinkedIn URL = `{{profile_url}}`

**Expected:** ~70% of missing emails recovered

---

## Step 5 — Email Verification

**Enrichment:** MillionVerifier
**Credits:** 1 per row
**Conditional:** `{{final_email}}` is not empty

Output: `email_verified` (valid / catch-all / invalid / unknown)

---

## Step 6 — Personalised Opener (GPT-4 Mini)

**Column:** `personalized_opener`
**Credits:** ~1 per row
**Conditional:** `{{final_email}}` is not empty AND `{{email_verified}}` != "invalid" AND `{{referral_fit}}` != "Competitor"

```
Write ONE opening sentence (under 20 words) for a cold email from Helpingme (an NDIS provider) to {{clean_first_name}}, {{Title}} at {{current_company}}.

Context about them:
- Their LinkedIn headline: "{{headline}}"
- Services they offer: {{service_type_raw}}
- Participants they serve: {{participant_type_raw}}
- Business stage: {{Years in Business}}
- Location: {{Locality}}

The email is about building a referral partnership between NDIS providers.

Rules:
- Lead with an observation about THEIR situation or challenges, not about Helpingme
- Reference their specific service type or participant focus if possible
- Do NOT mention "referral", "partnership", "Helpingme", or any product name
- Conversational, peer-to-peer tone — one NDIS provider talking to another
- No flattery, no "I hope this finds you well"
- Plain text, no punctuation tricks

Examples:
"Most NDIS providers focused on {{participant_type_raw}} tell me consistent participant flow is their biggest operational headache."
"Running {{service_type_raw}} at {{current_company}}'s scale usually means capacity gaps are a weekly reality."

Return ONLY the sentence. Nothing else.
```

---

## Step 7 — Table Views

| View | Filter | Purpose |
|---|---|---|
| Tier 1 Ready | signal_tier = "Tier 1 — Hot", send_ready = true | First launch batch |
| Tier 2 Ready | signal_tier = "Tier 2 — Warm", send_ready = true | Second batch |
| Partners Only | referral_fit = "Partner", send_ready = true | Cleanest list |
| No Email | final_email is empty | Manual outreach or LinkedIn only |
| Competitor | referral_fit = "Competitor" | Do not send |
| Cold / Tier 3 | signal_tier = "Tier 3 — Cold" | Hold for later |

---

## Run Order Summary

```
Step 0:   Filter CSV before import (qualify + NDIS yes only)

Step 1:   Import to Clay

Step 2:   Add ALL formula columns (0 credits) — run immediately:
          clean_first_name, signal_tier, service_type_raw, participant_type_raw,
          state, campaign_track, email_variant, subject_email3
          (final_email and send_ready come later)

Step 3:   GPT-4 Mini enrichments — run in this order:
  3-Sub:  subject_email1     (all rows, conditional: company not empty)  ~1 credit
  3a:     headline_hook      (conditional: headline not empty)            ~1 credit
  3b:     dgk_opener         (all rows)                                   ~1 credit
  3c:     dgk_ps_hook        (all rows)                                   ~1 credit
  3d:     dgk_pain_line      (all rows)                                   ~1 credit
  3e:     services_confirmed (conditional: service_type_raw = "General NDIS")  ~2 credits
  3f:     referral_fit       (conditional: not Tier 3, domain not empty)  ~2 credits
  3g:     dgk_pain_line_enriched (General NDIS rows only — overwrites 3d) ~4 credits

Step 4:   Email waterfall — LeadMagic → Prospeo → Hunter → Apollo
          (conditional: Work Email empty AND not Tier 3)

Step 5:   Add formula: final_email (merge waterfall + existing Work Email)

Step 6:   MillionVerifier (conditional: final_email not empty)

Step 7:   Add formula: send_ready (last step — after all enrichments done)

Step 8:   Filter to send_ready = true

Step 9:   Export Tier 1 — Hot first → Smartlead
          Include: all customVariable columns (1–9) + firstName + companyName + email
```

---

## Credit Estimate

Assume ~150 qualifying rows after filters.

| Step | Provider | Credits/row | Rows | Total |
|---|---|---|---|---|
| Headline Hook | GPT-4 Mini | 1 | 150 | 150 |
| Services Confirmed | GPT-4 Mini | 2 | ~40 | 80 |
| Referral Fit | GPT-4 Mini | 2 | 100 | 200 |
| Email Waterfall | 4 providers avg | 5 | ~90 | 450 |
| MillionVerifier | MillionVerifier | 1 | ~130 | 130 |
| Personalized Opener | GPT-4 Mini | 1 | ~100 | 100 |
| **Total** | | | | **~1,110 credits** |

At $0.01–$0.02/credit: **~$11–$22 for the full list**

---

## Smartlead Field Mapping

| Clay Column | Smartlead Field |
|---|---|
| `clean_first_name` | firstName |
| `last_name` | lastName |
| `final_email` | email |
| `current_company` | companyName |
| `Title` | title |
| `campaign_track` | campaignId (map to campaign) |
| `personalized_opener` | customVariable1 |
| `service_type_raw` | customVariable2 |
| `participant_type_raw` | customVariable3 |
| `headline_hook` | customVariable4 |
| `state` | customVariable5 |
| `email_variant` | customVariable6 |
| `dgk_pain_line` | customVariable7 |
| `subject_email1` | customVariable8 |
| `subject_email3` | customVariable9 |

**In Smartlead email templates use:**
- `{{firstName}}` — first name
- `{{companyName}}` — company
- `{{customVariable1}}` — personalized opener (first sentence of Email 1 and Email 3)
- `{{customVariable2}}` — their NDIS service type
- `{{customVariable3}}` — participant type they serve
- `{{customVariable4}}` — PS hook line (end of Email 1)
- `{{customVariable5}}` — state / geographic reference (Email 2)
- `{{customVariable7}}` — pain observation (Email 2 first line)
- `{{customVariable8}}` — Email 1 subject line field
- `{{customVariable9}}` — Email 3 subject line field

**Subject line setup in Smartlead:**

| Email step | Subject field | How |
|---|---|---|
| Email 1 | `{{customVariable8}}` | Type this into the Smartlead subject field |
| Email 2 | (leave blank) | Tick "Reply in thread" — Smartlead adds RE: automatically |
| Email 3 | `{{customVariable9}}` | Type this into the Smartlead subject field |
