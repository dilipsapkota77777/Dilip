# Campaign Plan — DGK Business Consultancy
Generated: 2026-06-16

---

## Business
Done-With-You B2B growth systems — CRM, outbound, content, and LinkedIn Ads built and handed over in 12 weeks. Client owns everything at the end, no agency dependency.
Website: https://dgkbusinessconsultancy-com-au.lovable.app/
Based in Darwin, Australia. National reach. 20+ clients across 7 industries in 10 months.

---

## ICP
- **Titles:** CEO, Founder, Managing Director, Operations Manager, Head of Marketing
- **Industries:** IT/MSP, Accounting, NDIS, Legal, Financial Planning, Construction, Recruitment
- **Headcount:** 3–59 employees
- **Revenue:** $200k–$10M AUD
- **Geography:** Australia only (hard filter)
- **Hard excludes:** B2C, solopreneurs, enterprise (60+ staff)

---

## Offer & Lead Magnet
- **Primary CTA:** "Worth a free 30-min pipeline audit?"
- **Free hook:** Pipeline Audit Call — Dilip diagnoses their pipeline live, gives 3 immediate actions, no pitch required
- **Delivery:** Calendly link, 30 min Zoom
- **Backup hook:** Outbound Readiness Scorecard (Typeform → PDF report, no calendar needed)

---

## Top 3 Recommended Campaigns

1. **SEEK Hiring Signal — Marketing Manager** — Targeting Aus B2B companies actively hiring a Marketing Manager on SEEK. Personalization: "biggest risk is they arrive and there's no system." Highest intent signal available. Start here.

2. **IT/MSP Referral Ceiling** — Targeting IT/MSP CEOs, 5–30 staff. Proven result: 0→6 enquiries in 60 days. Strong, named pain point. Build on Prospeo with title + industry filters.

3. **Darwin/NT Local** — Small list, hyper-relevant. Only Darwin-based consultancy with this offering. Easiest replies. Run for local credibility and fast wins.

Full 25-idea strategy in: `profiles/dgk-business-consultancy/campaign-strategy.md`

---

## Infrastructure Readiness
- [x] SMARTLEAD_API_KEY in .env
- [x] PROSPEO_API_KEY in .env
- [x] MILLIONVERIFIER_API_KEY in .env
- [x] Domains purchased
- [x] Inboxes warmed 2+ weeks

**Status: Ready to launch.**

---

## Next Steps (in order)

1. **Build your list** → Run `/prospeo-full-export` for Campaign #2 (IT/MSP, title-first)
2. **Score the list** → Run `/list-quality-scorecard` before uploading anything
3. **Write the copy** → Run `/campaign-copywriting` with this plan as input
4. **Check for spam words** → Run `/spam-word-checker` on the final copy
5. **Upload to Smartlead** → Run `/smartlead-campaign-upload-public`
6. **Once live** → Use `/cold-email-weekly-rhythm` as your weekly operating cadence
7. **Measure replies** → Run `/positive-reply-scoring` after first 100 sends

For Campaign #1 (SEEK signal), the list-building is manual — monitor SEEK for "Marketing Manager" postings from Australian B2B companies in your ICP industries, collect company domains, then run `/blitz-list-builder` to find the CEO/Founder contact.
