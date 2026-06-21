# Clay Workflows — Laxmi Home Loans
Generated: 2026-06-21

## Overview

Nine signal-based workflows covering every Tier 1–2 signal from campaign-strategy.md.
Designed for **Clay Starter plan** (~1,000–2,000 credits/month).

## Credit Management Strategy (Starter Plan)

**Golden rule: Filter first, enrich later.**
Never run Claygent on a raw list. Always apply cheap boolean filters first to reduce the list,
then run expensive enrichments only on leads that pass.

| Enrichment Type | Credit Cost | Use When |
|---|---|---|
| Standard field lookup (Apollo, LinkedIn basic) | 1 credit | First enrichment step always |
| Email waterfall (Prospeo → Hunter → Apollo) | 2–4 credits | After company/title confirmed |
| Claygent AI research (website scrape, review scan) | 5–15 credits | Last step, on filtered list only |
| LinkedIn post scan | 3–8 credits | After person confirmed |

**Recommended monthly credit allocation (Starter ~1,500 credits/month):**

| Workflow | Priority | Est. Credits/Month |
|---|---|---|
| No Broker Partner Gap | High | 300 |
| SEEK Hiring Signal | High | 200 |
| SMSF Accountants | High | 200 |
| New ABN | Medium | 150 |
| New Principal | Medium | 150 |
| Facebook Ads Running | Medium | 150 |
| LinkedIn Property Posts | Low | 100 |
| Nepali Business Detection | Low | 100 |
| Google Review Sentiment | Low | 150 |
| **Total** | | **~1,500** |

## Output Routing

| Signal Confidence | Output |
|---|---|
| High confidence (2+ signals confirmed) | Auto-push → Smartlead via webhook |
| Single signal, needs review | Export → CSV → manual review → Smartlead upload |

## Workflow Index

| # | Workflow File | Signal | Campaign | Output |
|---|---|---|---|---|
| 1 | `01-no-broker-gap.md` | No broker partner on website | Campaign #4 | Auto-push |
| 2 | `02-seek-hiring-signal.md` | SEEK job posting for sales agent | Campaign #7 | Auto-push |
| 3 | `03-smsf-accountants.md` | SMSF language on accountant website | Campaign #10 | Auto-push |
| 4 | `04-new-abn.md` | ABN registered <12 months | Campaign #6 | Auto-push |
| 5 | `05-new-principal.md` | Principal/Director job change <90 days | Campaign #8 | Auto-push |
| 6 | `06-facebook-ads-agents.md` | Agent running Facebook/Instagram ads | Campaign #9 | Manual review |
| 7 | `07-linkedin-property-posts.md` | Accountant posting property content on LinkedIn | Campaign #11 | Manual review |
| 8 | `08-nepali-business-detection.md` | Nepali-owned agency or firm | Campaign #16 | Manual review |
| 9 | `09-google-review-sentiment.md` | Google reviews mentioning settlement delays | Campaign #23 | Manual review |
