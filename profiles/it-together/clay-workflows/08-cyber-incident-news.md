# Workflow 08 — Cybersecurity Incident / Industry News
**Campaign:** #7 from campaign-strategy.md
**Signal:** A cybersecurity incident has been reported in a target industry (healthcare, legal, accounting, construction) in Australian news — prospect is in the same industry
**Output:** Manual review → Smartlead (time-sensitive, send within 48 hours of incident)
**Est. credits per lead:** 5–8
**Confidence:** Medium → manual review (timing is critical)

---

## Why This Works

After a high-profile breach in an industry, every business in that industry becomes more receptive to security outreach. The news does the fear-setting for you. Your email arrives as a solution, not a pitch.

**This is a reactive workflow** — it runs when a news trigger fires, not on a schedule.

---

## Logic

```
Monitor: Australian cybersecurity news (Google Alerts / Claygent)
  → Trigger: breach reported in healthcare, legal, accounting, construction, or education
  → Pull: existing Prospeo list filtered by that industry
  → Email waterfall (already enriched — just filter by industry)
  → Manual review → time-sensitive Smartlead send (within 48 hours)
```

---

## Setup: News Monitoring

**Option A: Google Alerts (free)**
Set up Google Alerts for:
- `"data breach" Australia healthcare`
- `"cyber attack" Australia legal OR accounting`
- `"ransomware" Australia SMB`
- `"data breach" Australia school OR education`

Alert frequency: As-it-happens. Forward to a dedicated Gmail label.

**Option B: Claygent Weekly Scan**
```
Prompt (run every Monday):
Search for Australian news articles from the last 7 days about:
- Data breaches affecting Australian businesses
- Ransomware attacks on Australian SMBs
- Cybersecurity incidents in healthcare, legal, accounting, or education in Australia

For each incident found, return:
- industry_affected: [industry]
- incident_type: [breach type — ransomware, phishing, data leak, etc.]
- news_headline: [headline]
- news_source: [publication name]
- incident_date: [date]
```

---

## Workflow Steps When Trigger Fires

### Step 1 — Identify Industry Affected

From the news alert: which industry was hit? (e.g. Healthcare)

### Step 2 — Pull Existing Industry List

From your Prospeo master list (already enriched from WF02 or WF03):
- Filter by `company_industry = [affected industry]`
- Filter by `email` found
- Filter by NOT already in active Smartlead sequence

If industry list isn't enriched yet → run a targeted Prospeo pull for that industry, enrich with email waterfall (2–4 credits/lead).

### Step 3 — Manual Review (Speed Matters)

Review list within 24 hours of incident. Send within 48 hours — after 72 hours the news cycle has moved on.

Check:
- [ ] Does the email reference the industry trend, NOT the specific victim company?
- [ ] Is the tone helpful, not exploitative?
- [ ] Is the incident real and verifiable (not rumour)?

---

## Email Sequence (Industry Breach Version)

**Email #1 — Lead magnet: Dark Web Scan**
> Subject: `{{industry}} breach — is {{company_name}} exposed?`
>
> Hey {{first_name}},
>
> You've probably seen the news about the recent {{industry}} data breach in Australia.
>
> These incidents are becoming more common — and the scary part is most businesses don't know their credentials are already exposed until it's too late.
>
> We run a free dark web scan that shows whether {{company_name}}'s data is already out there. Reply with your domain and I'll send results within 24 hours.
>
> [Name], IT Together

**Note:** Never name the victim company in the email subject or body — this can feel predatory and may have legal risk if the victim hasn't publicly disclosed. Reference "the recent {{industry}} breach" only.

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| Industry list filter (from existing data) | 0 (already enriched) |
| New leads if needed: Prospeo + email | 3–6 |
| **Total** | **~0–6/lead** |

**This workflow is nearly free if you maintain a pre-enriched industry list from WF02.**

---

## Reactive Send Calendar

Pre-build email variants for each industry so they're ready to deploy in <1 hour:

| Industry | Template Name |
|---|---|
| Healthcare | `ITT-breach-healthcare` |
| Legal | `ITT-breach-legal` |
| Accounting | `ITT-breach-accounting` |
| Construction | `ITT-breach-construction` |
| Education | `ITT-breach-education` |
| General SMB | `ITT-breach-smb` |
