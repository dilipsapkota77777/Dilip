# DGK Business Consultancy — Darwin NT Full GTM System
Generated: 2026-06-28 | List: 1,078 Darwin NT Decision Makers | Clay Budget: 5,000 credits

---

## PART 1 — WHAT DGK ACTUALLY SELLS (Know This Cold)

**Model:** Done-With-You (not done-for-you agency, not a DIY course)
**Tagline:** "The issue isn't effort. It's the infrastructure that was missing behind it."
**Engagement:** 12 weeks. Client owns everything. No lock-in. No retainer.
**Services:** Foundation Plan · Outbound Lead Gen · Content System · LinkedIn Ads
**Proof:** 20+ clients, 7 industries, 10 months

| Result | Industry |
|---|---|
| 0 → 6 qualified enquiries/month in 60 days | IT Services |
| Marketing hire ramped in 3 weeks vs 3+ months | Accounting |
| Daily content across 6 platforms, owner not writing a word | NDIS |
| CPL down 62% in Q1 | Legal |
| Full system handover in 12 weeks, no retainer needed | Recruitment |
| Same-week outreach from SEEK hiring signals | Financial Planning |

**Primary CTA everywhere:** "Worth a free 30-min pipeline audit?"

---

## PART 2 — ICP DEFINITION (Darwin-Specific)

### Hard Filters (must match ALL)
- **Title:** Owner / Director / CEO / Founder / Managing Director / Principal / Partner
  - NOT: Manager, Coordinator, Consultant (without ownership)
- **Location:** Northern Territory, Australia (Darwin + broader NT)
- **Business type:** B2B service business (NOT product, NOT government, NOT NFP)
- **Employees:** 3–50
- **Years in business:** 2+ (past pure survival stage)
- **Revenue estimate:** $300k+ AUD (has budget for $2,500–$8k/month)

### Soft Preferences (nice-to-have, use for scoring)
- Pipeline is referral-dependent (85%+ from word of mouth)
- Has website but no lead capture beyond "contact us"
- Not running Google/Facebook Ads for themselves
- LinkedIn profile exists but rarely/never posts
- Growing team (hiring signal on SEEK)
- Established brand (Google reviews, awards, longevity)

### Hard Excludes (never contact)
- Government / Public Sector / Councils / NT Government
- NFP / Charities / Community Organisations
- Solopreneurs (no employees)
- Enterprise (60+ staff — too complex for 12-week model)
- B2C-only businesses
- Competitors

### Priority Segments for Darwin List

| Rank | Segment | Why They're HOT | Est. Contacts |
|---|---|---|---|
| 1 | Professional Services | Referral-dependent, budget exists, decision-maker = owner | ~104 |
| 2 | Trades/Construction | Platform-dependent (Hipages), feast-or-famine, clear pain | ~57 |
| 3 | Agency/Consultancy | Cobbler's children, marketing-aware buyer | ~30 |
| 4 | Health (Private) | Private practice owners, understands marketing | ~69 |
| EXCLUDE | Gov/NFP | Not a fit | ~332 |
| TBD | Other/Unknown | Needs enrichment to classify | ~486 |

---

## PART 3 — ICP SCORING SYSTEM (100 Points)

### Clay Formula: `icp_score`

```javascript
const title = String({{raw_title}} || "").toLowerCase();
const segment = {{segment}} || "";
const hasEmail = !!({{email_final}} && {{email_final}}.includes("@"));
const hasLinkedIn = !!{{linkedin_url}};
const isHiring = String({{is_hiring}} || "").includes("YES");
const hiringMarketing = String({{is_hiring}} || "").toLowerCase().includes("marketing") ||
                         String({{is_hiring}} || "").toLowerCase().includes("business development") ||
                         String({{is_hiring}} || "").toLowerCase().includes("bdm");
const noSelfAds = {{runs_self_ads}} === "NO";
const onMarketplace = String({{on_marketplace}} || "").includes("YES");
const referralDependent = {{primary_acquisition}} === "Referral Only";

let score = 0;

// === TITLE (40 pts) ===
const tierA = ["owner","director","managing director","ceo","founder","co-founder","principal","partner","managing partner","proprietor"];
const tierB = ["general manager","gm","head of","operations manager"];
if (tierA.some(t => title.includes(t))) score += 40;
else if (tierB.some(t => title.includes(t))) score += 22;
else score += 8;

// === SEGMENT FIT (25 pts) ===
const topSegments = ["Professional Services","Agency","Health"];
const goodSegments = ["Trades"];
if (segment === "EXCLUDE - Gov/NFP") return 0;
if (topSegments.includes(segment)) score += 25;
else if (goodSegments.includes(segment)) score += 20;
else if (segment === "Other") score += 10;

// === BUYING SIGNALS (25 pts — stack for heat score) ===
if (hiringMarketing) score += 25;       // HIGHEST — hiring to solve this exact problem
else if (isHiring) score += 15;         // HIGH — growing, needs system
if (onMarketplace) score += 12;         // Paying per lead = pain
if (referralDependent) score += 10;     // Core pain confirmed
if (noSelfAds) score += 5;              // Cobbler's children angle

// === DATA QUALITY (10 pts) ===
if (hasEmail) score += 6;
if (hasLinkedIn) score += 4;

return Math.min(score, 100);
```

### Priority Tier Formula: `priority`

```javascript
const score = {{icp_score}};
const segment = {{segment}} || "";
if (segment === "EXCLUDE - Gov/NFP" || score === 0) return "EXCLUDE";
if (score >= 75) return "HOT 🔥";
if (score >= 50) return "WARM";
if (score >= 30) return "COLD";
return "NOT QUALIFIED";
```

---

## PART 4 — SIGNAL-BASED CAMPAIGN TABLE (20 Campaigns)

### Darwin NT — Campaign Master List

| # | Campaign Name | Level | List Filters | Signal | AI Strategy | Value Prop | Template |
|---|---|---|---|---|---|---|---|
| 1 | Darwin Decision Makers — Broad | Broad | All non-Gov/NFP owners/directors | None | Company description + segment opener | "Build a pipeline that doesn't stop when referrals do" | Not Too Different Persona |
| 2 | Referral-Dependent Darwin | Broad | All segments — referral language on website | Website has "referrals"/"word of mouth" | Claygent scans website for referral language | "What happens when your best referral source goes quiet?" | Ask Before Pitch |
| 3 | SEEK Hiring — Marketing/BD Role | Focused | Any Darwin B2B company hiring Marketing Manager or BDM on SEEK | Active SEEK job ad | Extract job title + requirements from posting | "Biggest risk: they arrive and there's no system" | Leverage Content |
| 4 | Platform-Dependent Tradies | Focused | Trades segment, listed on Hipages/ServiceSeeking | Marketplace listing found | Find platform listing, extract jobs done/reviews | "Stop paying per lead. Own your pipeline." | Why Are You Paying? |
| 5 | Professional Services — Pre-EOFY | Focused | Accountants, financial advisors, lawyers | Timing: March–May send | Check for content/blog on website | "After EOFY, where are your next clients coming from?" | Ask Before Pitch |
| 6 | Cobbler's Children — Agency | Focused | Agency/consultancy segment, no self-ads | No Facebook/Google ads detected | Facebook Ads Library check | "You help clients get leads. Who's helping you?" | Not Too Different Persona |
| 7 | SEEK Hiring — Growth Signal | Focused | All segments, hiring operations/staff roles | Any SEEK job posting | Extract role + company growth stage | "Before you scale ops, the sales system needs to be automated" | Upfront Value |
| 8 | Low Google Reviews — Established | Focused | 3+ years old, <20 Google reviews | Review gap vs business age | Google reviews count + years in business | "Your reputation doesn't match your quality online" | Creative Ideas |
| 9 | LinkedIn Inactive Owners | Focused | Owner/Director, 0 posts in 90+ days | LinkedIn last post date | LinkedIn activity check | "Darwin's best businesses are invisible online. Their competitors aren't." | Upfront Value |
| 10 | No Lead Capture on Website | Focused | Has website, no opt-in/lead magnet | Website contact form only | Check website for lead capture beyond "contact us" | "You have a website. Not a lead machine. Here's the difference." | Creative Ideas |
| 11 | Commercial Builder + Hiring | Niche | Construction, 10+ staff, hiring tradespeople | SEEK job posting for tradespeople | Job posting extraction + team size | "You're hiring because you have work. Let's make sure the pipeline matches your new capacity." | Ask Before Pitch |
| 12 | Health — Telehealth + Private Fees | Niche | Health segment, telehealth + private fees only | Website mentions telehealth + private fee | Website check for telehealth + fee structure | "You can serve clients nationally. Your marketing is still local." | Not Too Different Persona |
| 13 | NT Business Award Winners/Nominees | Niche | Any segment, award mention on LinkedIn/website | Award mention in last 18 months | Search for award mentions | "You're recognised as one of NT's best. Does your pipeline reflect that?" | Upfront Value |
| 14 | Podcast/Speaking Appearances | Niche | Any segment, appeared on podcast or panel | Podcast guest in last 12 months | Search for podcast guest appearances | "You're clearly comfortable with visibility — let's turn that into a lead gen asset." | Leverage Content |
| 15 | Recent Website Redesign | Niche | Any segment, new website in last 6 months | Website build date recent | BuiltWith/Claygent for website launch date | "Fresh website — great. Now let's make it generate leads instead of just looking good." | Creative Ideas |
| 16 | No Case Studies Visible | Niche | Professional Services, no testimonials online | Website check for social proof | Claygent checks for testimonials/case studies | "You have happy clients. Prospects can't find the proof." | Upfront Value |
| 17 | Price-Competing Language | Niche | Any segment, "competitive rates"/"affordable" on website | Price-competing copy on website | Website headline/copy analysis | "Price competition is a race to the bottom. Here's how to compete on outcomes instead." | Creative Ideas |
| 18 | Multi-Location Business | Niche | 2+ locations in Darwin/NT area | Multiple addresses on website | Count locations from Google/website | "Two locations. One broken acquisition system. Let's fix that." | Not Too Different Persona |
| 19 | Darwin Local — Hyper-Relevant | Niche | All Darwin-based, ANY segment | Geographic — Darwin/NT only | Local reference + Darwin-specific proof | "One of the few growth systems built specifically for Darwin businesses" | Case Study Reference |
| 20 | Seasonal — Dry Season Planning | Niche | Tourism, outdoor, events, construction | April–May timing | Business type + seasonal signal | "Use the dry season momentum to fund a pipeline that works year-round" | Ask Before Pitch |

---

## PART 5 — GEOGRAPHICAL TARGETING STRATEGY

### Phase 1: Darwin Core (Now — 1,078 contacts)
- **Who:** Darwin CBD + suburbs decision makers
- **Why start here:** Local advantage, face-to-face option, fastest trust
- **Campaign angle:** "One of the few growth consultancies based in Darwin — not a Sydney firm parachuting in"
- **Expected qualified:** ~200-300 after scoring

### Phase 2: Broader NT Expansion (Month 2-3)
- **Who:** Alice Springs, Palmerston, Katherine, Tennant Creek
- **List build:** Apollo search (Title: Owner/Director + State: NT + Industry: ICP industries)
- **Estimated new list:** 300-500 contacts
- **Angle:** Same Darwin campaigns but reference NT-wide reach

### Phase 3: National Expansion via LinkedIn (Month 3+)
- **Who:** All ICP industries in Australia (from existing campaign-strategy.md)
- **Best campaigns to scale nationally:** #3 (SEEK signal), #5 (EOFY), #6 (Cobbler's children)
- **Scale via:** Prospeo + LinkedIn outreach (not just email)
- **Advantage:** Proven Darwin results become national social proof ("we did it for Darwin, we can do it for you")

### Phase 4: Remote/Virtual Clients (Ongoing)
- **Segments that work fully remote:** Professional Services + Agency/Consultancy
- **Angle:** "We built the system for a Darwin accounting firm in 12 weeks — all via Zoom. Same process, wherever you are."
- **Target:** Any Australian ICP industry, not geography-locked

---

## PART 6 — 5,000 CLAY CREDIT BUDGET PLAN

### Guiding Principle
Run in priority order. The most valuable credit is the one that finds a valid email.
Filter at every step so Claygent only runs on the best contacts.

### Credit Allocation Table

| Phase | Action | Contacts | Credits/Each | Total Credits | Cumulative |
|---|---|---|---|---|---|
| 1 | Segment formula + ICP score formula | 1,078 | 0 (formula) | 0 | 0 |
| 2 | Remove Gov/NFP | 1,078 → 746 | 0 (filter) | 0 | 0 |
| 3 | Apollo Company Domain Search | 746 | 1 | 746 | 746 |
| 4 | Apollo Email Finder | 746 | 1 | 746 | 1,492 |
| 5 | Prospeo (fires if Apollo fails, ~55% = 410) | 410 | 1 | 410 | 1,902 |
| 6 | LeadMagic (fires if Prospeo fails, ~40% = 205) | 205 | 1 | 205 | 2,107 |
| 7 | Findymail (fires if LeadMagic fails, ~25% = 123) | 123 | 1 | 123 | 2,230 |
| 8 | Email Verification (~370 valid emails found) | 370 | 1 | 370 | 2,600 |
| 9 | SEEK Hiring Signal — Claygent (HOT/WARM 200) | 200 | 3 | 600 | 3,200 |
| 10 | Segment Signal (marketplace/self-ads/telehealth) | 200 | 3 | 600 | 3,800 |
| 11 | Company Description — Claygent (final 120) | 120 | 3 | 360 | 4,160 |
| 12 | Personalized Opener — Claygent (final 120) | 120 | 5 | 600 | 4,760 |
| 13 | Buffer (retries, extra lookups) | — | — | 240 | 5,000 |

**Expected output:** ~120 contacts with valid email + personalized opener + company description + signal data

### Run Order in Clay (Step by Step)

```
Step 1:  Upload CSV (semicolon delimiter) → 1,078 rows
Step 2:  Run Segment Formula → filter, mark Gov/NFP as EXCLUDE
Step 3:  Run ICP Score formula (partial — no email signal yet)
Step 4:  Filter: show only non-EXCLUDE = 746 rows
Step 5:  Run Apollo Company Search → fills company_domain column
Step 6:  Run Email Waterfall (Apollo → Prospeo → LeadMagic → Findymail) — conditional
Step 7:  Run waterfall merge formula → email_final column
Step 8:  Run Email Verification on email_final
Step 9:  Filter: Valid email only (~280-370 rows)
Step 10: Re-run ICP Score (now with email data) → update priority
Step 11: Filter: HOT + WARM only (~150-200 rows)
Step 12: Run Claygent — is_hiring (SEEK signal)
Step 13: Run Claygent — segment-specific signal (marketplace/self-ads/etc.)
Step 14: Re-score → final priority ranking
Step 15: Run Claygent — company_description (top 120)
Step 16: Run Claygent — email_opener (top 120)
Step 17: Export to Smartlead by segment
```

---

## PART 7 — SEGMENT-SPECIFIC PITCH ANGLES WITH CASE STUDY MATCHING

### Segment 1: Professional Services
**Best Case Study Match:** "CPL down 62% for a legal firm in Q1" + "Marketing hire ramped in 3 weeks (accounting)"
**Core Pain:** Referral-dependent, no second channel
**Pitch Frame:** Referral Diversification

**Subject Lines (test all 3):**
- `pipeline gap`
- `referral ceiling`
- `beyond referrals`

**Email 1 — Not Too Different Persona:**
```
{{firstName}},

Most [accountants/lawyers/financial advisors] in Darwin I speak to are getting 
80-90% of new clients from referrals — one relationship going quiet and the 
quarter gets ugly.

We helped a legal firm in Australia cut their CPL by 62% in Q1 by building 
a second channel alongside the referrals, not instead of them.

Worth a free 30-min pipeline audit to see if the same approach fits 
{{company_name}}?

[Name]
DGK Business Consultancy
```

---

### Segment 2: Trades & Construction
**Best Case Study Match:** None direct yet → use IT result as analogy ("0 to 6 enquiries in 60 days")
**Core Pain:** Platform dependency (Hipages), feast-or-famine
**Pitch Frame:** Own Your Pipeline

**Subject Lines:**
- `hipages alternative`
- `quiet months`
- `more jobs`

**Email 1 — Why Are You Paying? (Platform-Dependent angle):**
```
{{firstName}},

Quick question about {{company_name}} —

Are you currently on Hipages, ServiceSeeking, or similar platforms to find work?

I ask because most Darwin tradies I speak to are paying $80–$200 per lead on 
these platforms, competing against 5-10 others for the same job.

We built a system for a Darwin [trade type] that took them off the platforms 
entirely and got them 6+ qualified enquiries a month through their own pipeline.

Same model — you own it at the end, no retainer.

Worth a quick 30-min call to see if it'd work for {{company_name}}?

[Name]
DGK Business Consultancy
```

**Email 1 — No Marketplace Signal (broader Trades):**
```
{{firstName}},

Most trade business owners in Darwin I work with have the same pattern — 
summer's flat out, cooler months get quieter. Referrals fill the gaps but 
never quite enough.

We helped a similar business go from feast-or-famine to 6 consistent enquiries/month 
in 60 days by building a lead system they actually own.

If I could show you the exact framework in 30 minutes, would that be worth your time?

[Name]
```

---

### Segment 3: Agency & Consultancy
**Best Case Study Match:** None direct — use the meta-sell angle (they help others)
**Core Pain:** No outbound for themselves
**Pitch Frame:** Cobbler's Children

**Subject Lines:**
- `your pipeline`
- `cobbler's shoes`
- `who's helping you`

**Email 1 — Cobbler's Children:**
```
{{firstName}},

I imagine {{company_name}} helps [clients] grow their business.

Quick question — who's building {{company_name}}'s pipeline?

I ask because most Darwin agencies and consultancies I speak to have feast-or-famine months, 
and their own client acquisition is still 90% referrals.

We're one of the few consultancies that builds outbound systems for other consultancies.

Ironic? Maybe. Effective? Very.

30-min pipeline audit — worth it?

[Name]
DGK Business Consultancy
```

---

### Segment 4: Health (Private Practice)
**Best Case Study Match:** None direct → use general "0 to 6 enquiries" framework
**Core Pain:** Word of mouth only, no systematic patient acquisition
**Pitch Frame:** Systematic Acquisition

**Subject Lines:**
- `new patients`
- `referral system`
- `beyond GP referrals`

**Email 1 — Ask Before Pitch:**
```
{{firstName}},

How does {{company_name}} currently get new [patients/clients]?

I ask because most private practice owners in Darwin are 80-90% dependent 
on GP referrals or word of mouth — which works until one GP moves practice 
or a slow month hits.

We help private health businesses build a second acquisition system alongside 
the referrals — without advertising in a way that feels uncomfortable.

Worth a 30-min call to walk through what that could look like for {{company_name}}?

[Name]
```

---

## PART 8 — FULL 5-EMAIL SEQUENCE PER SEGMENT

### Sequence Timing (all segments)
- Email 1: Day 1 (Main angle)
- Email 2: Day 3 (Different proof point)
- Email 3: Day 7 (Value/resource)
- Email 4: Day 14 (Softer follow-up)
- Email 5: Day 21 (Breakup)

---

### PROFESSIONAL SERVICES — 5-Email Sequence

**Email 1 (Day 1) — Referral Diversification**
Subject: `{{subject_line}}` (AI-generated 2-word subject)

```
{{firstName}},

{{email_opener}}

We helped a legal firm cut their CPL by 62% in Q1 and an accounting firm 
ramp a new marketing hire in 3 weeks — by building the system first.

Worth a free 30-min pipeline audit to see if the same applies to {{company_name}}?

[Calendly link]

[Name]
```

**Email 2 (Day 3) — The "Done-With-You" Differentiator**
Subject: `not an agency`

```
{{firstName}},

Most growth consultancies take over your marketing and you become dependent on them.

We do the opposite — we build the system with you, and after 12 weeks you own 
everything. No retainer. No lock-in.

The accounting firm I mentioned? Their hire plugged straight into the system 
we built. Up and running in 3 weeks instead of the usual 3 months.

30 minutes to walk through how that works for a [profession] practice?

[Name]
```

**Email 3 (Day 7) — Resource Offer**
Subject: `sending this over`

```
{{firstName}},

Put together a quick framework on how professional services firms in Australia 
are building outbound pipelines alongside referrals (not instead of them).

Specifically relevant if:
- 70%+ of new clients currently come from referrals
- One referral source going quiet would hurt your quarter
- You want a system that doesn't depend on one person's relationships

Want me to send it over? No call needed — just say yes.

[Name]
```

**Email 4 (Day 14) — Gentle Nudge**
Subject: `{{firstName}}`

```
{{firstName}},

Sent a few notes your way recently about pipeline diversification for 
[profession] practices.

If the timing's wrong — totally fine, just say the word and I'll stop.

If it's on your radar at all, the 30-min audit takes nothing off your plate 
and gives you 3 specific steps regardless of whether we work together.

[Calendly link]

[Name]
```

**Email 5 (Day 21) — Breakup**
Subject: `closing the loop`

```
{{firstName}},

I'll stop reaching out after this one — I don't want to be in your inbox 
if it's not relevant.

If referral dependency and pipeline predictability ever becomes the pressing 
issue at {{company_name}}, the offer for a free 30-min pipeline audit stands.

We've done it for [legal / accounting / professional services] firms and the 
results have been consistent.

All the best either way.

[Name]
```

---

### TRADES/CONSTRUCTION — 5-Email Sequence

**Email 1 (Day 1)** — (See Segment Pitch Angles above — Platform or General version)

**Email 2 (Day 3) — The System Angle**
Subject: `own it`

```
{{firstName}},

The thing about Hipages, ServiceSeeking, and similar platforms is you're 
renting their audience.

The moment you stop paying, the leads stop.

We build systems where the leads come to you — email, SEO, Google, 
word-of-mouth funnelled through a process — and at the end of 12 weeks, 
{{company_name}} owns all of it. No ongoing fees.

Took an IT services company from 0 to 6 enquiries/month in 60 days with 
the same model.

Happy to walk through how it translates to a trade business — 30 minutes?

[Name]
```

**Email 3 (Day 7) — Social Proof Reference**
Subject: `dry vs wet season`

```
{{firstName}},

Darwin tradies always have the same problem — dry season is full-on, wet season 
gets quieter.

The businesses that don't have that problem are the ones that spent the dry season 
building a pipeline system instead of just riding the wave.

I've put together a quick breakdown of what that looks like for a trade business.

Want me to send it over?

[Name]
```

**Email 4 (Day 14)** — Gentle nudge (same structure as Prof Services Email 4)

**Email 5 (Day 21)** — Breakup (same structure, adapt profession reference)

---

### AGENCY/CONSULTANCY — 5-Email Sequence

**Email 1 (Day 1)** — Cobbler's Children (see above)

**Email 2 (Day 3) — Meta Proof**
Subject: `we did it for ourselves first`

```
{{firstName}},

The reason I can pitch this without irony is we built this system for DGK first.

20+ clients across 7 industries in 10 months. In Darwin.

For most of those clients, the main problem wasn't the quality of what they 
offered — it was the infrastructure that was missing behind it.

Sound familiar for {{company_name}}?

30-min call to walk through what a system like this looks like for an 
[agency/consultancy] your size?

[Calendly link]

[Name]
```

**Email 3 (Day 7) — Resource**
Subject: `agency outbound playbook`

```
{{firstName}},

Pulled together the exact outbound framework we use for agencies and consultancies 
who are tired of feast-or-famine client acquisition.

Specifically useful if:
- Most of your clients come from referrals or existing relationships
- You've tried content or ads but can't maintain consistency
- You want to build a pipeline you own (not rent from a platform)

Want me to send it? Just reply "yes" and it's yours.

[Name]
```

**Email 4 + 5** — Same structure as Professional Services.

---

## PART 9 — LINKEDIN OUTREACH SEQUENCES

### LinkedIn Strategy (all segments)
- Day 1: Connection request (NO note — higher acceptance rate)
- Day 3 after acceptance: LinkedIn Message 1
- Day 7: LinkedIn Message 2 (if no reply to Email 1-2)
- Day 12: LinkedIn Voice Note or Video (highest engagement tactic)

---

### LinkedIn Message 1 — Professional Services
```
Hi {{firstName}},

Thanks for connecting.

I work with [accountants/lawyers/financial advisors] in Darwin and noticed 
{{company_name}} — curious how you currently get most of your new clients?

Not pitching anything — genuinely interested in whether the referral-dependency 
pattern I see everywhere applies here too.

[Name]
```

### LinkedIn Message 2 — Trades
```
Hi {{firstName}},

Thanks for connecting.

Quick question for a [builder/electrician/plumber] in Darwin — is most of 
your work coming from existing clients and referrals, or do you have a 
consistent way to generate new enquiries?

[Name]
```

### LinkedIn Message 1 — Agency/Consultancy
```
Hi {{firstName}},

Thanks for connecting — I actually found you while looking at Darwin agencies 
helping local businesses grow.

Bit meta question: does {{company_name}} have a consistent outbound system 
for your own client acquisition, or is it still mostly referrals and inbound?

[Name]
```

---

## PART 10 — CLAY TABLE COLUMNS (MASTER LIST)

| Column | Type | Source | Priority |
|---|---|---|---|
| full_name | Text | CSV | Required |
| first_name | Formula | Split(full_name) | Required |
| raw_title | Text | CSV | Required |
| company_name | Text | CSV | Required |
| location | Text | CSV | Required |
| linkedin_url | URL | CSV | Required |
| phone_raw | Text | CSV | Optional |
| email_raw | Text | CSV | Optional |
| company_domain | Text | Apollo | Required |
| segment | Formula | Keyword classifier | Required |
| icp_score_v1 | Formula | Pre-email score | Required |
| email_apollo | Email | Apollo | Waterfall |
| email_prospeo | Email | Prospeo | Waterfall |
| email_leadmagic | Email | LeadMagic | Waterfall |
| email_findymail | Email | Findymail | Waterfall |
| email_final | Formula | Waterfall merge | Required |
| email_status | Text | Verification | Required |
| icp_score_v2 | Formula | Post-email score | Required |
| priority | Formula | HOT/WARM/COLD | Required |
| is_hiring | Text | Claygent (SEEK) | Signal |
| hiring_for | Text | Claygent | Signal |
| on_marketplace | Text | Claygent | Trades only |
| runs_self_ads | Text | Claygent | Agency only |
| primary_acquisition | Text | Claygent | Prof Services |
| offers_telehealth | Text | Claygent | Health only |
| google_reviews_raw | Text | Claygent | Trades |
| review_count | Formula | Extract number | Trades |
| virtual_capable | Formula | Logic | All |
| timing_signal | Formula | Signal stack | All |
| pitch_angle | Formula | Segment + signals | All |
| company_description | Text | Claygent | Personalization |
| top_3_problems | Text | Claygent | Personalization |
| subject_line | Text | Claygent | Personalization |
| email_opener | Text | Claygent | Personalization |
| smartlead_campaign | Formula | Segment router | Export |

---

## PART 11 — SMARTLEAD EXPORT & CAMPAIGN STRUCTURE

### 4 Campaigns in Smartlead

| Campaign | Segment Filter | Priority Filter | Email Filter | Est. Contacts |
|---|---|---|---|---|
| Darwin — Professional Services | Professional Services | HOT + WARM | Valid only | 40-80 |
| Darwin — Trades | Trades | HOT + WARM | Valid only | 20-40 |
| Darwin — Agency | Agency | HOT + WARM | Valid only | 10-25 |
| Darwin — Health | Health | HOT + WARM | Valid only | 15-30 |

### Smartlead Settings (All Campaigns)
- Emails per day per inbox: 30-40
- Delay between emails: 3-5 minutes
- Follow-up delays: as per sequences above
- Tracking: open tracking ON, click tracking OFF (deliverability)
- Unsubscribe: enabled (Spam Act compliance)

### Variables to Map from Clay → Smartlead

| Clay Column | Smartlead Variable |
|---|---|
| email_final | to_email |
| first_name | {{firstName}} |
| company_name | {{company}} |
| raw_title | {{title}} |
| segment | {{segment}} |
| subject_line | {{subject_line}} |
| email_opener | {{opener}} |
| company_description | {{companyDescription}} |
| pitch_angle | {{pitchAngle}} |

---

## PART 12 — NEXT STEPS (IN ORDER)

```
Week 1 — DATA
□ Upload Darwin CSV to Clay (semicolon delimiter)
□ Run segment formula + ICP v1 score + filter Gov/NFP
□ Run Apollo domain enrichment (746 contacts) → 746 credits
□ Run email waterfall (all 4 providers) → ~1,484 credits
□ Run email verification → ~370 credits
□ Filter to valid emails only

Week 1 — QUALIFICATION
□ Re-score ICP v2 (with email data)
□ Filter to HOT + WARM (~150-200 contacts)
□ Run is_hiring Claygent (SEEK signal) → 600 credits
□ Run segment-specific signal Claygent → 600 credits
□ Re-score and rank final HOT list

Week 2 — PERSONALIZATION
□ Run company_description Claygent (top 120) → 360 credits
□ Run email_opener Claygent (top 120) → 600 credits
□ Review all 120 openers manually (15-min quality check)
□ Fix any that are generic or off

Week 2 — LAUNCH
□ Export to Smartlead by segment (4 campaigns)
□ Set up sequences (5 emails each)
□ Map Clay variables to Smartlead
□ Test send to yourself (1 from each segment)
□ Run /spam-word-checker on all copy
□ Launch at 30 emails/day per inbox
□ Set LinkedIn connection requests for same contacts (Day 1)

Week 3-4 — MONITOR
□ Check open rates daily (target: 35%+)
□ Check reply rates weekly (target: 5-8% for signal-based)
□ Run /positive-reply-scoring on all replies
□ Book pipeline audit calls from positive replies
□ Iterate sequences based on results
```

---

## QUICK REFERENCE — DGK PROOF POINTS BY SEGMENT

Use these to match case studies to each prospect segment:

| Segment | Best Proof Point | How to Reference |
|---|---|---|
| IT/MSP | 0 → 6 enquiries in 60 days | "We did this for an IT firm last quarter" |
| Accounting | Marketing hire ramped in 3 weeks | "We built the system before the hire started" |
| NDIS | Daily content, owner not writing a word | "They publish daily, spends zero time on it" |
| Legal | CPL down 62% in Q1 | "Legal firm cut their CPL by 62% this quarter" |
| Recruitment | Full handover in 12 weeks, no retainer | "They own the whole system now" |
| Financial Planning | Same-week outreach from SEEK signals | "First responses came within days of launch" |
| Trades* | Use IT result as analogy | "Same 60-day model works for trade businesses" |
| Agency* | Use DGK itself as proof | "We built this for ourselves first — 20 clients in 10 months" |
| Health* | Use generic 0→6 framework | "Same framework, adapted for practice acquisition" |

*No direct case study yet — build one fast by getting a Darwin pilot client in each.

---

Generated by Claude Code | DGK GTM System v1.0
Run `/campaign-copywriting` to write full copy for any campaign in the table above.
Run `/spam-word-checker` before uploading sequences to Smartlead.
Run `/smartlead-campaign-upload-public` to automate the Smartlead upload.
