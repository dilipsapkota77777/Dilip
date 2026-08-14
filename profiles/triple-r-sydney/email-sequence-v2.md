# Triple R — Email Sequence v2
# Rebuilt after Campaign 3 diagnosis | Sydney + VIC
Generated: 2026-08-14

---

## What changed and why

| v1 (failed) | v2 (rebuilt) | Reason |
|---|---|---|
| "We take those participants off your plate" | "You keep the participant and your billable hours" | v1 asked coordinators to give up revenue |
| Hiring signal in the opening line | Signal used for selection only, never mentioned | v1 read as a recruitment agency |
| "We work with Support Coordinator who need" | "We work with support coordinators who…" | Singular title in 44.9% of sends |
| "Hi [First Name]," / double-name greeting | Single greeting, QA-gated | Merge tags shipped unrendered |
| "across NSW" sent to VIC | Region-matched copy + region-matched phone | 613 VIC emails cited NSW |
| Reply-only CTA, zero clickable asset | Referral pathway one-pager link | 0 clicks across 2,958 emails |
| Vague claims | 48-hour assessment, NDIS registered, RN-led only | Only proof points confirmed as real |

**Proof points permitted in copy (confirmed available):**
- Assessment within 48 hours; onboarding within one week
- NDIS registered; RN-led clinical governance

**Not permitted** (not yet verifiable): named client references, case studies, participant volumes, capacity claims, service-area guarantees.

---

## Core positioning

> **You stay the coordinator. We deliver the nursing you can't.**

The coordinator refers a participant with complex clinical needs. They remain the Support Coordinator, keep the participant on their caseload, and keep billing. Triple R delivers only the clinical nursing component.

This must appear explicitly in **every email**. It is the single fix that resolves the confusion in Christopher Mouawad's reply.

---

## Sequence structure

| Email | Angle | Day | CTA |
|---|---|---|---|
| Email 1 | The unplaceable participant | Day 0 | Soft — "worth a look?" |
| Email 2 | You keep the billing (reframe) | Day 4 | Direct — "reply and I'll tell you if we can take them" |
| Email 3 | Ask Before Pitch — genuine question | Day 9 | Question only, no pitch |

---

# SYDNEY

## Email 1 — The unplaceable participant
**Subject:** `the participant who sits`
**Alt subject (A/B):** `complex nursing referrals`

```
Hi {{firstName}},

When a participant on your caseload needs clinical nursing — wound care, PEG feeding, complex medication — how long does it take to find a provider who'll actually take them?

That's usually the referral that sits.

Triple R takes those. You stay the Support Coordinator, keep the participant, keep your billable hours. We deliver only the clinical nursing your organisation doesn't.

Assessed within 48 hours. NDIS registered, RN-led.

Worth seeing how the referral pathway works?

Kalpana Sharma
Triple R Community Care
(02) 8044 1775
```
**Words:** 84 ✅

---

## Email 2 — The reframe
**Subject:** RE: (same thread)

```
Hi {{firstName}},

Short one — the part most coordinators want clarified.

We don't take the participant off you. You keep coordinating, you keep billing. We handle the clinical nursing only.

Assessment within 48 hours, onboarded inside a week. NDIS registered, RN-led clinical governance.

If you have a participant sitting unplaced right now, reply with their support needs and I'll tell you today whether we can take them.

Kalpana Sharma
Triple R Community Care
(02) 8044 1775
```
**Words:** 78 ✅

---

## Email 3 — Ask Before Pitch
**Subject:** `quick question`

```
Hi {{firstName}},

Last one from me — a question rather than a pitch.

When you can't place a participant with complex nursing needs, what do you actually do? Hold them and keep looking, or send it back to the planner?

Asking because that specific gap is the only thing we do, and I'd rather know whether it's even a problem on your caseload.

If it isn't, no hard feelings.

Kalpana Sharma
Triple R Community Care
(02) 8044 1775
```
**Words:** 82 ✅

---

# VICTORIA

Identical structure. Every NSW/Sydney reference replaced. **Use the VIC phone number — do not send a (02) number to a Melbourne coordinator.**

## Email 1 — VIC
**Subject:** `the participant who sits`

```
Hi {{firstName}},

When a participant on your caseload needs clinical nursing — wound care, PEG feeding, complex medication — how long does it take to find a provider who'll actually take them?

That's usually the referral that sits.

Triple R takes those across Victoria. You stay the Support Coordinator, keep the participant, keep your billable hours. We deliver only the clinical nursing your organisation doesn't.

Assessed within 48 hours. NDIS registered, RN-led.

Worth seeing how the referral pathway works?

Kalpana Sharma
Triple R Community Care
{{vic_phone}}
```

## Email 2 — VIC
```
Hi {{firstName}},

Short one — the part most coordinators want clarified.

We don't take the participant off you. You keep coordinating, you keep billing. We handle the clinical nursing only.

Assessment within 48 hours, onboarded inside a week. NDIS registered, RN-led clinical governance.

If you have a participant sitting unplaced right now, reply with their support needs and I'll tell you today whether we can take them.

Kalpana Sharma
Triple R Community Care
{{vic_phone}}
```

## Email 3 — VIC
Same as Sydney Email 3, with `{{vic_phone}}` in the signature.

---

# C1 — Hiring Signal (rebuilt)

**The signal never appears in the copy.** It is used only to select who receives this sequence and when.

v1 opened with "Saw EML Group is hiring a Case Manager" and drew the reply *"we are not looking to partner with external recruitment agencies."*

## C1 Email 1 — rebuilt
**Subject:** `caseload growth`

```
Hi {{firstName}},

When a coordination team grows, the complex nursing participants are usually the ones that don't scale — they take three or four times longer to place than everything else.

Triple R takes those referrals. You stay the coordinator, keep the participant and the billing. We deliver the clinical nursing only.

Assessed within 48 hours. NDIS registered, RN-led.

Worth a look at the referral pathway?

Kalpana Sharma
Triple R Community Care
{{region_phone}}
```
**Words:** 76 ✅

The growth context is still there — but as an *observation about caseloads*, not an announcement that you've been watching their job ads.

---

## The clickable asset

Zero clicks across 2,958 emails because there was nothing to click. Add one:

**"Triple R Referral Pathway — one page"**

Contents (built only from confirmed proof points):
1. What we take — clinical nursing referrals (wound care, PEG, complex meds, post-acute)
2. What you keep — participant, coordination role, billing
3. Timeline — referral → assessment within 48 hours → onboarded within one week
4. Credentials — NDIS registration groups, RN-led clinical governance
5. How to refer — one contact point, what to send

Host it as a simple link. Track clicks — **click rate becomes your real engagement metric**, since open rate is unreliable at these inflated levels.

---

## Benchmarks for v2

| Metric | v1 actual | v2 target | Action if missed |
|---|---|---|---|
| Bounce rate | 1.9% | <1% | Re-verify; drop guessed addresses |
| Click rate | 0% | 3-6% | Asset or CTA is not compelling |
| Reply rate | 0.07% genuine | 6-10% | Re-test Email 1 hook |
| Positive reply share | 14% of replies | >40% | Tighten ICP filter |

**Do not resend to the 1,186 contacts for at least 30 days.** They received broken copy. Re-entering them immediately compounds the damage. Start v2 on fresh contacts, prove the numbers, then re-approach the original list with a genuinely different angle.
