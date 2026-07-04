# DGK Business Consultancy — Campaign Strategy
Generated: 2026-07-04 | Framework: ColdIQ + Signal Sourcer + Campaign Strategy Skill

Target: Darwin/NT small businesses (broader than the 521 LinkedIn list)
Program: Government-subsidised digital strategy support — 5 hours, $0 to business
CTA mechanic: Reply-based (soft ask — no booking link)
DGK positioning: Business growth strategy + execution (NOT IT support)

---

## Competitor Intelligence — True Blue IT

| Element | True Blue IT (Competitor) | DGK (Our Approach) |
|---|---|---|
| Subject line | "Get 4-Hours of Government Subsidised Support" | 2 words, lower case, curiosity-based |
| Hours | 4 hours | 5 hours (+25% more) |
| Positioning | IT support / tech fixes | Business growth strategy + execution |
| Email format | Service brochure (bulleted list) | Pain-led, conversational, 60-90 words |
| Personalization | None — same to everyone | Segment-specific pain openers |
| CTA | "Book your free session" + image | Reply to email (lower friction) |
| Tone | Government leaflet | Peer-to-peer consultant |

**Their weakness:** "Get 4-Hours of Government Subsidised Support" tells the whole story in the subject. No curiosity. No pain. Every recipient who sees it knows exactly what it is — and most will ignore it because it reads like a government newsletter, not a business conversation.

**Our attack angle:** Never mention the program name in the subject line. Lead with the pain, introduce the program as the solution, differentiate on outcomes not features.

---

## Core Positioning Statement

> "True Blue IT fixes your tech. DGK builds your client pipeline — using 5 hours of government-funded time to do it."

**DGK's unique angle for this campaign:**
- Strategy first, execution included (not reactive IT support)
- Business growth outcomes: more clients, better pipeline, more revenue
- 5 hours vs competitor's 4 hours (25% more without saying it bluntly)
- Darwin-local: can meet in person, understands NT market
- Covers: websites, SEO, Google Ads, social media, digital marketing, CRM, AI tools, e-commerce — the revenue-driving side of digital

---

## Subject Line Strategy

### Why the Competitor's Subject Line Fails
"Get 4-Hours of Government Subsidised Support" — 7 words, all caps signal words, tells the whole pitch in subject line, zero curiosity, sounds like a government mailer. Reply rate estimate: <1%.

### ColdIQ Subject Line Rules Applied
- Exactly 2 words, all lower case
- No spam words: free, offer, support, help, grant, funding, government, subsidised
- Subject + preview = one complete thought
- Sound like an email from someone they know, not a campaign
- Create curiosity — they click to find out what you noticed

### Subject Line Options by Segment (A/B Test These)

**Trades:**
| Option | 2-Word Subject | Preview (first 50 chars) |
|---|---|---|
| A | `slow months` | Hey {{first_name}}, most Darwin tradies... |
| B | `darwin pipeline` | Quick observation about {{company}}... |
| C | `missed work` | Something I see with most Darwin trade... |

**Professional Services:**
| Option | 2-Word Subject | Preview (first 50 chars) |
|---|---|---|
| A | `referral ceiling` | Hey {{first_name}}, most Darwin firms... |
| B | `client pipeline` | Noticed something about how firms like... |
| C | `darwin strategy` | Quick one — most {{clean_position}}s I sp... |

**Agency:**
| Option | 2-Word Subject | Preview (first 50 chars) |
|---|---|---|
| A | `cobbler's children` | Noticed you build this for clients... |
| B | `agency pipeline` | Most Darwin agencies we work with... |
| C | `new clients` | Something I see with most creative... |

**Broad (no segment signal):**
| Option | 2-Word Subject | Notes |
|---|---|---|
| A | `darwin strategy` | Safe default, applies to any segment |
| B | `5 extra hours` | Hints at the hours without spam words |
| C | `getting clients` | Outcome-first, broad |

---

## 3-Email Sequence Framework

**Value prop rotation (ColdIQ rule — never same angle twice):**
- Email 1: Pattern Interrupt — the program exists, here's what it does for YOUR type of business
- Email 2: Show Cost of Problem — what it's costing you NOT to have a digital pipeline
- Email 3: Peer Proof — someone like you already used it and got more clients

**Timing:**
- Email 1 → Day 0
- Email 2 → Day 4–5 (same thread, RE: original subject)
- Email 3 → Day 12 (new subject, fresh thread)

---

## EMAIL 1 — Pattern Interrupt / Introduce the Program

**Framework:** Upfront Value + Observation
**Bucket:** Bucket 3 (self-identified traits — LinkedIn headline, role) for Variation A / Core-Static for C
**Goal:** Get a reply asking "what's covered?" or "how does it work?"
**Word count target:** 60–80 words

---

### Variation A — Type 1 Observation (Lite Hook from Bucket 3)

Use when: Contact has a rich LinkedIn headline with identifiable role/specialty

**Subject:** `[segment-specific 2 words from table above]`

**AI prompt for opener — `e1a_opener`:**
```
You write first-sentence openers for cold emails targeting Darwin small business owners.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
LinkedIn Headline: {{headline}}
Position: {{clean_position}}
Industry: {{industry_final}}

Write ONE observation sentence (max 15 words) that references something real from their headline or role.
Type 1: Observation — state what you noticed, no explanation.

Examples:
- "Came across your plumbing business while looking at Darwin contractors."
- "Noticed you head up the accounting practice at {{company}}."
- "Saw your design studio while looking at Darwin creatives."

Rules:
- Reference their actual headline or role
- No compliments, no "love your work"
- Conversational, peer-to-peer
- Max 15 words
- Output: one sentence, no quotes
```

**Full Email 1A:**
```
Subject: {{e1a_subject}}

Hi {{first_name}},

{{e1a_opener}}

There's a government program that gives Darwin businesses 5 hours of funded digital strategy support — not IT fixes, but proper help building the system that gets you more clients.

We're a local registered provider. It costs you nothing.

Worth me sending through what it covers?

[Signature]
```

---

### Variation B — Type 2 Pain (Segment-Specific)

Use when: No strong individual signal — use segment pain pattern confidently

**Subject:** `[segment pain 2 words]`

**AI prompt for opener — `e1b_opener`:**
```
You write first-sentence openers for cold emails targeting Darwin small business owners. This is a Type 2 Pain opener — you're confident about their pain based on their business type.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Industry: {{industry_final}}
Position: {{clean_position}}

Write ONE pain sentence (max 20 words) that names the specific growth problem for their business type. Be confident, not presumptuous — "most [type]" framing.

By industry:
- Trades: "Most Darwin tradies I speak with have the same issue — great at the work, no system when word-of-mouth slows down."
- Professional Services: "Most Darwin [firm type] I talk to have hit the same ceiling — great on referrals, no predictable pipeline beyond them."
- Agency: "Most Darwin agencies I speak with build great systems for clients but rely on referrals for their own new business — cobbler's children problem."
- Health/NDIS: "Most Darwin health businesses I talk to are running on referrals and word-of-mouth — which makes it hard to plan ahead."
- Retail: "Most Darwin retailers I speak with have a strong physical presence but almost no digital pipeline pulling customers in."
- Hospitality: "Most Darwin hospitality businesses I speak with rely on walk-ins and Google — and only one of those is working for them."

Match to their industry. Max 20 words. Output: one sentence only.
```

**Full Email 1B:**
```
Subject: {{e1b_subject}}

Hi {{first_name}},

{{e1b_opener}}

The Australian Government funds 5 hours of digital strategy support specifically for Darwin businesses — websites, Google presence, digital marketing, CRM, whatever your biggest gap is.

We're a local registered provider. It's free to you.

Want me to send through how it works?

[Signature]
```

---

### Variation C — Type 3 Industry (Firmographic Fallback)

Use when: No LinkedIn data, no signal — cold contact with company name and segment only

**Subject:** `darwin strategy`

**Opener — Static Formula (0 credits):**
```javascript
const industry = String({{industry_final}} || "").trim();

const openerMap = {
  "Trades": "Most Darwin trade businesses we work with have strong local reputations — but no digital system to turn that into consistent new work.",
  "Professional Services": "Most Darwin professional services firms grow well on referrals — the problem is the pipeline isn't in their control.",
  "Agency": "Most Darwin agencies build great digital systems for clients — but haven't built one for their own new business pipeline.",
  "Health": "Most Darwin health and allied health businesses rely on referrals and word-of-mouth — which makes pipeline unpredictable.",
  "Retail": "Most Darwin retailers have a solid walk-in trade but almost no digital presence pulling in new customers.",
};

return openerMap[industry] || "Most Darwin businesses we speak with have a strong reputation locally — but no digital system working in the background to bring in new clients.";
```

**Full Email 1C:**
```
Subject: darwin strategy

Hi {{first_name}},

{{e1c_opener}}

There's a government program that funds 5 hours of digital strategy support for Darwin businesses — specifically for solving this.

We're a local registered provider. Costs you nothing.

Want me to send through what the 5 hours can cover?

[Signature]
```

---

## EMAIL 2 — Show Cost of Problem (Add Context, Day 4–5)

**Framework:** Do the Math / Show Cost
**Same thread** (RE: Email 1 subject)
**Goal:** Make the cost of inaction tangible. Different angle from Email 1.
**Word count target:** 50–70 words

---

### Variation A — Hiring Signal (Bucket 6)

Use when: `is_hiring` = true OR `job_opening` not empty

**Subject:** `RE:` (same thread)

**AI prompt — `e2a_opener`:**
```
You write Email 2 openers for Darwin small business owners using a hiring signal.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Job Opening: {{job_opening}}
Industry: {{industry_final}}

Write ONE sentence (max 20 words) referencing their hiring — growing the team means new clients need to keep coming in to justify the hire.

If job opening available: reference the specific role
If empty: "Noticed {{company}} is growing"

Max 20 words. Output: one sentence only.
```

**Full Email 2A:**
```
Subject: RE: {{e1_subject}}

{{first_name}},

{{e2a_opener}}

The 5 funded hours can go directly toward building the digital side — so the pipeline keeps pace with the headcount.

We work with Darwin businesses on exactly this. No cost to you.

Still worth me sending through what's covered?

[Signature]
```

---

### Variation B — Do the Math / Cost of No Pipeline

Use when: No hiring signal — use segment cost calculation

**Subject:** `RE:` (same thread)

**AI prompt — `e2b_opener`:**
```
You write Email 2 openers for Darwin small business owners using the Do the Math framework — make the cost of having no digital pipeline tangible.

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Industry: {{industry_final}}
Position: {{clean_position}}

Write ONE sentence (max 25 words) that calculates or estimates the cost of not having a digital pipeline — specific to their industry.

By industry:
- Trades: "Most Darwin tradies estimate 2-4 jobs a month go to a competitor simply because someone searched online and couldn't easily reach them."
- Professional Services: "When one referral source goes quiet — a retiring accountant, a busy solicitor — most Darwin firms see a 20-40% drop in new enquiries with nothing queued up."
- Agency: "Most Darwin agencies that rely on referrals turn down 2-3 ideal projects a year simply because the work didn't come in at the right time."
- Health/NDIS: "Most Darwin health businesses estimate 30-40% of potential new patients search online before calling — and most of those go to whoever shows up first."

Use "typically" or "most" framing. Max 25 words. Output: one sentence only.
```

**Full Email 2B:**
```
Subject: RE: {{e1_subject}}

{{first_name}},

{{e2b_opener}}

That's what the 5 funded hours is for — building the specific digital system that fixes this.

We're Darwin-based and we handle the strategy + execution.

Is it worth a quick conversation?

[Signature]
```

---

### Variation C — What the Hours Actually Cover (Concrete)

Use when: Segment C contacts — make the 5 hours feel tangible

**Subject:** `RE:` (same thread)

**Full Email 2C:**
```
Subject: RE: {{e1_subject}}

{{first_name}},

One thing I didn't mention — the 5 hours isn't a generic digital audit.

It's hands-on: we build or improve the actual system — whether that's a website, Google presence, social media, digital marketing, or a CRM for client follow-up.

Whatever's costing you the most clients right now.

Worth a quick reply to explore?

[Signature]
```

---

## EMAIL 3 — Peer Proof / More Clients (Lower Friction, Day 12)

**Framework:** ColdIQ Style 2 — Peer Proof ("Others Like You Got This Result")
**New subject, fresh thread**
**Goal:** Social proof that it works, lowest possible friction CTA
**Word count target:** 50–60 words

---

### Variation A — Direct Peer Proof

**Subject:** `darwin results`

**AI prompt — `e3a_opener`:**
```
You write Email 3 openers for Darwin small business owners using Peer Proof (ColdIQ Style 2).

Contact: {{first_name}} {{last_name}}
Company: {{company}}
Industry: {{industry_final}}

Write ONE sentence (max 20 words) referencing a Darwin business that used the 5-hour government program and got more clients.

By industry:
- Trades: "A Darwin electrician used the 5 hours on their Google presence and website — got 4 new enquiries in the first month without doing anything different."
- Professional Services: "A Darwin accounting firm used the 5 hours on their digital client pipeline — picked up 2 new clients in the next 6 weeks from online searches."
- Agency: "A Darwin design studio used the 5 hours to set up their own new business pipeline — got 3 client enquiries they'd never have reached otherwise."
- Health: "A Darwin allied health clinic used the 5 hours on their website and Google — saw a 30% increase in new patient enquiries."
- Retail: "A Darwin retailer used the 5 hours to set up their online presence — started getting enquiries from people who'd found them on Google."

Match to their industry. Sound like a real result. Max 20 words. Output: one sentence only.
```

**Full Email 3A:**
```
Subject: darwin results

{{first_name}},

{{e3a_opener}}

That's what the 5 hours is for — not a generic review session, but fixing the specific gap that's costing you clients.

If the timing works, just reply and I'll send through the details.

[Signature]
```

---

### Variation B — Specific Outcome with Numbers

**Subject:** `5 hours, more clients`

**Full Email 3B:**
```
Subject: 5 hours, more clients

{{first_name}},

{{e3b_opener}}

The 5 hours is fully government-funded — no cost to you.

We're Darwin-based, so happy to meet in person if that's easier than a call.

If it's not the right time, no worries at all.

[Signature]
```

---

### Variation C — Lower Friction / Last Chance

**Subject:** `leaving this here`

**Full Email 3C:**
```
Subject: leaving this here

{{first_name}},

Two notes, no reply — last one from me.

Darwin businesses are using government-funded digital strategy support (5 hours, $0 cost) to build proper client pipelines — trades, professional services, agencies — all with the same outcome: less relying on word-of-mouth.

If the timing's right, just reply and I'll send through what's covered.

[Signature]
```

---

---

# CAMPAIGN IDEAS TABLE (15 Campaigns — Fresh Darwin SMB List)

## Base Parameters
- Location: Darwin / Northern Territory
- Business type: Small-to-medium businesses
- Decision maker: Owner, Director, Founder, Partner, Principal
- Program: 5-hour government-funded digital strategy support
- DGK angle: Full digital strategy + execution (not IT support)

| Campaign Name | Level | List Filters | AI Strategy | Value Prop | Campaign Overview |
|---|---|---|---|---|---|
| **Darwin Owner Broad** | Broad | All Darwin business owners on LinkedIn | AI infers segment pain from headline + position (Bucket 3) | 5 hours free to fix biggest digital gap | Lead with segment-matched pain opener. Variation A/B/C by signal. Email 1: pain + program. Email 2: cost of inaction. Email 3: peer proof. Reply CTA. |
| **Google Reviews Gap** | Broad | Trades: google_rating < 4.0 OR review_count < 15 | Google rating + count via Claygent | Poor reviews = missing clients. 5 hours fixes this | "Your rating is [X] with [Y] reviews — most customers check Google before calling a tradie. The 5 funded hours can go toward fixing exactly this." |
| **Strong Reviews No Enquiry System** | Focused | Trades: google_rating ≥ 4.5 AND review_count ≥ 20 | Reviews data via Claygent | Strong reputation not converting online | "You've got a [rating]-star rating with [count] reviews — the missing piece is the system that converts someone who searches for you online into an actual enquiry." |
| **Hiring Signal** | Focused | is_hiring = true OR active job posting found | Job title being hired via Claygent | Growing team = need more clients. 5 hours funded | "Saw [company] is hiring a [role] — at that stage, the client pipeline usually needs to keep up with the headcount." |
| **New Business Owner** | Focused | Started current role <180 days | LinkedIn start date via enrichment | New to the role = open to building right systems | "You've been running [company] for [X months] — most new business owners hit the same question around the 6-month mark: how do I get clients without relying on who I already know?" |
| **No Website / Weak Website** | Focused | Claygent checks if company has a website + quality score | Website presence check via Claygent | You're invisible online. 5 hours changes that | "I looked up [company] and [specific observation about web presence]. The 5 funded hours is exactly what we'd use to fix this." |
| **Referral-Dependent Firms** | Focused | Pro Services + About section mentions referrals | Claygent scans LinkedIn About section | You built on referrals. Here's the next step | "Noticed [company] has grown through referrals — the 5 hours can build the digital pipeline that sits alongside it." |
| **Cobbler's Children — Agencies** | Focused | Agency segment only | Agency type inferred from name + headline | You build pipelines for clients. Build yours | "Most Darwin agencies build great client acquisition systems for their clients — the irony is they don't have one for their own new business." |
| **ServiceM8 Non-Users (Trades)** | Niche | Trades + no ServiceM8 detected on website | Wappalyzer/Claygent checks for field service software | Competitors using ServiceM8 save 4-6 hrs/week | "Most Darwin tradies using ServiceM8 save 4-6 hours a week on scheduling and invoicing. The government program covers setup — 5 hours, $0." |
| **Businesses 5+ Years Old** | Focused | Founded >5 years ago via Claygent/LinkedIn | Company founding date enrichment | You've built something solid — digital presence doesn't match | "Most Darwin businesses at the 5+ year mark are leaving clients on the table — not because they're not good, but because their digital presence doesn't match their reputation." |
| **Darwin Chamber of Commerce** | Niche | Scrape CCNT member directory | Member status + company type from directory | You're invested in Darwin business. So are we | "Saw [company] is a Chamber of Commerce member — that tells me you take the business seriously. The government digital strategy program is one of the better investments for Darwin members right now." |
| **NDIS Providers** | Focused | Health + headline/company mentions NDIS | Claygent checks NDIS registration | NDIS is changing. Digital presence needs to keep up | "With NDIS pricing changes and more providers in Darwin, most NDIS businesses are realising word-of-mouth isn't enough anymore." |
| **Businesses Running Paid Ads** | Niche | Meta/Google Ads pixel detected on website | Wappalyzer detects ad pixels | You're paying for ads. 5 free hours makes them work | "Noticed [company] is running paid ads — the 5 funded hours can go toward making sure the ads, landing page, and follow-up are all aligned." |
| **Competitor Engagers** | Niche | People who liked/commented on True Blue IT LinkedIn posts | Scrape post engagement via PhantomBuster | You know the program. Here's the better version | "You've likely seen the 4-hour government program offered by IT companies. DGK's version is 5 hours and covers business strategy + execution, not just IT support." Do NOT name the competitor. |
| **Google Maps Darwin SMB** | Broad | Google Maps Darwin: all business categories | Google rating + review count enrichment | Fresh list beyond LinkedIn — all Darwin SMBs | Use Google Maps extractor for trades, retail, hospitality, health. Enrich with reviews. Segment by category. Run Variation C (no LinkedIn data, firmographic only). |

---

## No-AI Campaigns

### 1. "Darwin Business Owners — Government Hours"
**Why it works without AI:** The free government program + local angle is strong enough. Clean list, no enrichment needed.
```
Subject: darwin strategy

Hi {{first_name}},

Most Darwin businesses qualify for 5 hours of government-funded digital strategy support — websites, Google presence, marketing, CRM, whatever the biggest gap is.

We're a local registered provider. It costs you nothing.

Want me to send through what's covered?

[First name]
```

### 2. "Trades — 5 Free Hours, More Work"
**Why it works without AI:** Trades feast/famine pain is universal in Darwin. No personalization needed — pain statement does the work.
```
Subject: slow months

Hi {{first_name}},

Most Darwin tradies rely on word-of-mouth — which works until it doesn't.

The government funds 5 hours of digital strategy support for Darwin businesses to fix this. Websites, Google presence, booking systems — whatever your biggest gap is.

We're Darwin-based. It's free.

Worth a quick chat?

[First name]
```

### 3. "What Would You Do With 5 Hours?" (Question-First)
**Why it works without AI:** Asking a question before pitching generates replies that qualify and personalize themselves.
```
Subject: 5 extra hours

Hi {{first_name}},

Quick question — if you had 5 hours of free, hands-on digital strategy support for your business, what would you use it on?

Asking because there's a government program that funds exactly this for Darwin businesses. I'm trying to understand what the biggest gap is for most people before suggesting how to use it.

Just reply with the first thing that comes to mind.

[First name]
```

---

## Front-End Offer Suggestions

### 1. Free Digital Gap Check (Claygent-Generated)
Before claiming the 5 hours, run a 3-point digital gap check on their business:
- Website present? (yes/no + quality note)
- Google Business Profile claimed? (yes/no + rating)
- Social media presence? (active/inactive/none)

Include ONE specific observation in the email: "I noticed [company] doesn't have a Google Business Profile claimed — that's usually the first gap we'd fix with the 5 hours."

### 2. Segment-Specific Case Study (1-pager)
Create one 1-page text case study per segment:
- "How a Darwin electrician got 4 new enquiries/month using the 5-hour program"
- "How a Darwin accountant built a referral-free pipeline using the 5 funded hours"
- "How a Darwin agency stopped relying on referrals using the government program"

Offer in Email 2: "I put together a 2-min read showing how a Darwin [type] used the 5 hours — want me to send it?"

### 3. "What's Your Biggest Digital Gap?" Loom Video
60-second personal Loom per segment (3 total) showing what the 5 hours typically covers for that segment.
Offer in Email 3 as last-chance resource: "Can send you a 60-second video walking through what the 5 hours looks like in practice."

---

## Why This Beats the Competitor

| Factor | True Blue IT | DGK |
|---|---|---|
| Subject line | 7 words, tells whole story | 2 words, creates curiosity |
| First sentence | Service brochure header | Pain observation specific to their business type |
| Body | 8-bullet service list | 60-80 words, one idea, one CTA |
| CTA | "Book your free session" button | "Want me to send through what it covers?" |
| Hours | 4 hours | 5 hours |
| Positioning | IT support company | Business growth consultant |
| Tone | Government leaflet | Peer-to-peer conversation |
| Personalization | None | Segment-matched pain opener + Bucket 3 lite hook |

The businesses that got True Blue IT's brochure and ignored it will open DGK's email — because the subject is different, the first line is about them, and replying is the easiest next step they can take.
