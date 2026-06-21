# Workflow 08 — Nepali-Owned Business Detection
**Campaign:** #16 from campaign-strategy.md
**Signal:** Real estate agency or accounting firm is Nepali-owned, operated by someone with a Nepali-origin name, or explicitly serves the Nepali/South Asian community
**Output:** Manual review → personalised Smartlead upload
**Est. credits per lead:** 6–10
**Confidence level:** Medium → manual review (cultural sensitivity required)

---

## Logic

```
Source list (Prospeo — agents + accountants, AU)
  → Claygent: name origin detection on principal/director
  → Filter: Nepali/South Asian name detected → keep
  → OR: Claygent website check for community language/service mentions
  → Enrich: email waterfall
  → Manual review → Smartlead (personalised sequence)
```

---

## Why This Workflow Matters

Laxmi Home Loans' bilingual English/Nepali capability is a genuine differentiator that no competitor can replicate. Nepali-owned or Nepali-serving businesses are the highest-trust, lowest-friction referral partners — a shared cultural background removes most of the cold-start trust barrier.

This workflow should run as an **always-on, low-volume** campaign targeting ~10–20 leads/month, prioritised over volume.

---

## Clay Table Setup

### Step 1 — Source the List (Prospeo)

```
job_titles: [Principal, Director, Owner, Managing Director, Founder, Partner]
industries: [Real Estate, Accounting, Financial Services]
headcount: 1–50
country: AU
```

---

### Step 2 — Name Origin Detection (Claygent, 3–4 credits/lead)

**Prompt:**
```
Is the name "{{first_name}} {{last_name}}" of likely Nepali, Indian, Sri Lankan, Bangladeshi, or South Asian origin?
Return:
- likely_south_asian: YES or NO
- likely_nepali_specifically: YES or NO (if you can tell)
- confidence: HIGH / MEDIUM / LOW
```

**Filter:** Keep `likely_south_asian = YES` with `confidence = HIGH or MEDIUM`

*Note: This is probabilistic. Some names are ambiguous. Manual review catches false positives.*

---

### Step 3 — Website Community Language Check (Claygent, 4–6 credits/lead)

Run on ALL leads from Step 1 regardless of name origin (catches Nepali businesses with Western-style trading names).

**Prompt:**
```
Visit {{company_website}}.

Does this business:
1. Mention serving the Nepali community specifically?
2. Mention serving South Asian, Indian, or multicultural communities?
3. Have any content in Nepali, Hindi, or other South Asian languages?
4. Have any staff names that appear to be of South Asian origin?

Return:
- serves_nepali_community: YES or NO
- serves_south_asian_community: YES or NO
- community_evidence: [quote or page URL, or "none"]
```

**Filter:** Keep if `serves_nepali_community = YES` OR `serves_south_asian_community = YES`

---

### Step 4 — Email Waterfall (2–4 credits/lead)

---

### Step 5 — Manual Review + Personalisation

Before sending, the reviewer should:
- [ ] Confirm the principal/director name appears South Asian
- [ ] Check LinkedIn profile photo to confirm (acceptable for manual review)
- [ ] Decide: use English email or Nepali opener?
- [ ] Add the contact's first name in Nepali script if opening in Nepali

**Personalisation decision tree:**
- Likely Nepali name + community language on website → Nepali opener
- South Asian name but no community language → English email with subtle cultural reference
- Western trading name but South Asian principals → English email, no cultural reference

---

## Email Copy Hooks

**Version A — Nepali opener (for confirmed Nepali-owned businesses):**
> "Namaste {{first_name}} ji — म Laxmi Home Loans बाट बोल्दैछु। हामी एउटा बिलिंगुअल mortgage brokerage हौं जसले Nepali र English दुवैमा सेवा दिन्छौं। तपाईंका clients हरुको लागि एउटा reliable broker partner चाहनुहुन्छ भने, हामीसँग कुरा गर्नुस्।"
>
> (Translation: "Namaste — I'm reaching out from Laxmi Home Loans. We're a bilingual mortgage brokerage serving clients in both Nepali and English. If you're looking for a reliable broker partner for your clients, let's talk.")

**Version B — English with cultural signal:**
> "Hi {{first_name}} — I noticed {{company_name}} works with the multicultural community in {{suburb}}. We're one of the few mortgage brokers in Australia offering bilingual English/Nepali service, which makes a real difference for Nepali families navigating the home loan process. Happy to explore a referral arrangement."

---

## Credit Estimate

| Step | Credits per Lead |
|---|---|
| Name origin detection | 3–4 |
| Website community check | 4–6 |
| Email waterfall | 2–4 |
| **Total** | **~9–14** |

**Volume target:** 10–20 leads/month. Quality over quantity — these are your highest-trust leads.

---

## Data Sources for Supplemental Sourcing

Beyond Prospeo, consider these sources to find Nepali-owned businesses directly:

1. **Federation of Nepalese Associations in Australia (FNAA)** — member directory
2. **Nepali community Facebook groups in Sydney/Melbourne/Brisbane** — business owners often post
3. **Google Maps search:** "Nepali real estate agent Sydney" / "Nepali accountant Melbourne"
4. **LinkedIn search:** Filter by name + industry + AU location manually
5. **Neplese community events** (NRN Australia, Dashain events) — often have business directories
