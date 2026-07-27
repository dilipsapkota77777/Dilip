# Darwin Professional Services — 3-Email Sequence
# ColdIQ Framework | NT Professional Services Outreach
# Offer: Client Pipeline System — CRM + Outbound + Google Presence + AI Automation
Generated: 2026-07-27

---

## Campaign Context

**From:** DGK Business Consultancy
**To:** CEOs, Founders, Managing Directors of Darwin/NT professional services firms
**Goal:** Book a 15-min discovery call
**Lead magnet:** "The 5-Step Client Pipeline: How Darwin Professional Services Firms Win Consistent Work Without Waiting for Referrals"
**Tone:** Peer-to-peer, direct, NT-aware — never corporate or salesy

---

## Sequence Structure

Value prop rotates per email — master-cold-email rule: change angle between emails.

| Email | ColdIQ Template | Value Prop Angle | Value Delivered | Subject | Day |
|---|---|---|---|---|---|
| Email 1 | Leverage Content | **Make money** — stop depending on referrals | Lead magnet — 5-step client pipeline guide | `{{customVariable7}}` (AI-generated) | Day 0 |
| Email 2 | Not Too Different Persona | **Save time** — the pipeline system runs without you | How Darwin firms like theirs are doing it differently | RE: same thread | Day 4 |
| Email 3 | Ask Before Pitch | **Save money** — the referral ceiling has a cost | 15 min to see if a pipeline system applies to their firm | `{{customVariable8}}` (Clayscript) | Day 9 |

---

## EMAIL 1 — Lead Magnet Offer
**ColdIQ Template: Leverage Content (Ethan Parker)**
**Subject:** `{{customVariable7}}` (from Clay `subject_email1` column)
**Value:** Full lead magnet — 5-step client pipeline guide for professional services in Darwin

### Standard Version (All Professional Services)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin professional services firms on building a consistent client pipeline — without waiting for the next referral.

Covers the 5 steps, including the one thing most firms with predictable monthly revenue have that others don't.

Can I send it over?

{{customVariable4}}
```

**Variables:**
- `{{customVariable1}}` = `ps_opener` (AI-generated, firm-type-specific first line)
- `{{customVariable4}}` = `google_reviews_ps` (Google reviews PS from Clay)

**Word count:** ~65 words ✅
**CTA:** "Can I send it over?" — zero-friction reply

---

### ACCOUNTING VARIANT (`industry_group = "Accounting"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin accounting firms on building a client pipeline that works outside EOFY — so revenue doesn't crater in July-October.

Covers how the firms doing consistent $80K+ months handle enquiries differently.

Can I send it over?

{{customVariable4}}
```

---

### LEGAL VARIANT (`industry_group = "Legal"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide on how Darwin solicitors and law practices are building client pipelines without relying on referrals — staying on the right side of professional conduct rules.

Covers the 5-step approach the firms with consistent enquiries use.

Can I send it over?

{{customVariable4}}
```

---

### CONSULTING VARIANT (`industry_group = "Consulting"`)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin consultants and advisors on building a retainer pipeline — so you're not hunting for the next project while delivering the current one.

Can I send it over?

{{customVariable4}}
```

---

### TIER A VARIANT (Hiring = Yes)
```
{{firstName}},

{{customVariable1}}

Put together a short guide for Darwin firms growing their team on making sure client pipeline grows with headcount — not after.

Covers what firms hiring right now are doing to make sure the next hire has clients to serve from day one.

Can I send it over?

{{customVariable4}}
```

**Word count:** ~60 words ✅

---

## EMAIL 2 — Not Too Different Persona
**ColdIQ Template: Not Too Different Persona**
**Subject:** RE: (same thread as Email 1)
**Value:** Peer proof — how other Darwin professional services firms are solving this

```
{{firstName}},

I work with professional services firms across Darwin and nationally.

The ones growing past referrals have one thing in common: a client pipeline that runs whether they're on the tools or not.

Most reach out when they realise they haven't had a cold enquiry in 30+ days.

Is that something {{company}} is dealing with?

{{signature}}
```

**Word count:** ~60 words ✅
**CTA:** Soft yes/no question — easy reply, reveals intent

---

### VARIANT A — Revenue-Aware
```
{{firstName}},

I work with professional services firms at {{company}}'s revenue level across Darwin.

The pattern I see: strong reputation, solid referrals, but no system for cold enquiries.

When referrals slow — Q3, end of financial year, school holidays — revenue stalls.

Is that the pattern at {{company}} too?

{{signature}}
```

---

### VARIANT B — Hiring Signal
```
{{firstName}},

Most Darwin firms growing their team right now are dealing with the same timing problem — new staff arrive before the client pipeline is ready to support them.

DGK builds the pipeline system before that gap opens up.

Worth a 15-min conversation to see if it applies?

{{signature}}
```

---

## EMAIL 3 — Ask Before Pitch
**ColdIQ Template: Ask Before Pitch (Will Allred)**
**Subject:** `{{customVariable8}}` (Clayscript — separate from Email 1 subject)
**Value:** How DGK builds the pipeline end-to-end — 15 min to see if it fits

```
{{firstName}},

How are you currently winning new clients outside your existing referral network?

{{customVariable2}}

DGK builds the full client acquisition system for Darwin professional services firms — outbound, Google presence, CRM, and automation — handed over and running in 12 weeks.

Worth 15 minutes to see if it's a fit?

{{customVariable4}}
```

**Variables:**
- `{{customVariable2}}` = `ps_pain_line` (AI-generated firm-specific pain observation)
- `{{customVariable4}}` = `google_reviews_ps` (only if not used in Email 1)

**Word count:** ~70 words ✅
**CTA:** "Worth 15 minutes to see if it's a fit?" — soft discovery ask

---

### BREAKUP VARIANT (no reply after Email 3)
```
{{firstName}},

Last one from me — happy to step back if the timing's off.

One thing I'll leave you with: every Darwin firm that's built a referral-independent pipeline said the same thing when we spoke — they wish they'd done it 12 months earlier.

If that resonates later, you know where to find me.

{{signature}}
```

---

## Subject Line Bank (for Clayscript + A/B Testing)

### For `subject_email1` (`{{customVariable7}}`)
AI-generated by Clay — see `clay-workflow.md` for prompt.
Fallback options:
- `referral ceiling`
- `client pipeline, {{firstName}}`
- `how Darwin [firm type] are winning new clients`
- `{{companyName}} — quick idea`
- `without ads`

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
- Version B: `referral ceiling` (static)

Measure open rate after 50 sends. Winner rolls to full list.

**Week 2 test (Email 2 structure):**
- Version A: Standard "I work with..." persona opener
- Version B: Revenue-aware variant

Measure reply rate. Winner continues.

---

## Sequence Benchmarks

| Metric | Target | Action if Below |
|---|---|---|
| Open rate Email 1 | 40-55% | Fix subject line — run A/B test |
| Reply rate Email 1 | 8-12% | Fix CTA — soften ask |
| Reply rate Email 2 | 5-8% | Fix pain specificity — run sub-segment variant |
| Reply rate Email 3 | 3-5% | Fix opener — use Ask Before Pitch more directly |
| Sequence total reply rate | 12-20% | Review targeting — tighten to Tier A + signals |
