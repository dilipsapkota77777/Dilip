# LinkedIn Segment Formula — DGK Business Consultancy
Generated: 2026-06-28

Input field: `{{current_company_position}}`
Tested against: 1,431 LinkedIn connection export rows

---

## Segment Breakdown (validated against actual data)

| Segment | Count | % | Action |
|---|---|---|---|
| Decision Maker | 1,072 | 74.9% | Primary outreach — pipeline audit CTA |
| Gov/NFP | 113 | 7.9% | **Exclude** — wrong buyer type |
| Other | 52 | 3.6% | Skip or manual review |
| Professional Services | 42 | 2.9% | CRM audit angle |
| Education | 40 | 2.8% | Low priority |
| Health | 35 | 2.4% | NDIS/allied health angle |
| Trades | 22 | 1.5% | Referral/word-of-mouth angle |
| Agency/Creative | 19 | 1.3% | Peer positioning angle |
| IT/Tech | 14 | 1.0% | IT/MSP referral ceiling proof point |
| Resources/Logistics | 13 | 0.9% | Low priority |
| Hospitality/Tourism | 6 | 0.4% | Low priority |
| Security | 3 | 0.2% | Low priority |

---

## Clay Formula

**Column name:** `segment`
**Field:** Formula
**Input:** `{{current_company_position}}`

```javascript
// ── SEGMENT CLASSIFIER ──────────────────────────────────────────────────────
// Input: {{current_company_position}} (LinkedIn export field)
// Output: one of 11 segment labels
// ────────────────────────────────────────────────────────────────────────────

const raw = String({{current_company_position}} || "").toLowerCase().trim();

if (!raw) return "No Position";

const has = (k) => raw.includes(k);
const word = (k) => new RegExp("\\b" + k.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b").test(raw);

// ── 1. GOV / NFP — exclude from outreach ────────────────────────────────────
const govKeys = [
  "councillor","alderman","deputy mayor","elected member","local government",
  "nt government","dept of","department of","chief minister","cabinet",
  "policy officer","senior policy","principal policy","strategic policy",
  "program coordinator","community justice","community wellbeing",
  "community services receptionist","engagement officer",
  "regional soils","first nations project",
  "fire management officer","police constable","correctional officer",
  "emergency medical dispatcher","emergency dispatcher",
  "child health outreach","icpa federal",
  "director suicide prevention","director safe nt","director transforming aboriginal",
  "director remote early","director external review","director qecnt",
  "director vet policy","director of immunisations","director of early years",
  "director of boarding","director supervision","director industrial ecologies",
  "acting chief executive","acting manager","assistant director",
  "intake officer","administrative officer","account officer",
  "communications officer","media liaison","payroll administrator",
  "sessional member","council member","official member","national safety committee",
  "independent member of the audit","ethics advisory",
  "witness assistance","graduate officer","research officer","senior project officer",
  "project officer","policy and program","employment services program",
  "community projects manager","senior human resources officer","human resources manager",
  "housing manager","internal communications","treasurer and public officer",
  "ntfl competition","defence industry",
  "regional director tiwi","general manager planning","general manager community",
  "director people and culture","people and quality","chief people","director people",
  "advisory board member","board member","non executive board",
  "committee member","investment committee member","member of the board",
  "honorary treasurer","secretary","public officer","retired",
  "nt bushfires","chief investigator","relationships partner"
];
if (govKeys.some(k => has(k))) return "Gov/NFP";

// ── 2. HEALTH / MEDICAL / ALLIED HEALTH ─────────────────────────────────────
const healthKeys = [
  "registered nurse","clinic registered nurse","senior midwifery","midwif",
  "physiotherapist","hand therapist","clinical specialist","clinical educator",
  "clinical registrar","clinical council","senior contracted clinician",
  "general practitioner","medical officer","chief medical officer",
  "head of department of medicine","director of medicine","director of anaesthetics",
  "director of psychiatry","director of health","director of disabilities",
  "provisional psychologist","social worker","carers counsellor",
  "home care worker","disability support worker","senior vet nurse","optometrist",
  "primary healthcare","family violence prevention",
  "injury prevention","family dispute resolution","public health physician",
  "team leader ndis"
];
if (healthKeys.some(k => has(k))) return "Health";

// ── 3. EDUCATION / TRAINING / ACADEMIC ──────────────────────────────────────
const eduKeys = [
  "adjunct professor","adjunct senior research","adjunct research fellow",
  "lecturer","professor","teacher","trainer assessor","trainer-facilitator",
  "technical trainer","head of training","learning and development",
  "head of special education","secondary music educator",
  "first nations academic","senior lecturer","beauty therapy lecturer",
  "vet lecturer","university fellow","professorial fellow",
  "doctoral student","phd student","phd scholar","instructor",
  "head trainer","digital learning","violin teacher",
  "education business consultant","product design and technology","academic",
  "kindergarten improvement advisor","cultural mentor"
];
if (eduKeys.some(k => has(k))) return "Education";

// ── 4. IT / TECH ─────────────────────────────────────────────────────────────
const itKeys = [
  "developer","dynamics 365","solution architect","systems administrator",
  "network engineer","ict co","gis administrator","system analyst",
  "technical coordinator","solution design","technical specialist",
  "telecommunications manager","chief technology officer"
];
if (itKeys.some(k => has(k))) return "IT/Tech";
if (word("cto")) return "IT/Tech";

// ── 5. TRADES / CONSTRUCTION ─────────────────────────────────────────────────
const tradesKeys = [
  "electrician","welder","refrigeration mechanic","formen","foreman",
  "autocad draftsman","construction estimator","construction supervisor",
  "structural engineer","civil engineer","plant maintenance",
  "workshop supervisor","leading hand","building project coordinator",
  "director construction","yardman","licenced aircraft engineer",
  "licenced aircraft maintenance","repair and warranty",
  "plumber","tiler","carpenter","boilermaker","truck driver","bus driver"
];
if (tradesKeys.some(k => has(k))) return "Trades";

// ── 6. AGENCY / MARKETING / CREATIVE ─────────────────────────────────────────
const agencyKeys = [
  "head of marketing","director of marketing","vp of marketing",
  "chief marketing officer","creative director","content creator",
  "graphic designer","marketing and tourism development",
  "head of marketing-retention","creative content and marketing",
  "senior producer","music producer","audio technician","actor model",
  "design project manager","strategic design lead"
];
if (agencyKeys.some(k => has(k))) return "Agency/Creative";

// ── 7. PROFESSIONAL SERVICES ──────────────────────────────────────────────────
// Law, accounting, finance, architecture, consulting
const psKeys = [
  "lawyer","barrister","solicitor","general counsel","principal lawyer",
  "chairperson of the legal","commissioner for oaths",
  "accountant","finance broker","investment strategist","private investor",
  "finance and administration manager",
  "architect","pharmacist",
  "consultant","principal consultant","business process optimisation",
  "strategic advisor","business mentor","practitioner",
  "migration agent","real estate","commercial property","property manager",
  "instigator","managing partner","principal partner",
  "business partner","employer"
];
if (psKeys.some(k => has(k))) return "Professional Services";
if (word("cfo") || word("cpa")) return "Professional Services";
if (has("chief financial officer") || has("managing director and principal")) return "Professional Services";

// Handle "partner" only as a standalone word (not "partnership", "department")
if (word("partner")) return "Professional Services";

// ── 8. RESOURCES / LOGISTICS / AVIATION ──────────────────────────────────────
const resourcesKeys = [
  "water services","airport operations","terminal coordinator",
  "supply and procurement","utilities and infrastructure",
  "flight operations","chief pilot","pilot vessel master",
  "maritime security guard","vessel master","station manager",
  "distribution specialist","general manager water","general manager built",
  "general manager strategic","general manager trading","head of flight",
  "licenced aircraft"
];
if (resourcesKeys.some(k => has(k))) return "Resources/Logistics";

// ── 9. SECURITY ───────────────────────────────────────────────────────────────
const securityKeys = [
  "corporate security officer","maritime security","correctional officer",
  "firefighter","fire management"
];
if (securityKeys.some(k => has(k))) return "Security";

// ── 10. HOSPITALITY / TOURISM / EVENTS ───────────────────────────────────────
const hospitalityKeys = [
  "food and beverage","night auditor","tour guide","kayak instructor",
  "venue management","event manager","box office","bar manager",
  "chef","kitchen","barista","accommodation"
];
if (hospitalityKeys.some(k => has(k))) return "Hospitality/Tourism";

// ── 11. DECISION MAKER — catch-all for C-suite / owner / leader ───────────────
// These titles span all industries — segment by industry separately if needed
const dmKeys = [
  "director","managing director","chief executive","owner","founder",
  "general manager","chairperson","chairman","chair","president",
  "executive director","sole proprietor","propriétaire","propietario",
  "proprietário","unternehmensinhaber","operator","co-owner","co owner",
  "regional manager","regional commercial","head of operations",
  "head of purpose","head of quality","head of compliance",
  "gm of","division manager","contract manager","vice president",
  "commercial structuring","executive manager","change manager",
  "workforce solutions","founding director","founding managing director",
  "co-founder","co founder","board director",
  "chief operating officer","operations manager","business development",
  "sales manager","sales executive","business manager","business owner",
  "company owner","senior manager","program director",
  "administration manager","admin manager","manager","project manager",
  "projects manager","project lead","team leader"
];
if (dmKeys.some(k => has(k))) return "Decision Maker";
if (word("ceo") || word("md") || word("gm")) return "Decision Maker";
if (has("head of ")) return "Decision Maker";

return "Other";
```

---

## How to Add This in Clay

1. Open your Clay table with the LinkedIn data
2. Click **+ Add Column** → **Formula**
3. Name the column: `segment`
4. Paste the formula above
5. Map `{{current_company_position}}` to your actual column (usually auto-detected)
6. Run on all rows

**Zero credits used** — formula columns are free in Clay.

---

## What to Do With Each Segment

### Primary — Decision Maker (75%)
These are directors, MDs, CEOs, owners, and GMs across all industries.
- **CTA:** Pipeline Audit Call (30 min, free Calendly)
- **Angle:** "Most {title}s I speak to in [industry/Darwin] have the same gap..."
- **Industry context:** Add `{{current_company}}` column to sub-segment by industry if needed

### High-Value Niche Segments

**Professional Services (3%)** — lawyers, accountants, architects, consultants
- Pain: referral-dependent, no repeatable pipeline
- Proof: "Legal firm — CPL down 62% in Q1"
- CTA: Free CRM Audit (check their HubSpot/spreadsheet live on Zoom)

**Health (2.4%)** — NDIS providers, allied health, clinical services
- Pain: word-of-mouth only, no digital pipeline, NDIS referral uncertainty
- Proof: NDIS daily content system
- CTA: Pipeline Audit Call

**Trades (1.5%)** — electricians, builders, construction
- Pain: feast/famine project cycle, no follow-up system
- Proof: construction/referral ceiling case study
- CTA: "I'll show you how we filled a 3-month pipeline for a Darwin tradie in 6 weeks"

**IT/Tech (1%)** — MSPs, solution architects, tech firms
- Pain: referral ceiling, no outbound motion
- Proof: "IT firm — 0 to 6 enquiries/month in 60 days"
- CTA: Pipeline Audit Call

**Agency/Creative (1.3%)** — marketers, designers, content creators
- Pain: inconsistent client flow, burning time on pitches
- Proof: Cobbler's children angle — "you do this for clients, not for yourself"
- CTA: Pipeline Audit Call

### Exclude
**Gov/NFP (8%)** — councillors, policy officers, board members, public servants
- Filter out before uploading to Smartlead

---

## Optional: Add ICP Score Column

After adding the segment column, add a second formula column:

```javascript
// ICP Score — 0 to 100
// Column name: icp_score

const pos = String({{current_company_position}} || "").toLowerCase();
const seg = String({{segment}} || "");

let score = 0;

// Title tier (40 pts)
const tierA = ["owner","director","managing director","ceo","founder",
               "chief executive","general manager","chairperson","chairman",
               "president","co-founder","co founder","sole proprietor",
               "managing partner","executive director","founding director"];
const tierB = ["operations manager","sales manager","business development",
               "head of","business owner","company owner","business manager"];

if (tierA.some(t => pos.includes(t))) score += 40;
else if (tierB.some(t => pos.includes(t))) score += 25;

// Segment value (30 pts)
if (["IT/Tech","Professional Services","Health","Agency/Creative"].includes(seg)) score += 30;
else if (["Trades","Decision Maker"].includes(seg)) score += 20;
else if (seg === "Gov/NFP") score -= 30;

// Data quality (30 pts) — add when email is enriched
// const hasEmail = !!({{email}} && {{email}}.includes("@"));
// if (hasEmail) score += 30;

return Math.min(Math.max(score, 0), 100);
```

---

## Smartlead Campaign Mapping

| Segment | Smartlead Campaign | Subject Line Hook |
|---|---|---|
| Decision Maker | `LI-Decision-Makers` | "quick question re: [company]'s pipeline" |
| Professional Services | `LI-Prof-Services` | "how [law/accounting] firms stop relying on referrals" |
| Health | `LI-Health-NDIS` | "NDIS pipeline — what's working in Darwin right now" |
| IT/Tech | `LI-IT-MSP` | "how an IT firm went 0→6 enquiries in 60 days" |
| Agency/Creative | `LI-Agency` | "the cobbler's children problem — for agencies" |
| Trades | `LI-Trades` | "feast or famine? Darwin tradies solving this in 2025" |
| Gov/NFP | **Exclude** | — |
