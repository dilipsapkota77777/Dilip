# Triple R — Clay QA Layer
# The gate that would have caught all 4 copy defects before send
Generated: 2026-08-14

---

## Why this exists

Campaign 3 shipped 2,958 emails containing:
- 149 unrendered `[First Name]` merge tags
- 791 double-name greetings
- 1,328 singular job titles
- 613 VIC emails citing NSW

Every one of these was detectable **before send** with a Clayscript column. None required judgement. This file adds a hard gate that blocks any row that would produce a defective email.

---

## Column 1 — `first_name_clean`

Never let a raw name field reach a template.

```javascript
const raw = String({{first_name}} || {{full_name}} || "").trim();
if (!raw) return "";

// Take first token, strip punctuation and initials-only values
let fn = raw.split(/\s+/)[0].replace(/[^A-Za-z'\-]/g, "");

// Reject initials ("A.", "J") and all-caps noise
if (fn.length < 2) return "";

// Title-case it — source data has ALL CAPS and lowercase entries
return fn.charAt(0).toUpperCase() + fn.slice(1).toLowerCase();
```

---

## Column 2 — `position_plural`

Fixes "We work with Support Coordinator who need…" (44.9% of v1 sends).

```javascript
const pos = String({{clean current position}} || {{current_company_position}} || "").toLowerCase().trim();

if (pos.includes("support coordinator")) return "support coordinators";
if (pos.includes("case manager")) return "case managers";
if (pos.includes("clinical care coordinator")) return "clinical care coordinators";
if (pos.includes("care coordinator")) return "care coordinators";
if (pos.includes("care manager")) return "care managers";
if (pos.includes("recovery coach")) return "recovery coaches";
if (pos.includes("plan manager")) return "plan managers";

// Safe generic fallback — never returns empty
return "coordinators";
```

---

## Column 3 — `region` and `region_phrase`

Fixes the 613 VIC emails that cited NSW.

```javascript
// region
const loc = String({{location_name}} || "").toLowerCase();
const state = String({{Campaign Label}} || "").toLowerCase();

if (loc.includes("victoria") || loc.includes("melbourne") || loc.includes("vic") ||
    state.includes("vic")) return "VIC";
if (loc.includes("new south wales") || loc.includes("sydney") || loc.includes("nsw") ||
    state.includes("sydney") || state.includes("nsw")) return "NSW";

return "UNKNOWN";
```

```javascript
// region_phrase
const r = String({{region}} || "");
if (r === "VIC") return "across Victoria";
if (r === "NSW") return "across NSW";
return "";  // omit the phrase entirely rather than guess
```

```javascript
// region_phone
const r = String({{region}} || "");
if (r === "VIC") return "{{VIC_PHONE}}";   // replace with the real VIC number
if (r === "NSW") return "(02) 8044 1775";
return "";
```

---

## Column 4 — `pers_sentence_safe`

Fixes the headless first-person bug that confused Oriana Cerven.

The failing sentence was:
> "Just joined the role at Abled Care Services — already juggling aged-care referrals…"

No grammatical subject, so it reads as *the sender* joining their company.

```javascript
const s = String({{pers_sentence}} || "").trim();
if (!s) return "";

// Reject headless fragments that begin with a bare verb/adverb —
// these read as first person about the SENDER
const headless = /^(just |recently |now |already |currently |newly )/i;
if (headless.test(s)) return "";   // drop it; template falls back to generic

// Reject sentences that are only a fragment (no subject pronoun anywhere)
if (!/\b(you|your|you're|youre)\b/i.test(s)) return "";

return s;
```

**Rule: a personalisation sentence that cannot be verified as second-person gets dropped, not sent.** A generic email beats an email that appears to claim the sender works at the recipient's company.

---

## Column 5 — `qa_pass` (THE GATE)

Nothing sends unless this returns `PASS`.

```javascript
const issues = [];

const fn    = String({{first_name_clean}} || "").trim();
const pos   = String({{position_plural}}  || "").trim();
const reg   = String({{region}}           || "").trim();
const phone = String({{region_phone}}     || "").trim();
const email = String({{Primary Email}}    || "").trim();
const pers  = String({{pers_sentence_safe}} || "").trim();

// 1. Name must exist and be clean
if (!fn)                       issues.push("no first name");
if (/[\[\]{}<>]/.test(fn))     issues.push("bracket/tag in first name");

// 2. Position must resolve
if (!pos)                      issues.push("no position");

// 3. Region must be known — prevents NSW copy going to VIC
if (reg === "UNKNOWN" || !reg) issues.push("region unresolved");
if (!phone)                    issues.push("no region phone");

// 4. Email must be valid-shaped
if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) issues.push("invalid email");

// 5. Personalisation must be second-person or absent (never headless)
if (pers && !/\b(you|your)\b/i.test(pers)) issues.push("personalisation not second-person");

return issues.length === 0 ? "PASS" : "BLOCK: " + issues.join("; ");
```

**Filter every send view to `qa_pass = "PASS"`. No exceptions.**

---

## Column 6 — `rendered_preview` (final safety net)

Renders the actual Email 1 body in Clay so you can eyeball it before export. Catches anything the rules missed.

```javascript
const fn    = String({{first_name_clean}} || "");
const phone = String({{region_phone}} || "");

const body = `Hi ${fn},

When a participant on your caseload needs clinical nursing — wound care, PEG feeding, complex medication — how long does it take to find a provider who'll actually take them?

That's usually the referral that sits.

Triple R takes those. You stay the Support Coordinator, keep the participant, keep your billable hours. We deliver only the clinical nursing your organisation doesn't.

Assessed within 48 hours. NDIS registered, RN-led.

Worth seeing how the referral pathway works?

Kalpana Sharma
Triple R Community Care
${phone}`;

// Self-check the rendered output
if (/\[|\]|\{\{|\}\}|undefined|null/.test(body)) return "❌ DEFECT IN RENDER";
if (/Hi ,/.test(body))                            return "❌ EMPTY NAME";
if (/  /.test(body))                              return "⚠️ DOUBLE SPACE";

return body;
```

Sort by this column and scan 20 rows before every export. Any `❌` means stop.

---

## Pre-send checklist

Run in order. Do not skip.

- [ ] `qa_pass` = "PASS" filter applied to the send view
- [ ] Row count after filter recorded (expect to lose 10–20% — that is the gate working)
- [ ] `rendered_preview` scanned on 20 random rows, zero `❌`
- [ ] Searched `rendered_preview` for `[` and `{{` — zero hits
- [ ] VIC rows spot-checked: no "NSW", no (02) number
- [ ] NSW rows spot-checked: no "Victoria", no VIC number
- [ ] **Sender name in the platform matches the signature name** (v1 failed this — signature said Kalpana, replies said Rajesh)
- [ ] All emails re-verified; bounce forecast under 1%
- [ ] Pattern-guessed addresses at large orgs (lwb.org.au, vinnies.org.au, anglicare.org.au, wesleymission.org.au) removed unless individually verified
- [ ] Send a live test to your own inbox and read it on a phone
- [ ] Referral pathway link tested and click-tracking confirmed firing

---

## Ongoing monitoring

| Check | Frequency | Trigger to stop |
|---|---|---|
| Bounce rate | Daily, first week | >2% → pause immediately |
| Click rate on referral pathway | Weekly | <2% after 200 sends → asset is wrong |
| Reply sentiment split | Weekly | >50% auto-replies → list is stale |
| Auto-reply share | Weekly | Rising trend → contacts have moved on |

**Note on auto-replies:** 9 of 14 v1 "replies" were out-of-office responders. Configure the sending platform to classify these separately so they never inflate the reply metric again.
