# Darwin Professional Services — Clay Personalization Prompts
# ColdIQ Framework | AI Prompt Library for NT Professional Services Outreach
Generated: 2026-07-27

---

## Overview

This file contains all Clay AI prompts for the Darwin professional services campaign, plus the industry pain library used to calibrate AI output. Prompts are designed to produce openers and pain lines that feel specific to the NT professional services market — not generic B2B copy.

---

## Industry Pain Library

Use this as internal reference. AI prompts draw on these patterns automatically.

### Accounting Firms
- Revenue is heavily seasonal — strong Q1 (EOFY), flat Q3-Q4
- New clients come through existing client referrals, not cold enquiry
- Partners are too busy doing work to build a pipeline
- Most have never done outbound — they don't know where to start
- Government and corporate clients require a strong online presence for procurement research

**Darwin-specific:** NT government is a major client for Darwin accounting firms — positioning around government procurement is high-value.

### Legal / Law Practices
- Professional conduct rules create anxiety about "marketing"
- All new clients come through referrals from existing clients or other professionals
- Solicitors have strong expertise but no system to turn expertise into inbound leads
- Google and LinkedIn are underutilised — most Darwin law firms have weak online presence
- No review strategy — but reviews are the #1 way clients choose a lawyer in Darwin

**Darwin-specific:** Darwin legal market is small — reputation travels fast. Firms with strong Google presence win referrals from outside their immediate network.

### Business Consulting / Advisory
- Classic feast-or-famine project cycle — full capacity or hunting for the next client
- Most work is project-based — no retainer model = no predictable revenue
- Strong word-of-mouth within NT government and corporate circles
- No outbound system — all business development is relationship-based
- LinkedIn is underused by Darwin consultants compared to their East Coast peers

**Darwin-specific:** NT government consulting market is tight — those who win repeat work have better visibility, not better relationships.

### HR / Recruitment Agencies
- New clients come from personal relationships with HR managers and hiring managers
- Client acquisition = BD phone calls and referrals — no inbound system
- Job boards and LinkedIn are procurement channels, not acquisition channels
- Recruitment agencies are great at placing people but terrible at placing themselves
- Revenue fluctuates with hiring cycles — no counter-cyclical pipeline

**Darwin-specific:** NT hiring market is tight. Recruitment agencies that get in front of mining, government, and construction companies early win the retained business.

### Financial Planning / Insurance
- All new clients come through referrals from accountants, solicitors, or existing clients
- ASIC compliance anxiety limits marketing — most planners under-market their services
- Most financial planners in Darwin do not appear in Google search for key terms
- Clients choose financial advisors based on trust — Google reviews are decisive
- No digital follow-up system — leads go cold after the first consultation

**Darwin-specific:** Darwin financial planning market is dominated by 3-4 large practices. Smaller independent planners win by hyper-local visibility and niche positioning.

---

## Chain-of-Thought Prompt: `ps_opener`

**Purpose:** First line of Email 1 — professional services segment
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row

**Full Prompt:**
```
You are writing a one-sentence cold email opener for DGK Business Consultancy, reaching out to a professional services firm owner in Darwin, Northern Territory, Australia.

CONTEXT:
- Recipient name: {{first_name}}
- Company name: {{current_company}}
- Industry group: {{industry_group}}
- LinkedIn headline: {{headline}}
- Company description: {{Description}}
- Position: {{current_company_position}}
- Hiring: {{Hiring Status & Job Openings hiring Status}}

CHAIN OF THOUGHT (think through this step by step, but return ONLY the final sentence):

Step 1: What type of professional services firm is this?
- Accounting / Consulting / Legal / HR / Insurance / Training / Other

Step 2: What is the most universal pain for this firm type in Darwin?
- Accounting → seasonal revenue, referral-only new clients
- Legal → can't market themselves, all referral-based
- Consulting → feast-or-famine, no retainer pipeline
- HR/Recruitment → relationship-based BD, no inbound
- Insurance/Financial Planning → referral-dependent, compliance anxiety around marketing

Step 3: Does the description or headline reveal any specific detail?
- If YES: use it to write something specific (e.g., "government advisory firms in Darwin")
- If NO: use the category-level pain for the firm type

Step 4: Write a sentence that:
- Is 10-15 words maximum
- Feels like it came from a local Darwin business peer, not a salesperson
- Does NOT start with "I noticed", "I saw", or "Congratulations"
- Does NOT mention a specific trigger (hiring, reviews, etc.) directly
- Sets up a conversation about client pipeline, not about DGK
- Is true and specific to the NT professional services market

RETURN ONLY THE FINAL SENTENCE. No explanation. No preamble.

GOOD EXAMPLES:
- "Most Darwin consulting firms I work with win clients the same way — until they don't."
- "Accounting firms in the NT usually hit a referral ceiling around the 5-year mark."
- "Legal practices in Darwin are often the last ones to build a digital client acquisition system."
- "NT recruitment agencies tend to win clients through relationships — which works until the next hiring freeze."

BAD EXAMPLES (do not write these):
- "I noticed you're hiring a senior consultant..." (signal mention)
- "Congratulations on your firm's success." (hollow)
- "I came across your profile on LinkedIn..." (generic)
- "I wanted to reach out because..." (weak opener)
```

---

## Chain-of-Thought Prompt: `ps_pain_line`

**Purpose:** Middle of Email 3 — firm-specific pain observation
**Model:** Claude Sonnet or GPT-4o
**Credits:** ~1 per row

**Full Prompt:**
```
You are writing a one-sentence pain observation for the middle of a cold email (Email 3 in a sequence) to a Darwin professional services firm owner.

CONTEXT:
- Company: {{current_company}}
- Industry group: {{industry_group}}
- Description: {{Description}}
- Hiring: {{Hiring Status & Job Openings hiring Status}}
- Annual Revenue: {{Annual Revenue}}

CHAIN OF THOUGHT:

Step 1: What is the firm type?
→ Accounting / Legal / Consulting / HR / Insurance / Training

Step 2: What is the referral ceiling pattern for this firm type?
- Accounting: "All new clients come through existing client referrals — and the waitlist only lasts until they leave."
- Legal: "Every new matter starts with someone who already knows you — or knows someone who does."
- Consulting: "Projects end and the pipeline starts from zero."
- HR: "Client relationships drive everything — until a hiring manager changes roles."
- Insurance: "Referral networks control the flow — and they're finite."

Step 3: Is there any signal from Description or Hiring that makes this more specific?
- Hiring → they're growing, which amplifies the pipeline gap
- Revenue > $1M → they're established, which means the referral ceiling is already real

Step 4: Write the sentence that:
- Names the pain without being accusatory
- Is 15-20 words maximum
- Sounds like an observation, not a sales pitch
- Connects naturally to "how are you currently winning new clients outside your referral network?"

RETURN ONLY THE FINAL SENTENCE.

EXAMPLES:
- "Most Darwin accounting firms at {{company}}'s stage are solid on delivery but haven't built a cold client acquisition system."
- "Consulting practices in Darwin tend to fill project pipelines through relationships — which is great until a key contact moves on."
- "Legal practices in the NT often have the strongest reputation in their area but the weakest online presence."
```

---

## Qualification Scoring Formula

Run this as a Clayscript column (`qualification_score`) before prioritising send order.

```javascript
let score = 0;
const reasons = [];

// Position Tier
const tier = String({{Position Tier}} || "").toUpperCase();
if (tier === "A") { score += 3; reasons.push("Tier A decision maker"); }
else if (tier === "B") { score += 1; reasons.push("Tier B — may have influence"); }

// Is Professional Services
const group = String({{industry_group}} || "");
const isPS = ["Accounting", "Legal", "Consulting", "HR", "Insurance", "Training"].includes(group);
if (isPS) { score += 2; reasons.push(`Professional services: ${group}`); }

// Hiring signal
const hiring = String({{Hiring Status & Job Openings hiring Status}} || "").toLowerCase();
if (hiring.includes("hiring")) { score += 2; reasons.push("Active hiring"); }

// Google presence
const reviews = parseInt({{Reviews}} || 0);
const rating = parseFloat({{Rating}} || 0);
if (reviews >= 10 && rating >= 4.0) { score += 2; reasons.push("Strong Google presence"); }
else if (reviews >= 5) { score += 1; reasons.push("Moderate Google presence"); }
else if (reviews === 0) { score -= 1; reasons.push("No Google reviews — possible weak online presence"); }

// Revenue signal
const revenue = String({{Annual Revenue}} || "").toLowerCase();
if (revenue.includes("1m") || revenue.includes("2m") || revenue.includes("5m") ||
    revenue.includes("10m") || revenue.includes("25m")) {
  score += 1; reasons.push("Confirmed revenue");
}

// LinkedIn Premium
const premium = String({{badges_premium}} || "").toLowerCase();
if (premium === "true") { score += 1; reasons.push("LinkedIn Premium"); }

// Valid email
const email = String({{Work Email}} || {{email}} || "").trim();
if (!email.includes("@")) { score = 0; reasons.push("NO EMAIL — exclude"); }

return `Score: ${score} | ${reasons.join(" | ")}`;
```

---

## Darwin Professional Services — Pain Calibration Reference

When reviewing AI output, check against these truths about NT professional services:

| Claim | True for Darwin? | Note |
|---|---|---|
| Referral-dependent client acquisition | YES — universally true | Safe to lead with |
| No outbound system | YES — most firms do zero cold outreach | Safe to lead with |
| Seasonal revenue (accounting) | YES — EOFY is extreme in NT | Use for accounting variants |
| Weak Google presence | YES — most NT professional services underinvested | Use for Google reviews PS |
| NT government is a major client | YES — for legal, consulting, accounting | Use for government-adjacent firms |
| Marketing anxiety (legal, financial) | YES — professional conduct rules | Be careful: don't suggest they're doing anything wrong |
| Small-town reputation dynamics | YES — Darwin is a small city, reputation matters | Use as NT social proof angle |

---

## Prompt Maintenance

- Run test batch of 10 rows before full campaign launch
- Read every output from `ps_opener` — reject anything generic, salesy, or that mentions triggers explicitly
- Acceptable failure rate: <10% (1 in 10 needs manual rewrite)
- Rebuild prompt if failure rate exceeds 20%
- Always use the same prompt version within a single send batch for consistency
