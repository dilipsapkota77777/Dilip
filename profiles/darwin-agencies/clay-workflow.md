# Darwin Agencies — Clay Workflow
# ColdIQ Framework | NT Agencies & Service Businesses Outreach
# Offer: Agency New Business System — Outbound + CRM + Google Presence + AI Automation
Generated: 2026-07-27

---

## Campaign Context

**From:** DGK Business Consultancy
**To:** CEOs, Founders, Managing Directors of Darwin/NT agencies
**Source:** Same Darwin business CSV (`darwinbusinessDefaultviewexport.csv` — 256 rows)
**Segment:** Agencies subset (~25-40 contacts)
**Goal:** Book a 15-min discovery call via 3-email sequence + lead magnet

---

## Step 1 — Import CSV into Clay

Use the same Darwin business CSV already imported for the darwin-business campaign. Create a new Clay table or add a new view/filter on the existing table.

Confirm these columns map correctly:
- `first_name`, `last_name`, `full_name`
- `headline`, `location_name`
- `current_company`, `current_company_position`, `clean positiom` (Position Tier input)
- `Position Tier`
- `Industry` (LinkedIn industry — used for agency segment filter)
- `Work Email`, `email`
- `Phone`, `Website`, `Google Maps Place Link`
- `Rating`, `Reviews`
- `Google Reviews Opener` (pre-generated in source CSV)
- `Hiring Status & Job Openings hiring Status`
- `Annual Revenue`, `Size`, `Employee Count`
- `Description` (LinkedIn company description)
- `profile_url` (LinkedIn)
- `badges_premium`

---

## Step 2 — Clayscript Columns (0 Credits Each)

### 2a — `clean_first_name`
```javascript
const name = String({{first_name}} || {{full_name}} || "").trim();
return name.split(" ")[0];
```

### 2b — `industry_group`
Classifies contacts into agency sub-segments for email copy routing.
```javascript
const ind = String({{Industry}} || "").toLowerCase();
const desc = String({{Description}} || "").toLowerCase();

// Recruitment / Labour hire
if (ind.includes("staffing") || ind.includes("recruiting") ||
    desc.includes("recruitment") || desc.includes("labour hire") ||
    desc.includes("labor hire") || desc.includes("talent")) {
  return "Recruitment";
}

// Marketing / Creative / Digital agency
if (ind.includes("marketing") || ind.includes("advertising") ||
    ind.includes("design") || ind.includes("graphic") ||
    desc.includes("digital agency") || desc.includes("marketing agency") ||
    desc.includes("creative agency") || desc.includes("branding")) {
  return "Marketing";
}

// Event / PR / Communications
if (ind.includes("events") || ind.includes("public relations") ||
    ind.includes("entertainment") || desc.includes("event management") ||
    desc.includes("communications agency") || desc.includes("PR firm")) {
  return "Event";
}

// NDIS / Health services
if (ind.includes("hospital") || ind.includes("health") || ind.includes("wellness") ||
    desc.includes("NDIS") || desc.includes("disability") || desc.includes("aged care") ||
    desc.includes("allied health") || desc.includes("community services")) {
  return "Health";
}

// Training / RTO / Learning
if (ind.includes("professional training") || ind.includes("e-learning") ||
    ind.includes("education management") || desc.includes("RTO") ||
    desc.includes("training provider") || desc.includes("registered training")) {
  return "Training";
}

// Photography / Media / Research
if (ind.includes("photography") || ind.includes("media production") ||
    ind.includes("research") || desc.includes("photography studio") ||
    desc.includes("media company") || desc.includes("research agency")) {
  return "Media";
}

// Not an agency — exclude
return "Other";
```

**Use:** Filter Clay view to show only rows where `industry_group` ≠ "Other" before building email sequence.

### 2c — `signal_score`
```javascript
let score = 0;

const tier = String({{Position Tier}} || "").toUpperCase();
if (tier === "A") score += 3;
else if (tier === "B") score += 1;

const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
if (hiring.includes("hiring")) score += 2;

const reviews = parseInt({{Reviews}} || 0);
if (reviews >= 5) score += 1;

const rating = parseFloat({{Rating}} || 0);
if (rating >= 4.0) score += 1;

const premium = String({{badges_premium}} || "").toLowerCase();
if (premium === "true") score += 1;

return score;
```

### 2d — `signal_tier`
```javascript
const score = parseInt({{signal_score}} || 0);
if (score >= 6) return "Hot";
if (score >= 4) return "Warm";
if (score >= 2) return "Standard";
return "Hold";
```

### 2e — `send_ready`
```javascript
const tier = String({{Position Tier}} || "").toUpperCase();
const email = String({{Work Email}} || {{email}} || "").trim();
const group = String({{industry_group}} || "");
const hasEmail = email.includes("@") && email.length > 5;
const isAgency = group !== "Other";
const isTierA = tier === "A";
return hasEmail && isAgency && isTierA ? "YES" : "NO";
```

### 2f — `google_reviews_ps`
```javascript
const reviews = parseInt({{Reviews}} || 0);
const rating = parseFloat({{Rating}} || 0);
const company = String({{current_company}} || "your agency");
if (reviews >= 5 && rating >= 4.0) {
  return `PS — ${company} has ${reviews} Google reviews at ${rating}. Most Darwin agencies at that level don't have a system that turns reputation into cold inbound enquiries.`;
}
if (reviews >= 1 && reviews < 5) {
  return `PS — Noticed ${company} has ${reviews} Google review${reviews > 1 ? "s" : ""}. Most agencies in Darwin aren't converting their reputation into measurable inbound — there's a system for that.`;
}
return "";
```

---

## Step 3 — AI Columns (Clay AI — Credits Used)

### 3a — `agency_opener`
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row
**Purpose:** Agency-type-specific, NT-aware first line for Email 1

**Prompt:**
```
You are writing the opening line of a cold email for DGK Business Consultancy, reaching out to an agency or service business owner in Darwin, Northern Territory, Australia.

CONTEXT:
- Recipient name: {{first_name}}
- Company name: {{current_company}}
- Agency type: {{industry_group}}
- LinkedIn headline: {{headline}}
- Company description: {{Description}}
- Position: {{current_company_position}}

CHAIN OF THOUGHT:

Step 1: What type of agency is this?
→ Recruitment / Marketing / Event / Health/NDIS / Training / Media / Other

Step 2: What is the cobbler's children pattern for this agency type?
- Recruitment: "Great at placing talent for clients but runs its own BD on cold calls and relationships"
- Marketing: "Builds marketing systems for clients but has no new business system for itself"
- Event: "Creates experiences for clients' audiences but wins its own new work through existing contacts"
- Health/NDIS: "Delivers great client/participant outcomes but referrals come through word-of-mouth from coordinators"
- Training: "Trains other organisations' staff but wins new institutional clients through tenders and relationships"

Step 3: Does the description or headline reveal a specific detail to use?
- If YES: reference it specifically (e.g., "Darwin's only [X] agency")
- If NO: use the category-level cobbler's pattern

Step 4: Write a sentence that:
- Is 10-15 words maximum
- Sounds like it's from a peer who knows agencies, not a vendor
- Does NOT start with "I noticed", "I saw", or "Congratulations"
- Does NOT mention a specific trigger explicitly
- Sets up the topic of "how agencies win their own new clients"
- Is observational, not salesy

RETURN ONLY THE FINAL SENTENCE.

GOOD EXAMPLES:
- "Darwin recruitment agencies are usually great at placing people — and not great at winning new employer clients."
- "Marketing agencies in the NT tend to be the last ones to have a marketing system for their own new business."
- "Most Darwin agencies win new clients the same way — until the referral pool runs dry."
- "NDIS providers in Darwin usually grow through coordinator referrals — which is great until it isn't."

BAD EXAMPLES:
- "I noticed you're hiring..." (signal mention)
- "Congratulations on building a great agency." (hollow)
- "I came across your agency online..." (generic)
```

### 3b — `agency_pain_line`
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row
**Purpose:** Middle of Email 3 — agency-specific pain observation

**Prompt:**
```
You are writing a one-sentence pain observation for the middle of Email 3 in a cold email sequence to a Darwin agency owner.

CONTEXT:
- Company: {{current_company}}
- Agency type: {{industry_group}}
- Description: {{Description}}
- Hiring: {{Hiring Status & Job Openings hiring Status}}
- Revenue: {{Annual Revenue}}

CHAIN OF THOUGHT:

Step 1: What is the specific new business pain for this agency type?
- Recruitment: "All new employer-client relationships start with someone they already know"
- Marketing: "Marketing agencies run campaigns for clients but have no equivalent system for themselves"
- Event/PR: "Projects come in through existing relationships — no cold pipeline"
- Health/NDIS: "Participant and client growth depends on coordinator word-of-mouth referrals"
- Training: "Institutional client acquisition comes from tenders and warm relationships"

Step 2: Is the agency hiring? If yes, add a growth urgency note.

Step 3: Write ONE sentence that:
- Names the pain without being accusatory
- Is 15-20 words maximum
- Sounds observational, not sales-y
- Connects naturally to "how are you currently winning new clients outside your existing network?"

RETURN ONLY THE FINAL SENTENCE.

EXAMPLES:
- "Most Darwin agencies at {{company}}'s stage win new clients the same way — through who they know."
- "Marketing agencies in Darwin are usually the best at building pipelines for their clients and the worst at building their own."
- "Recruitment agencies in Darwin typically win employer retainers through existing relationships — which means pipeline stalls when the contact changes roles."
```

### 3c — `subject_email1`
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row

**Prompt:**
```
Write a subject line for a cold email to {{first_name}} at {{current_company}}, a {{industry_group}} agency in Darwin, NT.

The email offers a lead magnet: "Agency New Business Blueprint: How Darwin Service Businesses Win Their Next 10 Clients Without Waiting for Referrals"

Subject line rules:
- 3-6 words max
- Lowercase only
- No emojis, no punctuation except natural comma or dash
- No "I" at the start
- No clickbait or hype
- Should feel like it came from a peer who knows agencies

Examples of GOOD subjects:
- "agency new business"
- "{{first_name}} — quick idea"
- "without referrals"
- "cobbler's problem"
- "darwin agencies — new clients"

Return ONLY the subject line.
```

### 3d — `subject_email3`
**Clayscript — 0 credits**
```javascript
const firstName = String({{first_name}} || "").trim().split(" ")[0];
const company = String({{current_company}} || "").trim();
const options = [
  "quick question",
  `${firstName} — how are you winning new clients?`,
  "worth 15 min?",
  "last one",
  `new clients at ${company}`
];
const idx = Math.abs(({{first_name}} || "").charCodeAt(0) + ({{current_company}} || "").charCodeAt(0)) % options.length;
return options[idx];
```

---

## Step 4 — Email Variant Logic

### 4a — `email_variant`
```javascript
const group = String({{industry_group}} || "Other");
const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
const tier = String({{Position Tier}} || "").toUpperCase();

if (tier === "A" && hiring.includes("hiring")) return "Tier_A_Hiring";
if (group === "Recruitment") return "Recruitment";
if (group === "Marketing") return "Marketing";
if (group === "Health") return "Health";
return "Standard";
```

---

## Step 5 — Filter & Sort for Send

1. Filter view: `send_ready` = "YES"
2. Sort by: `signal_score` descending
3. Export CSV or connect Smartlead integration

**Expected sendable contacts:** ~20-30 (of ~30-40 agency contacts)

---

## Step 6 — Smartlead Column Mapping

| Clay Column | Smartlead Variable | Used In |
|---|---|---|
| `clean_first_name` | `{{firstName}}` | All emails |
| `current_company` | `{{company}}` | All emails |
| `agency_opener` | `{{customVariable1}}` | Email 1 |
| `google_reviews_ps` | `{{customVariable4}}` | Email 1 + Email 3 |
| `agency_pain_line` | `{{customVariable2}}` | Email 3 |
| `subject_email1` | `{{customVariable7}}` | Email 1 subject |
| `subject_email3` | `{{customVariable8}}` | Email 3 subject |
| `email_variant` | `{{customVariable5}}` | Smartlead routing |
| `Work Email` | Recipient email | — |

---

## Step 7 — Pre-Send Checklist

- [ ] Verify all emails — bounce rate < 2%
- [ ] `send_ready` = "YES" filter applied
- [ ] Review 10 random rows for AI column quality
- [ ] Confirm `signal_tier` = "Hot" contacts are in first send batch
- [ ] Run `/spam-word-checker` on email copy
- [ ] Confirm Smartlead variable mapping above
- [ ] Max 30 emails/inbox/day
- [ ] Delays: Email 1 → Email 2: 4 days; Email 2 → Email 3: 5 days

---

## Expected Output Summary

| Metric | Expected |
|---|---|
| Total Darwin CSV rows | 256 |
| Agency segment | ~25-40 |
| Tier A with valid email | ~20-30 |
| Hot (signal score ≥ 6) | ~5-10 |
| Warm (signal score 4-5) | ~8-14 |
| Standard (signal score 2-3) | ~8-12 |
