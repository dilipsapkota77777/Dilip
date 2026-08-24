# Clay ↔ Supabase field map

Two Clay tables, one Supabase schema. Company is the parent; people join to it on `company_id`.

```
Clay: Companies table          Clay: People table
        │                              │
        │ write                        │ write
        ▼                              ▼
  ndis.companies  ◄── company_id ── ndis.people
        │                              │
        ▼                              ▼
  ndis.v_companies               ndis.v_people
  (Company preview)              (People preview)
```

## Join key

Companies dedupe on **normalised domain**: protocol, `www.`, path and query stripped, lowercased.
Where no domain resolved, a normalised company name is used instead (suffixes like
`pty`, `ltd`, `group`, `services` removed).

`company_id = sha1(company_key)[:16]` — stable across re-exports, so re-running the build
against a fresh Clay export updates rows in place rather than duplicating them.

## People table → `ndis.people`

| Clay column | Supabase column | Notes |
|---|---|---|
| `first_name` | `first_name` | Split from `full_name` where blank |
| `last_name` | `last_name` | Split from `full_name` where blank |
| `full_name` | `full_name` | |
| `linkedin url` | `personal_linkedin_url` | `/in/` URLs only |
| `Sales nav profile_url` | `sales_nav_url` | Sales Navigator URLs routed here |
| `headline` | `headline` | |
| `location_name` | `location_name` | |
| `badges_premium` + `badges_job_seeker` | `linkedin_plan_badge` | `Premium` / `Free` / `Free (Open to Work)` |
| `current_company` | `current_company` | |
| `current_company_position` | `current_company_position` | Raw title |
| `clean current position` | `clean_current_position` | Normalised title |
| `Official Website URL` / `Website - Company` | `official_website_url` | |
| — | `company_domain` | Derived, normalised |
| `Position Tier` | `position_tier` | `A` / `B` / `C` / `none` |
| `NDIS Direct Support` | `ndis_direct_support` | `Yes` / `No` / `Unclear` |
| `Reasoning NDIS Direct Support` | `ndis_direct_support_reasoning` | |
| `Nursing Care Relevance` | `nursing_care_relevance` | `Yes` / `No` / `Unclear` |
| `Support Coordinator` | `is_support_coordinator` | Boolean |
| `Seek Signal Job Title` | `seek_signal_job_title` | Live hiring signal |
| `Start Date` | `start_date` | Text (`May 2024`), not a date type |
| `Time Since Start` | `time_since_start` | `2 years` |
| `Primary Email` → 6 fallbacks | `primary_email` | Waterfall, see below |
| `Email Status - Email` / `Status` | `email_status` | Normalised to `valid` / `unavailable` / `invalid` / `risky` |
| `Quality` / `million verifer Email` | `email_quality` | |
| `Employees` | `company_employee_total` | + banded into `company_size` |
| `Industry - Company` | `company_industry` | |
| `Company Linkedin Url` | `company_linkedin_url` | |

**Email waterfall order:** `Primary Email` → `Final Work Email` → `Email - Email` →
`Email - Person` → `email` → `LH Email` → `FM Email`. First non-empty wins.

## Companies table → `ndis.companies`

| Clay column | Supabase column | Status |
|---|---|---|
| `current_company` | `company_name` | Most frequent spelling on the domain |
| — | `company_name_variants` | Other spellings seen — audit aid |
| `Employees` → band | `company_size` | Sydney export only |
| `Website - Company` | `website` | |
| — | `domain` | Derived |
| `Industry - Company` | `industry` | |
| **not in source** | `founded_in` | **Clay fills** |
| `Description` | `description` | Sydney export only |
| **not in source** | `linkedin_description` | **Clay fills** |
| **not in source** | `company_type` | **Clay fills** — NFP / Private / Government |
| **not in source** | `annual_revenue` | **Clay fills** |
| `Employees` | `employee_total` | Sydney export only |
| **not in source** | `company_email` | **Clay fills** — generic `info@` |
| `Company Linkedin Url` | `linkedin_url` | |

The five **Clay fills** columns exist and are NULL, so an enrichment run writes straight
back into the same shape — no migration.

## Writing back from Clay

Use the Supabase HTTP API with your **service role** key (RLS grants it full access;
`anon` gets nothing).

Upsert a company:

```
POST https://<project>.supabase.co/rest/v1/companies?on_conflict=company_id
Headers:
  apikey: <service_role_key>
  Authorization: Bearer <service_role_key>
  Content-Type: application/json
  Prefer: resolution=merge-duplicates
Body:
  { "company_id": "{{company_id}}", "founded_in": {{founded_year}},
    "company_email": "{{generic_email}}", "company_type": "{{type}}" }
```

`Prefer: resolution=merge-duplicates` means only the keys you send are updated —
existing values on other columns are untouched.

## Reading back into Clay

The lookup you run most — support coordinator emails for an organisation:

```sql
select * from ndis.support_coordinators('uniting');
```

As an HTTP GET from a Clay enrichment column:

```
GET https://<project>.supabase.co/rest/v1/rpc/support_coordinators?org=uniting
```

Or filter the view directly:

```
GET https://<project>.supabase.co/rest/v1/v_support_coordinator_emails?domain=eq.uniting.org
```

## Views available

| View | What it is |
|---|---|
| `ndis.v_people` | Preview mode 1 — one row per person, company data joined on |
| `ndis.v_companies` | Preview mode 2 — one row per organisation, people rolled up to counts |
| `ndis.v_support_coordinator_emails` | Support coordinators who have an email |
| `ndis.v_ready_to_send` | Tier A/B coordinators with a sendable email — the Smartlead list |
| `ndis.v_enrichment_gaps` | What Clay still needs to fill, biggest accounts first |

`v_people` adds a derived `send_readiness` column: `sendable` / `unverified` /
`do_not_send` / `no_email`.
