#!/usr/bin/env python3
"""
Build NDIS_Master_Database.xlsx - the field-review workbook.

Sheets:
  README          how the pieces fit together
  Field Map       every column: which view, source column, type, fill rate
  People View     preview mode 1 - one row per person
  Company View    preview mode 2 - one row per company
  Support Coords  the extraction you run most: coordinators with emails
  QA              coverage stats + flagged rows
"""
import argparse
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

NAVY = "1F3864"
GREY = "F2F2F2"
AMBER = "FFF2CC"
GREEN = "E2EFDA"
RED = "FCE4E4"

HDR_FONT = Font(bold=True, color="FFFFFF", size=11)
HDR_FILL = PatternFill("solid", fgColor=NAVY)
TITLE_FONT = Font(bold=True, size=14, color=NAVY)
THIN = Border(*[Side(style="thin", color="D0D0D0")] * 4)


def style_header(ws, row=1, ncols=None):
    ncols = ncols or ws.max_column
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HDR_FONT
        cell.fill = HDR_FILL
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 30
    ws.freeze_panes = ws.cell(row=row + 1, column=1)


def autosize(ws, max_w=52, header_row=1):
    for col in range(1, ws.max_column + 1):
        letter = get_column_letter(col)
        longest = 0
        for row in range(header_row, min(ws.max_row, 400) + 1):
            v = ws.cell(row=row, column=col).value
            if v is not None:
                longest = max(longest, min(len(str(v)), max_w))
        ws.column_dimensions[letter].width = max(11, min(longest + 3, max_w))


def add_df(wb, title, df, note=None, freeze_cols=0):
    ws = wb.create_sheet(title)
    start = 1
    if note:
        ws.cell(row=1, column=1, value=note).font = Font(italic=True, color="595959")
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(len(df.columns), 2))
        start = 3

    for j, col in enumerate(df.columns, start=1):
        ws.cell(row=start, column=j, value=str(col))
    for i, (_, r) in enumerate(df.iterrows(), start=start + 1):
        for j, col in enumerate(df.columns, start=1):
            v = r[col]
            if pd.isna(v):
                v = None
            elif isinstance(v, (list, dict)):
                v = str(v)
            elif not isinstance(v, (int, float, bool)):
                v = str(v)[:1000]
            ws.cell(row=i, column=j, value=v)

    style_header(ws, row=start)
    if freeze_cols:
        ws.freeze_panes = ws.cell(row=start + 1, column=freeze_cols + 1)
    autosize(ws, header_row=start)

    if len(df):
        ref = f"A{start}:{get_column_letter(len(df.columns))}{start + len(df)}"
        t = Table(displayName=title.replace(" ", "_"), ref=ref)
        t.tableStyleInfo = TableStyleInfo(
            name="TableStyleLight9", showRowStripes=True)
        ws.add_table(t)
    return ws


# ---------------------------------------------------------------------
# field map: the sheet you actually review before wiring Clay
# ---------------------------------------------------------------------

PEOPLE_MAP = [
    # (column, source column(s) in the Clay export, type, note)
    ("person_id", "derived: sha1(linkedin + name + company)", "text", "Primary key. Stable across re-exports."),
    ("first_name", "first_name", "text", "Split from full_name where blank."),
    ("last_name", "last_name", "text", "Split from full_name where blank."),
    ("full_name", "full_name", "text", ""),
    ("personal_linkedin_url", "linkedin url / profile_url", "text", "/in/ URLs only. Sales Nav URLs routed to sales_nav_url."),
    ("headline", "headline", "text", "LinkedIn headline."),
    ("location_name", "location_name", "text", "Free-text suburb, state, country."),
    ("state", "derived from source file", "text", "NSW or VIC."),
    ("linkedin_plan_badge", "badges_premium + badges_job_seeker", "text", "Premium / Free / Free (Open to Work)."),
    ("current_company", "current_company", "text", ""),
    ("current_company_position", "current_company_position", "text", "Raw job title."),
    ("clean_current_position", "clean current position", "text", "Normalised title."),
    ("official_website_url", "Website - Company > Official Website URL", "text", "Company site."),
    ("domain", "derived: normalised from website", "text", "Lowercase, no protocol/www/path. Join key to companies."),
    ("position_tier", "Position Tier", "text", "A / B / C / none. 'none' = evaluated, did not qualify."),
    ("ndis_direct_support", "NDIS Direct Support", "text", "Yes / No / Unclear."),
    ("ndis_direct_support_reasoning", "Reasoning NDIS Direct Support", "text", "AI justification paragraph."),
    ("nursing_care_relevance", "Nursing Care Relevance", "text", "Yes / No / Unclear."),
    ("is_support_coordinator", "Support Coordinator", "boolean", "True where the source flagged the role."),
    ("support_coordinator_job_signal", "Support Coordinator / Seek Signal Job Title", "text", "Hiring signal for the role."),
    ("seek_signal_job_title", "Seek Signal Job Title", "text", "Live Seek ad title, where found."),
    ("start_date", "Start Date", "text", "Source format 'May 2024'. Text, not date."),
    ("time_since_start", "Time Since Start", "text", "'2 years'. Tenure signal."),
    ("primary_email", "Primary Email > Final Work Email > ...", "text", "Waterfall across 7 source email columns."),
    ("email_status", "Email Status - Email / Status", "text", "Normalised: valid / unavailable / invalid / risky."),
    ("email_quality", "Quality / million verifier", "text", "Verifier verdict, e.g. good."),
    ("send_readiness", "derived (view only)", "text", "sendable / unverified / do_not_send / no_email."),
    ("company_size", "derived from Employees", "text", "Band: 11-50, 51-200, ..."),
    ("employee_total", "Employees", "integer", ""),
    ("industry", "Industry - Company", "text", "LinkedIn industry label."),
    ("company_linkedin_url", "Company Linkedin Url", "text", ""),
    ("company_id", "derived: sha1(domain key)", "text", "FK to companies."),
    ("company_name_matches_domain", "derived QA", "boolean", "FALSE = source enrichment put this person on the wrong domain. Review before sending."),
]

COMPANY_MAP = [
    ("company_id", "derived: sha1(domain key)", "text", "Primary key."),
    ("company_name", "current_company", "text", "Most frequent spelling on the domain."),
    ("company_name_variants", "current_company", "text", "Other spellings seen. Audit aid."),
    ("company_size", "derived from Employees", "text", "Band."),
    ("website", "Website - Company > Official Website URL", "text", ""),
    ("domain", "derived: normalised website", "text", "Dedupe key."),
    ("industry", "Industry - Company", "text", ""),
    ("founded_in", "NOT IN SOURCE", "integer", "EMPTY - Clay fills. Source 'Size - Company' was a mis-mapped date, kept as founded_raw."),
    ("description", "Description", "text", "Sydney export only. VIC rows empty - Clay fills."),
    ("linkedin_description", "NOT IN SOURCE", "text", "EMPTY - Clay fills from company LinkedIn About."),
    ("company_type", "NOT IN SOURCE", "text", "EMPTY - Clay fills. NFP / Private / Government."),
    ("annual_revenue", "NOT IN SOURCE", "text", "EMPTY - Clay fills."),
    ("employee_total", "Employees", "integer", "Sydney export only."),
    ("company_email", "NOT IN SOURCE", "text", "EMPTY - Clay fills. Generic info@/contact@."),
    ("linkedin_url", "Company Linkedin Url", "text", ""),
    ("state", "derived from source file", "text", "NSW / VIC."),
    ("ndis_direct_support", "NDIS Direct Support", "text", "Rolled up from its people."),
    ("nursing_care_relevance", "Nursing Care Relevance", "text", "Rolled up."),
    ("position_tier_best", "Position Tier", "text", "Best tier among its people."),
    ("people_count", "derived", "integer", "People on this company in the people table."),
    ("support_coordinator_count", "derived", "integer", "How many are support coordinators."),
    ("people_with_email_count", "derived", "integer", "How many have an email."),
    ("email_coverage_pct", "derived (view only)", "integer", "Reachability of the account."),
]


def fill_rate(df, col):
    if col not in df.columns:
        return ""
    return round(100 * df[col].notna().mean())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="../data")
    args = ap.parse_args()
    d = os.path.abspath(args.data)

    people = pd.read_csv(os.path.join(d, "people.csv"), low_memory=False)
    companies = pd.read_csv(os.path.join(d, "companies.csv"), low_memory=False)

    wb = Workbook()
    wb.remove(wb.active)

    # ---------------- README ----------------
    ws = wb.create_sheet("README")
    lines = [
        ("Triple R NDIS Outreach Database", "title"),
        ("", ""),
        ("Built from two Clay master-table cold exports, Campaign 3: Sydney (NSW) and VIC.", ""),
        ("", ""),
        ("WHAT IS IN HERE", "h"),
        ("Field Map", "Every column in both views: where it came from, its type, and how full it is. Review this sheet before wiring Clay."),
        ("People View", f"Preview mode 1. One row per person ({len(people):,} rows). Carries company data on each row."),
        ("Company View", f"Preview mode 2. One row per organisation ({len(companies):,} rows). No people columns - they roll up to counts."),
        ("Support Coords", "The extraction you run most: support coordinators who have an email, by organisation."),
        ("QA", "Coverage stats and the rows worth checking before you send."),
        ("", ""),
        ("HOW THE TWO VIEWS RELATE", "h"),
        ("", "people.company_id -> companies.company_id"),
        ("", "Companies are deduped on normalised domain (protocol/www/path stripped, lowercased),"),
        ("", "falling back to a normalised company name where no domain resolved."),
        ("", ""),
        ("IN SUPABASE", "h"),
        ("", "sql/01_schema.sql   tables, indexes, RLS"),
        ("", "sql/02_views.sql    ndis.v_people, ndis.v_companies, and the extraction views"),
        ("", "sql/03_load_from_csv.sql   load the two CSVs"),
        ("", ""),
        ("", "The query you asked for - support coordinator emails for an organisation:"),
        ("", "    select * from ndis.support_coordinators('uniting');"),
        ("", ""),
        ("KNOWN GAPS - Clay fills these", "h"),
        ("founded_in", "Not present in either export. The source 'Size - Company' column held a mis-mapped date with only 2 distinct values; kept as founded_raw for audit only."),
        ("company_email", "Not present. Generic info@/contact@ address."),
        ("company_type", "Not present. NFP / Private / Government."),
        ("annual_revenue", "Not present."),
        ("linkedin_description", "Not present. Company LinkedIn About text."),
        ("description, employee_total", "Sydney export only. Every VIC company row is empty."),
        ("", ""),
        ("These columns exist and are empty, so Clay writes straight back into the same shape - no migration needed.", ""),
    ]
    r = 1
    for a, b in lines:
        if b == "title":
            c = ws.cell(row=r, column=1, value=a); c.font = TITLE_FONT
        elif b == "h":
            c = ws.cell(row=r, column=1, value=a)
            c.font = Font(bold=True, size=11, color=NAVY)
        else:
            ws.cell(row=r, column=1, value=a).font = Font(bold=True)
            ws.cell(row=r, column=2, value=b)
        r += 1
    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 110
    for row in ws.iter_rows(min_col=2, max_col=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")

    # ---------------- Field Map ----------------
    rows = []
    for view, mapping, df in (("People", PEOPLE_MAP, people),
                              ("Company", COMPANY_MAP, companies)):
        for col, src, typ, note in mapping:
            lookup = {"domain": "company_domain", "employee_total": "company_employee_total",
                      "industry": "company_industry"}.get(col, col) if view == "People" else col
            fr = fill_rate(df, lookup)
            rows.append({
                "View": view,
                "Column": col,
                "Source column in Clay export": src,
                "Type": typ,
                "% filled": fr if fr != "" else ("0" if "NOT IN SOURCE" in src else ""),
                "Notes": note,
            })
    fm = pd.DataFrame(rows)
    ws = add_df(wb, "Field Map", fm,
                note="Review this before mapping Clay. '% filled' is measured on the built dataset. "
                     "NOT IN SOURCE = the column exists and is empty, waiting for Clay.")
    # colour-code coverage
    for i in range(4, ws.max_row + 1):
        v = ws.cell(row=i, column=5).value
        try:
            v = float(v)
        except (TypeError, ValueError):
            continue
        fill = GREEN if v >= 80 else (AMBER if v >= 30 else RED)
        ws.cell(row=i, column=5).fill = PatternFill("solid", fgColor=fill)

    # ---------------- People View ----------------
    pv_cols = [c for c in [
        "person_id", "first_name", "last_name", "full_name", "personal_linkedin_url",
        "headline", "location_name", "state", "linkedin_plan_badge", "current_company",
        "current_company_position", "clean_current_position", "official_website_url",
        "company_domain", "position_tier", "ndis_direct_support",
        "ndis_direct_support_reasoning", "nursing_care_relevance",
        "is_support_coordinator", "support_coordinator_job_signal", "seek_signal_job_title",
        "start_date", "time_since_start", "primary_email", "email_status", "email_quality",
        "company_size", "company_employee_total", "company_industry",
        "company_linkedin_url", "company_id", "company_name_matches_domain",
    ] if c in people.columns]
    add_df(wb, "People View", people[pv_cols],
           note=f"Preview mode 1 - one row per person. {len(people):,} rows. "
                f"Mirrors ndis.v_people in Supabase.", freeze_cols=4)

    # ---------------- Company View ----------------
    cv = companies.copy()
    cv["email_coverage_pct"] = (
        100 * cv["people_with_email_count"] / cv["people_count"].replace(0, pd.NA)
    ).round(0)
    cv_cols = [c for c in [
        "company_id", "company_name", "company_name_variants", "company_size", "website",
        "domain", "industry", "founded_in", "description", "linkedin_description",
        "company_type", "annual_revenue", "employee_total", "company_email",
        "linkedin_url", "state", "ndis_direct_support", "nursing_care_relevance",
        "position_tier_best", "people_count", "support_coordinator_count",
        "people_with_email_count", "email_coverage_pct",
    ] if c in cv.columns]
    add_df(wb, "Company View", cv[cv_cols],
           note=f"Preview mode 2 - one row per organisation. {len(cv):,} rows. "
                f"Mirrors ndis.v_companies. Sorted by support coordinator count.",
           freeze_cols=2)

    # ---------------- Support Coords ----------------
    sc = people[people["is_support_coordinator"].fillna(False).astype(bool)
                & people["primary_email"].notna()].copy()
    sc = sc.merge(companies[["company_id", "company_name", "domain", "industry"]],
                  on="company_id", how="left")
    sc_cols = ["company_name", "domain", "industry", "state", "full_name",
               "clean_current_position", "primary_email", "email_status",
               "email_quality", "personal_linkedin_url", "position_tier",
               "time_since_start"]
    sc = sc[[c for c in sc_cols if c in sc.columns]].sort_values(
        ["company_name", "full_name"])
    add_df(wb, "Support Coords", sc,
           note=f"{len(sc):,} support coordinators with an email on file. "
                f"Mirrors ndis.v_support_coordinator_emails.", freeze_cols=1)

    # ---------------- QA ----------------
    qa = []
    qa.append(("People rows", len(people)))
    qa.append(("  NSW", int((people["state"] == "NSW").sum())))
    qa.append(("  VIC", int((people["state"] == "VIC").sum())))
    qa.append(("Company rows", len(companies)))
    qa.append(("", ""))
    qa.append(("People with an email", int(people["primary_email"].notna().sum())))
    qa.append(("  email_status = valid", int((people["email_status"] == "valid").sum())))
    qa.append(("  email_status = unavailable", int((people["email_status"] == "unavailable").sum())))
    qa.append(("Support coordinators", int(people["is_support_coordinator"].fillna(False).astype(bool).sum())))
    qa.append(("  ...with an email", len(sc)))
    qa.append(("", ""))
    qa.append(("Position tier A", int((people["position_tier"] == "A").sum())))
    qa.append(("Position tier B", int((people["position_tier"] == "B").sum())))
    qa.append(("Position tier C", int((people["position_tier"] == "C").sum())))
    qa.append(("Position tier none (evaluated, no fit)", int((people["position_tier"] == "none").sum())))
    qa.append(("", ""))
    qa.append(("FLAG: company name disagrees with resolved domain",
               int((people["company_name_matches_domain"] == False).sum())))
    qa.append(("  These are source enrichment mismatches. Flagged, not dropped.", ""))
    qa.append(("", ""))
    qa.append(("Companies missing founded_in", int(companies["founded_in"].isna().sum())))
    qa.append(("Companies missing description", int(companies["description"].isna().sum())))
    qa.append(("Companies missing employee_total", int(companies["employee_total"].isna().sum())))
    qa.append(("Companies missing linkedin_url", int(companies["linkedin_url"].isna().sum())))
    qa.append(("Companies missing industry", int(companies["industry"].isna().sum())))

    ws = wb.create_sheet("QA")
    ws.cell(row=1, column=1, value="Coverage & data quality").font = TITLE_FONT
    ws.cell(row=3, column=1, value="Metric").font = HDR_FONT
    ws.cell(row=3, column=1).fill = HDR_FILL
    ws.cell(row=3, column=2, value="Count").font = HDR_FONT
    ws.cell(row=3, column=2).fill = HDR_FILL
    for i, (k, v) in enumerate(qa, start=4):
        ws.cell(row=i, column=1, value=k)
        ws.cell(row=i, column=2, value=v if v != "" else None)
        if str(k).startswith("FLAG"):
            ws.cell(row=i, column=1).fill = PatternFill("solid", fgColor=AMBER)
            ws.cell(row=i, column=2).fill = PatternFill("solid", fgColor=AMBER)
    ws.column_dimensions["A"].width = 52
    ws.column_dimensions["B"].width = 14
    ws.freeze_panes = "A4"

    out = os.path.join(d, "NDIS_Master_Database.xlsx")
    wb.save(out)
    print("wrote", out)
    for s in wb.sheetnames:
        print("  sheet:", s)


if __name__ == "__main__":
    main()
