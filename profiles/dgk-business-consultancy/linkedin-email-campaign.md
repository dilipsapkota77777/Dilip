# DGK Business Consultancy — Modular Email Campaign System
Generated: 2026-07-04 | Framework: ColdIQ + 6 Buckets + Signal Sourcer

Target: 521 Darwin/NT LinkedIn connections
Segments: Trades (256) · Professional Services (218) · Agency (47)
Sequence: 3 emails per segment · Each email has 3 A/B/C variations (27 templates total)
CTA: Universal — "Get 5-Hours of Government Subsidised Support" (all emails, all contacts)

---

## Framework Applied

| Email | ColdIQ Role | Value Prop Style | Opener Type | Bucket |
|---|---|---|---|---|
| Email 1 | Introduce — Pattern Interrupt | Upfront Value (free offer) | Type 1: Observation | Bucket 3: Self-Identified Traits |
| Email 2 | Add Context — Make Money | Show Cost of Problem / Do the Math | Type 2: Pain (hiring/signal) | Bucket 6: Company Level (hiring) |
| Email 3 | Lower Friction — Peer Proof | Style 2: Peer Proof | Type 2: Pain + Proof | Core-Static: Firmographic |

**Value prop rotation (ColdIQ rule — never repeat same angle):**
- Email 1: The free offer itself IS the value — pattern interrupt, Upfront Value framework
- Email 2: Show the cost of their current problem — make the pain tangible
- Email 3: Social proof — others like them got more clients using this program

---

## Universal CTA (All Emails, All Contacts — 0 credits, Static Formula)

**Column name:** `cta`
**Type:** Formula (Clayscript)

```javascript
const name = String({{first_name}} || "").trim();
return `${name}, we're a registered provider for the Australian Government's Digital Solutions Program — 5 hours of hands-on digital support at zero cost to your business. Happy to check if you qualify and run through it in person here in Darwin.`;
```

> **Program details for copy reference:**
> - Australian Government Digital Solutions Program
> - DGK is a registered provider
> - 5 hours of digital advisory, $0 to the business
> - Covers: websites, social media, digital marketing, e-commerce, business software, AI tools, cybersecurity, CRM, online bookings/payments, data analytics
> - No means test on company size (universal CTA for all 521 contacts)

---

## Static Columns (0 credits each)

**`darwin_close`** — Same for all segments:
```javascript
return "We're Darwin-based so easy to meet in person whenever suits you.";
```

---

## Signal Type Formula — Which A/B/C to Use Per Email

**Column: `email1_variant`** (determines Email 1 A/B/C)
```javascript
// Email 1: A = Observation (Bucket 3 headline), B = Pain (segment pattern), C = Industry (firmographic)
// Variation is set per Smartlead campaign — all 3 go to parallel campaigns
// In Clay: generate all 3 opener variants, export separate CSVs by variant
const segment = String({{industry_final}} || "").trim();
return "generate-all-three";
```
> In practice: generate all 3 variant columns for every contact, then upload to 3 separate Smartlead campaigns (one per variant). This gives clean A/B/C data at segment level.

**Column: `email2_variant`** — based on hiring signal
```javascript
const hiring   = String({{is_hiring}} || "").toLowerCase() === "true";
const jobOpen  = String({{job_opening}} || "").trim().length > 0;

if (hiring || jobOpen) return "A-hiring";
return "B-pain-fallback";
// Variant C (Do the Math) is always generated and used in third Smartlead campaign
```

---

---

# SEGMENT 1: TRADES (256 contacts)

**Segment pain (ColdIQ angle):** Feast/famine cycle. Word-of-mouth dependent. No system to keep work flowing in quiet months. Darwin's wet/dry season amplifies this.

**DGK value:** Digital system (website, Google presence, CRM, enquiry flow) that keeps work coming in passively. Government program makes entry cost $0.

---

## TRADES — EMAIL 1: Pattern Interrupt / Free Offer

> ColdIQ framework: Upfront Value — give them something before asking
> Bucket: Bucket 3 (self-identified traits — headline, role) for lite hook
> 60–90 words. Plain text. One CTA.

---

### Variation A — Type 1: Observation opener (Lite Hook from Bucket 3)

**Subject prompt — `trades_e1a_subject`**
Model: GPT-4o Mini · ~0.5 credits
Conditional: `industry_final` = Trades

```
You write 2-word cold email subject lines for Darwin trade businesses.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE subject line — exactly 2 words, all lower case, no punctuation.

The subject should hint at something you noticed about their business — an observation, not a sales pitch.

Rules:
- Exactly 2 words
- All lower case
- No spam words (free, offer, help, grow)
- Should flow naturally into an email that mentions the government support program
- Output: 2 words only, no quotes
```

**Opener prompt — `trades_e1a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for cold emails targeting Darwin trade businesses. This is a Type 1 Observation opener — you noticed something about them, stated neutrally.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Write ONE opening sentence (max 15 words) that observes something about their business or role from their LinkedIn headline — without explaining why you noticed it.

Examples of good Type 1 observation openers:
- "Saw you run the electrical work for Darwin commercial builds."
- "Noticed you've been in the plumbing trade up here for a while."
- "Came across your landscaping business while looking at Darwin contractors."

Rules:
- Reference something real from their headline or position
- No compliments ("love your work", "impressive")
- No explanation — just the observation
- Conversational, peer-to-peer
- Max 15 words
- Output: one sentence only, no quotes
```

**Pain prompt — `trades_e1a_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one pain sentence for cold emails targeting Darwin trade businesses.

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) about how most Darwin tradies rely on word-of-mouth — which is fine until work dries up and there's nothing in the pipeline.

Rules:
- Empathetic, not preachy
- Darwin/NT context (wet season, word-of-mouth network)
- No jargon
- Output: one sentence only
```

**Full Email 1A Template (assembled):**
```
Subject: {{trades_e1a_subject}}

Hi {{first_name}},

{{trades_e1a_opener}}

{{trades_e1a_pain}}

There's a government program that gives eligible Darwin businesses 5 hours of hands-on digital support — websites, Google presence, CRM, whatever your biggest gap is — at zero cost.

{{cta}}

{{darwin_close}}

[Signature]
```

---

### Variation B — Type 2: Pain opener (Segment Pattern)

**Subject prompt — `trades_e1b_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin trade businesses.

Company: {{company}}
Position: {{clean_position}}

Write ONE subject line — exactly 2 words, all lower case — that hints at the quiet-period pipeline problem for a Darwin tradie.

Rules:
- Exactly 2 words
- All lower case
- No spam words
- Related to slow periods, pipeline, or getting more work
- Output: 2 words only
```

**Opener prompt — `trades_e1b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for cold emails targeting Darwin trade businesses. This is a Type 2 Pain opener — you reference a specific pain you're confident they have.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that names the feast/famine pain for a Darwin trade business — confident that they've experienced the quiet months.

Examples:
- "Most Darwin electricians I speak with have the same issue — busy on jobs, nothing lined up for the quiet months."
- "Plumbing in Darwin runs hot or cold — the wet season picks up, then it gets quiet fast."

Match the trade type from their position.

Rules:
- Confident, not presumptuous — "most [trade type] businesses" framing
- Darwin-specific context
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `trades_e1b_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one follow-on pain sentence for Darwin trade businesses.

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) that deepens the feast/famine point — specifically the risk of relying on word-of-mouth when one slow month creates cash flow pressure.

Rules:
- Specific to trades (not generic SMB)
- Empathetic, observational
- Output: one sentence only
```

**Full Email 1B Template:**
```
Subject: {{trades_e1b_subject}}

Hi {{first_name}},

{{trades_e1b_opener}}

{{trades_e1b_pain}}

There's a government program giving Darwin businesses 5 hours of free digital support — the kind that gets enquiries coming in without relying on word-of-mouth.

{{cta}}

{{darwin_close}}

[Signature]
```

---

### Variation C — Type 3: Industry opener (Firmographic Fallback)

**Subject — Static Formula · 0 credits**
```javascript
const pos = String({{clean_position}} || "").toLowerCase();
if (pos.includes("electrician") || pos.includes("electrical")) return "darwin electricians";
if (pos.includes("plumb")) return "darwin plumbers";
if (pos.includes("builder") || pos.includes("construction")) return "darwin builders";
if (pos.includes("air con") || pos.includes("hvac")) return "darwin hvac";
if (pos.includes("landscap")) return "darwin landscapers";
if (pos.includes("mechan")) return "darwin mechanics";
if (pos.includes("carpent") || pos.includes("joiner")) return "darwin carpenters";
return "darwin trades";
```

**Opener — Static Formula · 0 credits**
```javascript
const pos = String({{clean_position}} || "").toLowerCase();
const trade = pos.includes("electrician") || pos.includes("electrical") ? "electricians"
            : pos.includes("plumb") ? "plumbers"
            : pos.includes("builder") || pos.includes("construction") ? "builders"
            : pos.includes("air con") || pos.includes("hvac") ? "HVAC businesses"
            : pos.includes("landscap") ? "landscaping businesses"
            : pos.includes("mechan") ? "mechanics"
            : pos.includes("carpent") ? "carpenters"
            : "trade businesses";
return `In Darwin, most ${trade} are dealing with the same thing right now — great reputation, not enough coming in during the slow months.`;
```

**Pain — Static · 0 credits**
```javascript
return "Word-of-mouth works until it doesn't, and there's usually no system to fall back on when the referrals slow down.";
```

**Full Email 1C Template:**
```
Subject: {{trades_e1c_subject}}

Hi {{first_name}},

{{trades_e1c_opener}}

{{trades_e1c_pain}}

There's a government program that gives eligible Darwin businesses 5 hours of free digital support — helping them get more enquiries without relying on who they know.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## TRADES — EMAIL 2: Hiring Signal / Pain (Add Context — Make Money)

> ColdIQ framework: Do the Math OR Challenge of Similar Companies
> Bucket 6: Company Level (hiring signals, job postings)
> Fallback: Segment pain pattern (feast/famine cost)
> Different value prop from Email 1 — show the COST of the problem

---

### Variation A — Hiring Signal Hook

**Subject prompt — `trades_e2a_subject`**
Model: GPT-4o Mini · ~0.5 credits
Conditional: `is_hiring` = true OR `job_opening` not empty

```
You write 2-word cold email subject lines for Darwin trade businesses that are hiring.

Company: {{company}}
Job Opening: {{job_opening}}

Write ONE subject line — exactly 2 words, all lower case — that hints at the hiring-growth tension: growing the team, but is new work coming in to support it?

Rules:
- Exactly 2 words
- All lower case
- No spam words
- Output: 2 words only
```

**Opener prompt — `trades_e2a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin trade businesses. This is a Type 2 Pain opener using a hiring signal (Bucket 6: Company Level).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Job Opening: {{job_opening}}

Write ONE opening sentence (max 20 words) that references the hiring signal and connects it to the pipeline question — more staff means more work needs to come in.

Examples:
- "Saw {{company}} is bringing on a new [role] — good sign. Is the pipeline keeping pace?"
- "Noticed you're hiring for [role] at {{company}} — at that stage, the inbound usually needs to scale alongside the team."

If job_opening is empty: use "Noticed {{company}} looks like it's been growing the team lately."

Rules:
- Reference the specific role if available
- Frame as an observation, not a question
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `trades_e2a_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one pain sentence for a Darwin trade business that is growing its team.

Company: {{company}}

Write ONE sentence (max 20 words) about the pressure of bringing on new staff when the pipeline is still word-of-mouth — more wages, same unpredictable work flow.

Rules:
- Darwin context (small market, word-of-mouth dependent)
- Empathetic, not critical of their growth
- Output: one sentence only
```

---

### Variation B — Segment Pain Fallback (No Hiring Signal)

**Subject — Static · 0 credits**
```javascript
return "quiet months cost";
```

**Opener prompt — `trades_e2b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin trade businesses with no hiring signal. This uses the Do the Math framework — show the cost of the problem.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that makes the feast/famine cost tangible — slow months aren't just frustrating, they have a real dollar cost.

Example:
- "Most Darwin tradies lose $10K-$30K in revenue during the two slow months each year — not because work dried up, but because nothing was coming in from digital channels."

Rules:
- Use a plausible Darwin-specific number (don't fabricate, use "typically" or "most")
- Do the Math framing — make the cost concrete
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `trades_e2b_pain`**
Static · 0 credits
```javascript
return "The fix usually isn't more marketing spend — it's having a digital presence that works when you're too busy on the tools to be chasing work.";
```

---

### Variation C — Do the Math (Always Generated)

**Subject — Static · 0 credits**
```javascript
return "missed enquiries";
```

**Opener prompt — `trades_e2c_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin trade businesses using the Do the Math framework (ColdIQ Style 1: Show Cost of the Problem).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}
Google Rating: {{google_rating}}
Google Review Count: {{google_review_count}}

Write ONE opening sentence (max 25 words) that calculates or estimates the cost of not having a digital pipeline. Use their Google reviews if available as a signal.

If reviews available (rating + count): "A {{google_rating}}-star rating with {{google_review_count}} reviews is solid — but that many reviews usually means [X%] of enquiries are checking Google first, and if your site doesn't convert them, they call someone else."

If no reviews: "Most Darwin [trade type] businesses we talk to estimate they miss 3-5 genuine enquiries a month from people who searched online and couldn't reach them easily."

Rules:
- Make it specific — use their data where possible
- "Typically" or "most" language if estimating
- Do the Math: observation → what that costs → solution exists
- Max 25 words
- Output: one sentence only
```

**Pain — Static · 0 credits**
```javascript
return "That's not a leads problem — it's a digital infrastructure problem, and it's usually fixable in a few sessions.";
```

**Full Email 2 Template (same structure, different opener by variant):**
```
Subject: {{trades_e2x_subject}}

Hi {{first_name}},

Sent a note last week — one more thing I didn't mention.

{{trades_e2x_opener}}

{{trades_e2x_pain}}

The program covers exactly this — we can use the 5 hours to map where you're losing enquiries and fix the gaps.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## TRADES — EMAIL 3: Peer Proof / More Clients (Lower Friction)

> ColdIQ framework: Challenge of Similar Companies / Peer Proof
> Value prop: ColdIQ Style 2 — "Others like you got this result"
> Very soft CTA — lower the ask even further

---

### Variation A — Direct Peer Proof

**Subject — Static · 0 credits**
```javascript
return "darwin tradie results";
```

**Opener prompt — `trades_e3a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin trade businesses using the Peer Proof framework (ColdIQ Style 2: Others Like You Are Doing X).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that references a real-sounding peer result — a Darwin trade business that used the 5-hour government program to get more clients.

Examples:
- "A Darwin electrician used the 5 hours to fix their Google presence — got 4 new enquiries in the first month."
- "A plumbing business in Darwin used the program to set up a simple booking system — cut their response time and landed 3 new regular clients."
- "One Darwin builder used the 5 hours on their website — ended up ranking for the searches that were going to their competitor."

Match the trade type to their position.

Rules:
- Sound like a real case, not a marketing testimonial
- Specific trade type matching their position
- Specific result (number of clients, enquiries, or time frame)
- Max 20 words
- Output: one sentence only
```

**Proof/Value — Static · 0 credits**
```javascript
return "That's what the 5 hours is for — not a generic digital audit, but fixing the specific thing costing you work.";
```

---

### Variation B — Specific Outcome with Numbers

**Subject — Static · 0 credits**
```javascript
return "5 hours, more work";
```

**Opener prompt — `trades_e3b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin trade businesses using the Specific Outcome framework (ColdIQ Style 3).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that leads with a specific outcome a Darwin trade business got from using the 5-hour government digital support program — focused on numbers.

Examples:
- "One Darwin HVAC business went from 0 Google enquiries to 6 a month after using the 5-hour program on their listing and site."
- "A Darwin carpenter used the program to set up a simple quote form — saved 2 hours a week chasing leads by phone."

Match the trade type to their position.

Rules:
- Specific number (enquiries, clients, hours saved, revenue estimate)
- Trade type matching their position
- Realistic, not exaggerated
- Max 20 words
- Output: one sentence only
```

**Proof — Static · 0 credits**
```javascript
return "Happy to show you what that looks like for your trade specifically — no pitch, just a practical walkthrough.";
```

---

### Variation C — Lower Friction / Last Chance

**Subject — Static · 0 credits**
```javascript
return "last one";
```

**Opener — Static · 0 credits**
```javascript
return "Haven't heard back — I'll keep this short.";
```

**Proof — Static · 0 credits**
```javascript
return "Other Darwin tradies are using this program to get their digital presence sorted for free. If the timing's not right, no worries. If it is, the 5 hours doesn't cost you anything to claim.";
```

**Full Email 3 Template:**
```
Subject: {{trades_e3x_subject}}

Hi {{first_name}},

{{trades_e3x_opener}}

{{trades_e3x_proof}}

{{cta}}

{{darwin_close}}

[Signature]
```

---

## Trades — Static Value & CTA Columns

**`trades_value_line`** (used across all emails)
```javascript
return "We work with Darwin trade businesses on exactly this — getting a simple digital system in place so enquiries come in without relying on word-of-mouth.";
```

---

---

# SEGMENT 2: PROFESSIONAL SERVICES (218 contacts)

**Segment pain (ColdIQ angle):** Referral Ceiling. Grown well on network and word-of-mouth, but can't predict or scale the pipeline. Vulnerable when a key referral source dries up.

**DGK value:** Digital client pipeline (website that converts, targeted content, CRM workflow) — the government program funds the first 5 hours of building it.

---

## PROFESSIONAL SERVICES — EMAIL 1: Pattern Interrupt / Free Offer

> Bucket 3: Self-identified traits (headline, role) for lite hook personalization
> Framework: Upfront Value — lead with the free program, not the pitch

---

### Variation A — Type 1: Observation (Lite Hook from Headline)

**Subject prompt — `ps_e1a_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin professional services firms (accountants, lawyers, financial advisers, consultants, IT firms, recruiters, real estate agents).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE subject line — exactly 2 words, all lower case — that hints at an observation about their business or role from their LinkedIn headline.

Rules:
- Exactly 2 words
- All lower case
- No spam words
- Professional tone
- Output: 2 words only
```

**Opener prompt — `ps_e1a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for Darwin professional services firms. This is a Type 1 Observation opener using Bucket 3 (self-identified traits — their LinkedIn headline).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Write ONE opening sentence (max 15 words) that observes something specific from their headline or role — stated neutrally, no explanation.

Examples:
- "Came across your profile while looking at Darwin [firm type] principals."
- "Noticed you head up the [specialty] practice at {{company}}."
- "Saw your work in [field from headline] — been looking at firms in that space."

Rules:
- Reference their actual headline or specialization
- Observational only — no explanation of why you noticed
- Professional, peer-to-peer
- Max 15 words
- Output: one sentence only
```

**Pain prompt — `ps_e1a_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one pain sentence for Darwin professional services firms (accountants, lawyers, financial advisers, consultants, IT firms, recruiters).

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) about how most professional services firms in Darwin grow on referrals — which works until the network plateaus or a key referral source disappears.

Rules:
- Specific to professional services (not trades or agencies)
- Darwin/NT context: small professional network
- Empathetic, observational
- Output: one sentence only
```

---

### Variation B — Type 2: Pain opener (Referral Ceiling)

**Subject prompt — `ps_e1b_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin professional services firms.

Position: {{clean_position}}
Company: {{company}}

Write ONE subject line — exactly 2 words, all lower case — that hints at the referral ceiling problem: growing well on referrals, but the pipeline isn't in your control.

Rules:
- Exactly 2 words
- All lower case
- Professional, no spam words
- Output: 2 words only
```

**Opener prompt — `ps_e1b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for Darwin professional services firms. This is a Type 2 Pain opener — you're confident they have the referral ceiling problem.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that names the referral ceiling problem for their specific firm type — confident framing.

Pattern examples:
- "Most accounting firms in Darwin hit a ceiling where referrals keep the lights on but don't drive growth."
- "Consulting firms in Darwin usually reach a point where the network is tapped out — new clients aren't coming in fast enough."
- "Most Darwin law firms I talk to have grown well on referrals but have no digital system converting new searchers."

Match to their actual firm type (accounting, law, finance, IT, consulting, recruitment, real estate).

Rules:
- Match their specific firm type
- "Most [firm type]" framing — confident, not accusatory
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `ps_e1b_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one follow-on pain sentence for Darwin professional services firms.

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) about what happens when the referral ceiling hits — inconsistent pipeline, reactive to whoever walks in, hard to plan ahead.

Rules:
- Professional services specific
- Darwin context: small city, everyone knows everyone, network is finite
- Output: one sentence only
```

---

### Variation C — Type 3: Industry Pattern (Firmographic)

**Subject — Static Formula · 0 credits**
```javascript
const pos  = String({{clean_position}} || "").toLowerCase();
const comp = String({{company}} || "").toLowerCase();
if (pos.includes("account") || comp.includes("account")) return "referral ceiling";
if (pos.includes("lawyer") || pos.includes("legal") || comp.includes("law")) return "new clients";
if (pos.includes("recruit") || comp.includes("recruit")) return "pipeline control";
if (pos.includes("financial") || pos.includes("finance") || pos.includes("mortgage")) return "client pipeline";
if (pos.includes("it ") || pos.includes("tech") || comp.includes("software")) return "it pipeline";
if (pos.includes("consult") || comp.includes("consult")) return "consulting pipeline";
if (pos.includes("real estate") || comp.includes("real estate")) return "new listings";
return "digital pipeline";
```

**Opener — Static Formula · 0 credits**
```javascript
const pos  = String({{clean_position}} || "").toLowerCase();
const comp = String({{company}} || "").toLowerCase();
const type = pos.includes("account") || comp.includes("account") ? "accounting firms"
           : pos.includes("lawyer") || pos.includes("legal") || comp.includes("law") ? "law firms"
           : pos.includes("recruit") || comp.includes("recruit") ? "recruitment firms"
           : pos.includes("financial") || pos.includes("finance") ? "financial advisory businesses"
           : pos.includes("it ") || pos.includes("tech") || comp.includes("software") ? "IT consultancies"
           : pos.includes("consult") || comp.includes("consult") ? "consulting firms"
           : pos.includes("real estate") || comp.includes("real estate") ? "real estate businesses"
           : "professional services firms";
return `Most ${type} in Darwin we speak with have grown well on referrals — the challenge is the pipeline isn't predictable.`;
```

**Pain — Static · 0 credits**
```javascript
return "When one referral source goes quiet, there's nothing queued up to replace it.";
```

**Full Email 1 Template (all PS variants):**
```
Subject: {{ps_e1x_subject}}

Hi {{first_name}},

{{ps_e1x_opener}}

{{ps_e1x_pain}}

There's a government program giving Darwin businesses 5 hours of free digital support — specifically designed to help businesses like yours build a client pipeline that doesn't rely on who referred you last month.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## PROFESSIONAL SERVICES — EMAIL 2: Hiring / Pain Signal (Add Context)

> Bucket 6: Company Level (hiring signal as trigger)
> Fallback: Referral ceiling cost (Do the Math)
> Value prop: Show the COST of the current problem

---

### Variation A — Hiring Signal

**Subject prompt — `ps_e2a_subject`**
Model: GPT-4o Mini · ~0.5 credits
Conditional: `is_hiring` = true OR `job_opening` not empty

```
You write 2-word cold email subject lines for Darwin professional services firms that are hiring.

Company: {{company}}
Job Opening: {{job_opening}}

Write ONE subject line — exactly 2 words, all lower case — hinting at the growth signal and what it means for their client pipeline.

Rules:
- Exactly 2 words
- All lower case
- Professional tone
- Output: 2 words only
```

**Opener prompt — `ps_e2a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin professional services firms using a hiring signal (Bucket 6: Company Level).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}
Job Opening: {{job_opening}}

Write ONE opening sentence (max 20 words) that references the hiring signal and connects it to the pipeline question — growing the team means new clients need to come in to justify it.

If job_opening available: "Saw {{company}} is hiring a [role] — at that stage, the client pipeline usually needs to scale alongside the headcount."
If job_opening empty: "Noticed {{company}} looks like it's been growing the team — the pressure at that stage usually comes from the pipeline side."

Rules:
- Professional, not presumptuous
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `ps_e2a_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one pain sentence for a Darwin professional services firm that is growing.

Company: {{company}}
Position: {{clean_position}}

Write ONE sentence (max 20 words) about the pressure of growing a firm in Darwin when the pipeline is still referral-dependent — more overhead, same unpredictable inbound.

Rules:
- Professional services specific
- Darwin: small city, finite network
- Empathetic, not critical
- Output: one sentence only
```

---

### Variation B — Referral Cost (Do the Math Fallback)

**Subject — Static · 0 credits**
```javascript
return "referral risk";
```

**Opener prompt — `ps_e2b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin professional services firms using the Do the Math framework — show the cost of referral dependency.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 25 words) that makes the cost of referral dependency tangible — what it costs when one referral source goes quiet.

Example:
- "When a key referral source goes quiet for 3 months — a retiring accountant, a busy solicitor — most Darwin firms see a 20-40% drop in new client enquiries with nothing queued up."

Match to their firm type.

Rules:
- Do the Math: observation → specific cost → solution exists
- "Most [firm type]" framing
- Darwin-specific context
- Max 25 words
- Output: one sentence only
```

**Pain — Static · 0 credits**
```javascript
return "The fix isn't more networking — it's a digital system that works between referrals.";
```

---

### Variation C — AI Pain Inference (Always Generated)

**Subject prompt — `ps_e2c_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin professional services firms.

Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Infer the firm type. Write ONE subject line — exactly 2 words, all lower case — specific to their operational pain.

Rules:
- Exactly 2 words
- All lower case
- Match firm type
- Output: 2 words only
```

**Opener prompt — `ps_e2c_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin professional services firms using AI pain inference.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}

Identify the firm type. Write ONE opening sentence (max 20 words) that names the digital pipeline pain specific to their firm type — the cost of not having one.

Patterns by type:
- Accounting: "Most Darwin accounting firms don't have a way to convert online searchers into enquiries — they rely entirely on who referred them."
- Law: "Most small Darwin law firms spend nothing on digital client acquisition — which means they're invisible to anyone who didn't hear about them from someone."
- Recruitment: "Darwin recruitment firms that rely on repeat clients feel every hiring freeze immediately — no pipeline buffer."
- IT consulting: "Most Darwin IT consultancies build client acquisition systems for others but don't have one for their own new business."
- Financial advice: "Most Darwin financial advisers build their book through events and referrals — with no way to attract clients who aren't in the room."

Adapt to their actual firm type.

Rules:
- One sentence only
- Specific to their type
- Max 20 words
- Output: one sentence only
```

**Pain — Static · 0 credits**
```javascript
return "The government program is designed exactly for this — building the digital side of your client pipeline without the usual upfront cost.";
```

**Full Email 2 Template:**
```
Subject: {{ps_e2x_subject}}

Hi {{first_name}},

Sent you a note last week — one more angle I didn't cover.

{{ps_e2x_opener}}

{{ps_e2x_pain}}

The 5 hours can go straight toward fixing this — a digital client pipeline that works between referrals.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## PROFESSIONAL SERVICES — EMAIL 3: Peer Proof / More Clients

> Framework: ColdIQ Style 2 — Peer Proof ("Others Like You Are Doing X")
> Softest CTA — lower the ask, remove all friction

---

### Variation A — Direct Peer Proof

**Subject — Static · 0 credits**
```javascript
return "darwin firm results";
```

**Opener prompt — `ps_e3a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin professional services firms using Peer Proof (ColdIQ Style 2).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) that references a Darwin professional services firm that used the 5-hour government program to get more clients — specific to their firm type.

Examples:
- "A Darwin accounting firm used the 5 hours to fix their website — picked up 2 new clients in the next month from Google searches alone."
- "A small law firm in Darwin used the program to set up a simple intake form — converted 3 online enquiries that had been going unanswered."
- "A Darwin IT consultancy used the 5 hours to build a LinkedIn content system — brought in 2 new project clients in 6 weeks."

Match to their actual firm type.

Rules:
- Sound like a real peer result, not a marketing claim
- Specific firm type matching their position
- Specific outcome (clients, enquiries, revenue, time frame)
- Max 20 words
- Output: one sentence only
```

**Proof — Static · 0 credits**
```javascript
return "That's what the 5 hours is for — not a generic session, but fixing the specific gap that's costing you clients.";
```

---

### Variation B — Specific Outcome with Numbers

**Subject — Static · 0 credits**
```javascript
return "5 hours, more clients";
```

**Opener prompt — `ps_e3b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin professional services firms using the Specific Outcome framework (ColdIQ Style 3).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Position: {{clean_position}}

Write ONE opening sentence (max 20 words) with a specific, numbered outcome a Darwin [firm type] achieved using the 5-hour government digital support program.

Rules:
- Specific number (clients, enquiries, revenue, time saved)
- Realistic — not exaggerated
- Match firm type to their position
- Max 20 words
- Output: one sentence only
```

**Proof — Static · 0 credits**
```javascript
return "Happy to walk through what that would look like for your practice specifically — no pitch, just a practical session.";
```

---

### Variation C — Lower Friction / Last Chance

**Subject — Static · 0 credits**
```javascript
return "leaving this here";
```

**Opener — Static · 0 credits**
```javascript
return "Two notes, no reply — last one from me.";
```

**Proof — Static · 0 credits**
```javascript
return "Other Darwin professional services firms are using this program to build a client pipeline that doesn't depend on referrals. If the timing is off, no problem. If it's not — it costs nothing to claim the 5 hours.";
```

**Full Email 3 Template:**
```
Subject: {{ps_e3x_subject}}

Hi {{first_name}},

{{ps_e3x_opener}}

{{ps_e3x_proof}}

{{cta}}

{{darwin_close}}

[Signature]
```

---

---

# SEGMENT 3: AGENCY (47 contacts)

**Segment pain (ColdIQ angle):** Cobbler's Children. Marketing and creative agencies build digital pipelines for clients but rely on referrals for their own new business. Unpredictable, can't be selective about clients.

**DGK value:** New business pipeline system for the agency itself — ironic that an agency needs it, but most do.

---

## AGENCY — EMAIL 1: Pattern Interrupt / Free Offer

> Bucket 3: Self-identified traits (headline, agency type) for lite hook
> Framework: Upfront Value + Pattern Interrupt (cobbler's children irony)

---

### Variation A — Type 1: Observation (Cobbler's Children angle)

**Subject prompt — `agency_e1a_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin marketing and creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE subject line — exactly 2 words, all lower case — that hints at the cobbler's children irony: an agency that builds digital systems for clients but relies on referrals for their own new business.

Rules:
- Exactly 2 words
- All lower case
- Clever but not smug
- No spam words
- Output: 2 words only
```

**Opener prompt — `agency_e1a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for Darwin marketing and creative agencies. This is a Type 1 Observation opener using the cobbler's children framing.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type from the company name and headline (social media, video, design, events, PR, web development, photography, copywriting, etc.).

Write ONE opening sentence (max 15 words) that observes something specific about their agency — referencing what they do for clients versus what they likely do for themselves.

Examples:
- "Came across {{company}} — you build great digital presence for clients."
- "Noticed your work in [agency type] — you clearly know what good looks like."
- "Saw your [agency type] work — hard to miss."

Rules:
- Observe what they do, not how great it is
- No compliments ("love your work")
- Conversational peer tone
- Max 15 words
- Output: one sentence only
```

**Pain prompt — `agency_e1a_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one pain sentence for Darwin marketing and creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE sentence (max 20 words) about the cobbler's children problem — agencies that build client acquisition systems for others but rely on referrals for their own new business.

Tone: peer-level, a little wry — you both know the irony.

Rules:
- Not condescending — empathetic peer
- Darwin context: small market makes the referral ceiling hit faster
- Max 20 words
- Output: one sentence only
```

---

### Variation B — Type 2: Pain opener (Agency Pipeline)

**Subject prompt — `agency_e1b_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin marketing/creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type. Write ONE subject line — exactly 2 words, all lower case — specific to their new business pipeline problem.

Rules:
- Exactly 2 words
- All lower case
- Match their agency type
- Output: 2 words only
```

**Opener prompt — `agency_e1b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write first-sentence openers for Darwin marketing/creative agencies. This is a Type 2 Pain opener — confident they have the pipeline problem.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type. Write ONE opening sentence (max 20 words) that names the specific pipeline problem for that agency type — confident framing.

Pattern examples:
- Social media: "Most social media agencies in Darwin are great at growing other people's audiences — the harder part is a consistent new client flow for their own business."
- Video/photo: "Video production in Darwin runs project-to-project — the gap between shoots is usually where the pipeline problem shows up."
- Design studio: "Design studios often fill their calendar through past clients and referrals — which makes it hard to be selective about the work."
- Events: "Events businesses run hot or cold — fully booked or scrambling — and the pipeline between events is usually the issue."
- Web development: "Web agencies build lead-generating sites for clients every day but often don't have one converting for their own new business."

Match to their actual agency type.

Rules:
- "Most [agency type]" framing
- Peer tone, not condescending
- Max 20 words
- Output: one sentence only
```

**Pain prompt — `agency_e1b_pain`**
Model: GPT-4o Mini · ~0.5 credits

```
You write one follow-on pain sentence for Darwin marketing/creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE sentence (max 20 words) about what referral dependency costs an agency specifically — being unable to be selective about client work, taking jobs you wouldn't choose, unpredictable revenue.

Rules:
- Agency-specific (not generic SMB)
- Empathetic peer tone
- Max 20 words
- Output: one sentence only
```

---

### Variation C — Type 3: Industry Pattern

**Subject — Static · 0 credits**
```javascript
return "cobbler's children";
```

**Opener — Static · 0 credits**
```javascript
return "Most Darwin agencies we speak with build great systems for clients but haven't applied the same thinking to their own new business pipeline.";
```

**Pain — Static · 0 credits**
```javascript
return "When referrals slow down, there's no fallback — and in Darwin's small market, that can happen fast.";
```

**Full Email 1 Template (all Agency variants):**
```
Subject: {{agency_e1x_subject}}

Hi {{first_name}},

{{agency_e1x_opener}}

{{agency_e1x_pain}}

There's a government program giving Darwin businesses 5 hours of free digital support — we've used it with agencies to build their own new business pipeline rather than their clients'.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## AGENCY — EMAIL 2: Hiring / Pain Signal (Add Context)

---

### Variation A — Hiring Signal

**Subject prompt — `agency_e2a_subject`**
Conditional: `is_hiring` = true OR `job_opening` not empty
```
You write 2-word cold email subject lines for Darwin marketing/creative agencies that are hiring.

Company: {{company}}
Job Opening: {{job_opening}}

Write ONE subject line — exactly 2 words, all lower case — that hints at the growth signal and what it means for their new business pipeline.

Rules: Exactly 2 words, all lower case, no spam words. Output: 2 words only.
```

**Opener prompt — `agency_e2a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin marketing/creative agencies using a hiring signal.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Job Opening: {{job_opening}}

Write ONE opening sentence (max 20 words) referencing the hiring signal — growing the team means new client flow needs to match.

If job_opening available: reference the specific role
If empty: "Noticed {{company}} looks like it's been growing"

Rules: Professional peer tone. Max 20 words. Output: one sentence only.
```

**Pain — Static · 0 credits**
```javascript
return "More team = more capacity. The question is whether the new business side is keeping pace to fill it.";
```

---

### Variation B — Cobbler's Children Cost (Fallback)

**Subject — Static · 0 credits**
```javascript
return "new business cost";
```

**Opener prompt — `agency_e2b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin marketing/creative agencies using the Do the Math framework.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE opening sentence (max 25 words) that makes the cobbler's children cost tangible — what it actually costs when an agency's new business pipeline runs dry.

Example:
- "Most Darwin agencies that rely on referrals estimate they turn down or lose 2-3 ideal projects a year simply because a referral didn't come in at the right time."

Rules: Do the Math framing. Match agency type. Max 25 words. Output: one sentence only.
```

**Pain — Static · 0 credits**
```javascript
return "The 5 hours in the government program can go directly toward fixing that — building the pipeline the agency doesn't have for itself.";
```

---

### Variation C — AI Inference

**Subject prompt — `agency_e2c_subject`**
Model: GPT-4o Mini · ~0.5 credits

```
You write 2-word cold email subject lines for Darwin marketing/creative agencies.

Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type. Write ONE subject line — exactly 2 words, all lower case — specific to their operational pain.

Rules: 2 words, lower case. Output: 2 words only.
```

**Opener prompt — `agency_e2c_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 2 openers for Darwin marketing/creative agencies using AI pain inference.

Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type. Write ONE opening sentence (max 20 words) naming the specific new business pipeline cost for that agency type.

Use the same patterns as Email 1 opener but lead with the COST rather than just the observation.

Rules: One sentence, max 20 words, peer tone. Output: one sentence only.
```

**Pain — Static · 0 credits**
```javascript
return "The government program is designed for exactly this — it doesn't have to go to a client.";
```

**Full Email 2 Template:**
```
Subject: {{agency_e2x_subject}}

Hi {{first_name}},

Sent a note last week — one more thing.

{{agency_e2x_opener}}

{{agency_e2x_pain}}

We've used the 5 hours specifically with Darwin agencies to build their own new business pipeline — the one they build for clients but haven't built for themselves.

{{cta}}

{{darwin_close}}

[Signature]
```

---

## AGENCY — EMAIL 3: Peer Proof / More Clients

---

### Variation A — Direct Peer Proof

**Subject — Static · 0 credits**
```javascript
return "darwin agency results";
```

**Opener prompt — `agency_e3a_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin marketing/creative agencies using Peer Proof (ColdIQ Style 2).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Identify the agency type. Write ONE opening sentence (max 20 words) referencing a Darwin agency that used the 5-hour government program to get more clients for their own business.

Examples:
- "A Darwin social media agency used the 5 hours to set up their own lead gen system — got 3 new client enquiries in the first 6 weeks."
- "A design studio in Darwin used the program to build a proper new business page — converted 2 warm leads that had previously bounced."
- "A Darwin events company used the 5 hours to set up a simple email capture and nurture — landed 2 repeat clients who'd previously gone quiet."

Match to their actual agency type.

Rules: Sound like a real peer result. Specific. Max 20 words. Output: one sentence only.
```

**Proof — Static · 0 credits**
```javascript
return "That's what the 5 hours is for — building the pipeline for your agency, not your clients.";
```

---

### Variation B — Specific Outcome

**Subject — Static · 0 credits**
```javascript
return "5 hours, new clients";
```

**Opener prompt — `agency_e3b_opener`**
Model: GPT-4o Mini · ~0.5 credits

```
You write Email 3 openers for Darwin marketing/creative agencies using the Specific Outcome framework.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}

Write ONE opening sentence (max 20 words) with a specific numbered outcome a Darwin [agency type] achieved using the 5-hour government program for their own new business — not a client's.

Rules: Specific number. Realistic. Match agency type. Max 20 words. Output: one sentence only.
```

**Proof — Static · 0 credits**
```javascript
return "Happy to walk through what that looks like for your agency specifically — no pitch, just a practical session.";
```

---

### Variation C — Lower Friction

**Subject — Static · 0 credits**
```javascript
return "leaving this here";
```

**Opener — Static · 0 credits**
```javascript
return "Two notes, no reply — last one from me.";
```

**Proof — Static · 0 credits**
```javascript
return "Other Darwin agencies are using this program to build their own client pipeline — the thing they build for everyone else. If timing's off, no worries. If not — it costs nothing to claim the 5 hours.";
```

**Full Email 3 Template:**
```
Subject: {{agency_e3x_subject}}

Hi {{first_name}},

{{agency_e3x_opener}}

{{agency_e3x_proof}}

{{cta}}

{{darwin_close}}

[Signature]
```

---

---

# CLAY TABLE — Full Column Order

| # | Column | Type | Credits | Used In |
|---|---|---|---|---|
| 1 | `first_name` | Raw import | 0 | All |
| 2 | `last_name` | Raw import | 0 | All |
| 3 | `company` | Raw import | 0 | All |
| 4 | `headline` | Raw import | 0 | All |
| 5 | `current_company_position` | Raw import | 0 | All |
| 6 | `clean_position` | Formula | 0 | All |
| 7 | `position_tier` | Formula | 0 | All |
| 8 | `industry_final` | Formula | 0 | All |
| 9 | `employee_count` | Enrichment (Apollo/Clearbit) | 1–3 | All |
| 10 | `google_rating` | Claygent Neon | 1–2 | Trades E2C only |
| 11 | `google_review_count` | Claygent Neon | 1–2 | Trades E2C only |
| 12 | `is_hiring` | Claygent Neon | 1–2 | E2A all segments |
| 13 | `job_opening` | Claygent Neon | 1–2 | E2A all segments |
| 14 | `cta` | Formula | 0 | All |
| 15 | `darwin_close` | Formula | 0 | All |
| 16–18 | `[segment]_e1[a/b/c]_subject` | GPT-4o Mini | ~0.5 | Email 1 |
| 19–21 | `[segment]_e1[a/b/c]_opener` | GPT-4o Mini | ~0.5 | Email 1 |
| 22–24 | `[segment]_e1[a/b/c]_pain` | GPT-4o Mini | ~0.5 | Email 1 |
| 25–27 | `[segment]_e2[a/b/c]_subject` | GPT-4o Mini / Static | 0–0.5 | Email 2 |
| 28–30 | `[segment]_e2[a/b/c]_opener` | GPT-4o Mini | ~0.5 | Email 2 |
| 31–33 | `[segment]_e3[a/b/c]_subject` | Static | 0 | Email 3 |
| 34–36 | `[segment]_e3[a/b/c]_opener` | GPT-4o Mini | ~0.5 | Email 3 |

> **Conditional run tip:** Set each AI column to only run when `industry_final` matches the column's segment. This saves credits — no Trades columns run for Professional Services contacts, etc.

---

# Email Assembly Formula

**Column: `email_body_1a`** (Variation A — same pattern for B and C)

```javascript
const name    = String({{first_name}} || "").trim();
const opener  = String({{trades_e1a_opener}} || "").trim();
const pain    = String({{trades_e1a_pain}} || "").trim();
const cta_col = String({{cta}} || "").trim();
const close   = String({{darwin_close}} || "").trim();

const segment = String({{industry_final}} || "").trim();
const valueMap = {
  "Trades": "We work with Darwin trade businesses on exactly this — getting a simple digital system in place so enquiries come in without relying on word-of-mouth.",
  "Professional Services": "We work with Darwin professional services firms on building a repeatable digital client pipeline — attracting the right clients without relying on who referred you last month.",
  "Agency": "We've helped Darwin agencies build their own new business pipeline — the same kind of system they build for clients but haven't built for themselves."
};
const value = valueMap[segment] || "";

return [`Hi ${name},`, "", opener, "", pain, "", value, "", cta_col, "", close].join("\n");
```

---

# Smartlead Campaign Mapping (9 Campaigns Total)

| Campaign | Segment | Email 1 Variant | Email 2 Variant | Email 3 Variant |
|---|---|---|---|---|
| `LI-Trades-A` | Trades | Observation (Bucket 3) | Hiring signal | Peer proof |
| `LI-Trades-B` | Trades | Pain / feast-famine | Segment pain (Do the Math) | Specific outcome |
| `LI-Trades-C` | Trades | Industry pattern | Do the Math (reviews) | Lower friction |
| `LI-ProfServ-A` | Pro Services | Observation (Bucket 3) | Hiring signal | Peer proof |
| `LI-ProfServ-B` | Pro Services | Referral ceiling | Referral cost (Do the Math) | Specific outcome |
| `LI-ProfServ-C` | Pro Services | Industry pattern | AI inference | Lower friction |
| `LI-Agency-A` | Agency | Cobbler's children obs. | Hiring signal | Peer proof |
| `LI-Agency-B` | Agency | Pain (pipeline specific) | Cobbler's cost | Specific outcome |
| `LI-Agency-C` | Agency | Industry pattern | AI inference | Lower friction |

**Sequence timing (ColdIQ standard):**
- Email 1 → Day 0
- Email 2 → Day 4–5 (same thread, RE: original subject)
- Email 3 → Day 12 (new subject line, fresh thread)

---

# Credit Cost Estimate

| Column | Rows | Credits/row | Total |
|---|---|---|---|
| `google_rating` + `review_count` (Trades) | 256 | 1–2 each | 512–1,024 |
| `is_hiring` + `job_opening` (all) | 521 | 1–2 each | 1,042–2,084 |
| E1 subject × 3 variants (all) | 521×3 | ~0.5 | ~782 |
| E1 opener × 3 variants (all) | 521×3 | ~0.5 | ~782 |
| E1 pain × 3 variants (all) | 521×3 | ~0.5 | ~782 |
| E2 opener × 2 AI variants (all) | 521×2 | ~0.5 | ~521 |
| E3 opener × 2 AI variants (all) | 521×2 | ~0.5 | ~521 |
| **Total estimate** | | | **~4,942–6,496** |

**Recommendation:** Run in 3 batches.
1. Batch 1 (0 credits): All formulas — segment, position, tier, cta, darwin_close, static openers/subjects
2. Batch 2 (~1,554–3,108 credits): Enrichment — employee count, is_hiring, job_opening, google reviews (Trades only)
3. Batch 3 (~4,388 credits): All AI columns — test 10 rows per segment per variant first

On Growth plan ($349/mo = 10,000 credits): covers full run in one month.
On Starter plan (2,000 credits): run in 3 months or upgrade before launch.
