# Campaign Plan — IT Together
Generated: 2026-06-21

---

## Business
Australian managed IT services provider (MSP) offering managed support, cybersecurity, cloud, and print solutions to SMBs and education — without the cost of a full-time hire.
Website: https://ittogether.com.au/

---

## ICP
- **Titles:** Business Owner, Director, CEO, Ops/Office/Practice Manager, IT Manager, IT Coordinator, School Principal, School Business Manager
- **Industries:** All industries + Education (schools, colleges, TAFEs)
- **Headcount:** 5–100 employees
- **Geography:** Greater Sydney (primary), Australia-wide (secondary)
- **Hard filters:**
  - No existing MSP/IT provider on website
  - Not enterprise (100+ with dedicated IT dept)
  - Not government agency (AusTender track separate)
  - Not competitor MSP
- **Excluded:** Competitor IT companies, businesses with confirmed managed IT partner

---

## Offer & Lead Magnets

| Campaign Trigger | Lead Magnet (Email #1) | Follow-up CTA (Email #2–3) |
|---|---|---|
| SEEK IT hiring signal | Hiring vs MSP Cost Calculator | Free 30-min IT Strategy Session |
| No IT provider on website | Free IT Health Check | Free 30-min IT Strategy Session |
| Cybersecurity / breach signal | Dark Web / Cyber Risk Scan | Free IT Health Check |
| M365 detected | Free IT Health Check (M365 angle) | Free 30-min IT Strategy Session |
| Operations Manager persona | IT Downtime Cost Calculator | Free 30-min IT Strategy Session |
| Education / schools | Free IT Health Check (formal) | Free 30-min IT Strategy Session |

---

## Top 3 Recommended Campaigns

**1. SEEK Hiring Signal** — Real-time trigger, highest intent
> Companies actively posting IT support roles on SEEK have already decided they need help — they just picked the expensive path (hiring). Intercept them with the cost comparison before they commit to a salary. Easy to automate weekly via SEEK scrape.
> Full details: campaign-strategy.md → Campaign #2

**2. No IT Provider on Website** — Broad, scalable, clear gap
> Businesses with no MSP listed are unmanaged and one incident away from serious pain. Website scrape via Claygent confirms the gap. Works across all industries. Pair with IT Health Check as the lead magnet.
> Full details: campaign-strategy.md → Campaign #4

**3. M365 Detected** — High personalisation, low competition
> BuiltWith detects M365 on their website. Almost every M365 SMB has misconfigured security settings. Email opens with a specific M365 risk angle — feels like genuine research, not a template. Extremely high open and reply rates.
> Full details: campaign-strategy.md → Campaign #6

Full strategy (25 campaigns) in: `profiles/it-together/campaign-strategy.md`

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

1. Build list → `/prospeo-full-export` (business owners + ops managers, 5–100, AU)
2. Layer signals → Clay workflows (see `clay-workflows/`)
3. Write copy → `/campaign-copywriting` (start with Campaign #2 — SEEK Hiring Signal)
4. Upload + launch → `/smartlead-campaign-upload-public`

---

*Files in this profile:*
- `client-profile.yaml` — ICP, offer, legal guardrails
- `lead-magnets.md` — scored lead magnet options + campaign mapping
- `campaign-strategy.md` — 25 campaign ideas with AI strategies
- `campaign-plan.md` — this file
- `clay-workflows/` — signal detection workflows for Clay
