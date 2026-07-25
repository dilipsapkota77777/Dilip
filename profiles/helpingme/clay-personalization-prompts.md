# DGK Personalization Prompts — NDIS Provider Campaign
# Clay GPT-4 Mini Columns
# Sender: DGK Business Consultancy → NDIS Provider CEOs/Founders/Directors
Generated: 2026-07-25

---

## Why the Generic Version Fails (Read This First)

The original prompts fail because they ask AI to do three things at once: figure out the prospect's situation, identify the relevant pain, AND write a human sentence. AI can't do all three well simultaneously — it collapses into safe, generic output.

**The fix: force AI to reason step-by-step before writing.**

Three specific changes across all prompts:
1. Give AI the NDIS pain patterns explicitly — don't ask it to infer them
2. Give it sentence templates to complete, not open-ended "write something specific"
3. Make it extract the specific detail FIRST, then write — chain of thought enforced, not described

---

## PROMPT 1 — THE OPENER
**Column:** `dgk_opener`
**Model:** GPT-4 Mini
**Credits:** ~1/row
**Condition:** `{{first_name}}` is not empty

### Clay Inputs
```
first_name, Title, current_company, headline, Description, Service Type, Participant Specialisation, Locality, Years in Business
```

### Prompt
```
You are writing the first line of a cold email from DGK Business Consultancy to an NDIS provider decision-maker. DGK helps NDIS providers build referral partner outreach systems — getting consistent participant referrals from support coordinators and case managers.

CONTACT:
- Name: {{first_name}} {{last_name}}, {{Title}} at {{current_company}}
- Headline: "{{headline}}"
- Description: "{{Description}}"
- NDIS services: {{Service Type}}
- Participants served: {{Participant Specialisation}}
- Location: {{Locality}}
- Stage: {{Years in Business}}

---

STEP 1 — IDENTIFY THE RELEVANT PAIN

Match their service type to the pain that fits. This is not your opinion — it is what operators in this service category consistently report:

SIL / SDA:
Coordinators maintain a shortlist of preferred SIL providers. That list rarely changes. New providers cannot get onto it without reaching out before the coordinator has a participant who needs them. Most providers never do this — they wait.

Allied Health (OT, speech pathology, psychology, physiotherapy):
Allied health practices with excellent clinicians routinely have empty appointment slots. The reason is almost always the same: coordinators only refer to practitioners they have personally met. Great clinicians who have not built coordinator relationships are invisible to the referrers who could fill their caseloads.

Behaviour Support / PBS:
Coordinators are cautious about behaviour support referrals because one bad match with a complex participant creates lasting damage to the relationship. They default to the 2-3 practitioners they already trust. Breaking into that shortlist takes months of relationship-building one coffee at a time.

Psychosocial / Mental Health / Recovery Coaching:
Facebook ads do not work for psychosocial participants. Families rely on coordinator recommendations. If a coordinator does not know a provider exists, the provider is invisible to the exact participants they are best suited to serve.

Core Supports / Daily Activities / Personal Care / Community Access:
Core supports is the most commoditised NDIS service category. Every provider offers the same thing. Providers with full caseloads do not have better services — they have better coordinator relationships than the providers who are half-full.

High Intensity / Nursing / Complex Care:
Coordinators desperately want to place complex participants but fear putting them with an unreliable provider. The first complex care provider who reaches out and demonstrates competence owns those coordinator relationships for years.

Support Coordination:
Support coordinators grow by building trust with plan managers and LACs. Most wait for referrals to come in. The ones growing fastest proactively build plan manager relationships before they need participants.

Plan Management:
Participant flow for plan managers comes from coordinator and LAC referrals. Most plan managers wait for word of mouth. The ones growing have one thing the others do not: a system for proactively connecting with coordinators in their region.

General NDIS (if service type is unclear):
The hardest thing about NDIS participant acquisition is that it looks like word of mouth but actually runs on coordinator relationships. Most providers treat them the same. They are not.

---

STEP 2 — EXTRACT ONE SPECIFIC DETAIL

From their headline "{{headline}}" and description "{{Description}}", find ONE of these:
- A geographic market (specific suburb, region, or state)
- A participant type (Autism, ABI, psychosocial, complex care, etc.)
- A team emphasis (retention focus, culturally responsive, clinical depth)
- A service combination that is notable (e.g., SIL + SDA + behaviour support)

If none of those are clear, use their location from {{Locality}}.

---

STEP 3 — WRITE THE OPENER

Combine the pain from Step 1 with the specific detail from Step 2.

Use ONE of these sentence structures:

PATTERN A: "Running [Step 2 detail] in [location] usually means [compressed version of Step 1 pain]."
PATTERN B: "Most [their service type] providers in [state] tell me [specific Step 1 pain observation]."
PATTERN C: "[Step 2 detail] at {{current_company}}'s scale usually means [Step 1 pain]."

---

HARD RULES (break any of these and the output is unusable):
- 10 to 18 words maximum
- Never start with "I" or "Your"
- Never restate their headline back to them — if their headline says "Allied Health specialist", do not write "As an allied health specialist..."
- Never use: impressive, amazing, great, love, wonderful, hope this finds you
- Never mention DGK, outbound, referral systems, or anything you are selling
- Plain English only — conversational, not corporate
- If their Description is empty, work only from headline and service type

---

Return ONLY the final sentence from Step 3. No quotes. No explanation. Nothing else.
```

---

## PROMPT 2 — THE PS HOOK
**Column:** `dgk_ps_hook`
**Model:** GPT-4 Mini
**Credits:** ~1/row
**Condition:** `{{headline}}` is not empty

### Clay Inputs
```
first_name, headline, summary, current_company, Service Type, Participant Specialisation
```

### Prompt
```
You are writing a PS line for a cold email from DGK Business Consultancy to an NDIS provider.

The PS goes after the signature. It should feel like a casual afterthought the sender noticed and wanted to mention — not a pitch, not a compliment, not a restatement of what was in the email.

CONTACT:
- {{first_name}}, {{Title}} at {{current_company}}
- LinkedIn headline: "{{headline}}"
- LinkedIn summary: "{{summary}}"
- NDIS services: {{Service Type}}
- Participants served: {{Participant Specialisation}}

---

STEP 1 — FIND THEIR UNIQUE ANGLE

Look at their headline and summary. Identify which of these they have (in priority order):

A. A MISSION STATEMENT — something they actively chose to say about why they do what they do
   Examples: "collaborating for a stronger NDIS community", "building the allied health workplace therapists stay at", "leading with ethics and quality"

B. A MARKET POSITION — the niche or specialisation they specifically named
   Examples: "complex and high-intensity NDIS care", "culturally responsive supports", "regional NDIS provider"

C. A VALUE THEY NAMED — the word or principle they put in their own headline
   Examples: "transparency", "quality", "collaboration", "retention", "family-centered"

If A, B, and C are all absent or generic, fall back to their service type + participant type and find the LEAST OBVIOUS insider observation about working in that space.

---

STEP 2 — WRITE THE PS LINE

Write ONE sentence that:
- Starts with "PS —"
- Names the specific angle from Step 1 (use their words, not a paraphrase)
- Adds ONE observation connecting that angle to participant flow or referral relationships — without pitching DGK
- Uses plain, conversational English — the kind of thing a peer would say, not a marketer

USE THIS STRUCTURE:
"PS — [their specific angle or words] [insider observation about what that means for participant acquisition or referral relationships]."

---

EXAMPLES OF THE STANDARD TO AIM FOR:

When they emphasise collaboration:
"PS — You specifically mention collaboration in your headline — referral networks are where that value creates actual participant flow."

When they emphasise therapist retention / staff culture:
"PS — Your focus on building a workplace therapists stay at tells me participant experience is what you optimise for, not just volume."

When they specialise in complex / high-intensity care:
"PS — Complex care specialists are often the providers coordinators trust most but struggle to find — they refer to whoever reaches out first."

When they serve psychosocial participants:
"PS — Psychosocial recovery coaching is one of the hardest NDIS services to fill through word of mouth alone — coordinators are the actual channel."

When they emphasise quality or ethics:
"PS — Providers who lead with quality tend to be the ones coordinators trust most for their most complex referrals."

When they are regional:
"PS — Regional NDIS providers often have less coordinator competition than metro — but also less coordinator outreach."

---

HARD RULES:
- 15 to 25 words after "PS —"
- Never compliment them: no "impressive", "love what you're doing", "great work", "I love your approach"
- Never mention the lead magnet, guide, or anything about what the email is offering
- Never restate their headline word-for-word — use it as a source, not a quote
- If their summary is empty, work from headline only — do not fabricate content
- If headline is completely generic (e.g., "NDIS provider" only), use their service type + participant type

Return ONLY the full PS line starting with "PS —". No quotes. No explanation. Nothing else.
```

---

## PROMPT 3 — THE PAIN OBSERVATION
**Column:** `dgk_pain_line`
**Model:** GPT-4 Mini
**Credits:** ~1/row
**Condition:** `{{Service Type}}` is not empty

### Clay Inputs
```
current_company, Service Type, Participant Specialisation, Locality, Size, Years in Business, Description
```

### Prompt
```
You are writing a PAIN OBSERVATION sentence for a cold email from DGK Business Consultancy to an NDIS provider.

This sentence names a specific operational truth about their market that the recipient would read and think "that is exactly what I see." It is NOT about DGK. It is NOT a pitch. It is an insider observation that shows the sender understands their world.

CONTACT:
- Company: {{current_company}}
- NDIS services: {{Service Type}}
- Participant focus: {{Participant Specialisation}}
- Location: {{Locality}}
- Team size: {{Size}}
- Stage: {{Years in Business}}
- Description: "{{Description}}"

---

STEP 1 — MATCH THE PAIN PATTERN

Use the service type to find the relevant pain. These are real patterns — do not soften or genericise them:

SIL / SDA:
PATTERN: "SIL providers in [location] [pain about coordinator preferred lists not changing]."
KNOWLEDGE: Coordinators maintain a fixed shortlist of preferred SIL providers. That list almost never changes. New providers cannot break onto it by waiting — they have to reach out before the coordinator has a participant who needs them. Most never do.

Allied Health (OT, speech, physio, psychology):
PATTERN: "Allied health practices in [location] with [staff type] [pain about empty caseloads despite clinical quality]."
KNOWLEDGE: Allied health practices often have excellent clinicians and empty appointment slots simultaneously. Coordinators refer to practitioners they have personally met. Clinical quality is assumed — coordinator relationships are the differentiator.

Behaviour Support / PBS:
PATTERN: "Most behaviour support providers in [state] [pain about coordinators defaulting to same trusted practitioners]."
KNOWLEDGE: Coordinators are cautious about behaviour support referrals. One bad match between a complex participant and a provider damages the relationship permanently. They default to the 2-3 practitioners they have personally vetted. Getting into that group requires months of proactive relationship building.

Psychosocial / Mental Health / Recovery Coaching:
PATTERN: "Psychosocial providers in [location] [pain about coordinator dependency vs ad ineffectiveness]."
KNOWLEDGE: Facebook ads send enquiries but rarely the right participants for psychosocial services. Families rely on coordinator recommendations. Providers who are not proactively building coordinator relationships are invisible to the channel that actually refers psychosocial participants.

Core Supports / Daily Activities / Personal Care / Community Access:
PATTERN: "Core supports providers in [location] [pain about commodity market and coordinator relationship as only differentiator]."
KNOWLEDGE: Core supports is the most competitive NDIS service category. Every provider in the area offers similar services. Providers with full caseloads do not have better services — they have more coordinator relationships than the providers sitting at 60% capacity.

High Intensity / Nursing / Complex Care:
PATTERN: "Complex care providers in [location] [pain about coordinators wanting to refer but needing to trust first]."
KNOWLEDGE: Coordinators desperately want to place complex participants but are scared of an unreliable provider. The first complex care provider who proactively reaches out and establishes competence owns those referrals for years. Most complex care providers wait.

Support Coordination:
PATTERN: "Support coordinators in [location] [pain about needing plan manager and LAC relationships to grow]."
KNOWLEDGE: Support coordinator businesses grow through plan manager and LAC referrals. Most wait for word of mouth. Proactive outreach to plan managers is the growth lever almost no one uses.

Plan Management:
PATTERN: "Plan managers in [location] [pain about participant flow depending on coordinator referrals they are not actively building]."
KNOWLEDGE: Plan managers get participants through coordinator and LAC referrals. Most plan managers are passive — they provide excellent service and wait for referrals. The ones growing fastest have built proactive coordinator outreach.

General NDIS (service type unclear):
PATTERN: "NDIS providers in [location] [pain about referral dependency looking like word of mouth but actually being coordinator relationships]."
KNOWLEDGE: Participant acquisition in the NDIS looks like word of mouth but runs on coordinator relationships. Providers who understand this have predictable pipelines. Those who treat it as word of mouth have unpredictable months.

---

STEP 2 — LOCALISE AND WRITE

Take the matching pain pattern and write ONE sentence (15-25 words) that:
- Names their specific service type (not just "NDIS provider")
- Includes their location — state name is enough if city is unclear
- Sounds like something a consultant who works in this sector would say — not a marketer, not an AI
- Uses present tense, active voice

PREFERRED STRUCTURES:
"[Service type] providers in [location] tell me [specific pain pattern]."
"Most [service type] founders in [state] [specific operational truth]."
"[Service type] in [location] usually means [specific participant acquisition constraint]."

HARD RULES:
- 15 to 25 words
- Never mention DGK or any solution
- Never use vague words: challenging, difficult, struggle, issues, problems — name the SPECIFIC mechanism instead
- Never write something that could apply to every NDIS provider equally

Return ONLY the sentence. No explanation. Nothing else.
```

---

## PROMPT 3B — WEBSITE-ENRICHED (General NDIS rows only)
**Column:** `dgk_pain_line_enriched`
**Model:** GPT-4 Mini + Claygent web access
**Credits:** ~3-5/row
**Condition:** `{{Service Type}}` = "General NDIS" AND `{{Domain}}` is not empty

```
Visit the website at {{Domain}}.

Find out:
1. Which specific NDIS support categories does {{current_company}} provide?
2. Which participant types do they work with?
3. Any geographic specialisation?
4. Any mention of referral partners, support coordinators, or how they receive participants?

Then write ONE pain observation sentence (15-25 words) using the patterns below.

Match their services to the relevant pain:
- SIL/SDA: coordinators have fixed preferred lists — new providers cannot break in without proactive outreach
- Allied Health: great clinicians, empty caseloads — coordinators only refer to practitioners they have personally met
- Behaviour Support: coordinators default to 2-3 trusted providers — breaking into that shortlist requires months of relationship building
- Psychosocial: ads send enquiries but not participants — coordinator recommendations are the actual channel
- Core Supports: commoditised service — coordinator relationships are the only differentiator
- High Intensity: coordinators want to refer complex participants but fear placing them with the wrong provider
- General: participant acquisition looks like word of mouth but actually runs on coordinator relationships

Write the sentence from the NDIS market perspective, naming their specific service type and location. Do NOT mention DGK. Do NOT offer a solution.

Return ONLY the pain sentence. Nothing else.
```

---

## EXAMPLE OUTPUTS — BEFORE vs AFTER

### Vatsal Ashar — 9D Care (SIL, SDA, Core Supports — VIC — "Collaborating for a Stronger NDIS Community")

| Output | Before (Generic) | After (Specific) |
|---|---|---|
| Opener | "Running general NDIS services from Broadmeadows puts you in one of the most competitive markets in Victoria." | "Running SIL and SDA in Broadmeadows usually means the same 5 coordinators control most of your participant flow." |
| PS Hook | "Your headline identifies 9D Care as an NDIS registered provider in the community." | "PS — You specifically mention collaboration in your headline — that is exactly what a coordinator referral network is built on." |
| Pain Line | (absent) | "SIL providers in Melbourne tell me coordinators have a fixed preferred list — and getting on it without proactive outreach is nearly impossible." |

### Neil Hensley — Medisense (Allied Health — QLD — "Building the allied health workplace therapists actually stay at")

| Output | Before | After |
|---|---|---|
| Opener | "I noticed Medisense is focused on creating a better workplace for allied health professionals in Queensland." | "Allied health practices that retain therapists long-term tend to hit a ceiling — great clinicians, not enough participants to fill their schedules." |
| PS Hook | "PS — Your commitment to allied health staff retention reflects your high standard of care for clients." | "PS — Your headline is about retention, not growth — which usually means the caseload side is the actual constraint at Medisense." |
| Pain Line | (absent) | "Most allied health founders in QLD tell me great clinicians and empty appointment slots come from the same root cause — coordinators only refer to practitioners they have met." |

### Ronald — Flonac Health (Complex Care, High Intensity — Gold Coast — "Leading the Way in Complex & High-Intensity NDIS Care")

| Output | Before | After |
|---|---|---|
| Opener | "Flonac Health's specialisation in complex and high-intensity NDIS care puts you in a challenging but important niche." | "Growing a complex care team on the Gold Coast means coordinators want to refer to you — but only after they trust you." |
| PS Hook | "PS — Your specialisation in high-intensity care shows your commitment to the most vulnerable participants." | "PS — Complex care specialists are often the providers coordinators trust most but struggle to find — they refer to whoever reached out first." |
| Pain Line | (absent) | "High-intensity NDIS providers on the Gold Coast tell me coordinators want to refer complex participants — but they place them with whoever they already know." |

---

## CRITICAL TEST — Run These 5 Rows First

Before running the full list, test on these 5 row types and review the raw output:

1. One row where `Service Type` = "SIL" — does the opener name SIL and a location?
2. One row where `Service Type` = "Allied Health" — does it reference the caseload/clinician gap?
3. One row where `Service Type` = "General NDIS" — does it still produce a specific line rather than a generic one?
4. One row where `headline` is short (under 5 words) — does the PS hook still work?
5. One row where `Description` is empty — does the opener degrade gracefully or break?

If any of those 5 produce generic output (starts with "Your", restates the headline, uses "challenges", "struggle"), adjust the relevant step in that prompt before scaling.

---

---

## SUBJECT LINE PROMPTS

### How Subject Lines Work Across the 3-Email Sequence

| Email | Day | Subject approach | Column needed |
|---|---|---|---|
| Email 1 | Day 0 | New subject — AI-generated (two-word formula) | `subject_email1` |
| Email 2 | Day 4 | **Same thread** — Smartlead sends as RE: [Email 1 subject] | None — Smartlead handles this |
| Email 3 | Day 9 | New thread — formula-generated (personal, short) | `subject_email3` |

Email 2 never gets a new subject. In Smartlead, tick "Reply in thread" on Email 2's step — it automatically sends as `RE: [Email 1 subject]`. This is the correct cold email approach (keeps the conversation context, higher open rate for follow-ups).

---

### COLUMN: `subject_email1`
**Type:** GPT-4 Mini
**Credits:** ~1/row
**Condition:** `{{current_company}}` is not empty

Uses the ColdIQ two-word formula — exactly 2 words, all lowercase, relevant to their NDIS business, creates curiosity without revealing the topic.

```
Write a two-word email subject line for a cold email to {{current_company}}, an NDIS provider.

Their services: {{service_type_raw}}
Their state: {{state}}
Their participants: {{participant_type_raw}}

Rules:
- MUST be exactly 2 words — no exceptions
- All lowercase, no punctuation, no numbers
- Relevant to participant acquisition, referral partnerships, or support coordinator relationships in NDIS
- Creates mild curiosity — does NOT reveal what the email is about
- No sales or buzz words: never write "sales", "outreach", "marketing", "partnership", "collaboration", "system", "solution", "services", "growth", "strategy"
- Should feel like it was typed by someone who knows their sector — not generated by an AI

GOOD examples (use these as your quality benchmark):
- "participant flow" — relevant to what every NDIS provider cares about, reveals nothing
- "coordinator pipeline" — insider language, creates curiosity
- "referral gap" — implies a problem, doesn't name the solution
- "care pipeline" — service-relevant but vague
- "coordinator access" — sounds like insider knowledge
- "allied pipeline" — service-specific to allied health providers
- "sil waitlist" — hyper-relevant for SIL providers

BAD examples (never produce these):
- "referral system" — reveals the pitch
- "new partnership" — buzz word
- "quick question" — massively overused, not two words of value
- "more participants" — sounds like advertising
- "participant acquisition" — too formal, too long
- "ndis outreach" — contains "outreach" which is a banned word

Return ONLY the two-word subject line. No quotes. No explanation. Nothing else.
```

---

### COLUMN: `subject_email3`
**Type:** Clayscript formula (0 credits)
**Condition:** `{{clean_first_name}}` is not empty

Email 3 is a low-pressure call offer (day 9, third touch). Subject should feel like a personal follow-up — the kind of subject line a human types in 2 seconds, not a marketing team. Very short, very personal.

```javascript
const firstName = String({{clean_first_name}} || "").trim().toLowerCase();
const company = String({{current_company}} || "").trim();
const tier = String({{Position Tier}} || "").trim();
const variant = String({{email_variant}} || "A");

// Take first word only if company name is long
const shortCo = company.length > 15
  ? company.split(/[\s,&]+/)[0]
  : company;
const co = shortCo.toLowerCase().replace(/[^a-z0-9]/g, "");

// Tier A (CEO/Founder) — very personal, uses first name
const patternsA_tierA = [
  `15 mins, ${firstName}?`,
  `worth it?`,
  `${firstName} — quick`,
  `one question`,
];

// Tier B (Director/MD) — company-focused, slightly more professional
const patternsA_tierB = [
  `15 mins?`,
  `worth a call?`,
  `quick one`,
  `one thing`,
];

// Variant B — company name based (for A/B testing)
const patternsB = [
  `${co}?`,
  `${firstName} — worth it?`,
  `15 min this week?`,
  `following up`,
];

const isTierA = tier === "Tier A";
const basePatterns = isTierA ? patternsA_tierA : patternsA_tierB;
const patterns = variant === "B" ? patternsB : basePatterns;

// Deterministic hash — same contact always gets same subject
const hash = company.split("").reduce((sum, c) => sum + c.charCodeAt(0), 0);
return patterns[hash % patterns.length];
```

---

### A/B TEST RECOMMENDATION (Email 1)

After generating `subject_email1` with GPT-4 Mini, the best A/B test is:

| Variant | Subject | Type |
|---|---|---|
| A | GPT-4 Mini output (`subject_email1`) | AI two-word, business-relevant |
| B | `idea for [company]` (hardcode in Smartlead) | Formula-based, personalized |

Run for at least 100 sends per variant. Measure open rate AND reply rate — a high-open / low-reply subject is clickbait and will hurt trust.

The winner tells you whether your audience responds better to business-relevant subjects (what they do) or company-personalized subjects (their name in the subject).

---

### SMARTLEAD SUBJECT LINE SETUP

In Smartlead:
- **Email 1 step → Subject field:** `{{customVariable8}}`
- **Email 2 step → Check "Reply in thread"** — subject is inherited automatically as `RE: {{customVariable8}}`
- **Email 3 step → Subject field:** `{{customVariable9}}`

Do NOT manually write the Email 2 subject — Smartlead handles the RE: threading. If you set a new subject on Email 2, it breaks the thread and it looks like a separate cold email, not a follow-up.

---

## CLAY WORKFLOW — RUN ORDER

```
STEP 1:  Import CSV (pre-filtered: qualify + NDIS yes)

STEP 2:  Formula columns (0 credits) — add all immediately:
         - clean_first_name
         - signal_tier
         - state
         - campaign_track
         - email_variant
         - service_type_raw
         - subject_email3       ← NEW (Clayscript, 0 credits)

STEP 3:  GPT-4 Mini columns — run in this order, each conditional:
         3a: dgk_opener       — all rows — ~1 credit/row
         3b: dgk_ps_hook      — all rows — ~1 credit/row
         3c: dgk_pain_line    — all rows — ~1 credit/row
         3d: subject_email1   — all rows — ~1 credit/row  ← NEW
         3e: dgk_pain_line_enriched — only "General NDIS" rows — ~3-5 credits/row
             → update dgk_pain_line for those rows with the enriched version

STEP 4:  Email waterfall (for rows missing Work Email)
         LeadMagic → Prospeo → Hunter → Apollo

STEP 5:  final_email formula (merge waterfall results + Work Email)

STEP 6:  MillionVerifier (conditional: final_email not empty)

STEP 7:  send_ready gate formula (last)

STEP 8:  Export to Smartlead
```

---

## SMARTLEAD FIELD MAPPING

| Clay Column | Smartlead Variable | Used In |
|---|---|---|
| `clean_first_name` | firstName | All emails |
| `current_company` | companyName | All emails |
| `dgk_opener` | customVariable1 | Email 1 first line + Email 3 first line |
| `service_type_raw` | customVariable2 | Email 2 body |
| `participant_type_raw` | customVariable3 | Email 2 body |
| `dgk_ps_hook` | customVariable4 | Email 1 PS line |
| `state` | customVariable5 | Email 2 geographic reference |
| `email_variant` | customVariable6 | A/B tracking |
| `dgk_pain_line` | customVariable7 | Email 2 opener |
| `subject_email1` | customVariable8 | Email 1 subject line |
| `subject_email3` | customVariable9 | Email 3 subject line |

### How to Use These in Smartlead Campaign Templates

**Email 1:**
- Subject field: `{{customVariable8}}`
- Body first line: `{{customVariable1}}`
- PS line: `{{customVariable4}}`

**Email 2:**
- Subject: **tick "Reply in thread"** — do not set a subject manually
- Body first line: `{{customVariable7}}` (the pain observation)

**Email 3:**
- Subject field: `{{customVariable9}}`
- Body first line: `{{customVariable1}}` (same opener as Email 1, still works)

---

## UPDATED EMAIL 1 (Using New Variables)

**Subject:** `referral guide`

```
{{firstName}},

{{customVariable1}}

Put together a short guide for NDIS providers on getting referral partners without spending on ads — the 5-step system, including one signal most providers completely miss.

Can I send it over?

{{customVariable4}}
```

**Subject B (A/B variant):** `ndis referral`

```
{{firstName}},

{{customVariable1}}

Built something for NDIS providers in {{customVariable5}} on building a referral partner pipeline without ads. Mind if I send it over?

{{customVariable4}}
```

---

## UPDATED EMAIL 2 (Using Pain Line)

**Subject:** `job post signal`

```
{{firstName}},

{{customVariable7}}

Here is what works better than reaching out to coordinators who have been in the role for years — those coordinators already have a provider list and rarely change it.

Reach out to a support coordinator in their first 2 weeks. They do not have providers yet. You become their go-to before anyone else does.

You can find them by tracking when organisations post coordinator roles on SEEK.

Is that something {{companyName}} has tried?
```

---

## CREDIT ESTIMATE (91 rows)

| Step | Provider | Credits/row | Rows | Total |
|---|---|---|---|---|
| Opener (dgk_opener) | GPT-4 Mini | 1 | 91 | 91 |
| PS Hook (dgk_ps_hook) | GPT-4 Mini | 1 | 91 | 91 |
| Pain Line (dgk_pain_line) | GPT-4 Mini | 1 | 91 | 91 |
| Subject Email 1 (subject_email1) | GPT-4 Mini | 1 | 91 | 91 |
| Subject Email 3 (subject_email3) | Clayscript | 0 | 91 | 0 |
| Pain Line Enriched (General NDIS only) | GPT-4 Mini + web | 4 avg | ~15 | 60 |
| Email waterfall (missing emails only) | 4 providers | 5 avg | ~55 | 275 |
| MillionVerifier | MillionVerifier | 1 | ~80 | 80 |
| **Total** | | | | **~779 credits** |

**Cost: ~$8–16 for the full 91-row list.**

4 AI columns per row + subject line + waterfall + verification — fully personalized, launch-ready.
