# DGK Business Consultancy — Modular Email Campaign System
Generated: 2026-07-04

Target: 521 Darwin/NT LinkedIn connections
Segments: Trades (256) · Professional Services (218) · Agency (47)
Sequence: 3 emails per segment · Email 1 has 3 A/B/C opener variations
Structure: 6 modular Clay columns per email · each element generated independently

---

## How This System Works

Each email is assembled from 6 Clay columns. Most columns are AI-generated with GPT-4o Mini (cheap, fast, good enough for sentence-level output). Static columns cost 0 credits. The final `email_body` column concatenates all 6 with a formula.

```
email_body = opener_line + "\n\n" + pain_line + "\n\n" + value_line + "\n\n" + cta + "\n\n" + darwin_close
```

Subject line is a separate column that Smartlead uses as the campaign subject.

---

## CTA Formula (Clay — Clayscript, 0 credits)

**Column name:** `cta`
**Type:** Formula
**Input:** `{{employee_count}}`, `{{first_name}}`

```javascript
const emp = parseInt(String({{employee_count}} || "0").replace(/[^0-9]/g, ""), 10);
const name = String({{first_name}} || "").trim();

if (emp > 0 && emp < 20) {
  return `${name}, we're a registered provider for the Australian Government's Digital Solutions Program — gives eligible businesses up to 5 hours of digital advisory at zero cost to you. Happy to check if you qualify and run through it — I'm Darwin-based so easy to meet in person.`;
} else {
  return `Worth 15–20 minutes? I'm Darwin-based so happy to meet in person or jump on a quick call — whichever's easier.`;
}
```

> **Note:** If `employee_count` is blank/null, defaults to discovery call CTA. Enrich `employee_count` via Apollo or Clearbit before running CTA formula.

---

## Signal Selector Formula (Clay — Clayscript, 0 credits)

**Column name:** `signal_type`
**Type:** Formula
**Input:** `{{industry_final}}`, `{{google_rating}}`, `{{google_review_count}}`, `{{employee_count}}`, `{{headline}}`, `{{is_hiring}}`

Determines which Email 1 variation (A/B/C) to send per contact.

```javascript
const segment  = String({{industry_final}} || "").trim();
const rating   = parseFloat(String({{google_rating}} || "0")) || 0;
const reviews  = parseInt(String({{google_review_count}} || "0").replace(/[^0-9]/g, ""), 10) || 0;
const emp      = parseInt(String({{employee_count}} || "0").replace(/[^0-9]/g, ""), 10) || 0;
const headline = String({{headline}} || "").toLowerCase();
const hiring   = String({{is_hiring}} || "").toLowerCase() === "true";

if (segment === "Trades") {
  if (rating >= 4.5 && reviews >= 15) return "A-reviews-strong";
  if (rating > 0 && (rating < 3.9 || reviews < 10)) return "A-reviews-gap";
  if (hiring || String({{job_opening}} || "").length > 0) return "B-hiring";
  return "C-firmographic";
}

if (segment === "Professional Services") {
  if (emp > 0 && emp <= 5) return "A-capacity-ceiling";
  if (headline.includes("referral") || headline.includes("word of mouth")) return "A-referral-risk";
  return "B-ai-inference";
}

if (segment === "Agency") {
  if (headline.includes("referral") || headline.includes("word of mouth")) return "A-cobbler";
  return "B-ai-inference";
}

return "C-firmographic";
```

---

## Google Reviews Enrichment (Trades ONLY)

Reviews data is only meaningful for B2C trade businesses where Google reputation drives new enquiries. Do NOT run for Professional Services or Agency.

**Column: `google_rating`**
- Type: Claygent Neon (1–2 credits)
- Conditional run: `industry_final` = `Trades`

```
Find the Google Business Profile for {{company}} in Darwin, Northern Territory, Australia.

Return ONLY their current Google star rating as a number (e.g., 4.7).

If no Google Business Profile exists, return: none
If the company is not in Darwin NT, return: none
Output: number only (e.g., 4.7) or the word "none"
```

**Column: `google_review_count`**
- Type: Claygent Neon (1–2 credits)
- Conditional run: `industry_final` = `Trades`

```
Find the Google Business Profile for {{company}} in Darwin, Northern Territory, Australia.

Return ONLY the total number of Google reviews as an integer (e.g., 23).

If no Google Business Profile exists, return: 0
Output: integer only (e.g., 23) or 0
```

---

---

# SEGMENT 1: TRADES (256 contacts)

**Core pain:** Feast/famine cycle — busy on jobs, no system to keep pipeline flowing during quiet months. Word-of-mouth dependent, Darwin's seasonal work patterns hit tradies hardest.

**DGK angle:** Digital system (website, Google presence, CRM, online enquiry flow) that keeps work coming in without the owner doing sales.

---

## Signal Priority Waterfall — Trades

| Priority | Condition | Variation |
|---|---|---|
| 1 | `google_rating` ≥ 4.5 AND `google_review_count` ≥ 15 | A — Reputation Leverage |
| 2 | `google_rating` < 3.9 OR `google_review_count` < 10 (with valid rating) | A — Reputation Gap |
| 3 | `is_hiring` = true OR `job_opening` not empty | B — Capacity/Hiring |
| 4 | No signal | C — Firmographic Fallback |

---

## TRADES — EMAIL 1, VARIATION A: Reviews Signal

Use when: `signal_type` = `A-reviews-strong` or `A-reviews-gap`

### Column: `trades_e1a_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-reviews`

```
You write cold email subject lines for a Darwin-based digital growth consultancy targeting trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Google Rating: {{google_rating}} stars ({{google_review_count}} reviews)

Write ONE subject line (max 7 words) that uses their review count or rating as a signal — hinting that their online reputation and their digital systems may not be aligned.

Rules:
- No clickbait, no exclamation marks, no question marks
- No "quick question" or generic hooks
- Sound like someone who noticed something specific
- Output: subject line text only, no quotes, no punctuation at end
```

### Column: `trades_e1a_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-reviews`

```
You write first-sentence openers for cold emails targeting Darwin trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Google Rating: {{google_rating}} stars
Review Count: {{google_review_count}}

Write ONE opening sentence (max 20 words) that references their Google Reviews rating and count.

If rating >= 4.5 AND reviews >= 15:
→ Frame as: strong reputation that isn't being fully leveraged to drive digital enquiries
→ Tone: "You've built trust — the question is whether your online presence is converting it."

If rating < 3.9 OR reviews < 10:
→ Frame as: they're good at the work but the online signal doesn't match the quality
→ Tone: "You're doing great work — the digital footprint doesn't show it yet."

Rules:
- Conversational, not corporate
- Sound like a peer who noticed something, not a salesperson
- No compliments ("love your work", "impressive business")
- Max 20 words
- Output: one sentence only, no quotes
```

### Column: `trades_e1a_pain`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-reviews`

```
You write one pain-acknowledgment sentence for cold emails targeting Darwin trade businesses.

Company: {{company}}

Write ONE sentence (max 20 words) about the feast/famine cycle in Darwin trades — busy during peak season with no follow-up system, then quiet periods with no pipeline.

Rules:
- Specific to trade businesses, not generic business pain
- Darwin/NT context welcome (wet season slowdown, cyclone prep, etc.)
- Empathetic tone — you've seen this before, not judging
- No jargon
- Output: one sentence only, no quotes
```

### Column: `trades_value_line`
Type: Static Formula · 0 credits

```javascript
return "Most Darwin tradies we work with were getting work through word-of-mouth — which works until it doesn't. We help them build a simple digital system that keeps new enquiries coming in even when they're heads-down on a job.";
```

---

## TRADES — EMAIL 1, VARIATION B: Hiring/Capacity Signal

Use when: `signal_type` = `B-hiring`

### Column: `trades_e1b_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-hiring`

```
You write cold email subject lines for a Darwin-based digital growth consultancy targeting trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Job Opening: {{job_opening}}

Write ONE subject line (max 7 words) that hints at the capacity pressure — growing the team, but the pipeline needs to keep pace.

Rules:
- No clickbait, no question marks
- Reference growth or hiring signal naturally
- Output: subject line text only, no quotes
```

### Column: `trades_e1b_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-hiring`

```
You write first-sentence openers for cold emails targeting Darwin trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Job Opening: {{job_opening}}

Write ONE opening sentence (max 20 words) that references the hiring or growth signal.

If job opening data available: reference the specific role they're hiring for
If job opening field is empty: use "Noticed {{company}} looks like it's been growing"

Frame as: "growing the team is one side of it — the other is making sure the pipeline keeps up."

Rules:
- Observational, not presumptuous
- Max 20 words
- No compliments
- Output: one sentence only, no quotes
```

### Column: `trades_e1b_pain`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-hiring`

```
You write one pain-acknowledgment sentence for cold emails targeting Darwin trade businesses during growth.

Company: {{company}}

Write ONE sentence (max 20 words) about the pressure of scaling a trade business in Darwin — more staff, same word-of-mouth pipeline, inconsistent workload.

Rules:
- Darwin context: small market, personal referrals, seasonal demand
- Empathetic — you understand the pressure
- Not critical of their growth decisions
- Output: one sentence only, no quotes
```

---

## TRADES — EMAIL 1, VARIATION C: Industry Pattern (Firmographic)

Use when: `signal_type` = `C-firmographic`

### Column: `trades_e1c_subject`
Type: Static Formula · 0 credits

```javascript
const pos = String({{clean_position}} || "").toLowerCase();
const comp = String({{company}} || "").toLowerCase();

if (pos.includes("electrician") || pos.includes("electrical") || comp.includes("electrical")) return "Darwin electricians — filling the quiet months";
if (pos.includes("plumb") || comp.includes("plumb")) return "Darwin plumbers — work beyond word of mouth";
if (pos.includes("builder") || pos.includes("construction") || comp.includes("build")) return "Darwin builders — steady pipeline beyond referrals";
if (pos.includes("air conditioning") || pos.includes("hvac") || comp.includes("air con")) return "HVAC — Darwin off-season pipeline";
if (pos.includes("landscap") || comp.includes("landscap")) return "Darwin landscapers — work in the quiet months";
if (pos.includes("mechan") || comp.includes("mechan")) return "Darwin mechanics — more cars, less word of mouth";
return "Darwin tradies — pipeline beyond who you know";
```

### Column: `trades_e1c_opener`
Type: Static Formula · 0 credits

```javascript
const pos = String({{clean_position}} || "").toLowerCase();
return `Most Darwin ${pos || "trade businesses"} we speak with are great at the work — the challenge is keeping a steady pipeline outside of who they already know.`;
```

### Column: `trades_e1c_pain`
Type: Static · 0 credits

```javascript
return "Word-of-mouth works until it doesn't — one slow month with nothing in the diary is all it takes to feel the pressure.";
```

---

## TRADES — EMAIL 2 (Follow-Up, Day 5)

### Column: `trades_e2_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write follow-up cold email subject lines for Darwin trade businesses that didn't reply to the first email.

Contact: {{first_name}} {{last_name}}
Company: {{company}}

Write ONE subject line (max 7 words) — a soft pattern interrupt that re-opens the conversation without being pushy.

Rules:
- No "just following up" or "checking in"
- No question marks
- Reference the Darwin quiet-period or pipeline problem
- Output: subject line text only, no quotes
```

### Column: `trades_e2_add`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write a follow-up value-add sentence for cold emails to Darwin trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Google Rating: {{google_rating}} (if available)
Employee Count: {{employee_count}}

Write ONE sentence (max 20 words) that adds a NEW angle not covered in Email 1. Choose one:
- Their Google reputation not converting to direct online enquiries
- The risk of relying on a referral pipeline they can't control
- What other Darwin tradies are doing to fill quiet months

Rules:
- Must be a new angle, not a repeat
- Specific to Darwin trades context
- No pressure language
- Output: one sentence only, no quotes
```

### Email 2 Full Template (assembled in Smartlead or Clay formula)
```
Hi {{first_name}},

Sent you a note last week — wanted to add one thing.

{{trades_e2_add}}

We've helped a handful of Darwin trade businesses get a system in place — usually takes a few sessions, then it runs itself.

{{cta}}

{{darwin_close}}

{{signature}}
```

### Column: `trades_darwin_close`
Type: Static · 0 credits

```javascript
return "Either way — we're Darwin-based, so easy to have a quick chat in person if that suits better.";
```

---

## TRADES — EMAIL 3 (Breakup, Day 12)

### Subject (A/B split — use Smartlead subject split)
- Option A: `{{first_name}}, closing your file`
- Option B: `not the right time?`

### Email 3 Template
```
Hi {{first_name}},

Haven't heard back — no worries at all.

I'll assume the timing isn't right. If that changes and you want to look at building a steadier flow of work through digital channels, happy to pick it up whenever.

We're Darwin-based so easy to grab a coffee when it suits.

{{signature}}
```

---

---

# SEGMENT 2: PROFESSIONAL SERVICES (218 contacts)

**Core pain:** Referral ceiling — grown well on word-of-mouth and network, but can't scale beyond that without a repeatable pipeline. Vulnerable when a key referral source dries up.

**DGK angle:** Digital client acquisition system (website that converts, targeted content, CRM workflow) that attracts qualified clients without ads or cold calls.

**No Google Reviews signal** — B2B buyers don't check Google stars for accountants or lawyers. Signal priority: capacity ceiling → referral dependency → AI pain inference → firmographic.

---

## Signal Priority Waterfall — Professional Services

| Priority | Condition | Variation |
|---|---|---|
| 1 | `employee_count` ≤ 5 | A — Capacity Ceiling |
| 2 | `headline` contains "referral" or "word of mouth" | A — Referral Risk |
| 3 | AI can infer digital gap from company type | B — AI Pain Inference |
| 4 | No signal | C — Firmographic Fallback |

---

## PROFESSIONAL SERVICES — EMAIL 1, VARIATION A: Capacity Ceiling / Referral Risk

Use when: `signal_type` = `A-capacity-ceiling` or `A-referral-risk`

### Column: `ps_e1a_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-`

```
You write cold email subject lines for a Darwin-based digital growth consultancy targeting professional services firms (accountants, lawyers, financial advisers, consultants, IT firms, recruiters, real estate agents).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}
Employee Count: {{employee_count}}

Write ONE subject line (max 7 words) about the referral ceiling — professional services firms that have grown to a comfortable size on referrals but can't scale further without a pipeline.

If employee_count <= 5: lean toward "high-output small team hitting capacity" angle
If employee_count > 5: lean toward "grown on referrals, now hitting the ceiling" angle

Rules:
- No clickbait, no question marks
- Professional tone, not salesy
- Output: subject line text only, no quotes
```

### Column: `ps_e1a_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-`

```
You write cold email openers for Darwin professional services firms.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}
Employee Count: {{employee_count}}
LinkedIn Headline: {{headline}}

Write ONE opening sentence (max 20 words) that observes the referral ceiling or capacity constraint.

If signal_type = A-capacity-ceiling (emp <= 5):
→ "Small high-output team that's grown on referrals — the ceiling hits when there's no bandwidth left to chase new work."

If signal_type = A-referral-risk:
→ "Firms that have grown on referrals reach a point where the next step requires a pipeline they can actually control."

Match to their specific firm type (accounting, law, finance, IT, etc.).

Rules:
- Sound like an outside observer who has seen this pattern across many similar firms in Darwin
- Not presumptuous — use "in my experience with firms like yours" framing
- Max 20 words
- No generic compliments
- Output: one sentence only, no quotes
```

### Column: `ps_e1a_pain`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` includes `A-`

```
You write one pain-acknowledgment sentence for cold emails targeting Darwin professional services businesses (accountants, lawyers, financial advisers, consultants, IT firms, recruiters).

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) about the referral dependency risk — what happens when a key referral source retires, a star employee leaves, or the network dries up.

Rules:
- Specific to professional services (not trades or agencies)
- Darwin/NT context: small professional network, everyone knows everyone
- Empathetic, not critical
- Output: one sentence only, no quotes
```

---

## PROFESSIONAL SERVICES — EMAIL 1, VARIATION B: AI Pain Inference

Use when: `signal_type` = `B-ai-inference`

### Column: `ps_e1b_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-ai-inference` AND `industry_final` = `Professional Services`

```
You write cold email subject lines for Darwin professional services firms.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Infer what type of professional services firm this is from the company name, headline, and position. Write ONE subject line (max 7 words) that targets the specific digital pipeline pain for that firm type.

Known pain patterns by type:
- Accounting: reliance on referrals, no digital presence converting visitors
- Law: no way to turn online searchers into enquiries
- IT/Tech consulting: builds systems for clients, not for own pipeline
- Recruitment: repeat client dependency, hiring freezes kill revenue
- Financial advice: no content strategy to attract ideal clients
- Real estate: portal dependency, no owned client list

Rules:
- No question marks, no clickbait
- Match to their actual firm type
- Output: subject line text only, no quotes
```

### Column: `ps_e1b_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-ai-inference` AND `industry_final` = `Professional Services`

```
You write cold email openers for Darwin professional services firms.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Identify this firm's type from the name, headline, and position. Write ONE opening sentence (max 20 words) that calls out the digital pipeline pain specific to their firm type.

Pattern examples to adapt:
- Accounting: "Most accounting firms in Darwin still get 80%+ of new clients from referrals — which works until your biggest referrer retires."
- Law: "Most small law firms in Darwin have no way to convert website visitors into enquiries — they rely on who they know."
- IT consulting: "Most Darwin IT consultancies build systems for clients but haven't applied the same thinking to their own new client pipeline."
- Recruitment: "Most recruitment firms in Darwin rely on repeat clients — the problem comes when one client pauses hiring."
- Financial advice: "Most financial advisers in Darwin build their book through referrals and events — and have no way to attract clients who aren't in their network yet."

Adapt the closest pattern to their actual firm type. Sound like you've seen this before.

Rules:
- One sentence only
- Observational, not accusatory
- Max 20 words
- Output: one sentence only, no quotes
```

### Column: `ps_e1b_pain`
Type: Reuse `ps_e1a_pain` — same prompt, same column.

---

## PROFESSIONAL SERVICES — EMAIL 1, VARIATION C: Firmographic Fallback

Use when: No specific signal available (rare — most will hit A or B)

### Column: `ps_e1c_subject`
Type: Static Formula · 0 credits

```javascript
const pos  = String({{clean_position}} || "").toLowerCase();
const comp = String({{company}} || "").toLowerCase();

if (pos.includes("account") || comp.includes("account")) return "how accounting firms stop relying on referrals";
if (pos.includes("lawyer") || pos.includes("legal") || comp.includes("law")) return "new clients without waiting for referrals";
if (pos.includes("recruit") || comp.includes("recruit") || comp.includes("staffing")) return "pipeline when clients pause hiring";
if (pos.includes("it ") || pos.includes("tech") || comp.includes("software") || comp.includes("cyber")) return "IT firms — pipeline beyond your existing clients";
if (pos.includes("financial") || pos.includes("finance") || pos.includes("mortgage")) return "financial advisers finding clients outside referrals";
if (pos.includes("real estate") || pos.includes("property") || comp.includes("real estate")) return "Darwin real estate — leads beyond the portals";
if (pos.includes("consult") || comp.includes("consult")) return "consulting pipeline that doesn't rely on referrals";
return "Darwin professional services — growth beyond referrals";
```

### Column: `ps_e1c_opener`
Type: Static Formula · 0 credits

```javascript
const pos  = String({{clean_position}} || "").toLowerCase();
const comp = String({{company}} || "").toLowerCase();
const type = pos.includes("account") || comp.includes("account") ? "accounting firms"
           : pos.includes("lawyer") || pos.includes("legal") || comp.includes("law") ? "law firms"
           : pos.includes("recruit") || comp.includes("recruit") ? "recruitment firms"
           : pos.includes("financial") || pos.includes("finance") ? "financial advisory businesses"
           : pos.includes("consult") || comp.includes("consult") ? "consulting firms"
           : "professional services businesses";

return `Most ${type} in Darwin we speak with have grown well on referrals — the challenge is that it's a pipeline they can't control or predict.`;
```

---

## Professional Services — value_line & darwin_close (Static)

### Column: `ps_value_line`
Type: Static · 0 credits

```javascript
return "We work with professional services firms in Darwin on building a repeatable digital client pipeline — not ads, not cold calls — a system that attracts the right clients and makes it easy for them to reach out.";
```

### Column: `ps_darwin_close`
Type: Static · 0 credits

```javascript
return "We're Darwin-based, so easy to meet in person if that's easier than a call.";
```

---

## PROFESSIONAL SERVICES — EMAIL 2 (Follow-Up, Day 5)

### Column: `ps_e2_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write follow-up cold email subject lines for Darwin professional services firms that didn't reply.

Contact: {{first_name}} {{last_name}}
Company: {{company}}

Write ONE subject line (max 7 words) — a soft re-open that adds a new angle.

Rules:
- No "following up" or "checking in"
- No question marks
- Reference the referral dependency or client pipeline problem
- Output: subject line text only, no quotes
```

### Column: `ps_e2_add`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write follow-up value-add sentences for cold emails to Darwin professional services firms.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) that adds a NEW angle not covered in Email 1. Choose one:
- A Darwin market insight: NT's small professional network means referral pools dry up faster than in Sydney or Melbourne
- An opportunity cost: every month without a pipeline is months of potential work that went to someone else
- A social proof: "We recently helped a Darwin [firm type] build a system that..."

Rules:
- Must be a genuinely new angle, not a restate
- Professional tone
- Max 20 words
- Output: one sentence only, no quotes
```

### Email 2 Full Template
```
Hi {{first_name}},

Sent you a note last week — wanted to add one more thing.

{{ps_e2_add}}

If the timing's off, no worries. But if it's something you've been thinking about, happy to compare notes — no pitch, just a conversation.

{{cta}}

{{ps_darwin_close}}

{{signature}}
```

---

## PROFESSIONAL SERVICES — EMAIL 3 (Breakup, Day 12)

### Subject (A/B split)
- Option A: `{{first_name}}, closing this off`
- Option B: `not right for you?`

### Email 3 Template
```
Hi {{first_name}},

No reply — completely fine.

I'll leave it here. If you ever want to revisit building a more consistent client pipeline that doesn't depend on who referred you last month, reach out whenever.

Darwin's small enough that we'll probably run into each other anyway.

{{signature}}
```

---

---

# SEGMENT 3: AGENCY (47 contacts)

**Core pain:** The cobbler's children problem — marketing and creative agencies build digital systems for clients but rely on word-of-mouth for their own new business. Unpredictable pipeline, client selectivity suffers.

**DGK angle:** New business pipeline system for Darwin agencies — not more cold calls, a content and digital system that attracts the right type of client work.

---

## Signal Priority Waterfall — Agency

| Priority | Condition | Variation |
|---|---|---|
| 1 | `headline` or description mentions referral/word-of-mouth | A — Cobbler's Children |
| 2 | AI infers pipeline gap from agency type | B — AI Pain Inference |
| 3 | No signal | C — Firmographic Fallback |

---

## AGENCY — EMAIL 1, VARIATION A: Cobbler's Children

Use when: `signal_type` = `A-cobbler`

### Column: `agency_e1a_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `A-cobbler`

```
You write cold email subject lines for a Darwin-based digital growth consultancy targeting marketing and creative agencies.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE subject line (max 7 words) about the "cobbler's children" irony — an agency that builds digital systems for clients but doesn't have a new business pipeline for themselves.

Rules:
- Clever but not smug or condescending
- No question marks, no exclamation marks
- Sound like a peer
- Output: subject line text only, no quotes
```

### Column: `agency_e1a_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `A-cobbler`

```
You write cold email openers for Darwin marketing and creative agencies.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE opening sentence (max 20 words) using the "cobbler's children" framing — this agency builds acquisition systems for clients but likely relies on referrals for their own new business.

Rules:
- Use the cobbler's children framing or a close equivalent ("the irony of being a marketing agency that grows on word-of-mouth")
- Peer tone — not condescending, not sycophantic
- Max 20 words
- Output: one sentence only, no quotes
```

### Column: `agency_e1a_pain`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `A-cobbler`

```
You write one pain-acknowledgment sentence for cold emails targeting Darwin marketing/creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE sentence (max 20 words) about the specific pain of an agency relying on referrals:
- Unpredictable new business
- Inability to be selective about client work
- The awkward position of being "too busy" or "too slow" with no middle ground

Darwin context: small market, personal network, hard to grow beyond known contacts.

Rules:
- Empathetic and peer-level
- Not preachy or critical
- Max 20 words
- Output: one sentence only, no quotes
```

---

## AGENCY — EMAIL 1, VARIATION B: AI Pain Inference

Use when: `signal_type` = `B-ai-inference` AND `industry_final` = `Agency`

### Column: `agency_e1b_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-ai-inference` AND `industry_final` = `Agency`

```
You write cold email subject lines for Darwin marketing and creative agencies.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type from the company name and headline (social media, video production, design studio, events, PR, web development, photography, copywriting, etc.).

Write ONE subject line (max 7 words) targeting the specific pipeline pain for their agency type.

Agency-specific pains:
- Social media agency: their own social isn't generating leads
- Video/photography: project-based income, no recurring pipeline
- Design studio: portfolio showcases client work, not their own lead magnet
- Events company: feast or famine around event seasons
- Web development: builds websites that convert for clients, not for themselves

Rules:
- No question marks, no clickbait
- Match their actual type
- Output: subject line text only, no quotes
```

### Column: `agency_e1b_opener`
Type: Claygent / GPT-4o Mini · ~0.5 credits
Conditional run: `signal_type` = `B-ai-inference` AND `industry_final` = `Agency`

```
You write cold email openers for Darwin marketing and creative agencies.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Identify this agency's type. Write ONE opening sentence (max 20 words) that calls out the pipeline problem specific to their agency type.

Pattern examples:
- Social media agency: "Most social media agencies in Darwin are excellent at growing other people's audiences — the harder part is keeping a consistent new client flow themselves."
- Design studio: "Design studios often fill their calendar through past clients and referrals — which makes it hard to be selective about the work you take on."
- Video production: "Video production businesses run project-to-project — the pipeline between shoots is the part most people don't solve."
- Events: "Events businesses run hot or cold — either fully booked or scrambling — and the pipeline problem is usually the same."
- Web development: "Web agencies build lead-generating websites for clients every day — but often don't have one working for their own new business."

Adapt the closest pattern to their actual type.

Rules:
- One sentence only
- Peer tone, observational
- Max 20 words
- Output: one sentence only, no quotes
```

### Column: `agency_e1b_pain`
Type: Reuse `agency_e1a_pain` — same prompt, same column.

---

## AGENCY — EMAIL 1, VARIATION C: Firmographic Fallback

### Column: `agency_e1c_subject`
Type: Static · 0 credits

```javascript
return "the cobbler's children problem — for agencies";
```

### Column: `agency_e1c_opener`
Type: Static · 0 credits

```javascript
return "Most Darwin agencies we speak with build great systems for clients but haven't turned that same thinking on their own new business pipeline.";
```

---

## Agency — value_line & darwin_close (Static)

### Column: `agency_value_line`
Type: Static · 0 credits

```javascript
return "We help Darwin agencies build a consistent new business pipeline — not more cold calls, a system that attracts the type of clients you actually want to work with.";
```

### Column: `agency_darwin_close`
Type: Static · 0 credits

```javascript
return "We're Darwin-based so happy to meet in person if that's easier.";
```

---

## AGENCY — EMAIL 2 (Follow-Up, Day 5)

### Column: `agency_e2_subject`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write follow-up cold email subject lines for Darwin marketing/creative agencies that didn't reply.

Contact: {{first_name}} {{last_name}}
Company: {{company}}

Write ONE subject line (max 7 words) — a soft re-open, new angle, not pushy.

Rules:
- No "following up" or "checking in"
- No question marks
- Reference the new business or pipeline theme for an agency
- Output: subject line text only, no quotes
```

### Column: `agency_e2_add`
Type: Claygent / GPT-4o Mini · ~0.5 credits

```
You write follow-up value-add sentences for cold emails to Darwin marketing/creative agencies.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE sentence (max 20 words) that adds a NEW angle not covered in Email 1. Options:
- A peer proof point: "We recently helped a Darwin creative studio build a system that..."
- A Darwin market insight: "Darwin's creative industry is small enough that the network fills up fast — getting in front of new clients requires a different approach."
- An opportunity cost angle: "Every month relying on the same referral sources is a month of potential new clients who didn't know to reach out."

Rules:
- Genuinely new angle, not a restate
- Peer and conversational
- Max 20 words
- Output: one sentence only, no quotes
```

### Email 2 Full Template
```
Hi {{first_name}},

Sent a note last week — one more thought.

{{agency_e2_add}}

If you're already sorted on the new business side, that's great. If not, happy to share what's worked for similar agencies in Darwin.

{{cta}}

{{agency_darwin_close}}

{{signature}}
```

---

## AGENCY — EMAIL 3 (Breakup, Day 12)

### Subject (A/B split)
- Option A: `{{first_name}}, leaving this here`
- Option B: `not the right fit?`

### Email 3 Template
```
Hi {{first_name}},

No response — completely understood.

I'll leave it here. If you ever want to look at building a new business pipeline that doesn't depend on who referred you last month, I'm easy to find in Darwin.

{{signature}}
```

---

---

# CLAY TABLE — Full Column Order

| # | Column | Type | Credits | Notes |
|---|---|---|---|---|
| 1 | `first_name` | Raw import | 0 | LinkedIn CSV |
| 2 | `last_name` | Raw import | 0 | LinkedIn CSV |
| 3 | `company` | Raw import | 0 | LinkedIn CSV |
| 4 | `headline` | Raw import | 0 | LinkedIn CSV |
| 5 | `current_company_position` | Raw import | 0 | LinkedIn CSV |
| 6 | `clean_position` | Formula | 0 | Position normalizer |
| 7 | `position_tier` | Formula | 0 | A/B/C tier |
| 8 | `industry_final` | Formula | 0 | 3-column industry system |
| 9 | `employee_count` | Enrichment | 1–3 | Apollo → Clearbit waterfall |
| 10 | `google_rating` | Claygent Neon | 1–2 | Conditional: Trades only |
| 11 | `google_review_count` | Claygent Neon | 1–2 | Conditional: Trades only |
| 12 | `is_hiring` | Claygent Neon | 1–2 | Conditional: Trades only, signal_type B |
| 13 | `signal_type` | Formula | 0 | Selector formula above |
| 14 | `subject_line` | Claygent/GPT-4o Mini | ~0.5 | Conditional on segment + signal |
| 15 | `opener_line` | Claygent/GPT-4o Mini | ~0.5 | Conditional on segment + signal |
| 16 | `pain_line` | Claygent/GPT-4o Mini | ~0.5 | Conditional on segment + signal |
| 17 | `value_line` | Formula | 0 | Static per segment |
| 18 | `cta` | Formula | 0 | Employee count conditional |
| 19 | `darwin_close` | Formula | 0 | Static per segment |
| 20 | `email_body_1` | Formula | 0 | Assembles all 6 elements |
| 21 | `e2_subject` | Claygent/GPT-4o Mini | ~0.5 | Run after E1 campaign |
| 22 | `e2_add` | Claygent/GPT-4o Mini | ~0.5 | Run after E1 campaign |
| 23 | `email_body_2` | Formula | 0 | Assembles E2 |

---

# Email Body Assembly Formula (Clayscript, 0 credits)

**Column: `email_body_1`**

```javascript
const opener  = String({{opener_line}} || "").trim();
const pain    = String({{pain_line}} || "").trim();
const value   = String({{value_line}} || "").trim();
const cta_col = String({{cta}} || "").trim();
const close   = String({{darwin_close}} || "").trim();
const name    = String({{first_name}} || "").trim();

const parts = [
  `Hi ${name},`,
  "",
  opener,
  "",
  pain,
  "",
  value,
  "",
  cta_col,
  "",
  close
].join("\n");

return parts;
```

---

# Credit Cost Estimate — Full Campaign

| Column | Rows | Credits/row | Total |
|---|---|---|---|
| `google_rating` (Trades only) | 256 | 1–2 | 256–512 |
| `google_review_count` (Trades only) | 256 | 1–2 | 256–512 |
| `is_hiring` (Trades B-signal only, est. 80 rows) | ~80 | 1–2 | 80–160 |
| `employee_count` (all) | 521 | 1–3 | 521–1,563 |
| `subject_line` AI | 521 | ~0.5 | ~261 |
| `opener_line` AI | 521 | ~0.5 | ~261 |
| `pain_line` AI | 521 | ~0.5 | ~261 |
| `e2_subject` AI | 521 | ~0.5 | ~261 |
| `e2_add` AI | 521 | ~0.5 | ~261 |
| **Total estimate** | | | **~2,218–3,852** |

**Recommendation:** Run in 2 batches.
- Batch 1: Enrich employee count + Google reviews (Trades) + run all static formulas = ~1,100–2,400 credits
- Batch 2: Run AI columns (subject/opener/pain/e2) = ~1,000–1,100 credits
- Test on 50 rows per segment first before full run.

On Starter plan (2,000 credits/mo): split across 2 months or upgrade to Growth ($349/mo = 10,000 credits).

---

# Smartlead Campaign Mapping

| `industry_final` | `signal_type` starts with | Campaign Name | Sequence |
|---|---|---|---|
| Trades | A-reviews | `LI-Trades-Reviews` | E1→E2(D5)→E3(D12) |
| Trades | B-hiring | `LI-Trades-Hiring` | E1→E2(D5)→E3(D12) |
| Trades | C-firmographic | `LI-Trades-Pattern` | E1→E2(D5)→E3(D12) |
| Professional Services | A- | `LI-ProfServices-Referral` | E1→E2(D5)→E3(D12) |
| Professional Services | B- | `LI-ProfServices-AI` | E1→E2(D5)→E3(D12) |
| Agency | A- | `LI-Agency-Cobbler` | E1→E2(D5)→E3(D12) |
| Agency | B- | `LI-Agency-AI` | E1→E2(D5)→E3(D12) |

Export filter from Clay: separate CSV per `signal_type` group → upload to matching Smartlead campaign.
