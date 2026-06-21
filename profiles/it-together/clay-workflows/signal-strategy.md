# Signal Strategy — IT Together
Generated: 2026-06-21

## Signal Map

```
┌──────────────────────────────────────────────────────────────────────┐
│                    IT TOGETHER SIGNAL SYSTEM                         │
├───────────────────────────────┬──────────────────────────────────────┤
│   REAL-TIME TRIGGERS          │   ENRICHMENT-BASED SIGNALS           │
│   (run weekly)                │   (run on Prospeo base list)         │
├───────────────────────────────┼──────────────────────────────────────┤
│                               │                                      │
│  WF01 SEEK IT Hiring ─────────▶ Campaign #2 (auto-push)             │
│  "They want to hire IT"       │ Lead magnet: Hiring vs MSP Calc      │
│                               │                                      │
│  WF05 Fast Growth ────────────▶ Campaign #8 (auto-push)             │
│  "3+ SEEK roles in 30 days"   │ Lead magnet: IT Health Check         │
│                               │                                      │
│  WF04 New Leader ─────────────▶ Campaign #9 (auto-push)             │
│  "New CEO/Ops <90 days"       │ Lead magnet: IT Health Check         │
│                               │                                      │
│  WF07 New Office ─────────────▶ Campaign #11 (auto-push)            │
│  "Opened/moved location"      │ Lead magnet: IT Health Check         │
│                               │                                      │
│  WF08 Cyber News ─────────────▶ Campaign #7 (manual, 48hr SLA)      │
│  "Industry breach in news"    │ Lead magnet: Dark Web Scan           │
│                               │                                      │
├───────────────────────────────┼──────────────────────────────────────┤
│                               │                                      │
│                               │  WF02 No IT Provider ───────────────▶│
│                               │  Campaign #4 (auto-push)             │
│                               │  Lead magnet: IT Health Check        │
│                               │                                      │
│                               │  WF03 M365 Detected ────────────────▶│
│                               │  Campaign #6 (auto-push)             │
│                               │  Lead magnet: M365 Security Check    │
│                               │                                      │
│                               │  WF06 Google Review Pain ───────────▶│
│                               │  Campaign #10 (manual review)        │
│                               │  Lead magnet: IT Health Check        │
│                               │                                      │
├───────────────────────────────┴──────────────────────────────────────┤
│                  EDUCATION TRACK (separate cadence)                  │
├─────────────────────────────────────────────────────────────────────┤
│  WF09 Education / AusTender ─────────────────────────────────────── │
│  Track A: Active tenders → formal email (manual, 14-day SLA)        │
│  Track B: Schools cold outreach → formal email (manual review)      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Double-Signal Routing (Priority Escalation)

| Signal 1 | Signal 2 | Combined | Routing |
|---|---|---|---|
| SEEK IT Hiring (WF01) | No IT Provider (WF02) | Very High | Auto-push, Day 1, priority sequence |
| SEEK IT Hiring (WF01) | Fast Growth (WF05) | Very High | Auto-push, Hiring vs MSP Calculator lead |
| M365 Detected (WF03) | No IT Provider (WF02) | Very High | Auto-push, M365 + Health Check combined |
| New Leader (WF04) | SEEK IT Hiring (WF01) | High | Auto-push, new leader + IT problem framing |
| Google Review Pain (WF06) | No IT Provider (WF02) | Very High | Manual review, highest personalisation |
| Cyber News (WF08) | No IT Provider (WF02) | Very High | Rush send, Dark Web Scan lead |
| Fast Growth (WF05) | New Office (WF07) | High | Auto-push, growth + infrastructure angle |

---

## Triple Signal (Highest Priority — Campaign #19)

**SEEK IT Hiring + M365 Detected + No IT Provider = Maximum urgency**

Route to dedicated Smartlead campaign: `ITT — Triple Signal`

Email:
> "I noticed {{company_name}} is hiring a {{it_role}}, running Microsoft 365, and doesn't currently have a managed IT provider — that combination usually means IT is being handled informally by someone who has other priorities.
>
> Before you commit to a hire, it's worth seeing what managed IT costs vs in-house. I can send a cost comparison and free M365 security check today."

---

## Smartlead Campaign Mapping

| Workflow | Smartlead Campaign | Lead Magnet |
|---|---|---|
| WF01 SEEK IT Hiring | `ITT — SEEK IT Hiring` | Hiring vs MSP Calculator |
| WF02 No IT Provider | `ITT — No IT Provider Gap` | IT Health Check |
| WF03 M365 Detected | `ITT — M365 Security Check` | M365 Security Check |
| WF04 New Leader | `ITT — New Leader Welcome` | IT Health Check |
| WF05 Fast Growth | `ITT — Fast Growth` | IT Health Check |
| WF06 Google Reviews | `ITT — Tech Review Pain` | IT Health Check |
| WF07 New Office | `ITT — New Office` | IT Health Check |
| WF08 Cyber News | `ITT — Cyber Incident [Industry]` | Dark Web Scan |
| WF09 Education | `ITT — Education Outreach` | IT Health Check (formal) |
| Double Signal | `ITT — Double Signal Priority` | Best-fit magnet |
| Triple Signal | `ITT — Triple Signal` | Hiring vs MSP Calculator |

---

## Weekly Operating Rhythm

### Monday
- [ ] Run WF01 (SEEK IT Hiring) — new postings from last 7 days
- [ ] Run WF05 (Fast Growth) — companies with 3+ new SEEK postings
- [ ] Run WF08 (Cyber News) — check Google Alerts for weekend news

### Wednesday
- [ ] Run WF02 (No IT Provider) — 25 new leads from Prospeo export
- [ ] Run WF03 (M365 Detected) — 30 new leads from Prospeo export
- [ ] Run WF04 (New Leader) — check LinkedIn for new job changes

### Friday
- [ ] Manual review queue: WF06, WF07, WF08, WF09 leads
- [ ] Approve and upload to Smartlead
- [ ] Review Smartlead reply rates from prior week

### Monthly
- [ ] Run WF09 Education (Track B) — 15 new school leads
- [ ] Run WF06 (Google Reviews) — 15 high-review targets
- [ ] Credit audit: check Clay Starter balance, adjust batch sizes
- [ ] Update Master Exclusion Sheet with new clients + won deals

---

## Credit Budget (Starter ~1,500/month)

| Workflow | Leads/Month | Credits/Lead | Monthly Total |
|---|---|---|---|
| WF01 SEEK IT Hiring | 30 | 6–10 | 180–300 |
| WF02 No IT Provider | 25 | 14–22 | 350–550 |
| WF03 M365 Detected | 40 | 4–8 | 160–320 |
| WF04 New Leader | 20 | 5–9 | 100–180 |
| WF05 Fast Growth | 15 | 8–12 | 120–180 |
| WF06 Google Reviews | 15 | 12–19 | 180–285 |
| WF07 New Office | 10 | 7–12 | 70–120 |
| WF08 Cyber News | 20 | 0–6 | 0–120 |
| WF09 Education | 15 | 8–12 | 120–180 |
| **Total** | **190** | | **~1,280–2,235** |

**Starter plan recommendation:** Prioritise WF01 + WF03 + WF02 (highest ROI, most credit-efficient). Reduce WF06 + WF09 if credits are tight. Upgrade to Explorer/Growth when volume exceeds 150 leads/month.

---

## Deduplication System

Maintain a **Master Exclusion Google Sheet** with columns:
- `email`
- `company_domain`
- `date_contacted`
- `campaign_name`
- `status` (active / replied / bounced / unsubscribed / won / lost)

**Rules:**
- Same email → never contact again if active/replied/unsubscribed
- Same company domain → only one contact at a time (no overlapping sequences)
- Won client domains → add to permanent exclusion list

**Clay implementation:** HTTP lookup against Google Sheets webhook before every Smartlead push.

---

## Personalisation Variable Reference

| Variable | Source | Example |
|---|---|---|
| `{{first_name}}` | Prospeo | "Sarah" |
| `{{company_name}}` | Prospeo | "Harbour Legal" |
| `{{it_role}}` | WF01 SEEK | "IT Support Officer" |
| `{{job_suburb}}` | WF01 SEEK | "Parramatta" |
| `{{company_industry}}` | Prospeo / Claygent | "Legal" |
| `{{company_suburb}}` | Prospeo / Claygent | "North Sydney" |
| `{{previous_company}}` | WF04 LinkedIn | "PwC" |
| `{{days_in_role}}` | WF04 LinkedIn | "34" |
| `{{departments_hiring}}` | WF05 SEEK | "Sales, Finance, Admin" |
| `{{active_seek_postings_count}}` | WF05 SEEK | "5" |
| `{{new_location}}` | WF07 LinkedIn/Maps | "Chatswood" |
| `{{pain_theme}}` | WF06 Claygent | "system outages affecting service" |
| `{{pain_keyword}}` | WF06 Claygent | "system was down all morning" |
| `{{tender_title}}` | WF09 AusTender | "Managed IT Services RFT" |
| `{{tender_type}}` | WF09 AusTender | "Request for Tender" |
| `{{closing_date}}` | WF09 AusTender | "15 July 2026" |

---

## Compliance Checklist (Before Every Send)

- [ ] Working unsubscribe link in every email (Australian Spam Act 2003)
- [ ] No "guaranteed uptime" or unverifiable claims
- [ ] WF06 emails do not quote reviewer names or direct review text
- [ ] WF08 cyber news emails do not name the breach victim
- [ ] WF09 education emails use formal salutation (Dear, not Hey)
- [ ] No pricing claims in cold email body
- [ ] All data sourced from public sources only
