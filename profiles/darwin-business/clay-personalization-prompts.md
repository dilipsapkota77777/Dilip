# Darwin Business — Clay Personalization Prompts
# ColdIQ Framework | NT Trades & Commercial Outreach
Generated: 2026-07-27

---

## Overview

Three AI prompts + one Clayscript column for personalisation at scale across 256 Darwin/NT trade business contacts.

All prompts use chain-of-thought structure: force AI to extract a specific detail BEFORE writing. This eliminates generic outputs like "Your headline identifies you as a leader in..."

| Column | Model | Credits | Used In |
|---|---|---|---|
| `darwin_opener` | GPT-4 Mini | ~1/row | Email 1 line 1, Email 3 line 1 |
| `darwin_pain_line` | GPT-4 Mini | ~1/row | Email 2 line 1 |
| `darwin_case_study_line` | GPT-4 Mini | ~1/row | Email 3 PS |
| `google_reviews_ps` | Clayscript | 0 | Email 1 PS |

---

## PROMPT 1 — `darwin_opener`

**Purpose:** Personalized first line for Email 1 and Email 3. Sets the NT-specific growth angle.
**Model:** GPT-4 Mini
**Conditional:** Only run if `darwin_opener` is empty

```
You are writing the first line of a cold email to {{clean_first_name}}, {{current_company_position}} at {{current_company}} in Darwin, Northern Territory, Australia.

STEP 1 — Identify their business context using the industry group: {{industry_group}}

Pain context by industry group (internal reasoning only — never output this):
- Construction: Tenders and word-of-mouth dominate, but Google search is growing as a procurement research channel. Builders who dominate local search win contracts others don't know exist.
- Resources (Oil/Gas/Mining/Aviation/Energy): Existing contractor frameworks dominate. Digital presence is under-invested. A Google-first positioning gets companies into conversations before RFQs are issued.
- Commercial: Referrals drive most business. Review platforms and Google Business are underutilised. Strong digital presence converts reputation into inbound enquiries.

STEP 2 — Extract ONE specific, unique detail from these inputs:
- Headline: {{headline}}
- Company description: {{Description}}
- Company: {{current_company}}
- Location: {{location_name}}

Pick exactly ONE of:
(a) A specific service, specialty, or market they name
(b) A geographic claim (NT-specific, remote, Darwin-based)
(c) A mission or values statement they express
(d) A market position (largest, only, first, etc.)

STEP 3 — Write ONE sentence using one of these patterns:

Pattern A (observation about their model):
"[Specific thing from Step 2] in the NT market usually means [a specific growth constraint or opportunity]."

Pattern B (NT-specific peer observation):
"Most [their industry type] businesses in Darwin still [what they rely on] — the ones growing commercial clients consistently are changing that."

Pattern C (their specific position + opportunity):
"[Specific claim from Step 2] positions {{current_company}} for exactly the kind of [outcome] that referrals alone can't deliver consistently."

Rules:
- Maximum 25 words
- No greetings, no "Hi", no "I noticed", no "I came across"
- No compliments ("impressive", "great work", "love what you do")
- No mention of DGK, digital marketing, or any services
- Peer-level observation only — not a pitch
- All lowercase except proper nouns and company names
- No full stop at the end of the sentence

Output only the single sentence. Nothing else.
```

---

### `darwin_opener` — Good vs Bad Examples

**Good outputs:**
- "Civil construction in the NT market usually means strong project wins — but commercial enquiries rarely find you online before they call someone else."
- "Most aviation maintenance businesses in Darwin still win contracts through existing relationships — the ones adding new commercial clients are building a different channel."
- "Larrakia-owned civil construction at AKJ's scale means your reputation is strong locally — but commercial buyers outside your existing network rarely find you through Google."

**Bad outputs (what to avoid):**
- "Your headline identifies you as a Managing Director at Banksia Civil." ← NEVER
- "I came across your company and was impressed by your work." ← NEVER
- "Your focus on indigenous employment is commendable." ← NEVER
- "As a leader in NT construction..." ← too generic

---

## PROMPT 2 — `darwin_pain_line`

**Purpose:** First line of Email 2. Industry-specific pain that opens the conversation naturally.
**Model:** GPT-4 Mini
**Conditional:** Only run if `darwin_pain_line` is empty

```
You are writing the opening sentence of Email 2 in a cold email sequence to {{clean_first_name}}, {{current_company_position}} at {{current_company}} in Darwin, NT.

This email teaches a specific technique. The opening line must name the pain that makes the technique relevant — without pitching anything.

STEP 1 — Select the base pain pattern for their industry group: {{industry_group}}

PAIN PATTERNS:
- Construction: "Most Darwin construction businesses I speak to win work through relationships and reputation — then hit a ceiling when those networks dry up or a new commercial buyer enters the market."
- Resources: "Most NT operators in [oil & gas / aviation / mining / energy] rely on existing contractor frameworks and relationships — and struggle to get in front of new commercial opportunities when a contract cycle opens."
- Commercial: "Most commercial service businesses in Darwin tell me the same thing — clients come through referrals, and new client growth stops when referrals slow down."

STEP 2 — Localise the base pattern using:
- Their specific LinkedIn industry: {{Industry}}
- Their company description (check for any specific context): {{Description}}
- Their position: {{current_company_position}}

Localise means: swap the generic industry label (e.g. "construction businesses") for their specific type (e.g. "civil contractors in Darwin") if the description gives you a clearer category. Do not change the pain itself.

STEP 3 — Write the localised sentence.

Rules:
- Maximum 28 words
- One complete sentence
- Full stop at the end
- No pitch, no mention of DGK or digital marketing
- Peer-level tone — written as if you understand their industry from working with similar businesses
- Do not start with "I" — start with "Most" or the company type

Output only the single sentence. Nothing else.
```

---

### `darwin_pain_line` — Good vs Bad Examples

**Good outputs:**
- "Most Darwin civil contractors I speak to win work through relationships — then hit a ceiling when a new commercial buyer enters the market and doesn't know them."
- "Most NT aviation maintenance operators rely on existing framework contracts — and struggle to get in front of new commercial opportunities when a tender cycle opens."
- "Most commercial service businesses in Darwin tell me the same thing — clients come through referrals, and growth stalls when referrals slow down."

**Bad outputs:**
- "I see that you are in the construction industry." ← NEVER
- "You probably struggle with getting new clients." ← too direct/presumptuous
- "Digital marketing can help your business grow." ← pitch too early

---

## PROMPT 3 — `darwin_case_study_line`

**Purpose:** PS line for Email 3. Social proof that makes the offer concrete and believable.
**Model:** GPT-4 Mini
**Conditional:** Only run if `darwin_case_study_line` is empty

**IMPORTANT:** Before running this prompt at scale, fill in a real DGK client case study below. Replace `[CLIENT_TYPE]`, `[BEFORE_STATE]`, `[AFTER_STATE]`, and `[TIMEFRAME]` with real data.

**Current placeholder:**
```
[CLIENT_TYPE] = "Darwin electrical contractor"
[BEFORE_STATE] = "3 enquiries per month from word-of-mouth"
[AFTER_STATE] = "9 inbound commercial enquiries per month from Google"
[TIMEFRAME] = "90 days"
```

```
Write a one-sentence PS social proof line for a cold email to {{clean_first_name}} at a {{industry_group}} company in Darwin, NT.

Context:
- DGK helps NT trade businesses get more commercial clients through digital marketing, Google presence optimisation, CRM setup, and AI automation.
- Use this case study: [CLIENT_TYPE] went from [BEFORE_STATE] to [AFTER_STATE] in [TIMEFRAME] — without running a single paid ad.

Industry group: {{industry_group}}

Rules:
- Start with "PS —"
- One sentence only
- Match the case study to their industry group where possible (Construction → construction client, Resources → operator/contractor, Commercial → service business)
- Use specific numbers from the case study
- No exclamation marks
- No mention of the client's name — just their company type and location/territory

Output only the PS line. Nothing else.
```

---

### `darwin_case_study_line` — Example Output

**For Construction:**
"PS — A Darwin civil contractor went from 3 referral enquiries a month to 9 inbound commercial enquiries through Google positioning — in 90 days, zero paid ads."

**For Resources:**
"PS — An NT aviation services operator used Google Business and digital positioning to get shortlisted for two new commercial contracts in their first month — without ads."

**For Commercial:**
"PS — A Darwin service business went from relying on referrals to 9 consistent inbound commercial enquiries per month through Google — in 90 days, without running ads."

---

## Clayscript Column — `google_reviews_ps`

**Purpose:** Pulls the pre-generated Google reviews opener from CSV into a clean PS format for Email 1.
**Cost:** 0 credits (Clayscript)

```javascript
const opener = String({{Google Reviews Opener}} || "").trim();
if (opener.length > 10) return `PS — ${opener}`;

// Fallback: generate from raw data if opener column is empty
const rating = parseFloat({{Rating}} || 0);
const reviews = parseInt({{Reviews}} || 0);

if (rating >= 4.5 && reviews >= 20) {
  return `PS — ${rating} from ${reviews} reviews tells me ${String({{current_company}} || "your business")} has built real trust in Darwin. Most trade businesses never turn that into consistent inbound enquiries.`;
}
if (rating >= 4.0 && reviews >= 5) {
  return `PS — ${rating} from ${reviews} reviews is a strong foundation. The question is whether that trust is showing up when commercial buyers search for you.`;
}
if (reviews < 5) {
  return `PS — Building a review base on Google is step one — once it's there, the rest of the system amplifies it.`;
}
return "";
```

---

## Industry Group Classification

The `industry_group` Clayscript column assigns one of three values used across all prompts and email copy.

| industry_group | LinkedIn Industries (from CSV) | Count |
|---|---|---|
| `Construction` | Construction, Civil Engineering, Specialty Trade Contractors, Building Construction | ~75 |
| `Resources` | Oil & Gas, Mining, Airlines/Aviation, Aerospace, Utilities, Environmental Services, Energy | ~50 |
| `Commercial` | IT Services, Manufacturing, Maritime, Logistics, Wholesale, Retail, Facilities, Services | ~130 |

---

## Qualification Scoring

Use this Clayscript to assign a `quality_score` for prioritising outreach order:

```javascript
let score = 0;

// Tier A = decision maker (CEO/Founder/MD/Director)
if (String({{Position Tier}} || "") === "A") score += 30;

// Hiring = growing business = capacity before clients
if (String({{Hiring Status & Job Openings hiring Status}} || "") === "hiring") score += 20;

// Strong Google reviews
const rating = parseFloat({{Rating}} || 0);
const reviews = parseInt({{Reviews}} || 0);
if (rating >= 4.5 && reviews >= 20) score += 20;
else if (rating >= 4.0 && reviews >= 5) score += 10;

// Revenue signals
const rev = String({{Annual Revenue}} || "");
if (rev.includes("10M") || rev.includes("25M") || rev.includes("75M")) score += 15;
else if (rev.includes("5M")) score += 10;
else if (rev.includes("1M")) score += 5;

// Employee count (sweet spot: 11-200 for DGK's offer)
const size = String({{Size}} || "");
if (size.includes("11-50") || size.includes("51-200")) score += 10;

// Valid email
const email = String({{Work Email}} || {{email}} || "");
if (email.includes("@") && !email.includes("not found")) score += 10;

return score;
```

**Score tiers:**
- 70+ → Contact first (Hot)
- 50–69 → Second batch (Warm)
- 30–49 → Third batch (Standard)
- Below 30 → Hold / LinkedIn only

---

## Personalisation Best Practices for This Campaign

**DO:**
- Reference their specific NT location or remote market context — Darwin is a small market, that specificity lands
- Name their industry type (civil contractor, aviation services, waste management) not just "business owner"
- Reference the Google reviews data you have — it shows you've done research
- Use hiring signal as proof of growth (company is growing = right time to build a client system)

**DON'T:**
- Generic AI compliments ("Love your work!", "Your leadership is impressive")
- Open with "I" — always open with "Most [industry] businesses..." or their specific detail
- Reveal the technique (Google/digital strategy) in Email 1 — that's the hook for Email 2
- Mention "AI automation" in Email 1 — too early, sounds like a tech pitch
- Use the same opener for a Tier A CEO and a General Manager — tailor the angle
