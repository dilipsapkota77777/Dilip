# Darwin Agencies — 3-Email Sequence
# ColdIQ Framework | NT Agencies & Service Businesses Outreach
# Offer: Agency New Business System — Outbound + CRM + Google Presence + AI Automation
Generated: 2026-07-27

---

## Campaign Context

**From:** DGK Business Consultancy
**To:** CEOs, Founders, Managing Directors of Darwin/NT agencies
**Goal:** Book a 15-min discovery call
**Lead magnet:** "Agency New Business Blueprint: How Darwin Service Businesses Win Their Next 10 Clients Without Waiting for Referrals"
**Tone:** Peer-to-peer, direct, NT-aware — the cobbler's children angle throughout

---

## Sequence Structure

Value prop rotates per email.

| Email | ColdIQ Template | Value Prop Angle | Value Delivered | Subject | Day |
|---|---|---|---|---|---|
| Email 1 | Leverage Content | **Make money** — agency new business system | Lead magnet — agency new business blueprint | `{{customVariable7}}` (AI-generated) | Day 0 |
| Email 2 | Not Too Different Persona | **Save time** — the pipeline runs without you | How Darwin agencies like theirs are winning new clients | RE: same thread | Day 4 |
| Email 3 | Ask Before Pitch | **Save money** — cost of running BD manually | 15 min to see if it applies to their agency | `{{customVariable8}}` (Clayscript) | Day 9 |

---

## EMAIL 1 — Lead Magnet Offer
**ColdIQ Template: Leverage Content (Ethan Parker)**
**Subject:** `{{customVariable7}}` (from Clay `subject_email1` column)
**Value:** Agency New Business Blueprint lead magnet

### Standard Version (All Agency Types)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin agencies on winning new clients consistently — without relying on referrals, warm intros, or hustle.

Covers the 5-step system, including the one thing agencies with predictable new business have that most don't.

Can I send it over?

{{customVariable4}}
```

**Variables:**
- `{{customVariable1}}` = `agency_opener` (AI-generated, agency-type-specific first line)
- `{{customVariable4}}` = `google_reviews_ps` (Google reviews PS from Clay)

**Word count:** ~65 words ✅
**CTA:** "Can I send it over?" — zero-friction reply

---

### RECRUITMENT VARIANT (`industry_group = "Recruitment"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin recruitment agencies on winning new employer-client retainers — without cold calls or depending on existing relationships.

Covers how the NT recruitment firms with consistent new employer growth have built their BD system.

Can I send it over?

{{customVariable4}}
```

---

### MARKETING / CREATIVE AGENCY VARIANT (`industry_group = "Marketing"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide on how Darwin marketing and creative agencies are building their own new business pipeline — the way they build it for their clients.

Covers the 5 steps the agencies with consistent new client growth use.

Can I send it over?

{{customVariable4}}
```

---

### NDIS / HEALTH SERVICES VARIANT (`industry_group = "Health"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin NDIS and health service providers on building a consistent participant and referral pipeline — without depending on coordinator word-of-mouth.

Can I send it over?

{{customVariable4}}
```

---

### TIER A + HIRING VARIANT
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin agencies growing their team on making sure new client pipeline keeps pace with headcount.

Covers what the agencies hiring right now are doing to make sure new staff have work to bill from day one.

Can I send it over?

{{customVariable4}}
```

---

## EMAIL 2 — Not Too Different Persona
**ColdIQ Template: Not Too Different Persona**
**Subject:** RE: (same thread)
**Value:** Peer proof — how other Darwin agencies are solving the cobbler's problem

```
{{firstName}},

I work with agencies and service businesses across Darwin.

The pattern I see at most of them: brilliant at getting results for clients, but the agency's own new business runs on referrals and whoever the founder knows.

When referrals slow, so does revenue.

Is that what new business looks like at {{company}} right now?

{{signature}}
```

**Word count:** ~60 words ✅
**CTA:** Soft yes/no — easy reply

---

### VARIANT A — Cobbler's Children (for marketing/creative agencies)
```
{{firstName}},

I work with marketing agencies in Darwin.

Most of them are running campaigns for their clients' new business but have no equivalent system for their own.

The ones with consistent new client growth treat their agency like their best client — and built a proper new business function.

Is that something you've thought about at {{company}}?

{{signature}}
```

---

### VARIANT B — Recruitment-Specific
```
{{firstName}},

I work with recruitment agencies across Darwin and nationally.

The ones winning new employer-client retainers consistently have one thing the others don't: a systematic BD approach that isn't dependent on existing relationships.

When a hiring manager changes roles or puts a freeze on, their pipeline doesn't stop.

Is that a challenge at {{company}}?

{{signature}}
```

---

### VARIANT C — Hiring Signal
```
{{firstName}},

Most Darwin agencies growing their team right now are facing the same timing problem — the new hire starts before the client pipeline is ready to support them.

DGK builds the new business system before that gap opens up.

Worth 15 minutes to see if it applies?

{{signature}}
```

---

## EMAIL 3 — Ask Before Pitch
**ColdIQ Template: Ask Before Pitch (Will Allred)**
**Subject:** `{{customVariable8}}` (Clayscript)
**Value:** The new business system — 15 min to see if it fits

```
{{firstName}},

How are you currently winning new clients outside your existing referral network?

{{customVariable2}}

DGK builds the full new business system for Darwin agencies — outbound, CRM, Google presence, and AI automation — handed over and running in 12 weeks.

Worth 15 minutes to see if it's a fit for {{company}}?

{{customVariable4}}
```

**Variables:**
- `{{customVariable2}}` = `agency_pain_line` (AI-generated, agency-specific pain observation)
- `{{customVariable4}}` = `google_reviews_ps` (only if not used in Email 1)

**Word count:** ~70 words ✅
**CTA:** Soft discovery ask

---

### BREAKUP VARIANT (no reply after Email 3)
```
{{firstName}},

Last one from me — happy to step back if the timing's off.

One thing I'll leave you with: every Darwin agency that's built a referral-independent new business system said the same thing when we spoke — they wish they'd done it before the last quiet patch.

If that resonates later, you know where to find me.

{{signature}}
```

---

## Subject Line Bank

### For `subject_email1` (`{{customVariable7}}`)
AI-generated by Clay — see `clay-workflow.md` for prompt.
Fallback options:
- `agency new business`
- `{{firstName}} — quick idea`
- `cobbler's children problem`
- `new clients without referrals`
- `how darwin agencies are winning new clients`
- `{{companyName}} — 3 ideas`

### For `subject_email3` (`{{customVariable8}}`)
- `quick question`
- `{{firstName}} — how are you winning new clients?`
- `last one`
- `worth 15 min?`
- `new clients at {{companyName}}`

---

## A/B Test Framework

**Week 1 test (Email 1 subject):**
- Version A: `{{customVariable7}}` (AI-generated)
- Version B: `agency new business` (static)

Measure open rate after 30 sends. Winner rolls to full list.

**Week 2 test (Email 1 CTA):**
- Version A: "Can I send it over?" (standard)
- Version B: "Worth a look?" (shorter)

Measure reply rate.

---

## Sequence Benchmarks

| Metric | Target | Action if Below |
|---|---|---|
| Open rate Email 1 | 40-55% | Fix subject line — run A/B |
| Reply rate Email 1 | 8-15% | Fix opener or CTA — agencies respond to peer framing |
| Reply rate Email 2 | 6-10% | Fix persona specificity — use recruitment/marketing variant |
| Reply rate Email 3 | 3-6% | Fix opener — make cobbler's angle more direct |
| Sequence total | 15-25% | Review targeting — tighten to Tier A + signal stack |

**Note:** Agency founders often reply to Email 2 more than Email 1 — they recognise themselves in the "Not Too Different Persona" framing. Don't stop the sequence after Email 1 no-replies.
