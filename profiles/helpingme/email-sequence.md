# Helpingme — 3-Email Referral Partner Sequence
# ColdIQ Framework | NDIS Provider Outreach
Generated: 2026-07-24

---

## Campaign Context

**From:** Helpingme (NDIS registered provider)
**To:** Decision-makers at other NDIS providers (CEOs, Founders, MDs, Directors)
**Goal:** Build a bidirectional referral partnership — they send you participants, you send them participants
**Positioning:** Peer-to-peer, not sales. One NDIS provider reaching out to another.
**Tone:** Direct, warm, no jargon, no NDIS-sector clichés

---

## Sequence Structure

| Email | ColdIQ Template | Value Type | Subject | Timing |
|---|---|---|---|---|
| Email 1 | Leverage Content | Lead Magnet | `referral guide` | Day 0 |
| Email 2 | Not Too Different Persona | Technique | `partner pipeline` | Day 4 |
| Email 3 | Ask Before Pitch | How We Help | `quick question` | Day 9 |

**Day 0 = Day they're added to Smartlead**
**No email on Day 1–3 (let Email 1 breathe)**
**No email on Day 5–8**
**Email 3 on Day 9 only if no reply to Email 1–2**

---

## EMAIL 1 — Lead Magnet
**ColdIQ Template: Leverage Content (Ethan Parker)**
**Subject:** `referral guide`
**Value:** Give something useful before asking for anything

```
{{firstName}},

Put together a short checklist on building NDIS referral partnerships that actually produce consistent participants — not just coffee meetings that go nowhere.

Covers 7 questions we ask before formalising any referral relationship, including how to set up a shared intake process so both sides actually follow through.

Can I send it over?

PS — {{customVariable4}}
```

**Variables:**
- `{{firstName}}` — from Clay `clean_first_name`
- `{{customVariable4}}` — the `headline_hook` from Claygent (e.g., "Your focus on high-intensity participants stands out — they're often the hardest to place quickly.")

**Word count:** 68 words — within 60–90 target
**CTA:** Soft reply-based ("Can I send it over?") — zero friction
**PS:** Personalised signal that shows you researched them specifically

---

**TIER A VARIANT (CEO/Founder — Tier A contacts):**

```
{{firstName}},

Put together a short resource on what separates NDIS providers with stable, consistent participant flow from those constantly chasing referrals.

The short version: it's not more networking events. It's 3–5 formalised partner relationships with a proper intake process.

Can I send it over?

PS — {{customVariable4}}
```

**Why different:** CEOs/Founders think strategically — lead with the business outcome, not the tactical checklist.

---

## EMAIL 2 — Technique
**ColdIQ Template: Not Too Different Persona (Will Allred)**
**Subject:** `partner pipeline`
**Value:** Share a specific technique — peer insight, not a pitch

```
{{firstName}},

Most NDIS providers I speak to in {{customVariable5}} have the same issue — referral partners who agree to everything over coffee, then send one participant in six months.

The ones with consistent participant flow do one thing differently: they formalise it. A shared intake form, a dedicated contact person, and a monthly check-in.

Not a CRM. Not a lengthy MOU. Just structure.

Is that something you've tried at {{companyName}}?
```

**Variables:**
- `{{customVariable5}}` — `state` (e.g., "QLD", "NSW")
- `{{companyName}}` — company name

**Word count:** 83 words
**CTA:** Open question — invites a genuine reply, not a yes/no
**Why it works:** Validates their pain ("most providers I speak to"), delivers a specific insight, asks if they've tried it — not pushy, genuinely curious

---

**TIER A VARIANT (CEO/Founder):**

```
{{firstName}},

Most NDIS founders I speak to have built their referral network the same way — one relationship at a time, no structure, hoping partners remember to send someone.

Works early on. Doesn't scale past 20 participants.

The ones who've solved it treat referral partnerships like B2B accounts — intake process, contact, quarterly review. Same participant, more consistent.

Is that the kind of approach you've been thinking about?
```

---

## EMAIL 3 — How We Help
**ColdIQ Template: Ask Before Pitch (Will Allred)**
**Subject:** `quick question`
**Value:** Be specific about how Helpingme fits into their referral network — no vague "let's connect"

```
{{firstName}},

{{customVariable1}}

Quick question — when you have a participant who needs [HELPINGME_SERVICE] and your team is at capacity, where do they end up?

We work with providers across {{customVariable5}} in a simple referral track: participants who need [HELPINGME_SERVICE] come to us, and when we have someone needing {{customVariable2}}, we refer straight back to providers like {{companyName}}.

Worth 15 minutes to see if the setup makes sense?
```

**Variables:**
- `{{customVariable1}}` — `personalized_opener` from Clay GPT-4 Mini
- `{{customVariable5}}` — `state`
- `{{customVariable2}}` — `service_type_raw` (their services)
- `[HELPINGME_SERVICE]` — **fill in what Helpingme specifically provides** (e.g., "Support Coordination", "Community Participation", "SIL")

**Word count:** 88 words
**CTA:** "Worth 15 minutes" — specific, low commitment, reply-based
**Why it works:** Opens with a question about their real operational problem (capacity overflow), then shows exactly how Helpingme fits — bilateral, not one-sided

---

**TIER A VARIANT (CEO/Founder):**

```
{{firstName}},

{{customVariable1}}

At your scale, I'd guess participants occasionally fall through the gap between providers — not because you can't place them, but because the referral relationship isn't formal enough to guarantee a spot.

We've built that kind of structured relationship with a few providers across {{customVariable5}} — and it works both ways.

Worth a 15-minute call to see if it makes sense for {{companyName}}?
```

---

## Personalisation Logic

### When to use the Strong Hook (verbatim from their headline):

Use when the `headline` contains:
- A phrase about collaboration ("Collaborating for a Stronger NDIS Community" — Vatsal at 9D Care)
- A partnership value ("Your Trusted Partner in Quality Support" — Ronald at Flonac)
- A clear niche ("Complex & High-Intensity NDIS Care")

**Strong Hook example for Vatsal Ashar (9D Care):**
> PS — Your headline says "Collaborating for a Stronger NDIS Community" — that's exactly the kind of approach we're looking for in a referral partner.

**Strong Hook example for Ronald at Flonac:**
> PS — Your focus on complex and high-intensity NDIS care stands out — those participants are often the hardest to place when your team is at capacity.

### When to use Lite Hook (theme only):

Use for all other rows where the headline doesn't have a quotable phrase.

**Lite Hook examples:**
> PS — Noticed {{companyName}} covers {{customVariable2}} in {{customVariable5}} — that's a service we get referral requests for regularly.

> PS — Sent this because providers focused on {{customVariable3}} often need complementary support partners the most.

---

## Smartlead Campaign Settings

**Campaign name:** `NDIS-REFERRAL-PARTNERS-AUS`

OR split into two campaigns if preferred:
- `NDIS-FOUNDER-AUS` — Tier A contacts (CEO, Founder)
- `NDIS-DIRECTOR-AUS` — Tier B contacts (MD, Director, Head of Ops)

**Settings:**
- Sending window: Mon–Fri, 8:00am–11:00am local time
- Timezone: Australia (set per lead based on `state`)
- Daily send cap: 20–30 per inbox during warm-up, up to 50 when warmed
- Stop on reply: Yes
- Track opens: No (hurts deliverability)
- Track clicks: No (hurts deliverability)

**Unsubscribe footer:** Required — include plain text unsubscribe link

---

## Subject Line Strategy

All subjects are 2-word lowercase — ColdIQ standard.

| Email | Subject | Why |
|---|---|---|
| Email 1 | `referral guide` | Describes the lead magnet — they know what they're getting |
| Email 2 | `partner pipeline` | Frames the topic — they understand it's about referral flow |
| Email 3 | `quick question` | Classic ColdIQ follow-up — low pressure, high open rate |

**A/B test Email 1 subjects:**
- `referral guide` vs `ndis partners` vs `partner checklist`
Run 50/50 on first 100 sends, keep winner.

---

## Expected Performance Benchmarks (NDIS sector, cold outreach)

| Metric | Target | Excellent |
|---|---|---|
| Email 1 open rate | 40–55% | 60%+ |
| Email 1 reply rate | 8–12% | 15%+ |
| Email 2 reply rate | 5–8% | 10%+ |
| Email 3 reply rate | 3–5% | 8%+ |
| Overall sequence reply rate | 12–18% | 20%+ |
| Meetings booked per 100 sends | 4–8 | 10+ |

**NDIS advantage:** This is a relationship-based sector. Decision-makers are owner-operators who respond personally. Reply rates will be higher than typical B2B cold outreach if the personalisation is genuine.

---

## What To Do With Replies

**"Yes, send it over" (Email 1 reply):**
→ Send the lead magnet immediately (see `lead-magnet.md`)
→ Follow up 48 hours later: "Hope that was useful — did anything stand out as relevant for {{companyName}}?"

**"Not right now / busy" reply:**
→ Mark as "Nurture" in Smartlead
→ Follow up in 30 days with one of the other two emails

**"Tell me more" or "let's chat":**
→ Send your Calendly link immediately
→ Meeting confirmed — remove from sequence

**No reply after Email 3:**
→ Move to LinkedIn: connection request + 1 DM only (see LinkedIn sequence below)

---

## LinkedIn Follow-Up (After Email 3, No Reply)

**Day 12 — Connection Request:**
*(No note — blank connection requests convert better)*

**Day 14 — First DM (after they accept):**
```
Hey {{firstName}}, thanks for connecting.

I reached out by email last week about building a referral partnership between providers — didn't want to assume you'd seen it.

Would it make sense to jump on a quick call?
```

**Day 21 — Final DM (if no reply):**
```
{{firstName}}, I'll leave it here — but if participant referral flow ever becomes a priority, feel free to reach out.

Happy to share what's been working for other providers in {{state}}.
```

No more contact after this. 5-touch total (3 email, 2 LinkedIn DM).
