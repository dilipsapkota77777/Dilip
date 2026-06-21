# Signal Strategy — Laxmi Home Loans
Generated: 2026-06-21

## Overview

This document defines how all nine Clay workflows connect into a unified signal-based outreach system.
Each workflow detects one or more buying signals and routes leads into the correct Smartlead campaign sequence.

---

## Signal Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    LAXMI HOME LOANS SIGNAL SYSTEM               │
├────────────────────────────────┬────────────────────────────────┤
│       TRACK A: AGENTS          │      TRACK B: ACCOUNTANTS      │
├────────────────────────────────┼────────────────────────────────┤
│                                │                                │
│  WF01 No Broker Partner ───────┼── WF03 SMSF Language           │
│       ↓ (auto-push)            │        ↓ (auto-push)           │
│  Campaign #4                   │   Campaign #10                 │
│                                │                                │
│  WF02 SEEK Hiring ─────────────┼── WF07 LinkedIn Post           │
│       ↓ (auto-push)            │        ↓ (manual review)       │
│  Campaign #7                   │   Campaign #11                 │
│                                │                                │
│  WF05 New Principal ───────────┼── WF05 New Principal           │
│       ↓ (auto-push)            │        ↓ (auto-push)           │
│  Campaign #8                   │   Campaign #2/3 (new hire)     │
│                                │                                │
│  WF06 Facebook Ads ────────────┤                                │
│       ↓ (manual review)        │                                │
│  Campaign #9                   │                                │
│                                │                                │
│  WF09 Google Reviews ──────────┼── WF09 Google Reviews          │
│       ↓ (manual review)        │        ↓ (manual review)       │
│  Campaign #23                  │   Campaign #23                 │
│                                │                                │
├────────────────────────────────┴────────────────────────────────┤
│              CROSS-TRACK SIGNALS (both audiences)               │
├─────────────────────────────────────────────────────────────────┤
│  WF04 New ABN ─────────────────────────────────────────────────▶│
│       ↓ (auto-push)    agents + accountants    Campaign #6      │
│                                                                 │
│  WF08 Nepali Detection ────────────────────────────────────────▶│
│       ↓ (manual review)  agents + accountants  Campaign #16     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Double-Signal Routing (Priority Escalation)

When a lead matches TWO or more signals simultaneously, they move to a higher-priority sequence.

| Signal 1 | Signal 2 | Combined Confidence | Routing |
|---|---|---|---|
| No Broker Partner (WF01) | SEEK Hiring (WF02) | Very High | Auto-push, priority sequence, Day 1 send |
| SMSF Language (WF03) | LinkedIn Property Post (WF07) | Very High | Auto-push, skip manual review |
| New Principal (WF05) | Facebook Ads (WF06) | High | Auto-push |
| New ABN (WF04) | No Broker (WF01) | Very High | Auto-push, first-mover sequence |
| Nepali Detection (WF08) | Any signal | High | Manual review with Nepali personalisation |
| Google Reviews Pain (WF09) | No Broker (WF01) | Very High | Manual review, highest-priority personalisation |

---

## Smartlead Campaign Mapping

| Workflow | Smartlead Campaign Name | Email Sequence |
|---|---|---|
| WF01 — No Broker Gap | `LHL — No Broker Partner (Agents)` | 3 emails: Gap observation → 1-pager offer → book call |
| WF02 — SEEK Hiring | `LHL — SEEK Hiring Signal` | 3 emails: Congrats on hiring → pre-qual offer → book call |
| WF03 — SMSF Accountants | `LHL — SMSF Accountants` | 3 emails: SMSF question → explainer offer → book call |
| WF04 — New ABN | `LHL — New Business Launch` | 3 emails: Congrats on launch → partner overview → book call |
| WF05 — New Principal | `LHL — New Principal Welcome` | 3 emails: Congrats on role → pre-qual offer → book call |
| WF06 — Facebook Ads | `LHL — Facebook Ads Agents` | 3 emails: Reference ad → conversion angle → book call |
| WF07 — LinkedIn Posts | `LHL — LinkedIn Property Posts (Accountants)` | 3 emails: Reference post → SMSF explainer → book call |
| WF08 — Nepali Detection | `LHL — Nepali Community Outreach` | 3 emails: Bilingual opener → service overview → book call |
| WF09 — Google Reviews | `LHL — Settlement Pain` | 3 emails: Reference pain pattern → 24hr pre-qual → book call |

---

## Weekly Operating Rhythm

### Monday — Trigger Workflows
- [ ] Run WF02 (SEEK Hiring) — check new job postings from last 7 days
- [ ] Run WF05 (New Principal) — check LinkedIn for new role changes

### Wednesday — Enrichment Batch
- [ ] Run WF01 (No Broker Gap) on 25 new leads from Prospeo export
- [ ] Run WF03 (SMSF Accountants) on 25 new leads from Prospeo export

### Friday — Review & Upload
- [ ] Manual review queue: WF06, WF07, WF08, WF09 leads from the week
- [ ] Approve and upload to Smartlead CSV
- [ ] Check Smartlead reply rates from previous week's sequences

### Monthly
- [ ] Run WF04 (New ABN) on latest ABN bulk extract
- [ ] Run WF08 (Nepali Detection) on 30–40 leads
- [ ] Run WF09 (Google Reviews) on 20 high-review-count targets
- [ ] Credit audit: check remaining Clay Starter credits and adjust batch sizes

---

## Credit Budget (Starter Plan ~1,500/month)

| Workflow | Leads/Month | Credits/Lead | Monthly Total |
|---|---|---|---|
| WF01 — No Broker Gap | 25 | 14–20 | 350–500 |
| WF02 — SEEK Hiring | 30 | 8–12 | 240–360 |
| WF03 — SMSF Accountants | 20 | 14–22 | 280–440 |
| WF04 — New ABN | 20 | 7–11 | 140–220 |
| WF05 — New Principal | 25 | 5–9 | 125–225 |
| WF06 — Facebook Ads | 15 | 10–15 | 150–225 |
| WF07 — LinkedIn Posts | 15 | 10–16 | 150–240 |
| WF08 — Nepali Detection | 10 | 9–14 | 90–140 |
| WF09 — Google Reviews | 10 | 12–19 | 120–190 |
| **Total** | **170** | | **1,645–2,540** |

**Note:** On Starter (~1,500 credits), you'll need to trim batch sizes. Recommended prioritisation:
1. Run WF01 + WF02 + WF03 at full volume (highest ROI)
2. Run WF04 + WF05 at half volume
3. Run WF06–WF09 only when credits allow (or upgrade to Explorer/Growth)

---

## Deduplication System

To avoid emailing the same person across multiple workflows, maintain a **Master Exclusion Sheet** in Google Sheets:

**Columns:**
- `email`
- `company_domain`
- `date_added_to_smartlead`
- `campaign_name`
- `current_status` (active / replied / bounced / unsubscribed)

**Rule:** Before any Clay workflow pushes to Smartlead, check the Master Exclusion Sheet:
- If `email` already exists with `current_status = active` → skip
- If `company_domain` already exists with any status → skip (don't email another contact at the same company)

**Clay implementation:** Use a Clay HTTP lookup against a Google Sheets webhook to check the exclusion list in real time.

---

## Personalisation Variable Reference

| Variable | Source Workflow | Example Value |
|---|---|---|
| `{{first_name}}` | All | "Sarah" |
| `{{company_name}}` | All | "Harbour View Real Estate" |
| `{{job_title}}` | All | "Principal" |
| `{{company_suburb}}` | WF01, WF02, WF04 | "Parramatta" |
| `{{role_being_hired}}` | WF02 | "Senior Sales Agent" |
| `{{previous_company}}` | WF05 | "Ray White Newtown" |
| `{{days_in_role}}` | WF05 | "47" |
| `{{ad_suburb}}` | WF06 | "Bondi" |
| `{{active_ad_count}}` | WF06 | "3" |
| `{{post_topic}}` | WF07 | "negative gearing changes" |
| `{{smsf_description}}` | WF03 | "SMSF auditing and LRBA advice" |
| `{{pain_summary}}` | WF09 | "settlement delays due to finance issues" |
| `{{example_keyword}}` | WF09 | "settlement fell through at the last minute" |
| `{{months_since_launch}}` | WF04 | "4" |

---

## Compliance Checklist (Apply Before Every Send)

- [ ] Email footer includes Laxmi Home Loans credit licence number
- [ ] Every email has a working unsubscribe link
- [ ] No "guaranteed approval", "best rate", or other banned phrases
- [ ] WF09 emails do not quote reviewer names or direct review text
- [ ] WF08 Nepali emails reviewed by a native Nepali speaker before sending
- [ ] All prospect data sourced from public sources only (no private databases)
