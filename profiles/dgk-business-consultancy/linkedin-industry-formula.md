# LinkedIn Industry Classification — DGK Business Consultancy
Generated: 2026-06-28

Input fields: `{{current_company_position}}` + `{{current_company}}` + `{{headline}}`
Tested against: 1,431 LinkedIn connection export rows

---

## 3-Column Clay Workflow

| Column | Type | Credits | Purpose |
|---|---|---|---|
| `industry` | Formula | 0 | Keyword classifier — covers ~52% |
| `industry_ai` | Claygent | ~1/row | AI classifier — handles remaining "Other" |
| `industry_final` | Formula | 0 | Merge: use `industry` if not "Other", else `industry_ai` |

---

## Industry Breakdown (formula layer only, validated against 1,431 rows)

| Industry | Count | % |
|---|---|---|
| Other | 692 | 48.4% |
| Professional Services | 252 | 17.6% |
| Gov/NFP | 217 | 15.2% |
| Trades | 128 | 8.9% |
| Health | 105 | 7.3% |
| Agency | 37 | 2.6% |

After Claygent runs on 692 "Other" rows, expect final "Other" < 5%.

---

## Column 1 — `industry` (Formula, 0 credits)

**Column name:** `industry`
**Type:** Formula
**Input fields:** `{{current_company_position}}`, `{{current_company}}`, `{{headline}}`

```javascript
// ── INDUSTRY CLASSIFIER — LAYER 1 ────────────────────────────────────────────
// Combines position + company + headline for maximum keyword coverage.
// Gov/NFP checked FIRST to prevent NFP health orgs misclassifying as Health.
// ~52% classification rate — remaining "Other" handled by Claygent (Column 2).
// ─────────────────────────────────────────────────────────────────────────────

const pos  = String({{current_company_position}} || "").toLowerCase().trim();
const comp = String({{current_company}} || "").toLowerCase().trim();
const hl   = String({{headline}} || "").toLowerCase().trim();
const combined = pos + " " + comp + " " + hl;

const has = (k) => combined.includes(k);

// ── 1. GOV / NFP — check first ───────────────────────────────────────────────
const govKeys = [
  "nt government","territory government","northern territory government",
  "department of","dept of","chief minister","cabinet office",
  "shire council","city council","regional council","town council","darwin city council",
  "land council","aboriginal corporation","indigenous corporation",
  "chamber of commerce","chamber of industry",
  "not for profit","non-profit","nonprofit","nfp ",
  "aboriginal and torres strait","reconciliation","foundation australia",
  "relationships australia","anglicare","salvation army","st john",
  "lifeline","red cross","mission australia","uniting care",
  "volunteering","youth network","community enterprise",
  "charles darwin university","cdu ","batchelor institute",
  "school ","primary school","high school","college of",
  "northern land council","tiwi land council",
  "territory families","territory housing","territory corrections",
  "attorney-general","attorney general","audit office","ombudsman",
  "police force","fire and rescue","emergency services",
  "darwin port","port darwin","power water","power and water",
  "tourism nt","tourism top end","tourism australia",
  "sport and recreation","lacrosse","cricket nt","football federation",
  "arts centre","museum and art","darwin symphony","festival of darwin",
  "northern territory racing","northern territory netball",
  "caama","indigitise","myhealth darwin"
];
if (govKeys.some(k => has(k))) return "Gov/NFP";

// ── 2. HEALTH / ALLIED HEALTH / DISABILITY ───────────────────────────────────
const healthKeys = [
  "health","medical","medicine","clinic","hospital","pharmacy","pharmacist",
  "physiotherap","occupational therap","speech therap","chiropractic",
  "optometry","optometrist","dental","dentist","audiolog",
  "disability","ndis","aged care","age care","home care","respite",
  "mental health","counselling","counseling","psychology","psychologist",
  "social work","community care","support service","care service",
  "nursing","midwif","paramedic","ambulance",
  "fitness","personal trainer","gym ","crossfit","yoga","pilates",
  "childcare","child care","early childhood","kindergarten","daycare",
  "therapy","therapist","rehabilitation","wellbeing","wellness"
];
if (healthKeys.some(k => has(k))) return "Health";

// ── 3. TRADES / CONSTRUCTION / PRIMARY INDUSTRY ───────────────────────────────
const tradesKeys = [
  "builder","building ","construction","concreting","concrete",
  "plumb","plumber","electrician","electrical","electri",
  "air conditioning","hvac","refrigeration","mechanical services",
  "civil ","earthwork","excavat","drainag","paving",
  "carpentry","carpenter","cabinet maker","joinery",
  "painting","painter","tiler","tiling","flooring",
  "roofing","scaffolding","waterproofing","insulation",
  "mining","resources ","oil and gas","petroleum","drilling",
  "agriculture","agri","pastoral","cattle","beef","livestock","cropping",
  "horticulture","farming","station ","rural ",
  "transport","trucking","haulage","logistics","freight","courier",
  "marine","shipping","vessel","boat build",
  "auto","mechanic","automotive","panel beat","smash repair",
  "landscap","arborist","tree service",
  "sitzler","hosepower","abigroup","downer","seymour whyte",
  "mcconnell dowell","laing o'rourke","laing orourke",
  "manufacturing","fabricat","metal work","welding","steel",
  "security guard","security service","guard service"
];
if (tradesKeys.some(k => has(k))) return "Trades";

// ── 4. AGENCY / MARKETING / CREATIVE ─────────────────────────────────────────
const agencyKeys = [
  "marketing","social media","branding","brand agency",
  "advertising","ad agency","media agency","pr agency","public relations",
  "digital agency","digital marketing","seo","search engine",
  "creative agency","creative studio","design studio","graphic design",
  "content creat","content market","copywriting","copywriter",
  "video product","film product","photography","photographer",
  "event manag","event plann","event company","events company",
  "virtual assist","virtual pa","virtual exec",
  "web design","web develop","website design","ux design",
  "animation","motion graphic","post production",
  "media production","production house","production company",
  "influencer","podcast","broadcast","radio station","television",
  "music production","recording studio",
  "digitally buzzed","the social","social club","the media"
];
if (agencyKeys.some(k => has(k))) return "Agency";

// ── 5. PROFESSIONAL SERVICES ──────────────────────────────────────────────────
const professionalKeys = [
  "accountant","accounting","bookkeeping","bookkeeper","audit","cpa ",
  "financial planning","financial planner","financial advisor","financial adviser",
  "insurance","mortgage broker","finance broker","wealth management",
  "investment","fund management","superannuation","super fund",
  "lawyer","legal","law firm","barrist","solicitor","conveyancing",
  "real estate","property ","propri","realty","rental management",
  "consulting","consultancy","management consult","business consult",
  "recruitment","staffing","labour hire","workforce","talent",
  "human resources","hr consult","people and culture",
  "technology","tech ","it solutions","it services","managed services",
  "software","saas","app develop","cloud service","cyber security","cybersecurity",
  "engineering consult","structural consult","project consult","environmental consult",
  "architect","architecture","urban planning","town planning","surveying",
  "education consult","training provider","rto ","registered training",
  "business broker","commercial broker","buyers agent",
  "import","export","wholesale","distribution","supplier",
  "travel agent","travel consult","migration agent","visa consult",
  "printing","signage","promo product","merchandise"
];
if (professionalKeys.some(k => has(k))) return "Professional Services";

return "Other";
```

---

## Column 2 — `industry_ai` (Claygent, ~1 credit/row)

**Column name:** `industry_ai`
**Type:** Claygent
**Model:** Claygent Neon (1–2 credits/row)
**Conditional run:** Only run when `industry` = `"Other"`

### Conditional Run Setup in Clay
- Click the column settings gear → **Conditional Run**
- Condition: `industry` **is** `Other`
- This saves ~739 credits (only 692 rows need AI)

### Claygent Prompt

```
You are classifying a business contact's employer into one of these industry categories.

Company name: {{current_company}}
LinkedIn headline: {{headline}}

Classify this business into EXACTLY ONE of these categories:

- Trades: construction, building, electrical, plumbing, mechanical, mining, resources, agriculture, transport, logistics, manufacturing, marine, automotive, landscaping, security services
- Agency: marketing agency, PR, events, creative studio, design agency, digital marketing, video production, photography, virtual assistant services, media production
- Professional Services: accounting, finance, law, real estate, property management, IT services, technology, software, consulting, recruitment, HR, architecture, engineering consulting, training, education consulting, insurance, mortgage, travel, import/export
- Health: medical, dental, pharmacy, allied health, disability support, NDIS, aged care, childcare, mental health, counselling, fitness, therapy, wellness
- Gov/NFP: government department, local council, Indigenous corporation, charity, not-for-profit, sporting association, arts organisation, education institution

Rules:
- Use the company name and headline as your only signals
- If the company is clearly identifiable (e.g., "Darwin Plumbing" → Trades, "Smith Lawyers" → Professional Services), return that category
- If genuinely unclear after reviewing both signals, return Other
- Return ONLY the category name — no explanation, no punctuation

Output examples:
Trades
Professional Services
Health
Gov/NFP
Agency
Other
```

---

## Column 3 — `industry_final` (Formula, 0 credits)

**Column name:** `industry_final`
**Type:** Formula
**Purpose:** Merge formula and Claygent results into final classification

```javascript
// ── INDUSTRY FINAL MERGE ──────────────────────────────────────────────────────
// Uses keyword formula result unless it returned "Other",
// in which case falls back to Claygent AI result.
// ─────────────────────────────────────────────────────────────────────────────

const formula = String({{industry}} || "").trim();
const ai      = String({{industry_ai}} || "").trim();

if (formula && formula !== "Other") return formula;
if (ai && ai !== "purple") return ai;
return "Other";
```

---

## How to Add All 3 Columns in Clay

### Step 1 — `industry` (Formula)
1. **+ Add Column** → **Formula**
2. Name: `industry`
3. Paste Column 1 formula
4. Map fields: `{{current_company_position}}`, `{{current_company}}`, `{{headline}}`
5. Run on all rows — **0 credits**

### Step 2 — `industry_ai` (Claygent)
1. **+ Add Column** → **Claygent**
2. Name: `industry_ai`
3. Model: **Claygent Neon**
4. Paste the Claygent prompt above
5. Map: `{{current_company}}` and `{{headline}}`
6. **Conditional Run** → `industry` is `Other`
7. Test on 10 rows first, then run all — **~1 credit/row**

### Step 3 — `industry_final` (Formula)
1. **+ Add Column** → **Formula**
2. Name: `industry_final`
3. Paste Column 3 merge formula
4. Map: `{{industry}}` and `{{industry_ai}}`
5. Run on all rows — **0 credits**

---

## Credit Cost Estimate

| Step | Rows | Credits/row | Total Credits |
|---|---|---|---|
| `industry` formula | 1,431 | 0 | 0 |
| `industry_ai` Claygent | ~692 | 1–2 | ~700–1,400 |
| `industry_final` formula | 1,431 | 0 | 0 |
| **Total** | | | **~700–1,400** |

On a Starter plan ($149/mo = 2,000 credits), this covers the full run with credits to spare.

---

## Outreach Strategy by Industry

| Industry | Volume (est.) | DGK Angle | CTA |
|---|---|---|---|
| Professional Services | ~400+ | Referral ceiling — no repeatable pipeline | Pipeline Audit |
| Gov/NFP | ~217 | **Exclude** — wrong buyer type | — |
| Trades | ~200+ | Feast/famine cycle, no follow-up system | "6 weeks to fill a 3-month pipeline" |
| Health / NDIS | ~150+ | Word-of-mouth only, NDIS uncertainty | Pipeline Audit |
| Agency | ~80+ | Cobbler's children — builds for clients, not self | Pipeline Audit |

### Smartlead Campaign Mapping

| `industry_final` | Campaign Name | Subject Hook |
|---|---|---|
| Professional Services | `LI-Prof-Services` | "how [law/accounting] firms stop relying on referrals" |
| Trades | `LI-Trades` | "feast or famine? Darwin tradies solving this in 2025" |
| Health | `LI-Health-NDIS` | "NDIS pipeline — what's working in Darwin right now" |
| Agency | `LI-Agency` | "the cobbler's children problem — for agencies" |
| Gov/NFP | **Exclude** | — |
| Other | Manual review | — |

---

## Stack Order in Clay Table (full recommended column order)

| Column | Type | Source |
|---|---|---|
| `current_company_position` | Raw import | LinkedIn CSV |
| `current_company` | Raw import | LinkedIn CSV |
| `headline` | Raw import | LinkedIn CSV |
| `clean_position` | Formula | Position normalizer formula |
| `position_tier` | Formula | Position tier formula |
| `industry` | Formula | This formula (Layer 1) |
| `industry_ai` | Claygent | This prompt (Layer 2, conditional) |
| `industry_final` | Formula | Merge formula (Layer 3) |
| `email` | Enrichment | Prospeo / Apollo waterfall |
| `icp_score` | Formula | Score formula (separate) |
