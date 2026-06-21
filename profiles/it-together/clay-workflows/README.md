# Clay Workflows — IT Together
Generated: 2026-06-21

## Overview

Nine signal-based workflows covering all triggers from campaign-strategy.md.
Designed for **Clay Starter plan** (~1,000–2,000 credits/month).

## Credit Management (Starter Plan)

**Rule: Filter first, enrich later. Never run Claygent on a raw list.**

| Enrichment Type | Credit Cost |
|---|---|
| Standard field lookup (Apollo, LinkedIn basic) | 1 credit |
| Email waterfall (Prospeo → Hunter → Apollo) | 2–4 credits |
| BuiltWith / tech stack detection | 1–2 credits |
| Claygent AI research (website scrape, review scan) | 5–15 credits |
| LinkedIn post/activity scan | 3–8 credits |

**Monthly credit allocation (Starter ~1,500 credits/month):**

| Workflow | Priority | Est. Credits/Month |
|---|---|---|
| WF01 SEEK IT Hiring Signal | High | 300 |
| WF02 No IT Provider on Website | High | 250 |
| WF03 M365 Detected | High | 200 |
| WF04 New CEO / Ops Manager | Medium | 150 |
| WF05 Fast Growth (Multiple SEEK Roles) | Medium | 150 |
| WF06 Negative Google Reviews | Medium | 150 |
| WF07 New Office / Relocation | Low | 100 |
| WF08 Cybersecurity Incident News | Low | 100 |
| WF09 Education / AusTender | Low | 100 |
| **Total** | | **~1,500** |

## Output Routing

| Confidence | Output |
|---|---|
| High (2+ signals confirmed) | Auto-push → Smartlead |
| Single signal | CSV export → manual review → Smartlead |

## Workflow Index

| # | File | Signal | Campaign | Output |
|---|---|---|---|---|
| 1 | `01-seek-it-hiring.md` | SEEK job posting for IT role | Campaign #2 | Auto-push |
| 2 | `02-no-it-provider.md` | No MSP/IT company on website | Campaign #4 | Auto-push |
| 3 | `03-m365-detected.md` | M365/Azure on website (BuiltWith) | Campaign #6 | Auto-push |
| 4 | `04-new-leader.md` | New CEO/Ops/Practice Manager <90 days | Campaign #9 | Auto-push |
| 5 | `05-fast-growth.md` | 3+ SEEK job postings in 30 days | Campaign #8 | Auto-push |
| 6 | `06-google-review-pain.md` | Google reviews mentioning tech issues | Campaign #10 | Manual review |
| 7 | `07-new-office.md` | New office opened or relocated | Campaign #11 | Auto-push |
| 8 | `08-cyber-incident-news.md` | Cybersecurity incident in industry news | Campaign #7 | Manual review |
| 9 | `09-education-austender.md` | School/college IT tender on AusTender | Campaign #13 | Manual review |
