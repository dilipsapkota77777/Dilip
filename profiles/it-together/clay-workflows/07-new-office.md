# Workflow 07 — New Office / Relocation Signal
**Campaign:** #11 from campaign-strategy.md
**Signal:** Company recently opened a new office, expanded to a new location, or relocated
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 7–10
**Confidence:** Medium-High → auto-push

---

## Logic

```
Source: LinkedIn company announcements + Google Maps new listing detection
  → Filter: new address OR new office announcement in last 60 days
  → Filter: company headcount 5–100
  → Find: decision-maker contact
  → Email waterfall
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source: LinkedIn Company Announcements (Claygent)

**Option A: LinkedIn Company Page Monitoring**
```
Prompt (run weekly):
Check the LinkedIn company page for {{company_linkedin_url}}.
Look for any posts in the last 60 days announcing:
- A new office opening
- Office expansion or relocation
- A new address or location
- "We've moved", "new home", "new office", "opening a new location"

Return:
- has_office_announcement: YES or NO
- announcement_date: [date if found]
- new_location: [suburb or address if mentioned]
- post_url: [LinkedIn post URL if found]
```

**Option B: Google Maps New Listing Detection**
Monitor Google Maps for new business listings in target suburbs. Use Claygent to scrape new listings weekly by category + suburb.

---

### Step 2 — Company Headcount Filter (2–3 credits)

LinkedIn Company enrichment. Keep 5–100 headcount.

---

### Step 3 — Find Decision-Maker (2–3 credits)

LinkedIn People Search for Owner / Director / Operations Manager.

---

### Step 4 — Email Waterfall (2–4 credits)

---

### Step 5 — Auto-Push to Smartlead

**Campaign:** `ITT — New Office Signal`

**Variables:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `contact_first_name` |
| `{{company_name}}` | `company_name` |
| `{{new_location}}` | `new_location` |

---

## Email Sequence

**Email #1 — Lead magnet: IT Health Check**
> Subject: `congrats on the new {{company_name}} office`
>
> Hey {{first_name}},
>
> Congrats on the new office in {{new_location}} — exciting milestone.
>
> New locations are the best time to get IT set up right from day one. The alternative is inheriting a mess 6 months in when the patching is months behind and half the team is sharing credentials.
>
> Happy to run a free IT health check so you've got a clean baseline from the start.
>
> [Name], IT Together

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| LinkedIn announcement check | 3–5 |
| Company headcount | 2–3 |
| Email waterfall | 2–4 |
| **Total** | **~7–12** |

**Cadence:** Run every 2 weeks. Discard announcements older than 60 days.
