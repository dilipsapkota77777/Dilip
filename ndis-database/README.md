# Triple R NDIS Outreach Database

Two Clay master-table cold exports (Sydney/NSW + VIC, Campaign 3) combined into one
database with two preview modes: **people** and **company**.

```
ndis-database/
├── data/
│   ├── NDIS_Master_Database.xlsx   ← start here: field map + both views + QA
│   ├── people.csv                  3,202 rows — people view
│   ├── companies.csv               1,537 rows — company view
│   └── master_combined.csv         3,215 rows × 91 cols — raw union, nothing dropped
├── sql/
│   ├── 01_schema.sql               tables, indexes, RLS
│   ├── 02_views.sql                v_people, v_companies + extraction views
│   └── 03_load_from_csv.sql        load instructions (dashboard or psql)
├── scripts/
│   ├── build_dataset.py            regenerate the CSVs from fresh exports
│   └── build_workbook.py           regenerate the Excel workbook
└── docs/
    └── clay_field_map.md           Clay ↔ Supabase mapping + API snippets
```

## What's in it

| | Rows |
|---|---|
| People | 3,202 (1,913 NSW, 1,289 VIC) |
| Companies | 1,537 |
| People with an email | 1,449 — 931 verified valid |
| Support coordinators | 698 — 324 with an email |
| Position tier A | 2,550 |

## Setup

1. Supabase → SQL Editor → run `sql/01_schema.sql`, then `sql/02_views.sql`.
2. Load the data — Table Editor → import CSV, **companies first** (people reference it),
   or `psql "$SUPABASE_DB_URL" -f sql/03_load_from_csv.sql` from the `sql/` directory.

## The query this was built for

```sql
select * from ndis.support_coordinators('uniting');
select * from ndis.support_coordinators('abilityoptions.org.au');
```

Matches on domain or company name, case-insensitive and partial. Returns name, position,
email, verification status and LinkedIn URL for every support coordinator at that org.

## Regenerating

```bash
cd scripts
python3 build_dataset.py --sydney <sydney.csv> --vic <vic.csv> --out ../data
python3 build_workbook.py --data ../data
```

`person_id` and `company_id` are content hashes, so a re-run against a fresh export
updates rows in place instead of duplicating them.

## Data notes

**Company dedupe** is on normalised domain (protocol/`www`/path stripped, lowercased),
falling back to a normalised company name. Company names use the *most frequent* spelling
on a domain — 27 "Uniting" people and 1 mislabelled row on `uniting.org` resolve to
"Uniting", with the outlier preserved in `company_name_variants`.

**300 people carry `company_name_matches_domain = false`** — the source enrichment put
them on a domain that disagrees with their stated employer. They are flagged, not dropped.
Worth a look before sending.

**Missing by design.** These columns exist and are NULL for Clay to fill:
`founded_in`, `company_email`, `company_type`, `annual_revenue`, `linkedin_description`.
`description` and `employee_total` are Sydney-only — every VIC company row is empty.

**`Size - Company`** in the source was a mis-mapped date field (two distinct values across
both files, e.g. `2001-11-20T00:00:00.000Z`). It is *not* company size. Real size is banded
from `Employees` into `company_size`; the original is kept as `founded_raw` for audit only.

**`position_tier = 'none'`** means evaluated and did not qualify — distinct from NULL,
which means never evaluated. 497 rows are explicitly `none`.
