# Darwin Professional Services — Clay Workflow
# ColdIQ Framework | NT Professional Services Outreach
# Offer: Client Pipeline System — CRM + Outbound + Google Presence + AI Automation
Generated: 2026-07-27

---

## Campaign Context

**From:** DGK Business Consultancy
**To:** CEOs, Founders, Managing Directors of Darwin/NT professional services firms
**Source:** Same Darwin business CSV (`darwinbusinessDefaultviewexport.csv` — 256 rows)
**Segment:** Professional services subset (~40-55 contacts)
**Goal:** Book a 15-min discovery call via 3-email sequence + lead magnet

---

## Step 1 — Import CSV into Clay

1. New Clay table → Import CSV
2. Upload the Darwin business CSV (same file as darwin-business campaign)
3. Confirm these columns map correctly:
   - `first_name`, `last_name`, `full_name`
   - `headline`, `location_name`
   - `current_company`, `current_company_position`, `clean positiom` (Position Tier input)
   - `Position Tier`
   - `Industry` (LinkedIn industry — used for segment filter)
   - `Work Email`, `email`
   - `Phone`, `Website`, `Google Maps Place Link`
   - `Rating`, `Reviews`
   - `Google Reviews Opener` (pre-generated in source CSV)
   - `Hiring Status & Job Openings hiring Status`
   - `Annual Revenue`, `Size`, `Employee Count`
   - `Description` (LinkedIn company description)
   - `profile_url` (LinkedIn)
   - `badges_premium` (LinkedIn Premium flag)

---

## Step 2 — Clayscript Columns (0 Credits Each)

### 2a — `clean_first_name`
```javascript
const name = String({{first_name}} || {{full_name}} || "").trim();
return name.split(" ")[0];
```

### 2b — `industry_group`
Classifies each contact into Professional Services sub-segments for email copy routing.
```javascript
const ind = String({{Industry}} || "").toLowerCase();
const desc = String({{Description}} || "").toLowerCase();
const pos = String({{current_company_position}} || "").toLowerCase();

// Accounting / bookkeeping / financial services
if (ind.includes("accounting") ||
    (ind.includes("financial services") && !ind.includes("capital")) ||
    desc.includes("accountant") || desc.includes("bookkeeping") ||
    desc.includes("financial planning") || desc.includes("tax")) {
  return "Accounting";
}

// Legal / law practice
if (ind.includes("law practice") || ind.includes("legal services") ||
    desc.includes("solicitor") || desc.includes("barrister") ||
    desc.includes("law firm") || desc.includes("legal")) {
  return "Legal";
}

// Consulting / advisory
if (ind.includes("management consulting") || ind.includes("business consulting") ||
    ind.includes("strategy") || desc.includes("consultant") ||
    desc.includes("advisory") || desc.includes("consulting")) {
  return "Consulting";
}

// HR / recruitment / staffing
if (ind.includes("staffing") || ind.includes("recruiting") ||
    ind.includes("human resources") || desc.includes("recruitment") ||
    desc.includes("labour hire") || desc.includes("HR consulting")) {
  return "HR";
}

// Insurance / financial planning
if (ind.includes("insurance") || desc.includes("insurance") ||
    desc.includes("financial planner") || desc.includes("wealth management")) {
  return "Insurance";
}

// Training / education / RTO
if (ind.includes("professional training") || ind.includes("education management") ||
    desc.includes("RTO") || desc.includes("training provider")) {
  return "Training";
}

// Filter out — not professional services
return "Other";
```

**Use:** Filter Clay view to show only rows where `industry_group` ≠ "Other" before building email sequence.

### 2c — `signal_score`
Numeric score for prioritisation (higher = send first).
```javascript
let score = 0;

// Position Tier A = +3
const tier = String({{Position Tier}} || "").toUpperCase();
if (tier === "A") score += 3;
else if (tier === "B") score += 1;

// Hiring = +2
const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
if (hiring.includes("hiring")) score += 2;

// Google Reviews ≥ 5 = +1
const reviews = parseInt({{Reviews}} || 0);
if (reviews >= 5) score += 1;

// Rating ≥ 4.0 = +1
const rating = parseFloat({{Rating}} || 0);
if (rating >= 4.0) score += 1;

// LinkedIn Premium = +1
const premium = String({{badges_premium}} || "").toLowerCase();
if (premium === "true") score += 1;

return score;
```

### 2d — `signal_tier`
Converts `signal_score` into a send-priority tier.
```javascript
const score = parseInt({{signal_score}} || 0);
if (score >= 6) return "Hot";
if (score >= 4) return "Warm";
if (score >= 2) return "Standard";
return "Hold";
```

### 2e — `send_ready`
Final send-gate — only Tier A contacts with a valid email go to Smartlead.
```javascript
const tier = String({{Position Tier}} || "").toUpperCase();
const email = String({{Work Email}} || {{email}} || "").trim();
const group = String({{industry_group}} || "");
const hasEmail = email.includes("@") && email.length > 5;
const isPS = group !== "Other";
const isTierA = tier === "A";
return hasEmail && isPS && isTierA ? "YES" : "NO";
```

### 2f — `google_reviews_ps`
Builds the PS line for Email 1 from Google data. Returns empty string if no reviews.
```javascript
const reviews = parseInt({{Reviews}} || 0);
const rating = parseFloat({{Rating}} || 0);
const company = String({{current_company}} || "your firm");
if (reviews >= 5 && rating >= 4.0) {
  return `PS — ${company} has ${reviews} Google reviews at ${rating}. Most firms at that level still don't have a system that turns those reviews into inbound enquiries.`;
}
if (reviews >= 1 && reviews < 5) {
  return `PS — Noticed ${company} has ${reviews} Google review${reviews > 1 ? "s" : ""}. Most professional services firms in Darwin have 20+ and still aren't converting them into leads.`;
}
return "";
```

---

## Step 3 — AI Columns (Clay AI — Credits Used)

### 3a — `ps_opener`
**Model:** Claude (recommended) or GPT-4o
**Credits:** ~1 per row
**Purpose:** Industry-specific, NT-aware first line for Email 1

**Prompt:**
```
You are writing the first line of a cold email for a Darwin-based business consultancy (DGK) reaching out to a professional services firm owner in the Northern Territory.

The recipient:
- Name: {{first_name}}
- Company: {{current_company}}
- Industry group: {{industry_group}}
- Position: {{current_company_position}}
- LinkedIn headline: {{headline}}
- Company description: {{Description}}

Write ONE short sentence (max 15 words) that:
1. References something specific and true about their firm type OR their NT market context
2. Connects naturally to the idea of "building a client pipeline beyond referrals"
3. Does NOT start with "I noticed" or "I saw"
4. Does NOT mention a specific trigger (hiring, reviews, etc.) explicitly
5. Sounds like it came from someone who actually knows Darwin professional services

Examples of GOOD openers:
- "Darwin accounting firms at your size usually have one problem in common."
- "Most NT consulting firms I speak to have the same pipeline challenge."
- "Legal practices in Darwin typically build their reputation before they build their pipeline."

Examples of BAD openers:
- "I noticed you're hiring..." (too salesy)
- "I saw your LinkedIn profile..." (too generic)
- "Congratulations on your success..." (hollow)

Return ONLY the sentence. No explanation.
```

### 3b — `ps_pain_line`
**Model:** Claude or GPT-4o
**Credits:** ~1 per row
**Purpose:** Firm-specific pain observation for Email 3

**Prompt:**
```
You are writing one sentence that goes in the middle of a cold email (Email 3 in a sequence) to a Darwin professional services firm owner.

The recipient:
- Company: {{current_company}}
- Industry group: {{industry_group}}
- Description: {{Description}}
- Hiring: {{Hiring Status & Job Openings hiring Status}}
- Revenue: {{Annual Revenue}}

Write ONE sentence (max 20 words) that:
1. Names a pain specific to their firm type in the NT/Darwin market
2. Does NOT mention a trigger or signal explicitly
3. Sounds observational, not accusatory
4. Connects naturally to "building a client pipeline"

Industry-specific pain angles to draw from:
- Accounting: "Seasonal revenue swings — strong in Q1, quiet in Q3"
- Legal: "All new clients come through existing client referrals or word of mouth"
- Consulting: "Projects end and the pipeline starts from zero again"
- HR/Recruitment: "Client acquisition depends on relationships, not systems"
- Insurance: "New clients come through financial planner referrals, rarely direct"
- General: "Darwin professional services firms typically have strong reputations but no pipeline system"

Return ONLY the sentence. No explanation.
```

### 3c — `subject_email1`
**Model:** Claude or GPT-4o
**Credits:** ~1 per row
**Purpose:** AI-generated subject line for Email 1

**Prompt:**
```
Write a subject line for a cold email to {{first_name}} at {{current_company}}, a {{industry_group}} firm in Darwin, NT.

The email offers a lead magnet: "The 5-Step Client Pipeline: How Darwin Professional Services Firms Win Consistent Work Without Waiting for Referrals"

Subject line rules:
- 3-6 words max
- Lowercase only (never title case)
- No emojis, no punctuation except a comma or dash if natural
- No "I" at the start
- No clickbait or hype words
- Should feel like it came from a peer, not a vendor
- Reference their situation or the lead magnet topic

Examples of GOOD subjects:
- "client pipeline, {{first_name}}"
- "darwin {{industry_group}} — quick question"
- "without waiting for referrals"
- "consistent clients, darwin"

Return ONLY the subject line. No explanation.
```

### 3d — `subject_email3`
**Clayscript — 0 credits**
```javascript
const firstName = String({{first_name}} || "").trim().split(" ")[0];
const options = [
  "quick question",
  `${firstName} — how are you winning new clients?`,
  "worth 15 min?",
  "last one",
  `new clients at {{current_company}}`
];
const idx = Math.abs({{first_name}}.charCodeAt(0) + {{current_company}}.charCodeAt(0)) % options.length;
return options[idx];
```

---

## Step 4 — Email Variant Logic

### 4a — `email_variant`
Routes each contact to the right Email 1 copy block.
```javascript
const group = String({{industry_group}} || "Other");
const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
const tier = String({{Position Tier}} || "").toUpperCase();

// Tier A + Hiring → premium variant
if (tier === "A" && hiring.includes("hiring")) return "Tier_A_Hiring";

// Industry-specific variants
if (group === "Accounting") return "Accounting";
if (group === "Legal") return "Legal";
if (group === "Consulting") return "Consulting";

// Default — all professional services
return "Standard";
```

---

## Step 5 — Filter & Sort for Send

1. Filter view: `send_ready` = "YES"
2. Sort by: `signal_score` descending (highest-priority contacts first)
3. Export to CSV or connect Smartlead integration

**Expected sendable contacts:** ~30-40 (of ~50 professional services contacts)

---

## Step 6 — Smartlead Column Mapping

| Clay Column | Smartlead Variable | Used In |
|---|---|---|
| `clean_first_name` | `{{firstName}}` | All emails |
| `current_company` | `{{company}}` | All emails |
| `ps_opener` | `{{customVariable1}}` | Email 1 |
| `google_reviews_ps` | `{{customVariable4}}` | Email 1 + Email 3 |
| `ps_pain_line` | `{{customVariable2}}` | Email 3 |
| `subject_email1` | `{{customVariable7}}` | Email 1 subject |
| `subject_email3` | `{{customVariable8}}` | Email 3 subject |
| `email_variant` | `{{customVariable5}}` | Smartlead routing |
| `Work Email` | Recipient email | — |

---

## Step 7 — Pre-Send Checklist

- [ ] Verify all emails (Millionverifier or Prospeo) — bounce rate must stay < 2%
- [ ] Check `send_ready` = "YES" filter applied
- [ ] Review 10 random rows for AI column quality (ps_opener, ps_pain_line)
- [ ] Confirm `signal_tier` = "Hot" contacts are in first send batch
- [ ] Run `/spam-word-checker` on email copy before upload
- [ ] Confirm Smartlead campaign uses correct variable mapping above
- [ ] Set sending limit: max 30/inbox/day
- [ ] Set sequence delays: Email 1 → Email 2: 4 days; Email 2 → Email 3: 5 days

---

## Expected Output Summary

| Metric | Expected |
|---|---|
| Total Darwin CSV rows | 256 |
| Professional services segment | ~40-55 |
| Tier A with valid email | ~30-40 |
| Hot (signal score ≥ 6) | ~8-15 |
| Warm (signal score 4-5) | ~10-18 |
| Standard (signal score 2-3) | ~10-15 |
