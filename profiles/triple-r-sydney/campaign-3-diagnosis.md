# Triple R — Campaign 3 Diagnosis
# Why 2,958 emails produced 2 opportunities
Prepared by DGK Business Consultancy | Analysed: 2026-08-14

---

## Headline

This was not a targeting failure. It was a **quality-control failure stacked on an inverted value proposition**. Both are fixable without rebuilding the list.

---

## The real numbers

| Metric | Sydney | VIC | Combined |
|---|---|---|---|
| Leads | 543 | 643 | 1,186 |
| Emails sent | 1,297 | 1,661 | 2,958 |
| Reported open rate | 62.5% | 74.5% | 67.7% |
| **Clicks** | **0** | **0** | **0** |
| Bounces | 35 | 21 | 56 (1.9%) |
| Logged replies | 9 | 5 | 14 |

### The 14 replies, decoded

| Category | Count | Note |
|---|---|---|
| Out-of-office / maternity leave / left company | 9 | Not replies — auto-responders |
| "Remove me from your contacts" | 1 | Opt-out |
| Polite rejection | 2 | One misread us as a recruitment agency |
| **Genuine interest** | **2** | Oriana Cerven (Abled Care), Trent Brook (I-HDS) |

**True opportunity rate: 2 / 2,958 = 0.07%.**

### Two metrics were lying to you

1. **Open rates of 62–75% are not real.** Genuine cold-email opens run 30–50%. Rates this high indicate corporate security scanners and Apple Mail Privacy Protection auto-opening messages. Open rate was never a signal of health here.

2. **Zero clicks across 2,958 emails is not a low click-through rate — it means there was nothing to click.** No link, no asset, no calendar. The only CTA was "reply the word yes."

---

## Fault 1 — Broken copy shipped at scale

Measured across every email body actually sent:

| Defect | Volume | Share |
|---|---|---|
| `Hi [First Name],` — merge tag never rendered | 149 | 100% of C3 Cold Sydney Email 2 |
| Double-name greeting ("Hi Bea," then "Bea, curious…") | 791 | 26.7% of all sends |
| Singular job title ("We work with Support Coordinator who need…") | 1,328 | 44.9% of all sends |
| VIC emails referencing NSW or a Sydney (02) number | 613 | 36.9% of VIC sends |

### The headless personalisation sentence

The tenure hook was generated as a sentence fragment with no grammatical subject:

> "Just joined the role at Abled Care Services — already juggling aged-care referrals while working out which providers genuinely deliver."

With no "You" at the front, the implied subject is **the sender**. It reads as *I* just joined their company.

**This is not theoretical.** Oriana Cerven replied specifically to ask about it:

> "I just wanted to clarify your email, as it mentions you've joined Abled Care Services, but your signature is for Triple R Community Care."

She was one of only two genuinely interested prospects in the entire campaign — she asked for nursing services, service areas and current capacity. The copy bug forced her to spend her reply on clarification instead of the offer.

---

## Fault 2 — The value proposition was inverted

The core line across all three campaigns:

> "At Triple R we take those participants off your plate."

**A Support Coordinator's participants are their business.** "Off your plate" reads as losing billable clients. The email asked them to give up revenue and framed it as a favour.

Christopher Mouawad read the full sequence and still had to ask:

> "Could you please explain further? Are you referring clients to me or am I sending my new clients to you for the onboarding process?"

The direction of value was genuinely unclear to the reader.

**The actual model:** the coordinator refers, keeps coordinating, and keeps billing. Triple R delivers only the clinical nursing. That is a materially better offer than what was sent — and it was never stated.

---

## Fault 3 — C1 Hiring Signal read as a recruitment agency

> "Saw EML Group is hiring a Case Manager — usually means higher caseloads…"

Cassandra Elsamad's reply:

> "We are currently handling all of our hiring internally and are not looking to partner with external recruitment agencies at this time."

The hiring signal was used **literally**, in the opening line. Signals should drive *selection and timing*, never become the subject of the email. C1 was the worst performer of the three: 0.4% Sydney, **0.0%** VIC.

---

## Fault 4 — Two sender identities on one campaign

The signature reads **Kalpana Sharma**. Four replies open with **"Hi Rajesh."** Recipients received mail from one name and replied to another. Combined with the "you've joined Abled Care" bug, the sender's identity was incoherent.

---

## Fault 5 — List quality

- **Wrong ICP present:** Georgia Shaw (`georgia.shaw@dpie.nsw.gov.au`) is a solicitor at the NSW Department of Planning, Industry & Environment — not an NDIS coordinator.
- **Bounces cluster on guessed patterns at large orgs:** Life Without Barriers ×4, St Vincent de Paul ×2, Wesley Mission, Anglicare, The Benevolent Society. These read as pattern-generated addresses rather than verified ones.
- 1.9% bounce rate is just under the 2% danger threshold — close enough to threaten domain reputation if repeated.

---

## What this cost

Both genuine opportunities arrived **in spite of** the copy, not because of it:

- **Oriana Cerven** — spent her reply asking who you were
- **Trent Brook (I-HDS)** — asked for a call directly

With clean copy and a clear offer, a list of 1,186 correctly-targeted NDIS coordinators should produce **8–12% reply rates**, not 0.07%. The list is not the problem.

---

## Fix priority

| # | Fix | Effort | Impact |
|---|---|---|---|
| 1 | Rewrite value prop: "you keep the participant and the billing" | Low | **Highest** |
| 2 | Add QA gate in Clay that blocks any row with a broken merge field | Low | **Highest** |
| 3 | Region-correct all VIC copy (Victoria references, VIC phone) | Low | High |
| 4 | Single sender identity across all sequences | Low | High |
| 5 | Add one clickable asset (referral pathway one-pager) | Medium | High |
| 6 | Rewrite C1 so the hiring signal never appears in the copy | Low | Medium |
| 7 | Re-verify emails; drop pattern-guessed addresses at large orgs | Medium | Medium |

See `email-sequence-v2.md` for the rebuilt copy and `clay-qa-layer.md` for the QA gate.
