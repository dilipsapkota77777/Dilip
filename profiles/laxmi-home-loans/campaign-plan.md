# Campaign Plan — Laxmi Home Loans
Generated: 2026-06-21

---

## Business
Australian mortgage brokerage offering home loans, investment loans, and SMSF/LRBA finance across 40+ lenders — with bilingual English/Nepali service.
Website: https://www.mortgagepros.com.au/

---

## ICP
- **Titles:** Real Estate Agent, Sales Agent, Buyer's Agent, Buyer's Advocate, Principal, Director, Accountant, Tax Agent, CPA, Financial Planner, Financial Adviser
- **Industries:** Real Estate, Accounting, Financial Services
- **Headcount:** 1–50 employees
- **Geography:** Australia (all states — priority: NSW, VIC, QLD)
- **Campaign mode:** B2B referral partnerships (not direct to consumer)
- **Hard filters:**
  - Must be Australian business
  - Must be independent (not franchise HQ)
  - Must be in Real Estate, Accounting, or Financial Services
- **Excluded:**
  - Big 4 banks (ANZ, CBA, NAB, Westpac)
  - Competitor mortgage brokers (Mortgage Pros, Shore Financial, Everest Home Loans)
  - Franchise real estate HQs (Ray White, LJ Hooker — individual offices fine)
  - Insurance companies

---

## Offer & Lead Magnets

| Track | Audience | Lead Magnet (Opener) | CTA |
|---|---|---|---|
| A | Real Estate Agents | Free 24-hour buyer pre-qualification | "Send me your next buyer's basic details — I'll tell you if they can get finance within 24 hours." |
| B | Accountants / Financial Planners | SMSF Property Loan Explainer (PDF) | "Reply and I'll send our SMSF lending explainer — covers what SMSF clients can borrow for and the 3 LRBA mistakes that get loans declined." |
| Fallback | All referral partners | Broker Referral 1-Pager | "Reply and I'll send our broker overview — lender panel, turnaround times, one page, 60 seconds to read." |
| Follow-up #2 | All | Book 15-min intro call | "Worth a 15-min call to see if there's a fit?" |

**Primary CTA (email #1):** Send the asset
**Follow-up CTA (email #2–3):** Book a 15-min call

---

## Top 3 Recommended Campaigns (from campaign-strategy.md)

**1. No Broker Partner Gap** — Broad targeting, automated via website scrape
> Target agents and accountants with no mortgage broker partner mentioned on their website. Clear gap, easy to automate with Clay/Claygent. Best first campaign because it requires zero trigger monitoring — just a website crawl.
> Full details: campaign-strategy.md → Campaign #4

**2. SMSF Accountants** — Focused targeting, high ACV per referral
> Accountants whose website mentions SMSF services. LRBA lending is a specialist area that very few brokers handle — Laxmi's expertise here is a genuine differentiator. Lead magnet (SMSF Explainer) is easy to produce and directly solves a pain point accountants face weekly.
> Full details: campaign-strategy.md → Campaign #10

**3. SEEK Hiring Signal — Growing Agencies** — Focused, real-time trigger
> Agencies actively hiring sales agents on SEEK have a growing buyer pipeline and need broker capacity now. Easy to automate via SEEK job posting scrape. Timing is perfect — they're investing in growth and haven't locked in all their partner relationships.
> Full details: campaign-strategy.md → Campaign #7

Full strategy (25 campaigns) in: `profiles/laxmi-home-loans/campaign-strategy.md`

---

## Infrastructure Readiness

- [x] SMARTLEAD_API_KEY in .env: **yes**
- [x] PROSPEO_API_KEY in .env: **yes**
- [x] MILLIONVERIFIER_API_KEY in .env: **yes**
- [x] Domains purchased: **yes**
- [x] Inboxes warmed 2+ weeks: **yes**

**Status: READY TO LAUNCH**

---

## Next Steps

Infrastructure is fully ready. Your next step is building the list.

Based on your ICP (real estate agents + accountants, 1–50 staff, Australia-wide), choose your list-building method below.

**Recommended path:**
1. Build list → `/prospeo-full-export` (title-first search for agents + accountants in AU)
2. Enrich + verify → MillionVerifier via the enrichment waterfall
3. Write copy → `/campaign-copywriting` (start with Campaign #4 — No Broker Partner Gap)
4. Upload + launch → `/smartlead-campaign-upload-public`

---

*Files in this profile:*
- `client-profile.yaml` — ICP, offer, legal guardrails
- `lead-magnets.md` — scored lead magnet options + top picks
- `campaign-strategy.md` — 25 campaign ideas with AI strategies, targeting, overviews
- `campaign-plan.md` — this file
