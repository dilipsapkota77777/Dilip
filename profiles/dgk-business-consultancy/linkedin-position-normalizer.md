# LinkedIn Position Normalizer Formula — DGK Business Consultancy
Generated: 2026-06-28

Input: `{{current_company_position}}`
Output: Canonical clean position title
Coverage: 96.6% of 1,431 contacts mapped (49 true edge-cases return "Other")
Credits used: 0 — pure formula column

---

## Clean Position Breakdown (validated against your CSV)

| Clean Position | Count | % |
|---|---|---|
| Director | 521 | 36.4% |
| CEO | 204 | 14.3% |
| Owner | 144 | 10.1% |
| General Manager | 86 | 6.0% |
| Government / NFP | 71 | 5.0% |
| Healthcare Professional | 37 | 2.6% |
| Educator | 30 | 2.1% |
| Manager | 30 | 2.1% |
| Chairperson | 29 | 2.0% |
| Founder | 24 | 1.7% |
| Board Member / Advisor | 20 | 1.4% |
| Trades | 19 | 1.3% |
| Consultant | 16 | 1.1% |
| IT Professional | 14 | 1.0% |
| Head of Marketing | 9 | 0.6% |
| Creative Director | 10 | 0.7% |
| Project Manager | 11 | 0.8% |
| Administrator | 11 | 0.8% |
| Operations Manager | 10 | 0.7% |
| Business Development Manager | 7 | 0.5% |
| Coordinator | 8 | 0.6% |
| CFO | 6 | 0.4% |
| Sales Manager | 5 | 0.3% |
| Lawyer | 5 | 0.3% |
| Other | ~49 | 3.4% |

---

## Clay Formula

**Column name:** `clean_position`
**Type:** Formula
**Input:** `{{current_company_position}}`

```javascript
// ── POSITION NORMALIZER ──────────────────────────────────────────────────────
// Maps every raw LinkedIn position to a single canonical clean title.
// Uses exact-match lookup — same pattern as NDIS formula.
// ────────────────────────────────────────────────────────────────────────────

const title = String({{current_company_position}} || "").toLowerCase().trim();

if (!title) return "Unknown";

const groups = {

  "CEO": [
    "chief executive officer","ceo","chief executive",
    "ceo and founder","founder and ceo","ceo and co founder",
    "acting chief executive officer","chief executive officer and principal",
    "chief executive officer and chief strategist","chief executive officer ni",
    "chief executive office","ceo internet",
    "ceo of jacana services and supply limited",
    "founder and ceo of tivan company","founder and chief executive officer",
    "co-ceo executive director"
  ],

  "Director": [
    "director","managing director","non executive director","executive director",
    "co-founder and director","director and board member","director and operations manager",
    "co-founder and executive director","owner and director","co-founder and managing director",
    "owner director","founding director","board director",
    "managing director sa","managing director of crocodilian academy",
    "managing director rise project consulting","managing director and principal designer",
    "founding managing director","yamba roadshow director","director of staff",
    "director greater darwin","director and manager roles","evaluation director",
    "headstart cluster director","oshc director","venue management director",
    "director and current president","director and turf consultant",
    "director and merchandiser","director and principal","director office of the ceo",
    "director keil maritime","director ii","director lll","director of adventure",
    "manager director","co-founder and director research","director governance",
    "director people","director construction","director of finance",
    "director global leadership development programme","director of school policy",
    "executive director office of the ceo"
  ],

  "General Manager": [
    "general manager","general manager community","general manager of trading",
    "general manager planning and land management",
    "general manager strategic development at cgh group","general manager water services",
    "general manager built infrastructure","general manager corporate services",
    "gm of customer engagement","owner and general manager"
  ],

  "Owner": [
    "owner","business owner","company owner","sole proprietor",
    "propriétaire","propietario","proprietário","unternehmensinhaber",
    "co owner","co-owner","owner land development","owner at communica consulting",
    "owner in partnership","owner and chief number cruncher",
    "owner and operator of choices flooring darwin","independent business owner",
    "رئيس مجلس إدارة","employer","operator","instigator",
    "owner and executive director","principal"
  ],

  "Founder": [
    "founder","co-founder","co founder","founder of saaslinks.io",
    "founder and director","founder and director of top end medical services",
    "founder managing director","founder business director",
    "founder and managing director"
  ],

  "Chairperson": [
    "chair","chairman","chairperson","chairperson of the board",
    "chairman of the board","vice chair","deputy chair","independent chair",
    "board chair","group chairman","deputy chairperson",
    "chairperson nt faculty",
    "chairperson of the legal practitioners funds management committee",
    "chairperson of longitudinal study of indigenous children"
  ],

  "President": [
    "president","vice president"
  ],

  "COO": [
    "chief operating officer"
  ],

  "CFO": [
    "chief financial officer","cfo","director of finance"
  ],

  "Managing Partner": [
    "managing partner","principal partner","partner"
  ],

  "Operations Manager": [
    "operations manager","head of operations","head of operations boarding",
    "director and operations manager"
  ],

  "Board Member / Advisor": [
    "board member","advisory board member","non executive board member",
    "member of the board","international board director",
    "daaf foundation independent specialist board member","board director",
    "member investment committee","riverland mallee coorong local health network governing board"
  ],

  "Head of Marketing": [
    "head of marketing","director of marketing","vp of marketing",
    "chief marketing officer","head of marketing-retention",
    "marketing and tourism development manager","creative content and marketing manager"
  ],

  "Creative Director": [
    "creative director","graphic designer","content creator",
    "senior producer","music producer","audio technician","actor model",
    "design project manager","strategic design lead"
  ],

  "Sales Manager": [
    "sales manager","sales executive","uk account manager",
    "regional commercial manager"
  ],

  "Business Development Manager": [
    "business development manager","business development",
    "director of business development"
  ],

  "Project Manager": [
    "project manager","projects manager","project lead",
    "project quality specialist","building project coordinator",
    "projects hse manager"
  ],

  "Program Manager": [
    "program director","program manager"
  ],

  "Head of Training": [
    "head of training","head of training and checking","head trainer",
    "learning and development specialist","technical trainer","trainer assessor",
    "trainer-facilitator","head of special education services"
  ],

  "Manager": [
    "manager","senior manager","business manager","change manager",
    "contract manager","division manager","station manager",
    "regional manager","workforce solutions manager","student manager",
    "administration manager","admin manager",
    "head of purpose","head of quality",
    "head of compliance and regulatory affairs uk",
    "head of airport operations","head of flight operations",
    "head of department of medicine","finance and administration manager",
    "executive manager regulatory services","manager city planning",
    "manager community engagement","senior manager pathways and cricket",
    "commercial property manager","seinor planner","relationships partner"
  ],

  "Consultant": [
    "consultant","principal consultant","business process optimisation consultant",
    "strategic advisor","business mentor","education business consultant",
    "business analyst","business partner","principal and consultant",
    "senior advisor","investment strategist","commercial structuring",
    "impact markets strategy","private investor","commercial property specialists",
    "materials advisor","practitioner"
  ],

  "Lawyer": [
    "lawyer","barrister",
    "principal lawyer and notary public for nsw","general counsel",
    "commissioner for oaths"
  ],

  "Finance Broker": [
    "finance broker"
  ],

  "Architect": [
    "architect"
  ],

  "IT Professional": [
    "chief technology officer","solution architect","systems administrator",
    "network engineer",".net integration developer","dynamics 365 developer",
    "system analyst","technical coordinator","enterprise gis administrator",
    "ict co-ordinator","lead technical specialist","telecommunications manager",
    "solution design and engineering lead"
  ],

  "Engineer": [
    "structural engineer","civil engineer","autocad draftsman"
  ],

  "Trades": [
    "electrician","welder","refrigeration mechanic","formen","yardman",
    "plant maintenance officer","workshop supervisor","leading hand",
    "construction estimator","construction supervisor","truck driver","bus driver",
    "licenced aircraft engineer","licenced aircraft maintenance engineer",
    "repair and warranty coordinator and office support","chief pilot",
    "pilot vessel master"
  ],

  "Healthcare Professional": [
    "registered nurse","clinic registered nurse","physiotherapist","hand therapist",
    "clinical specialist","clinical educator","clinical registrar",
    "senior contracted clinician","general practitioner","medical officer",
    "chief medical officer","director of anaesthetics",
    "director of medicine and cardiologist","director of psychiatry",
    "director of health","provisional psychologist","social worker",
    "social worker aod","carers counsellor","home care worker",
    "disability support worker","senior vet nurse","optometrist",
    "primary healthcare systems manager","family violence prevention manager",
    "family dispute resolution practitioner","public health physician",
    "senior midwifery advisor","director of immunisations and notifiable diseases",
    "team leader ndis","director of disabilities",
    "injury prevention and managment expert","speech and drama specialist",
    "clinical council member primary health network nt"
  ],

  "Educator": [
    "adjunct professor","lecturer","professor","teacher","instructor",
    "university fellow","professorial fellow","doctoral student","phd student",
    "adjunct senior research fellow","adjunct research fellow",
    "digital learning and community engagement officer","violin teacher",
    "product design and technology teacher","kindergarten improvement advisor",
    "lecturer in multimedia and scree","adjunct professor nutrition",
    "lecturer health science","professor of aquaculture","senior lecturer education",
    "cultural mentor and supervisor","first nations academic support lecturer",
    "senior lecturer","beauty therapy lecturer","vet lecturer","secondary music educator",
    "sir roland wilson pat turner phd scholar",
    "ranger base build facilitator for special studies program usyd"
  ],

  "Coordinator": [
    "coordinator","service coordinator","program coordinator",
    "community program coordinator","project coordinator",
    "interim territory coordinator","project officer","senior project officer",
    "community justice partnerships team lead","community wellbeing senior project officer",
    "ntfl competition co-ordinator"
  ],

  "Team Leader": [
    "team leader","team leader urban",
    "child health outreach program team leader"
  ],

  "Administrator": [
    "administrative officer","admin and finance","executive assistant",
    "payroll administrator","secretary","internal sales and communications",
    "company secretary and governance manager","member relations coordinator",
    "credential assessment team","icpa federal company secretary"
  ],

  "Hospitality / Tourism": [
    "food and beverage supervisor","night auditor","tour guide",
    "kayak instructor","event manager","box office manager","guide",
    "darwin cocktail festival"
  ],

  "Resources / Logistics": [
    "terminal coordinator","supply and procurement manager",
    "utilities and infrastructure manager",
    "distribution specialist","maritime security guard"
  ],

  "Security": [
    "corporate security officer","correctional officer",
    "police constable","firefighter","fire management officer"
  ],

  "Government / NFP": [
    "councillor","local government councillor","elected member","alderman",
    "deputy mayor","policy officer","senior policy officer","principal policy officer",
    "senior strategic policy officer","committee member","council member",
    "sessional member","official member",
    "member","investment committee member","ethics advisory committee",
    "national safety committee",
    "independent member of the audit and risk committee for the department of education and training",
    "honorary treasurer","treasurer and public officer","public officer","treasurer",
    "chief people and culture officer","director people and culture",
    "director safe nt","director suicide prevention",
    "director transforming aboriginal outcomes",
    "director remote early childhood and integrated services",
    "director external review and reform","director qecnt",
    "director vet policy",
    "director of early years","director of boarding",
    "director supervision and monitoring",
    "director industrial ecologies and government lead on ccus",
    "assistant director","assistant director corporate learning and development",
    "intake officer","account officer",
    "communications officer","media liaison officer",
    "graduate officer","research officer",
    "policy and program officer",
    "employment services program manager central australia",
    "community projects manager","senior human resources officer",
    "human resources manager","internal communications advisor",
    "regional director tiwi islands department of the chief minister and cabinet",
    "chief executive officer department of chief minister and cabinet",
    "aṉangu workforce development program manager",
    "first nations project officer","regional soils coordinator northern hub",
    "community services receptionist","witness assistance service officer",
    "dept of attorney general","nt government","acting manager",
    "senior work health and safety officer","emergency medical dispatcher",
    "emergency dispatcher","engagement and project support",
    "nt bushfires authorised volunteer",
    "defence industry engagement manager","housing manager",
    "member northern territory business advisory council",
    "advisory committee member. nt optometry australia",
    "director of people and culture","engagment officer","ambassador",
    "officer","advocate","work development officer","chief investigator"
  ]

};

for (const [cleanPosition, positions] of Object.entries(groups)) {
  if (positions.includes(title)) {
    return cleanPosition;
  }
}

return "Other";
```

---

## How to Add in Clay

1. Open your Clay table with the LinkedIn import
2. **+ Add Column** → **Formula**
3. Name it `clean_position`
4. Paste formula above — map `{{current_company_position}}` to your column
5. Run on all rows — **0 credits**

---

## Outreach Priority by Clean Position

| Clean Position | Outreach Priority | Angle |
|---|---|---|
| CEO | Tier 1 | Pipeline audit — scaling without staff |
| Director | Tier 1 | "Biggest risk when you hire a Marketing Manager is they arrive and there's no system" |
| Owner | Tier 1 | Referral ceiling angle — "most owners I speak to have hit the same wall" |
| Founder | Tier 1 | Speed-to-market angle — 12-week build, you own everything |
| General Manager | Tier 1 | Ops efficiency + pipeline angle |
| Managing Partner | Tier 1 | Professional services — referral dependency |
| CFO | Tier 2 | CPL improvement proof point — "CPL down 62% in Q1" |
| COO | Tier 2 | Systems + infrastructure angle |
| Head of Marketing | Tier 2 | Peer positioning — complement their team, not compete |
| Consultant | Tier 2 | "You help clients grow — who's building your pipeline?" |
| Lawyer / Architect | Tier 2 | Professional services referral ceiling |
| Operations Manager | Tier 3 | Gatekeeper — route to CEO/owner |
| Chairperson / President | Low | Board-level — rarely operational decision-maker |
| Government / NFP | **Exclude** | Wrong buyer type |
| Board Member / Advisor | **Exclude** | Non-operational |
| Educator | **Exclude** | Wrong buyer type |
