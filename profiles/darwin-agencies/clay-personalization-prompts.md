# Darwin Agencies — Clay Personalization Prompts
# ColdIQ Framework | AI Prompt Library for NT Agencies Outreach
Generated: 2026-07-27

---

## Overview

All Clay AI prompts for the Darwin agencies campaign, plus the agency pain library used to calibrate AI output. The core frame throughout is the **cobbler's children paradox** — agencies help clients win business but run their own new business on referrals and hustle.

---

## Agency Pain Library

### Recruitment / Labour Hire Agencies
- New employer-client relationships start through personal connections — someone the founder or BD person already knows
- Cold BD = cold calls down the phone book — no inbound, no digital, no system
- When a hiring manager moves on, the relationship needs rebuilding from scratch
- Labour hire agencies are particularly referral-heavy — procurement buyers use the same 2-3 agencies they've always used
- Google presence is near zero for most Darwin labour hire firms

**Darwin-specific:** NT mining, construction, and government are the target buyer segments. All three industries use preferred-supplier panels — DGK builds the digital presence that gets agencies onto those panels.

### Marketing / Creative / Digital Agencies
- Classic cobbler's children: expert at building client pipelines, running on referrals for their own
- Most Darwin marketing agencies have 3-5 anchor clients — if one leaves, revenue drops 30-40%
- No cold outbound: "we don't need to do outbound, we get inbound referrals"
- Zero Google presence for their own agency: no reviews, no blog, weak SEO
- LinkedIn underused for new business: profiles not optimised, no content strategy

**Darwin-specific:** Darwin is a small market — most creative work goes to East Coast agencies or is won by 2-3 local incumbents. DGK's angle: the agencies that dominate NT win it through local presence and trust, not product superiority.

### Event / PR / Communications
- Project-based revenue model: no retainer pipeline, feast or famine
- New projects come through existing client relationships or industry contacts
- No system for converting project clients into retainer clients
- Darwin event/PR market is small — limited TAM, which makes pipeline predictability critical
- No digital outbound: all BD is relationship-based, which is labour-intensive

**Darwin-specific:** NT government events and corporate Darwin events are the highest-value segments. Agencies that win NT government event retainers have a digital presence that signals credibility to procurement teams.

### NDIS / Health Services Agencies
- Participant pipeline = coordinator referrals = dependent on 5-10 coordinator relationships
- No direct outbound to potential participants — NDIS rules create compliance anxiety
- Referral partnership system is informal: no CRM, no follow-up, no pipeline visibility
- Google presence matters — participants and families Google NDIS providers before calling
- Review strategy is non-existent: most Darwin NDIS providers have < 5 Google reviews

**Darwin-specific:** NT has one of the highest NDIS per-capita participation rates in Australia. Darwin NDIS providers that build coordinator referral systems and Google presence have sustainable growth; others plateau.

### Training / RTO Organisations
- Institutional client acquisition comes through tenders, government contracts, and existing relationships
- No outbound to attract new corporate or government training clients
- RTO compliance anxiety limits marketing confidence
- Most Darwin RTOs have weak Google presence — poor for attracting individual learners
- Revenue is lumpy: big government contracts separated by dry patches

---

## Chain-of-Thought Prompt: `agency_opener`

**Purpose:** First line of Email 1
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row

**Full Prompt:**
```
You are writing the opening line of a cold email from DGK Business Consultancy to an agency owner in Darwin, NT, Australia.

The core message is: agencies help their clients build pipelines but run their own new business on referrals and hustle. DGK fixes that.

CONTEXT:
- Recipient: {{first_name}}
- Company: {{current_company}}
- Agency type: {{industry_group}}
- Headline: {{headline}}
- Description: {{Description}}
- Position: {{current_company_position}}

CHAIN OF THOUGHT (think through, return only the final sentence):

Step 1 — What agency type?
Recruitment / Marketing / Event / Health-NDIS / Training / Media / Other

Step 2 — What is the cobbler's paradox for this type?
- Recruitment: "Helps employers build great teams — wins its own new employer clients through cold calls and relationships"
- Marketing: "Builds marketing pipelines for clients — runs its own new business on referrals"
- Event/PR: "Creates reach for clients' brands — wins its own work through existing contacts"
- NDIS/Health: "Delivers participant outcomes — new participants come through coordinator word-of-mouth"
- Training: "Upskills other organisations — wins institutional clients through tenders and warm relationships"

Step 3 — Is there a specific detail in Description or headline to use?
- YES: use it to make the opener specific ("Darwin's [X] agency..." or "[specific service] businesses in NT...")
- NO: use the category-level cobbler's pattern

Step 4 — Write the sentence:
- 10-15 words max
- Peer-level tone — someone who understands how Darwin agencies work
- No "I noticed", "I saw", "Congratulations"
- No explicit signal mention (hiring, reviews, etc.)
- Observational, sets up "how do you win your own new clients"

RETURN ONLY THE FINAL SENTENCE. No explanation.

GOOD EXAMPLES:
- "Darwin marketing agencies are usually the last ones to have a marketing system for their own new business."
- "Most Darwin recruitment agencies win new employer clients the same way — through who they know."
- "NDIS providers in the NT tend to grow through coordinator referrals — which is great until the referral pool plateaus."
- "Event agencies in Darwin win new projects through relationships — which works right up until it doesn't."

BAD EXAMPLES:
- "I noticed you're hiring..." (signal)
- "Congratulations on your growing agency." (hollow)
- "I saw your website..." (generic)
- "As a fellow Darwin business..." (weak)
```

---

## Chain-of-Thought Prompt: `agency_pain_line`

**Purpose:** Middle of Email 3
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row

**Full Prompt:**
```
You are writing one sentence for the middle of Email 3 in a cold email sequence to a Darwin agency owner.

This sentence is a pain observation — it names the new business pain specific to this agency type in Darwin.

CONTEXT:
- Company: {{current_company}}
- Agency type: {{industry_group}}
- Description: {{Description}}
- Hiring: {{Hiring Status & Job Openings hiring Status}}
- Revenue: {{Annual Revenue}}

CHAIN OF THOUGHT:

Step 1 — What is the new business acquisition pattern for this agency type?
- Recruitment: "New employer clients come from existing relationships and cold calls — no inbound"
- Marketing: "New clients are won through referrals and word of mouth — no cold pipeline"
- Event/PR: "New projects come through existing client relationships — feast or famine"
- NDIS/Health: "New participants come through coordinator referrals — dependent on 5-10 key relationships"
- Training: "New corporate clients come through tenders and government relationships"

Step 2 — Is the agency hiring or growing? If yes, add urgency (more staff = need more clients faster).

Step 3 — Write ONE sentence that:
- Names the pain clearly but without being accusatory
- Is 15-20 words maximum
- Sounds like an observation from someone who knows Darwin agencies
- Connects naturally to "how are you currently winning new clients outside your existing network?"

RETURN ONLY THE FINAL SENTENCE.

EXAMPLES:
- "Most Darwin agencies at {{company}}'s stage win new clients the same way — through who they know."
- "Recruitment agencies in Darwin typically build employer relationships through BD calls and referrals — there's rarely a system behind it."
- "Marketing agencies in the NT are usually the last ones to apply to themselves what they build for clients."
- "NDIS providers in Darwin are often growing through coordinator relationships that work until a key coordinator changes roles."
```

---

## Qualification Scoring Formula (`qualification_score`)

```javascript
let score = 0;
const reasons = [];

const tier = String({{Position Tier}} || "").toUpperCase();
if (tier === "A") { score += 3; reasons.push("Tier A"); }
else if (tier === "B") { score += 1; reasons.push("Tier B"); }

const group = String({{industry_group}} || "");
const highValueAgency = ["Recruitment", "Marketing", "Health"].includes(group);
if (highValueAgency) { score += 2; reasons.push(`High-value agency type: ${group}`); }
else if (group !== "Other") { score += 1; reasons.push(`Agency: ${group}`); }

const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
if (hiring.includes("hiring")) { score += 2; reasons.push("Active hiring"); }

const reviews = parseInt({{Reviews}} || 0);
const rating = parseFloat({{Rating}} || 0);
if (reviews >= 5 && rating >= 4.0) { score += 2; reasons.push("Strong Google presence"); }
else if (reviews >= 1) { score += 1; reasons.push("Some Google reviews"); }

const revenue = String({{Annual Revenue}} || "").toLowerCase();
if (revenue.match(/\d+m/) || revenue.includes("million")) {
  score += 1; reasons.push("Revenue confirmed");
}

const premium = String({{badges_premium}} || "").toLowerCase();
if (premium === "true") { score += 1; reasons.push("LinkedIn Premium"); }

const email = String({{Work Email}} || {{email}} || "").trim();
if (!email.includes("@")) { score = 0; reasons.push("NO EMAIL — exclude"); }

return `Score: ${score} | ${reasons.join(" | ")}`;
```

---

## Darwin Agencies — Calibration Reference

When reviewing AI output, check against these NT-specific truths:

| Claim | True for Darwin? | Note |
|---|---|---|
| Agencies run their own BD on referrals | YES — universally true | Safe cobbler's angle |
| Marketing agencies have no new business system | YES — strongest form of cobbler's paradox | Use for marketing segment |
| NDIS providers grow through coordinator referrals | YES — NT NDIS market is coordinator-driven | Use for NDIS segment |
| Recruitment agencies win employer clients through relationships | YES — especially NT mining/government/construction | Use for recruitment segment |
| Darwin agency market is small — reputation travels fast | YES | Use for NT social proof angle |
| Government procurement is key for some agencies | YES — NT government is major buyer | Use for agencies serving government |
| Most Darwin agencies have weak Google presence | YES | Use for Google reviews PS |

---

## Prompt Maintenance

- Test batch: 10 rows minimum before full campaign send
- Read every `agency_opener` — reject generic, salesy, or trigger-mentioning outputs
- Acceptable failure rate: <15% (agencies are niche — prompts need tuning)
- Review `agency_pain_line` for specificity — should feel agency-type-specific, not generic B2B
- Rebuild prompt if failure rate > 20%
