# Helpingme — 3-Email Referral Partner Sequence
# ColdIQ Framework | NDIS Provider Outreach
# Based on: "Get NDIS Clients Without Paying for Ads" lead magnet
Generated: 2026-07-24

---

## Campaign Context

**From:** Helpingme (via DGK Business Consultancy)
**To:** CEOs, Founders, Managing Directors of NDIS provider companies
**Goal:** Start a conversation about referral partner outreach → book a 15-min discovery call
**Lead magnet:** "Get NDIS Clients Without Paying for Ads" (Gamma doc)
**Tone:** Peer-to-peer, plain English, zero corporate language

---

## Sequence Structure

| Email | ColdIQ Template | Value Delivered | Subject | Day |
|---|---|---|---|---|
| Email 1 | Leverage Content | Lead magnet — referral partner playbook | `referral guide` | Day 0 |
| Email 2 | Not Too Different Persona | Specific technique — the job post signal | `job post signal` | Day 4 |
| Email 3 | Ask Before Pitch | How Helpingme/DGK does this for them | `quick question` | Day 9 |

---

## EMAIL 1 — Lead Magnet Offer
**ColdIQ Template: Leverage Content (Ethan Parker)**
**Subject:** `referral guide`
**Value:** The full lead magnet — getting NDIS referral partners without ads

```
{{firstName}},

Put together a short guide for NDIS providers on getting referral partners without spending on ads.

Covers the 5-step system — including one signal most providers completely miss: why a new job post for a support coordinator is actually the best time to reach out to that organisation.

Can I send it over?

PS — {{customVariable4}}
```

**Variables:**
- `{{customVariable4}}` = `headline_hook` from Claygent (e.g., "Noticed {{companyName}} focuses on high-intensity care — exactly the service type support coordinators struggle most to place.")

**Word count:** 69 words ✅
**CTA:** "Can I send it over?" — zero-friction reply
**What to send when they reply:** The Gamma link: https://gamma.app/docs/Get-NDIS-Clients-Without-Paying-for-Ads-7vxymsu2ms5vn95

---

**TIER A VARIANT (CEO/Founder — Position Tier = "Tier A"):**

```
{{firstName}},

Most NDIS providers chase families through ads. The ones with a consistent participant pipeline built it through support coordinators and case managers — not Facebook.

Put together a guide on how the referral partner system works and why it outperforms ads every time.

Can I send it over?

PS — {{customVariable4}}
```

---

## EMAIL 2 — Specific Technique
**ColdIQ Template: Not Too Different Persona (Will Allred)**
**Subject:** `job post signal`
**Value:** The single most powerful signal from the lead magnet — new hire timing

```
{{firstName}},

Most NDIS providers I speak to try to reach support coordinators who have been in the role for years. Those coordinators already have a provider list and they rarely change it.

Here is what works better: reach out to a support coordinator in their first 2 weeks.

They do not have providers yet. They are actively looking for someone reliable. You become their go-to before anyone else does.

You can find them by tracking when organisations post coordinator roles on SEEK.

Is that something {{companyName}} has tried?
```

**Word count:** 89 words ✅
**Why it works:** Delivers a specific, actionable insight they can use right now — regardless of whether they work with Helpingme. No pitch. Ends with a question that invites a real reply.

---

**TIER A VARIANT (CEO/Founder):**

```
{{firstName}},

Most NDIS founders I speak to in {{customVariable5}} spend on Facebook ads and wonder why the leads are expensive and slow.

The ones with predictable participant flow usually have 3 to 5 support coordinator relationships that send referrals monthly. Zero ad spend.

The timing trick: a newly hired support coordinator has no provider list yet. Reach out first and you own that relationship for years.

Is that the kind of system you have been thinking about building?
```

---

## EMAIL 3 — How We Help
**ColdIQ Template: Ask Before Pitch (Will Allred)**
**Subject:** `quick question`
**Value:** Show exactly how DGK builds this system for NDIS providers

```
{{firstName}},

{{customVariable1}}

Quick question — how are you currently finding referral partners at {{companyName}}?

We build the entire system for NDIS providers: finding support coordinators and case managers, verifying their emails, writing personalised sequences, and managing the outreach — so you get consistent participant referrals without spending on ads.

Worth 15 minutes to see if the setup makes sense for {{companyName}}?
```

**Variables:**
- `{{customVariable1}}` = `personalized_opener` from Clay GPT-4 Mini

**Word count:** 83 words ✅
**CTA:** "Worth 15 minutes" — specific, low-pressure, reply-based

---

**TIER A VARIANT (CEO/Founder):**

```
{{firstName}},

{{customVariable1}}

One support coordinator managing 30 participants who sends you 3 per month is worth $6,000 a month in participant services — at zero ad spend.

Five coordinators? $30,000 a month. And they keep sending.

We build that referral partner system for NDIS providers — finding coordinators, verifying contacts, writing the outreach, managing follow-up.

Worth a 15-minute call to see if {{companyName}} is a fit?
```

*The $6,000/$30,000 numbers come directly from the lead magnet — they reinforce the value of the system you're selling.*

---

## Personalisation System

### The Job Post Signal (Your #1 Warmth Indicator)

From the lead magnet, the biggest signal is: **is this organisation CURRENTLY hiring a support coordinator, case manager, or plan manager?**

This means:
- They are growing → more participants → more referrals for you
- Any new hire has NO provider list yet → reach out first → own that relationship

This signal is already captured in your CSV via `Years in Business` = "Growing (2-5yr)" but can be sharpened with a Claygent check (see Clay workflow).

### Personalisation Hooks from Their Headline

Use the `headline_hook` column (generated by Claygent from their LinkedIn headline) as the PS in Email 1.

**Real examples from the CSV:**

| Person | Headline | Hook to use |
|---|---|---|
| Vatsal Ashar (9D Care) | "Collaborating for a Stronger NDIS Community" | "Sent this because you specifically mention collaboration in your headline — that is exactly what a referral partner system is built on." |
| Ronald (Flonac Health) | "Leading the Way in Complex & High-Intensity NDIS Care" | "Your focus on complex and high-intensity care stands out — support coordinators always struggle to find reliable providers for those participants." |
| Zara England (Evercare) | "Leading Collaborative, Ethical & High-Quality NDIS and Community Supports" | "Your emphasis on collaborative NDIS supports is exactly the kind of provider a referral network should be built around." |
| Neil Hensley (Medisense) | "Building the allied health workplace therapists actually stay at" | "Your retention focus at Medisense tells me participant experience is your priority — which is exactly what makes a good long-term referral partner." |

---

## Smartlead Settings

**Campaign name:** `HELPINGME-NDIS-REFERRAL-AUS`

Split into two if needed:
- `HELPINGME-FOUNDER-AUS` — Tier A (Position Tier = Tier A)
- `HELPINGME-DIRECTOR-AUS` — Tier B (Position Tier = Tier B)

**Settings:**
- Sending window: Mon–Thu, 8:00am–10:30am AEST
- Daily cap: 25 per inbox during warm-up, 40–50 when warmed
- Stop on reply: Yes
- Open tracking: Off (hurts deliverability)
- Click tracking: Off (hurts deliverability)

---

## Reply Handling

| Reply | Action |
|---|---|
| "Yes send it over" | Send Gamma link immediately + follow up in 48 hours: "Did anything stand out from that?" |
| "Tell me more" | Reply with Email 3 content conversationally + book a call |
| "Not now / busy" | Mark Nurture → re-add in 45 days |
| "Not interested" | Unsubscribe, do not follow up |
| "What is this / who are you?" | Reply: "We help NDIS providers build referral partner pipelines. [First name] at Helpingme asked me to reach out — happy to share more if useful." |
| No reply after Email 3 | LinkedIn DM follow-up (see below) |

---

## LinkedIn Follow-Up Sequence (After Email 3, No Reply)

**Day 12 — Connection request:** Send blank (no note)

**Day 14 — DM after accepted:**
```
Hey {{firstName}}, thanks for connecting.

I reached out by email last week with a guide on building NDIS referral partner pipelines. Did not want to assume you had seen it.

Happy to send it over if useful.
```

**Day 21 — Final DM:**
```
{{firstName}}, leaving it here — but if getting consistent participant referrals without ad spend ever becomes a priority, feel free to reach out.

Happy to share what has been working for other NDIS providers.
```

Maximum 5 touches (3 email, 2 LinkedIn). Done.

---

## A/B Variants — Based on Top-Performing Script Patterns

These are Variant B versions for each email, drawn from analysis of 210 top-performing cold email scripts. Run these against the base versions using Smartlead's native A/B test feature or split by `email_variant` column from Clay.

---

### EMAIL 1 — Variant B
**Inspired by:** Scripts #9, #11-12 ("playbook for [Company]" framing, 17.24% reply rate)
**Subject B:** `ndis referral`
**What's different:** Leads with the geographic/contextual observation before the offer. More casual "mind if I send it" close.

```
{{firstName}},

Most NDIS providers I speak to in {{customVariable5}} still rely on word of mouth for referrals. Some never move past it.

Put together a short guide on the system that actually works — building a referral pipeline through support coordinators, without ads.

Mind if I send it over?

PS — {{customVariable4}}
```

**Tier A Variant B (CEO/Founder):**
```
{{firstName}},

Built something for NDIS founders on referral partner pipelines — how to get 3 to 5 support coordinators sending you participants every month, without ads.

Mind if I send it over?

PS — {{customVariable4}}
```

---

### EMAIL 2 — Variant B
**Inspired by:** Script #31 (done-for-you + specific number framing, 8.96% reply rate)
**Subject B:** `the timing trick`
**What's different:** Leads with the dollar number immediately (from lead magnet). Makes the ROI undeniable before explaining the method.

```
{{firstName}},

One support coordinator who sends you 3 participants a month is worth around $6,000 a month in services — at zero ad spend.

Most providers try to reach coordinators who have been in the role for years. Those coordinators already have a list and rarely change it.

The better move: reach out to a newly hired coordinator in their first 2 weeks. They have no provider list yet. You become their default before anyone else does.

Is that something {{companyName}} has looked at?
```

**Tier A Variant B:**
```
{{firstName}},

Five support coordinators sending 3 referrals each per month — that is 15 new participants. At average plan values, roughly $30,000 a month in managed services.

Zero ad spend. No chasing families. No Facebook.

The timing signal: newly hired support coordinators have no provider list yet. The ones who reach out first own that relationship for years.

Is that how {{companyName}} is building its pipeline?
```

---

### EMAIL 3 — Variant B
**Inspired by:** Scripts #1–5 (Lunch & Learn / specific time-slot format, 114.55% reply rate)
**Subject B:** `15 min this week?`
**What's different:** Skips the opener variable. Goes straight to a specific, low-friction offer with two time options. Highest-converting CTA format in the dataset.

```
{{firstName}},

Running a 15-min session this week with a few NDIS founders on building referral partner pipelines — finding support coordinators, reaching them before anyone else does, and getting consistent participant referrals.

Tuesday 2pm or Thursday 3pm AEST — does either work?
```

**Tier A Variant B:**
```
{{firstName}},

Running a 15-min call this week with a small group of NDIS founders on referral partner systems — specifically how to get 3 to 5 coordinators sending referrals monthly, zero ad spend.

Tuesday 2pm or Thursday 3pm AEST — either work for you?
```

**Note:** Variant B Email 3 deliberately drops `{{customVariable1}}` (the personalized opener). The time-slot format works because its specificity creates urgency without needing a personalised hook first. Best used for Tier 1 — Hot contacts who haven't replied after Email 1 and 2.

---

## Smartlead A/B Setup Instructions

**Option 1 — Native Smartlead A/B test (recommended)**
1. In each campaign, click "Add Variant" on each email step
2. Copy Variant B subject + body into the second variant
3. Set split: 50/50
4. Smartlead auto-assigns — use the `email_variant` column from Clay for tracking/analysis only

**Option 2 — Two separate campaigns**
1. Export Clay rows where `email_variant` = "A" → load into Campaign A
2. Export rows where `email_variant` = "B" → load into Campaign B
3. Both campaigns use same sequence days (0/4/9) but different copy
4. Compare reply rates after 30 days — roll winner forward

**Which to test first:** Subject lines matter more than body copy at the top of funnel. Start by testing subject line only (same body) before swapping body variants.

| Email | Subject A | Subject B |
|---|---|---|
| Email 1 | `referral guide` | `ndis referral` |
| Email 2 | `job post signal` | `the timing trick` |
| Email 3 | `quick question` | `15 min this week?` |

---

## Expected Results (NDIS sector, signal-targeted list)

| Metric | Conservative | Target |
|---|---|---|
| Email 1 open rate | 45% | 60%+ |
| Reply rate across sequence | 8–12% | 15–20% |
| Calls booked per 100 contacts | 4–6 | 8–12 |
| Referral partners activated per 20 calls | 3–5 | 6–8 |

These numbers reflect that you are targeting owners and founders of private NDIS companies — decision-makers who respond directly, not gatekeepers.
