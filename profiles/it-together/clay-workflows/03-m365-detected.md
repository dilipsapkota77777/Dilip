# Workflow 03 — Microsoft 365 Detected
**Campaign:** #6 from campaign-strategy.md
**Signal:** Company website has Microsoft 365 or Azure detected via BuiltWith or MX record check
**Output:** Auto-push to Smartlead
**Est. credits per lead:** 6–9
**Confidence:** High → auto-push

---

## Why This Signal Works

Nearly every Australian SMB on M365 has misconfigured security settings:
- MFA not enforced on all accounts
- Shared mailboxes with weak/no passwords
- No email archiving or retention policy
- Default spam filters (not enough for modern phishing)
- No conditional access policies

IT Together can demonstrate this immediately with a free M365 security check. The personalisation writes itself — "you're on M365, here's what's probably wrong."

---

## Logic

```
Source list (Prospeo — all titles, 5–100, AU)
  → Enrich: MX record check on company domain
  → Filter: MX record points to Microsoft (outlook.com, protection.outlook.com)
  → OR: BuiltWith API detects Microsoft 365 / Office 365 on website
  → Filter: company has no IT provider on website (cross-reference WF02)
  → Enrich: email waterfall
  → Auto-push to Smartlead
```

---

## Clay Table Setup

### Step 1 — Source List (Prospeo)

Same base list as WF02:
```
job_titles: [Business Owner, Director, CEO, Ops Manager, Office Manager, Practice Manager, IT Manager]
headcount: 5–100
country: AU
```

---

### Step 2 — MX Record Check (1–2 credits)

**Clay HTTP enrichment:** DNS/MX lookup on `company_domain`

```
Check MX records for {{company_domain}}.
Return:
- mx_provider: Microsoft / Google / Other
- mx_record_value: [raw MX value]
```

**Filter:** Keep `mx_provider = Microsoft`

Common Microsoft MX patterns:
- `*.mail.protection.outlook.com`
- `*.onmicrosoft.com`
- `outlook.com`

---

### Step 3 — BuiltWith Enrichment (1–2 credits, optional)

If MX check is inconclusive, run BuiltWith on `company_website`:

```
Detect technologies on {{company_website}}.
Is Microsoft 365 / Office 365 / SharePoint / Teams detected?
Return: has_m365 YES/NO, detected_microsoft_tools: [list]
```

---

### Step 4 — Cross-Reference: No IT Provider (from WF02)

Before pushing, check Master Exclusion Sheet:
- If company already has a confirmed IT provider → exclude
- If already in WF02 pipeline → deduplicate (send WF02 version, not this one)

---

### Step 5 — Email Waterfall (2–4 credits)

Prospeo → Hunter → Apollo.

---

### Step 6 — Auto-Push to Smartlead

**Campaign:** `ITT — M365 Detected`

**Variables:**
| Variable | Clay Column |
|---|---|
| `{{first_name}}` | `first_name` |
| `{{company_name}}` | `company_name` |
| `{{company_domain}}` | `company_domain` |
| `{{company_industry}}` | `company_industry` (from Prospeo) |

---

## Email Sequence

**Email #1 — Lead magnet: Free M365 Security Check**
> Subject: `{{company_name}}'s Microsoft 365 setup`
>
> Hey {{first_name}},
>
> I noticed {{company_name}} is running Microsoft 365 — great choice for a team your size.
>
> The catch is most SMBs have 3–4 default settings that leave them exposed: MFA not enforced on all accounts, shared mailboxes with weak passwords, no archiving policy. None of these are obvious unless you know where to look.
>
> Happy to run a free M365 security check and send the findings — takes me 20 minutes, no commitment from you.
>
> [Name], IT Together

**Email #2 (Day 4):**
> Subject: `the M365 check — still happy to run it`
>
> Hey {{first_name}}, just following up.
>
> The free M365 security check is still on the table — I can usually turn it around in 24 hours. Would the findings be useful?
>
> [Name]

**Email #3 (Day 9):**
> Subject: `one last thing`
>
> Last one from me — if the M365 check isn't useful right now, no worries.
>
> But if you ever want a second set of eyes on your Microsoft setup, happy to help.
>
> [Name], IT Together

---

## Credit Estimate

| Step | Credits/Lead |
|---|---|
| MX record check | 1–2 |
| BuiltWith (optional) | 1–2 |
| Email waterfall | 2–4 |
| **Total** | **~4–8** |

**This is the most credit-efficient workflow.** Run at full volume — 50–75 leads/month.
