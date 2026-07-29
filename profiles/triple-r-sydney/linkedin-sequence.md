# Triple R Sydney — LinkedIn Sequence (Campaign 3 Cold)
# ColdIQ Multi-Channel | Support Coordinators + Case Managers + Care Managers
# Built using: linkedin-campaign-complete + coldiq-messaging-templates + personalization-playbooks
Generated: 2026-07-29

---

## Context

**Client:** Triple R
**Campaign:** Campaign 3 — Cold
**List:** Sydney Support Coordinators, Case Managers, Care Managers (~200+ contacts)
**Channel:** LinkedIn — multi-channel alongside existing email sequence
**Tool:** LinkedIn automation (Heyreach, Expandi, or equivalent)

---

## Multi-Channel Timing Map

LinkedIn interleaves with email — never sends on the same day.

```
Day 0  → EMAIL 1 (Leverage Content — lead magnet / pain hook)
Day 1  → LI: View profile (automated, no message)
Day 2  → LI: Like a recent post (automated, no message)
Day 2  → LI: CONNECTION REQUEST sent
         [wait for acceptance]
Day 3  → LI: DM 1 sent (4-24 hrs after acceptance)
Day 4  → EMAIL 2 (Not Too Different Persona)
Day 8  → LI: DM 2 sent (if no LI reply)
Day 9  → EMAIL 3 (Ask Before Pitch)
Day 14 → LI: DM 3 Breakup (if still no reply)
```

**Rule:** If they reply on LinkedIn at any step, pause the email sequence for that contact.
**Rule:** If they reply to email, pause the LinkedIn sequence.

---

## Variant Routing Logic

Four variants based on columns already in the CSV.

| Variant | Trigger | Priority |
|---|---|---|
| `New_Role` | `Time Since Start` contains "month" OR starts with < 12 months | Highest |
| `CALD` | `CALD Services` = "Yes" | High |
| `Tenured` | `Time Since Start` contains year AND numeric > 7 | Standard |
| `Standard` | All others | Default |

**Position routing** (applied within each variant):
- `clean current position` = "Support Coordinator" → coordinator language
- `clean current position` = "Case Manager" → case manager language
- `clean current position` = "Care Manager" OR "Care Coordinator" OR "Clinical Care Coordinator" → care manager language

---

## STEP 1 — View Profile (Day 1, Automated)

No message. The profile view notification primes them to recognise your name when the connection request arrives 24 hours later.

**Tool setting:** Enable "view profile" in automation tool before connection request step.

---

## STEP 2 — Like Recent Post (Day 1-2, Automated)

No message. Like their most recent LinkedIn post (if they have one in last 30 days).

**Tool setting:** Enable "like recent post" in automation. Set to skip if no recent post.

---

## STEP 3 — Connection Request Note (Day 2-3)

**Character limit: 300 characters hard max. Every word earns its place.**
**Frame: Colleague Mimic — peer reaching out, zero pitch, pure curiosity**
**No CTA, no ask, no mention of Triple R**

### Variant A — New Role (`li_variant` = "New_Role")
```
{{firstName}}, looks like you're fairly new to the {{li_position}} role — I work with a lot of Sydney coordinators and care managers. Always keen to connect and compare notes.
```
**Chars:** ~175 ✅

### Variant B — CALD (`li_variant` = "CALD")
```
{{firstName}}, noticed {{company}} works with CALD communities — I work with coordinators across Sydney supporting similar participants. Would love to connect.
```
**Chars:** ~160 ✅

### Variant C — Tenured (`li_variant` = "Tenured")
```
{{firstName}}, {{li_tenure}} as a {{li_position}} — I work with a lot of Sydney coordinators. Would love to connect and hear how you've seen provider access change over that time.
```
**Chars:** ~175 ✅

### Variant D — Standard (`li_variant` = "Standard")
```
{{firstName}}, I work with a lot of Sydney {{li_position}}s across different orgs — always trying to understand how the coordination side of things is evolving. Would love to connect.
```
**Chars:** ~185 ✅

---

## STEP 4 — DM 1 (4-24 Hours After Connection Accepted)

**Max: 3-4 sentences. One question. No pitch. Zero mention of Triple R.**
**Frame: ColdIQ Ask Before Pitch — open-ended question, creates conversation**
**This is different from Email 2 — asks about process, not pain**

### Variant A — New Role
```
{{firstName}}, thanks for connecting.

Quick question — when you're new to a {{li_position}} role, how do you build your provider list from scratch? Rely on what the previous coordinator left, or start fresh with your own vetting?

Asking because I speak to a lot of Sydney coordinators and curious if there's a pattern.
```
**Words:** ~55 ✅

### Variant B — CALD
```
{{firstName}}, thanks for connecting.

One thing I'm curious about — when you need a provider for a CALD participant, how often does language or cultural background actually limit your options in Sydney?

Trying to understand where the real gaps sit for coordinators working with multicultural communities.
```
**Words:** ~52 ✅

### Variant C — Tenured
```
{{firstName}}, thanks for connecting.

Curious — after {{li_tenure}} in the role, how has provider access in Sydney changed? Harder, easier, or just different problems than when you started?

Comparing notes with a few long-term coordinators across different orgs.
```
**Words:** ~45 ✅

### Variant D — Standard (Support Coordinator)
```
{{firstName}}, thanks for connecting.

Quick one — when a participant needs support that's outside what your org directly provides, do you have a go-to list of providers you trust, or is it a fresh search each time?

Trying to understand how coordinators in Sydney typically handle the gap.
```
**Words:** ~52 ✅

### Variant D — Standard (Case Manager / Care Manager)
```
{{firstName}}, thanks for connecting.

Quick one — when a client needs care that your team doesn't directly deliver, how do you handle the provider search? Established referral network, or depends entirely on the situation?

Just comparing notes with case managers and care managers across Sydney.
```
**Words:** ~50 ✅

---

## STEP 5 — DM 2 (Day 8, If No Reply to DM 1)

**Max: 3 sentences. Change the angle. Add light social proof.**
**Frame: ColdIQ Not Too Different Persona — peer proof, different question**

### Standard (Support Coordinator / Support Coordinator + CALD)
```
{{firstName}}, following up on my earlier message.

Most Sydney support coordinators I speak to say the same thing — provider reliability is fine until it isn't, and the complex or urgent placements are where things fall apart.

Would a quick 10-minute call to compare notes be worth it?
```
**Words:** ~52 ✅

### New Role variant
```
{{firstName}}, following up.

A lot of coordinators new to the role tell me the hardest part isn't the coordination itself — it's knowing which providers are actually reliable before a participant has a bad experience.

Worth a quick call to swap notes?
```
**Words:** ~47 ✅

### Case Manager / Care Manager variant
```
{{firstName}}, following up on my earlier message.

Most case and care managers I speak to across Sydney say provider reliability is manageable — until there's a complex or urgent clinical gap and the usual options aren't available.

Worth 10 minutes to compare notes?
```
**Words:** ~50 ✅

### CALD variant
```
{{firstName}}, following up.

Most coordinators working with CALD participants I've spoken to say the real gap isn't access to providers — it's access to providers with genuine language and cultural fit.

Worth a quick call to compare notes on what's actually available in Sydney?
```
**Words:** ~50 ✅

---

## STEP 6 — DM 3 Breakup (Day 14, If Still No Reply)

**Max: 2-3 sentences. Low pressure. Leave the door open.**
**Frame: Breakup — no obligation, no hard sell**

### All variants (universal)
```
{{firstName}}, last one from me — happy to step back if now's not the right time.

If you ever need a reliable provider for participants with complex support needs in Sydney, feel free to reach back out.

Good luck with the coordination work.
```
**Words:** ~47 ✅

---

## Clay Column Setup

### New columns to add to existing Clay table

#### `li_variant`
Clayscript — 0 credits
```javascript
const timeStr = String({{Time Since Start}} || "").toLowerCase();
const cald = String({{CALD Services}} || "").toLowerCase();

// Check for new role (months or very short tenure)
if (timeStr.includes("month") || timeStr.match(/^[0-9]\s*(month|mo)/)) {
  return "New_Role";
}

// CALD override
if (cald === "yes") {
  return "CALD";
}

// Extract years if available
const yearMatch = timeStr.match(/(\d+)\s*year/);
if (yearMatch && parseInt(yearMatch[1]) >= 8) {
  return "Tenured";
}

return "Standard";
```

#### `li_position`
Normalises position for use in LinkedIn messages. Clayscript — 0 credits.
```javascript
const pos = String({{clean current position}} || {{current_company_position}} || "").toLowerCase().trim();

if (pos.includes("support coordinator")) return "support coordinator";
if (pos.includes("case manager")) return "case manager";
if (pos.includes("clinical care coordinator")) return "care coordinator";
if (pos.includes("care coordinator")) return "care coordinator";
if (pos.includes("care manager")) return "care manager";
if (pos.includes("transitional care")) return "care manager";
if (pos.includes("peer support")) return "support coordinator";

// Fallback
return "coordinator";
```

#### `li_tenure`
Formats tenure for use in Variant C messages. Clayscript — 0 credits.
```javascript
const raw = String({{Time Since Start}} || "").trim();
if (!raw || raw === "") return "your time in the role";

// e.g. "15 years" → "15 years"
// e.g. "Apr 2011" → calculate from date
if (raw.match(/^\d+\s*year/i)) return raw.toLowerCase();

// Date format — calculate
const months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];
const lower = raw.toLowerCase();
for (let i = 0; i < months.length; i++) {
  if (lower.includes(months[i])) {
    const yearMatch = raw.match(/\d{4}/);
    if (yearMatch) {
      const startYear = parseInt(yearMatch[0]);
      const currentYear = new Date().getFullYear();
      const diff = currentYear - startYear;
      if (diff >= 1) return `${diff}+ years`;
    }
  }
}

return raw.toLowerCase();
```

#### `li_dm1`
AI-generated DM 1 text for personalisation at scale. Claude Sonnet, ~1 credit per row.

**Prompt:**
```
You are writing the first LinkedIn DM for a support provider (Triple R) reaching out to NDIS coordinators and care managers in Sydney.

Contact details:
- Name: {{first_name}}
- Role: {{li_position}}
- Company: {{current_company}}
- Variant: {{li_variant}}
- Tenure: {{li_tenure}}
- CALD services: {{CALD Services}}

Write a LinkedIn DM (max 60 words, 3-4 sentences) that:
1. Starts with "{{first_name}}, thanks for connecting."
2. Asks ONE open-ended question about how they handle provider gaps or participant placements
3. Frames you as a peer comparing notes — NOT a vendor
4. Never mentions Triple R or any product
5. Uses the variant logic:
   - New_Role → ask about building a provider list from scratch
   - CALD → ask about finding providers with cultural/language fit
   - Tenured → ask about how provider access has changed over their tenure
   - Standard → ask about their process when a participant needs external provider support

Return ONLY the message text. No subject line, no explanation.
```

#### `li_connection_note`
Routes to correct static template based on `li_variant` and `li_position`. Clayscript — 0 credits.
```javascript
const variant = String({{li_variant}} || "Standard");
const firstName = String({{first_name}} || "").trim().split(" ")[0];
const position = String({{li_position}} || "coordinator");
const tenure = String({{li_tenure}} || "your time in the role");
const company = String({{current_company}} || "your organisation");

if (variant === "New_Role") {
  return `${firstName}, looks like you're fairly new to the ${position} role — I work with a lot of Sydney coordinators and care managers. Always keen to connect and compare notes.`;
}
if (variant === "CALD") {
  return `${firstName}, noticed ${company} works with CALD communities — I work with coordinators across Sydney supporting similar participants. Would love to connect.`;
}
if (variant === "Tenured") {
  return `${firstName}, ${tenure} as a ${position} — I work with a lot of Sydney coordinators. Would love to connect and hear how you've seen provider access change over that time.`;
}
// Standard
return `${firstName}, I work with a lot of Sydney ${position}s across different orgs — always trying to understand how the coordination side of things is evolving. Would love to connect.`;
```

---

## Smartlead / HeyReach / Expandi Mapping

| Clay Column | Tool Variable | Step |
|---|---|---|
| `linkedin url` | Profile URL input | All steps |
| `li_connection_note` | Connection request note | Step 3 |
| `li_dm1` (AI) OR static DM 1 by variant | Message body | Step 4 |
| `first_name` | `{{firstName}}` | All messages |
| `current_company` | `{{company}}` | DM 2 |
| `li_position` | `{{li_position}}` | Connection note + DM 1 |
| `li_tenure` | `{{li_tenure}}` | Variant C messages |
| `li_variant` | Campaign routing tag | Segment filter |

---

## LinkedIn Limits & Compliance

| Limit | Value | Note |
|---|---|---|
| Connection requests per day | 20-25 max | Go lower if account is <3 months old |
| DMs per day | 30-40 max | Spread across the day |
| Profile views per day | 80-100 | Automated via tool |
| Acceptance rate target | >30% | Below 20% = stop, review connection note |
| Reply rate target (DM 1) | 8-18% | Below 8% = rewrite DM 1 question |

**Warning signs to watch:**
- LinkedIn "Pending" requests pile up over 800 → withdraw old ones (>21 days pending)
- Reply rate to DM 1 below 8% after 30 sends → stop, retest connection note
- Acceptance rate below 20% → connection note is too salesy, rewrite immediately

---

## A/B Test Plan

**Week 1: Test connection note**
- Version A: Standard (role + peer curiosity)
- Version B: Location-specific ("I work with a lot of Penrith/Bankstown/Sydney coordinators")
- Measure: Acceptance rate after 50 sends per version

**Week 2: Test DM 1 question**
- Version A: Provider process ("go-to list or fresh search?")
- Version B: Pain-based ("when things fall apart, what's the usual gap?")
- Measure: Reply rate after connection accepted

---

## Full Sequence Summary

| Step | Day | Action | Message | Chars/Words |
|---|---|---|---|---|
| 1 | Day 1 | View profile | — | — |
| 2 | Day 1-2 | Like recent post | — | — |
| 3 | Day 2-3 | Connection request | `li_connection_note` | ≤300 chars |
| — | — | [wait for acceptance] | — | — |
| 4 | +4-24h | DM 1 | `li_dm1` | ≤60 words |
| 5 | Day 8 | DM 2 (no reply) | Static by variant | ≤55 words |
| 6 | Day 14 | DM 3 Breakup | Static universal | ≤50 words |
