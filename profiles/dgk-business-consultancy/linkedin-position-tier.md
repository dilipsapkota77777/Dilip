# LinkedIn Position Tier Formula — DGK Business Consultancy
Generated: 2026-06-28

Input: `{{clean_position}}` (output of the position normalizer formula)
Output: `A — Decision Maker` / `B — Influencer` / `C — Not Fitted`
Prerequisite: Add `clean_position` column first (see `linkedin-position-normalizer.md`)

---

## Tier Breakdown (validated against 1,431-row LinkedIn export)

| Tier | Count | % | Description |
|---|---|---|---|
| **A — Decision Maker** | 1,032 | 72.1% | Can say YES. Sign the cheque. Feel the pipeline pain. |
| **B — Influencer** | 150 | 10.5% | Has authority in their function but needs CEO/owner sign-off. |
| **C — Not Fitted** | 249 | 17.4% | Wrong buyer type, non-operational, or outside DGK's ICP. |

---

## Tier A Breakdown (1,032 contacts)

| Clean Position | Count |
|---|---|
| Director | 526 |
| CEO | 204 |
| Owner | 145 |
| General Manager | 86 |
| Chairperson | 29 |
| Founder | 24 |
| Managing Partner | 8 |
| President | 7 |
| COO | 3 |

---

## Tier B Breakdown (150 contacts)

| Clean Position | Count | Why B not A |
|---|---|---|
| Manager | 36 | Operational, but not the growth decision-maker |
| Consultant | 19 | Can buy for their own practice — warm up first |
| IT Professional | 14 | CTO in small firms may be co-owner — check company size |
| Project Manager | 12 | Executes, doesn't buy |
| Operations Manager | 10 | Strong influence on systems — route to CEO |
| Creative Director | 10 | Creative/delivery lead — not pipeline owner |
| Head of Marketing | 9 | Potential internal champion — CEO still buys DGK |
| Head of Training | 8 | Functional lead — not growth decision-maker |
| Business Development Manager | 7 | Execution role in larger firms — owner if small |
| CFO | 6 | Financial gatekeeper — CPL proof point resonates |
| Sales Manager | 5 | Can influence — CEO owns the system decision |
| Lawyer | 5 | May own the firm — pitch pipeline audit |
| Program Manager | 4 | Delivery role |
| Engineer | 3 | Technical, not business |
| Finance Broker | 1 | May own practice — treat as Tier A |
| Architect | 1 | May own practice — treat as Tier A |

---

## Tier C Breakdown (249 contacts)

| Clean Position | Count | Why excluded |
|---|---|---|
| Government / NFP | 79 | DGK explicitly excludes — wrong procurement model |
| Healthcare Professional | 38 | Clinical role, not a business buyer |
| Educator | 32 | Academic — not a growth-system buyer |
| Board Member / Advisor | 22 | Non-operational, non-executive |
| Trades | 19 | Trade practitioner (not the trade firm owner) |
| Other | 18 | Uncategorised — skip |
| Administrator | 11 | Support role, no authority |
| Coordinator | 9 | Execution role, no decision authority |
| Hospitality / Tourism | 8 | Outside DGK's B2B ICP |
| Security | 6 | Outside DGK's ICP |
| Resources / Logistics | 5 | Low probability fit |
| Team Leader | 2 | Front-line, no growth authority |

---

## Clay Formula

**Column name:** `position_tier`
**Type:** Formula
**Prerequisite:** `clean_position` column must already exist in this table

```javascript
// ── POSITION TIER CLASSIFIER ─────────────────────────────────────────────────
// Input:  {{clean_position}}  (from the position normalizer formula)
// Output: "A — Decision Maker" / "B — Influencer" / "C — Not Fitted"
//
// Tier A: Full authority — can say YES to DGK engagement
// Tier B: Functional authority — needs CEO/owner approval
// Tier C: Wrong buyer type, non-operational, outside DGK ICP
// ────────────────────────────────────────────────────────────────────────────

const pos = String({{clean_position}} || "").trim();

const groups = {

  "A — Decision Maker": [
    "CEO",
    "Owner",
    "Founder",
    "Director",
    "General Manager",
    "Chairperson",
    "President",
    "COO",
    "Managing Partner"
  ],

  "B — Influencer": [
    "CFO",
    "Operations Manager",
    "Head of Marketing",
    "Business Development Manager",
    "Sales Manager",
    "Creative Director",
    "Head of Training",
    "Program Manager",
    "Project Manager",
    "Manager",
    "Consultant",
    "IT Professional",
    "Engineer",
    "Lawyer",
    "Architect",
    "Finance Broker"
  ],

  "C — Not Fitted": [
    "Government / NFP",
    "Board Member / Advisor",
    "Educator",
    "Healthcare Professional",
    "Administrator",
    "Coordinator",
    "Team Leader",
    "Trades",
    "Security",
    "Hospitality / Tourism",
    "Resources / Logistics",
    "Other",
    "Unknown"
  ]

};

for (const [tier, positions] of Object.entries(groups)) {
  if (positions.includes(pos)) {
    return tier;
  }
}

return "C — Not Fitted";
```

---

## How to Add in Clay

1. Make sure `clean_position` column already exists (run the normalizer first)
2. **+ Add Column** → **Formula**
3. Name it `position_tier`
4. Paste formula — map `{{clean_position}}` to your normalizer output column
5. Run — **0 credits**

---

## How to Use This for Retargeting

### Smartlead Upload Filter
Before uploading to any campaign: `position_tier != "C — Not Fitted"`

This removes 249 contacts (17.4%) who are wrong buyer type.

### Sequencing Priority

**Tier A — Direct pipeline audit CTA**
> "Worth a free 30-min pipeline audit, [First Name]?"

Sent to: Directors, CEOs, Owners, GMs, Founders
Volume: 1,032 contacts — run as 3 separate Smartlead campaigns by clean_position:
- Campaign 1: `CEO` + `Owner` + `Founder` (373 contacts)
- Campaign 2: `Director` (526 contacts)
- Campaign 3: `General Manager` + `Managing Partner` + `COO` (97 contacts)

**Tier B — Softer opener, route to owner**
> "I work with a lot of [City] firms in your space — who in your team owns the pipeline / growth side? Happy to send something useful either way."

Sent to: Managers, BDMs, Heads of Marketing, Consultants
Volume: 150 contacts — run as 1 campaign, shorter 2-touch sequence

**Tier C — Do not contact**
Archive or suppress. No outreach.

---

## Stack Order in Clay Table (recommended column order)

| Column | Type | Source |
|---|---|---|
| `current_company_position` | Raw import | LinkedIn CSV |
| `clean_position` | Formula | Normalizer formula |
| `position_tier` | Formula | This formula |
| `email` | Enrichment | Prospeo / Apollo waterfall |
| `icp_score` | Formula | Score formula (separate) |
