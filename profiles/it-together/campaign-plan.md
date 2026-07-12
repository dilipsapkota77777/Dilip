# Campaign Plan — IT Together
Generated: 2026-06-16

---

## Business
AI-driven Managed Services Provider — networking, cybersecurity, IT support, cloud (AWS), and AI/agentic operations under one provider. Proactive 24/7 monitoring, not break/fix.
Website: https://ittogether.com.au/
Based in Parramatta NSW. ~43 employees. National reach.

---

## ICP
- **Titles:** CEO, Managing Director, Operations Manager, CFO, IT Manager, Head of Technology
- **Industries:** Professional services (legal, accounting, financial planning), healthcare, construction, recruitment, education/RTO, manufacturing
- **Headcount:** 10–200 employees
- **Revenue:** $1M–$50M AUD
- **Geography:** Australia only (hard filter)
- **Hard excludes:** Micro-businesses under 10 staff, businesses with large in-house IT teams, government

---

## Offer & Lead Magnet
- **Primary CTA:** "Worth a free 45-min network and security assessment?"
- **Free hook:** Network & Security Assessment — live review of their IT environment, 1-page findings + 3 prioritised actions
- **Delivery:** Remote screen share, 45 min, Calendly
- **Backup hook:** Free Cybersecurity Risk Report (automated external scan, zero calendar friction — use for high-volume sequences)
- **AI angle hook:** Free AI-Ready IT Scorecard (Typeform → PDF) — use for Copilot/AI campaigns

---

## Top 3 Recommended Campaigns

1. **SEEK Signal — IT Manager Hire** — Targeting Australian SMBs actively advertising for an IT Manager or Sysadmin on SEEK. Personalization: MSP as cheaper and faster alternative to a full-time hire. Highest intent signal available. Start here.

2. **Legal Firms Cybersecurity** — Targeting boutique law firms 10–50 staff. Free Cybersecurity Risk Report as automated lead magnet. Easy Prospeo list (title: Managing Partner, industry: Legal). Strong, compliance-driven pain.

3. **AI Readiness / Microsoft Copilot** — Targeting M365 SMBs trying to adopt Copilot and AI tools. Uses IT Together's unique AI differentiator. No other MSP is running this angle. Free AI-Ready IT Scorecard as lead magnet.

Full 25-idea strategy in: `profiles/it-together/campaign-strategy.md`

---

## Infrastructure Readiness
- [x] Domains purchased
- [x] Inboxes warmed 2+ weeks
- [x] SMARTLEAD_API_KEY in .env
- [x] PROSPEO_API_KEY in .env
- [x] MILLIONVERIFIER_API_KEY in .env

**Status: Ready to launch.**

---

## Key Gaps to Fix Before Launch
1. **No case studies** — sequences will lean on pain/fear openers rather than proof points. Priority: get even one anonymised client result (e.g. "reduced IT incidents by 70% for a 30-person law firm") to use in follow-up email #2.
2. **No lead magnet page** — need a Calendly link for the assessment, and ideally a landing page for the Cybersecurity Risk Report. Can use a simple Typeform in the short term.

---

## Next Steps (in order)

1. **Build IT Manager SEEK list** → Monitor SEEK daily for IT Manager/Sysadmin ads from Australian SMBs → collect company domains → run `/blitz-list-builder` to find CEO/MD contacts
2. **Build legal firms list** → Run `/prospeo-full-export` (Title: Managing Partner, Industry: Legal, Country: AU, Headcount: 10–50)
3. **Score both lists** → Run `/list-quality-scorecard`
4. **Write the copy** → Run `/campaign-copywriting` — start with Campaign #1 (SEEK signal)
5. **Spam check** → Run `/spam-word-checker`
6. **Upload** → Run `/smartlead-campaign-upload-public`
7. **Weekly rhythm** → Run `/cold-email-weekly-rhythm` once live
8. **Score replies** → Run `/positive-reply-scoring` after first 100 sends
