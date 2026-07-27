# Darwin Business — Clay Workflow
# ColdIQ Framework | NT Trades & Commercial Outreach
# Offer: Digital Marketing + Google Presence + CRM + AI Automation
Generated: 2026-07-27

---

## Campaign Context

**From:** DGK Business Consultancy
**To:** CEOs, Founders, Managing Directors of Darwin/NT trade and commercial businesses
**Goal:** Book a 15-min discovery call via 3-email sequence + lead magnet
**Lead Magnet:** "Get More Commercial Contracts Without Ads: How Darwin Trade Businesses Win Work Online"
**Tone:** Direct, peer-level, NT-aware — never corporate

---

## CSV Source

**File:** `darwinbusinessDefaultviewexport.csv`
**Rows:** 256
**All contacts:** Trades category — Construction, Aviation, Mining/Resources, Environmental, IT, Utilities, Commercial Services

---

## Step 1 — Import CSV into Clay

1. New Clay table → Import CSV
2. Upload the Darwin business CSV
3. Check field mapping — ensure these source columns come through cleanly:
   - `first_name`, `last_name`, `full_name`
   - `headline`, `location_name`
   - `current_company`, `current_company_position`, `clean positiom` (Position Tier input)
   - `Position Tier`
   - `Work Type Classification` (Commercial / Both / Residential)
   - `tradies Work Type Classification primary Type`
   - `Industry` (LinkedIn industry — Construction, Airlines, Oil & Gas, etc.)
   - `Work Email`, `email`
   - `Phone`, `Website`, `Google Maps Place Link`
   - `Rating`, `Reviews`
   - `Google Reviews Opener` (pre-generated in source CSV)
   - `Hiring Status & Job Openings hiring Status` (hiring / noOpenRolesFound)
   - `Annual Revenue`, `Size`, `Employee Count`
   - `Description` (LinkedIn company description)
   - `profile_url` (LinkedIn)

---

## Step 2 — Clayscript Columns (0 Credits Each)

### 2a — `clean_first_name`
```javascript
const name = String({{first_name}} || {{full_name}} || "").trim();
return name.split(" ")[0];
```

### 2b — `industry_group`
Classifies each contact into one of 3 email copy tracks based on LinkedIn industry.
```javascript
const ind = String({{Industry}} || "").toLowerCase();
const company = String({{Description}} || "").toLowerCase();

// Construction / Civil track
if (ind.includes("construction") || ind.includes("civil") || ind.includes("specialty trade") ||
    ind.includes("building") || ind.includes("engineering services") ||
    company.includes("construction") || company.includes("civil")) {
  return "Construction";
}

// Resources / Aviation / Energy track
if (ind.includes("oil") || ind.includes("gas") || ind.includes("mining") ||
    ind.includes("aviation") || ind.includes("aerospace") || ind.includes("airlines") ||
    ind.includes("utilities") || ind.includes("electric") || ind.includes("energy") ||
    ind.includes("environmental") || ind.includes("agriculture") ||
    company.includes("mining") || company.includes("aviation") || company.includes("energy")) {
  return "Resources";
}

// Commercial Services track (IT, Manufacturing, Maritime, Logistics, Retail, etc.)
return "Commercial";
```

### 2c — `work_type_clean`
```javascript
const wt = String({{Work Type Classification}} || "").trim();
if (wt === "Commercial") return "Commercial";
if (wt === "Both") return "Both";
if (wt === "Residential") return "Residential";
return "Commercial";
```

### 2d — `signal_score` (Weighted — based on master-signal-sourcer framework)

Multi-signal stacking: 1 signal = 18-22% reply, 3+ signals = 35-40% reply.
Never mention signals explicitly in copy — use them to set timing and angle only.

```javascript
let score = 0;

// Signal 1: Decision maker (Tier A = CEO/MD/Director)
const tier = String({{Position Tier}} || "B");
if (tier === "A") score += 30;  // Highest weight — right person

// Signal 2: Hiring (budget confirmed, growing = capacity before clients)
const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
if (hiring === "hiring") score += 20;  // Act within 1-2 weeks of detection

// Signal 3: Google reviews (strong reputation signal, not yet converting)
const rating = parseFloat({{Rating}} || 0);
const reviews = parseInt({{Reviews}} || 0);
if (rating >= 4.5 && reviews >= 20) score += 20;
else if (rating >= 4.0 && reviews >= 10) score += 15;
else if (rating >= 4.0 && reviews >= 5) score += 10;

// Signal 4: Revenue scale (budget available for DGK's services)
const rev = String({{Annual Revenue}} || "");
if (rev.includes("75M") || rev.includes("200M")) score += 15;
else if (rev.includes("25M") || rev.includes("10M")) score += 12;
else if (rev.includes("5M")) score += 8;
else if (rev.includes("1M")) score += 4;

// Signal 5: Company size (sweet spot for DGK = 11-200 employees)
const size = String({{Size}} || "");
if (size.includes("51-200")) score += 10;
else if (size.includes("11-50")) score += 8;
else if (size.includes("201-500")) score += 6;

// Signal 6: Valid email confirmed
const email = String({{Work Email}} || {{email}} || "");
if (email.includes("@") && !email.includes("not found")) score += 10;

return score;
```

### 2d2 — `signal_tier` (Derived from signal_score)
```javascript
const score = parseInt({{signal_score}} || 0);
if (score >= 70) return "Hot";      // Contact same day — 35-40% reply target
if (score >= 50) return "Warm";     // Contact within 72 hours — 18-25% reply target
if (score >= 30) return "Standard"; // Contact within 1 week — 12-18% reply target
return "Low";                        // LinkedIn only — 6-8% reply target
```

### 2e — `email_variant`
A/B split by name hash (deterministic — same person always gets same variant).
```javascript
const name = String({{first_name}} || "") + String({{last_name}} || "");
const seed = name.split("").reduce((acc, c) => acc + c.charCodeAt(0), 0);
return seed % 2 === 0 ? "A" : "B";
```

### 2f — `google_reviews_ps`
Pulls the Google Reviews signal into a clean PS format. Falls back gracefully if empty.
```javascript
const opener = String({{Google Reviews Opener}} || "").trim();
if (opener.length > 10) return `PS — ${opener}`;
const rating = parseFloat({{Rating}} || 0);
const reviews = parseInt({{Reviews}} || 0);
if (rating >= 4.0 && reviews >= 5) {
  return `PS — ${rating} from ${reviews} reviews is a strong foundation. Most trades businesses in Darwin never turn that into consistent inbound enquiries.`;
}
return "";
```

### 2g — `subject_email1`
Industry-matched 2-word subject. Costs 0 credits.
```javascript
const group = String({{industry_group}} || "Commercial");
const wt = String({{work_type_clean}} || "Commercial");
const variant = String({{email_variant}} || "A");

const construction = variant === "A"
  ? ["darwin contracts", "nt tenders", "more projects", "contract pipeline"]
  : ["winning tenders", "project flow", "darwin work", "contract growth"];

const resources = variant === "A"
  ? ["nt operators", "site contracts", "darwin ops", "resource jobs"]
  : ["field contracts", "site pipeline", "nt resources", "darwin supply"];

const commercial = variant === "A"
  ? ["nt clients", "darwin growth", "more enquiries", "client pipeline"]
  : ["darwin leads", "nt business", "client flow", "more work"];

const pool = group === "Construction" ? construction
           : group === "Resources" ? resources
           : commercial;

const company = String({{current_company}} || "");
const hash = company.split("").reduce((sum, c) => sum + c.charCodeAt(0), 0);
return pool[hash % pool.length];
```

### 2h — `subject_email3`
Casual low-friction subject for Email 3.
```javascript
const firstName = String({{clean_first_name}} || "").trim().toLowerCase();
const tier = String({{Position Tier}} || "B");
const variant = String({{email_variant}} || "A");

const patternsA_tierA = [`15 mins, ${firstName}?`, `worth it?`, `quick one`, `one question`];
const patternsA_tierB = [`15 mins?`, `worth a call?`, `quick one`, `one thing`];
const patternsB = [`${firstName} — worth it?`, `15 min this week?`, `following up`, `quick question`];

const basePatterns = tier === "A" ? patternsA_tierA : patternsA_tierB;
const patterns = variant === "B" ? patternsB : basePatterns;

const company = String({{current_company}} || "");
const hash = company.split("").reduce((sum, c) => sum + c.charCodeAt(0), 0);
return patterns[hash % patterns.length];
```

### 2i — `send_ready`
Gate before sending to Smartlead — only push rows with a valid email and Tier A or Hot/Warm signal.
```javascript
const email = String({{Work Email}} || {{email}} || "").trim();
const tier = String({{Position Tier}} || "");
const signal = String({{signal_tier}} || "");
const hasEmail = email.includes("@") && !email.includes("not found");
const isQualified = tier === "A" || signal === "Hot" || signal === "Warm";
return hasEmail && isQualified ? "Yes" : "No";
```

---

## Step 3 — AI Enrichment (Paid — Run Conditionally)

**Run order:** Only run if `send_ready` = "Yes" to avoid wasting credits.

### Prompt 0 — `subject_email1` (Optional AI Override)

Only use this if the Clayscript subject in Step 2g feels too generic for a specific contact.
Model: GPT-4 Mini (~1 credit)

```
Write a two-word email subject line for a cold email to {{clean_first_name}} at {{current_company}}.

Context:
- Company: {{current_company}}
- Industry: {{Industry}}
- Location: Darwin / Northern Territory, Australia
- What we do: Help NT trade businesses get more commercial clients through digital marketing, Google presence, and AI systems.

Rules:
- MUST be exactly 2 words
- All lowercase
- Relevant to their NT business context
- No sales/spam words ("free", "grow", "boost", "leads")
- Creates curiosity — does not reveal the topic
- Should flow naturally as an email subject line

Output only the 2-word subject. Nothing else.
```

### Prompt 1 — `darwin_opener` (Email 1 Line 1 and Email 3 Line 1)
Model: GPT-4 Mini (~1 credit/row)
Conditional: Only run if `darwin_opener` is empty

```
You are writing the first line of a cold email to {{clean_first_name}}, {{current_company_position}} at {{current_company}} in Darwin, Northern Territory, Australia.

STEP 1 — Identify their industry group: {{industry_group}}
Use the pain library below to understand the specific challenge for their type of business.

PAIN LIBRARY (internal — do not mention in output):
- Construction: Win rate on tenders is unpredictable, leads come in waves not consistently, Google presence is often neglected vs word-of-mouth reputation
- Resources (Oil/Gas/Mining/Aviation/Energy): Contract wins rely on relationships and existing frameworks, online presence rarely used as a prospecting channel, procurement contacts are hard to reach cold
- Commercial: Enquiries rely on referrals and word of mouth, Google reviews sit unused as a conversion tool, digital marketing feels expensive or complicated

STEP 2 — Extract ONE specific detail from their headline or description:
Headline: {{headline}}
Company description: {{Description}}

Use this specific detail — a market focus, a specific service, a geographic claim, a mission — as the anchor for the opener.

STEP 3 — Write ONE sentence using this pattern:
Pattern A: "Most [industry type] businesses in Darwin still rely on [specific thing they do] to win work — and it [observation about the limitation]."
Pattern B: "The [specific thing from their description] approach {{current_company}} takes is exactly the kind of signal that [observation about online opportunity]."
Pattern C: "[Specific claim from their headline] in the NT market usually means [specific growth constraint that DGK's offer solves]."

Rules:
- Maximum 25 words
- No greetings, no "I noticed", no "I came across"
- No compliments ("impressive", "love your work")
- Must sound like a peer observation, not a pitch
- Do not mention DGK or any services
- All lowercase except proper nouns
- No full stop at end

Output only the sentence. Nothing else.
```

### Prompt 2 — `darwin_pain_line` (Email 2 Body Line 1)
Model: GPT-4 Mini (~1 credit/row)
Conditional: Only run if `darwin_pain_line` is empty

```
You are writing the opening sentence of Email 2 in a cold email sequence to {{clean_first_name}} at {{current_company}} in Darwin, NT.

STEP 1 — Identify their industry: {{industry_group}}
STEP 2 — Select the matching pain pattern below:

PAIN PATTERNS:
- Construction: "Most construction businesses in Darwin I speak to win work through relationships and reputation — then hit a ceiling when those dry up."
- Resources: "Most NT operators in [oil & gas / aviation / mining] rely on existing contractor frameworks for work — and struggle when a new contract cycle opens."
- Commercial: "Most commercial service businesses in Darwin tell me the same thing — clients come through referrals, and they stop when referrals stop."

STEP 3 — Localise the selected pattern using:
- Their specific industry: {{Industry}}
- Their company: {{current_company}}
- Their position: {{current_company_position}}

Rules:
- Maximum 25 words
- Complete sentence, no pitch, no mention of DGK
- End with a full stop
- Peer-level tone — not a lecture

Output only the sentence. Nothing else.
```

### Prompt 3 — `darwin_case_study_line` (Email 3 Social Proof)
Model: GPT-4 Mini (~1 credit/row)
Conditional: Only run if `darwin_case_study_line` is empty

**Note:** Replace the placeholder with a real DGK client case study before sending.

```
Write a one-line social proof PS for a cold email to {{clean_first_name}} at a {{industry_group}} company in Darwin.

Context: DGK helps NT trade businesses get more commercial clients through digital marketing, Google presence, and AI automation.

Use this case study template (fill in from DGK's real client data):
"PS — [Client type, e.g. Darwin electrical contractor] went from [before state] to [after state, e.g. 3 inbound enquiries per week from Google] in [timeframe] — without running a single ad."

Rules:
- Start with "PS —"
- One sentence only
- Specific numbers if available
- Do not mention client name — just company type and state/territory
- No exclamation marks

Output only the PS line. Nothing else.
```

---

## Step 4 — Email Waterfall

Run in this order. Each step only runs if the previous returned empty.

| Step | Provider | Clay Integration | Cost |
|---|---|---|---|
| 1 | LeadMagic | LeadMagic → Find Work Email | ~1 credit |
| 2 | Prospeo | Prospeo → Email Finder | ~1 credit |
| 3 | Hunter | Hunter → Email Finder | ~1 credit |
| 4 | Apollo | Apollo → Find Email | ~2 credits |

**Conditional formula for each step:**
```javascript
// Only run if previous email columns are empty
const existing = String({{Work Email}} || {{email}} || "").trim();
return existing.length > 5 ? "skip" : "run";
```

**Note:** The source CSV already has `Work Email` and `email` columns populated for many contacts. Run Step 1 only for rows where both are empty.

---

## Step 5 — Smartlead Export

Filter: `send_ready` = "Yes"

**Map these Clay columns to Smartlead custom variables:**

| Smartlead Variable | Clay Column | Used In |
|---|---|---|
| `{{firstName}}` | `clean_first_name` | All emails |
| `{{companyName}}` | `current_company` | All emails |
| `{{customVariable1}}` | `darwin_opener` | Email 1 line 1, Email 3 line 1 |
| `{{customVariable2}}` | `industry_group` | Email 1 body, Email 2 body |
| `{{customVariable3}}` | `work_type_clean` | Email 2 (optional context) |
| `{{customVariable4}}` | `google_reviews_ps` | Email 1 PS |
| `{{customVariable5}}` | `darwin_pain_line` | Email 2 line 1 |
| `{{customVariable6}}` | `email_variant` | A/B tracking |
| `{{customVariable7}}` | `subject_email1` | Email 1 subject field |
| `{{customVariable8}}` | `subject_email3` | Email 3 subject field |
| `{{customVariable9}}` | `darwin_case_study_line` | Email 3 PS |
| `{{customVariable10}}` | `signal_tier` | Prioritisation only |

---

## Smartlead Campaign Settings

**Campaign name:** `DGK-DARWIN-TRADES-NT`

Split into two campaigns if needed:
- `DGK-DARWIN-CONSTRUCTION` — industry_group = "Construction"
- `DGK-DARWIN-RESOURCES` — industry_group = "Resources"
- `DGK-DARWIN-COMMERCIAL` — industry_group = "Commercial"

**Settings:**
- Sending window: Mon–Thu, 8:00am–10:30am ACST (Darwin does not observe daylight saving)
- Daily cap: 25 per inbox during warm-up, 40–50 when warmed
- Stop on reply: Yes
- Open tracking: Off
- Click tracking: Off
- Email 2: Reply in thread (RE: auto-applies)

---

## Qualification Logic

### Tier 1 — Hot (contact first)
- signal_tier = "Hot"
- Position Tier = "A"
- Hiring = "hiring"
- Reviews ≥ 10 AND Rating ≥ 4.0

### Tier 2 — Warm (contact second batch)
- signal_tier = "Warm"
- Position Tier = "A"
- Either hiring OR strong reviews (not both)

### Tier 3 — Standard (contact third)
- Position Tier = "A"
- No strong hiring or review signal

### Disqualify / Don't Send
- send_ready = "No" (no valid email)
- Position Tier = "B" AND signal_tier = "Low"
- Work Type = "Residential" (DGK focuses on commercial)
- Revenue = "0-500K" (too small for DGK's services)

---

## Credit Budget Estimate

| Action | Credits |
|---|---|
| Email waterfall (rows without email) | ~200 credits |
| darwin_opener AI prompt (256 rows) | ~256 credits |
| darwin_pain_line AI prompt (256 rows) | ~256 credits |
| darwin_case_study_line (256 rows) | ~256 credits |
| subject_email1 AI override (optional) | ~50 credits |
| **Total estimate** | **~1,000–1,200 credits** |

Run test on 50 rows first. Conditional formulas on all paid steps.
