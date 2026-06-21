# Workflow 09 — Education / AusTender IT Procurement
**Campaign:** #12 + #13 from campaign-strategy.md
**Signal:** School, college, or TAFE has posted an IT-related tender on AusTender, OR is a target education institution with no IT provider listed
**Output:** Manual review → Smartlead (formal tone)
**Est. credits per lead:** 8–12
**Confidence:** Medium → manual review (longer sales cycle, formal approach)

---

## Two Sub-Tracks

### Track A: AusTender Monitoring (Active Procurement)
School or government-adjacent institution has posted an active IT tender. Highest intent — they've decided to buy and are taking quotes.

### Track B: Education Cold Outreach (Proactive)
Schools and colleges with no visible IT provider, targeted proactively. Longer sales cycle but high LTV — education contracts tend to be multi-year.

---

## Track A — AusTender Monitoring

### Step 1 — Monitor AusTender

**URL:** https://www.tenders.gov.au/

**Claygent weekly scrape:**
```
Prompt:
Go to https://www.tenders.gov.au/ and search for IT-related tenders published in the last 14 days.

Filter for:
- Category: Information Technology, IT Services, Managed Services, Cybersecurity, Infrastructure
- Entity type: Schools, Education, TAFE, Local Government (small-to-medium)
- Status: Open

For each result extract:
- Organisation name
- Tender title
- Tender type (RFT, RFQ, EOI)
- Closing date
- Location (state)
- Tender URL
```

**Add columns:**
- `organisation_name`
- `tender_title`
- `tender_type`
- `closing_date`
- `tender_url`
- `tender_state`

---

### Step 2 — Filter Relevant Tenders

Keep where:
- `tender_title` contains: "IT", "managed", "technology", "cybersecurity", "infrastructure", "support", "helpdesk", "Microsoft", "cloud"
- `closing_date` is at least 14 days away (enough time to respond)
- `tender_state` = NSW (primary) or all states

---

### Step 3 — Find Contact (3–5 credits)

**Claygent:**
```
Find the IT Manager, Business Manager, or Principal at {{organisation_name}} in Australia.
Return: name, job title, email (if publicly listed), LinkedIn URL.
```

---

### Step 4 — Manual Review

Before sending:
- [ ] Is the tender scope within IT Together's capability?
- [ ] Is the closing date realistic for a response?
- [ ] Is the tone appropriately formal for a school/government body?

---

### Track A Email

**Subject:** `{{organisation_name}} — IT tender enquiry`

> Dear {{first_name}},
>
> I'm reaching out regarding {{organisation_name}}'s recent {{tender_type}} for {{tender_title}}.
>
> IT Together provides managed IT services to schools and educational institutions across Australia, including helpdesk support, cybersecurity, device management, and Microsoft 365 administration.
>
> We'd welcome the opportunity to discuss the scope further before the closing date of {{closing_date}}. Would a brief call this week be possible?
>
> Kind regards,
> [Name], IT Together

---

## Track B — Education Cold Outreach

### Step 1 — Source Education Institutions

**Option A: Google Maps**
```
Search Google Maps for:
- "Primary school Sydney"
- "Private school Sydney"
- "TAFE NSW"
- "College Sydney"
Extract: name, address, website, phone number, Google rating.
```

**Option B: State Education Department Directories**
NSW: dec.nsw.gov.au has a searchable school directory.
Scrape school name + suburb + website for non-government/independent schools (they have IT procurement discretion — government schools use DET contracts).

**Focus on:** Independent and Catholic schools (50–500 students) — they make their own IT decisions.

---

### Step 2 — Website Check: No IT Provider (Claygent, 5–8 credits)

```
Prompt:
Visit {{school_website}}. Does this school mention a named IT provider, technology partner, or managed IT company anywhere on the site?
Return: has_it_provider YES/NO, provider_name if found.
```

Keep `has_it_provider = NO`.

---

### Step 3 — Find Contact (2–3 credits)

```
Prompt:
At {{school_name}}, find the Business Manager, IT Coordinator, or Principal.
Return: name, job title, email if listed on website.
```

---

### Track B Email (Formal Tone)

**Subject:** `IT support for {{school_name}}`

> Dear {{first_name}},
>
> I'm reaching out to {{school_name}} regarding your technology and IT support arrangements.
>
> IT Together works with independent schools across Sydney to provide managed IT support, device management, cybersecurity, and Microsoft 365 administration — without the cost of a full-time IT hire.
>
> We'd be happy to provide a free IT health assessment for {{school_name}} at no obligation. Would that be of interest?
>
> Kind regards,
> [Name], IT Together

---

## Credit Estimate

| Track | Credits/Lead |
|---|---|
| Track A: AusTender scrape + contact find | 5–8 |
| Track B: Website check + contact find | 8–12 |

**Volume:** 10–15 leads/month combined. Education is a longer-cycle, lower-volume, high-LTV track.

---

## Education-Specific Notes

- **Independent schools** have full IT procurement discretion → target these first
- **Catholic systemic schools** → check if they use diocesan IT contracts before outreach
- **Government schools (DET NSW)** → use DET approved vendor process, not cold email
- **TAFE NSW** → state government procurement, AusTender track only
- **Private colleges / RTOs** → fully open to cold outreach, treat like any SMB
