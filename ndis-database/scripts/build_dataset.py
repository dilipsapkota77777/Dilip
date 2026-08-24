#!/usr/bin/env python3
"""
Build the unified Triple R NDIS outreach database from the Sydney (NSW) and VIC
Clay master-table exports.

Outputs (into ../data):
  people.csv           - one row per person  (people-level view)
  companies.csv        - one row per company (company-level view)
  master_combined.csv  - full union of both source files, columns aligned
  NDIS_Master_Database.xlsx - Excel workbook: field map + both views + QA

Usage:
  python3 build_dataset.py --sydney <path.csv> --vic <path.csv> --out ../data
"""
import argparse
import hashlib
import os
import re
import pandas as pd

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

BAD = {"", "nan", "none", "null", "n/a", "na", "-", "#n/a"}
JUNK_PREFIX = ("❌", "⚠️")


def clean(v, keep_none=False):
    """Normalize any cell to a stripped string or None.

    keep_none preserves a literal "none" -- for Position Tier that is a real
    verdict (evaluated, did not qualify), not a missing value.
    """
    if v is None:
        return None
    s = str(v).strip()
    if s.startswith(JUNK_PREFIX):
        return None
    if s.lower() in BAD and not (keep_none and s.lower() == "none"):
        return None
    return s


def first(row, *cols):
    """First non-empty value across a priority list of source columns."""
    for c in cols:
        if c in row.index:
            v = clean(row[c])
            if v:
                return v
    return None


def norm_domain(url):
    """example: https://www.SSI.org.au/about?x=1 -> ssi.org.au"""
    u = clean(url)
    if not u:
        return None
    u = u.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("/")[0].split("?")[0].split("#")[0].strip(" .,")
    if "." not in u or " " in u:
        return None
    return u or None


def norm_linkedin(url):
    """Canonical personal LinkedIn /in/ URL, no query string or trailing slash.

    Returns None for Sales Navigator URLs -- those belong in sales_nav_url.
    """
    u = clean(url)
    if not u or "/sales/" in u:
        return None
    u = u.split("?")[0].rstrip("/").strip()
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://[a-z]{2,3}\.linkedin\.com", "https://www.linkedin.com", u)
    return u or None


def norm_name_key(name):
    """Loose company-name key: lowercase alnum, common suffixes dropped."""
    n = clean(name)
    if not n:
        return None
    n = n.lower()
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(
        r"\b(pty|ltd|limited|inc|incorporated|llc|group|australia|aust|"
        r"services|service|the|and|co)\b",
        " ",
        n,
    )
    n = re.sub(r"\s+", "", n)
    return n or None


def yes_no(v):
    """The AI columns hold 'No' or a long 'Yes, <org> provides...' paragraph."""
    s = clean(v)
    if not s:
        return None
    low = s.lower()
    if low.startswith("no"):
        return "No"
    if low.startswith("yes"):
        return "Yes"
    if low.startswith(("unclear", "uncertain", "unknown")):
        return "Unclear"
    # a descriptive paragraph with no lead-in still asserts provision
    return "Yes" if len(s) > 40 else s


def sid(*parts):
    """Stable id from any set of parts."""
    raw = "|".join(p or "" for p in parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def plan_badge(premium, jobseeker):
    p = clean(premium)
    j = clean(jobseeker)
    if p and p.upper() == "TRUE":
        return "Premium"
    if j and j.upper() == "TRUE":
        return "Free (Open to Work)"
    if p and p.upper() == "FALSE":
        return "Free"
    return None


EMAIL_STATUS = {
    "verified": "valid", "valid": "valid", "ok": "valid", "deliverable": "valid",
    "unavailable": "unavailable", "not_found": "unavailable",
    "invalid": "invalid", "risky": "risky", "catch_all": "catch_all",
    "catch-all": "catch_all", "accept_all": "catch_all", "unknown": "unknown",
}


def norm_email_status(v):
    s = clean(v)
    if not s:
        return None
    return EMAIL_STATUS.get(s.strip().lower(), s.strip().lower())


def int_or_none(v):
    s = clean(v)
    if not s:
        return None
    try:
        return int(float(s.replace(",", "")))
    except ValueError:
        return None


def size_band(n):
    """Employee count -> the band Clay and LinkedIn both speak."""
    if n is None:
        return None
    for hi, label in (
        (1, "1"), (10, "2-10"), (50, "11-50"), (200, "51-200"),
        (500, "201-500"), (1000, "501-1000"), (5000, "1001-5000"),
        (10000, "5001-10000"),
    ):
        if n <= hi:
            return label
    return "10001+"


# --------------------------------------------------------------------------
# people-level mapping
# --------------------------------------------------------------------------

def build_person(row, state, source_file):
    linkedin = norm_linkedin(first(row, "linkedin url", "profile_url"))
    sales_nav = first(row, "Sales nav profile_url", "linkedin url", "profile_url")
    sales_nav = sales_nav if sales_nav and "/sales/" in sales_nav else None
    full_name = first(row, "full_name")
    first_name = first(row, "first_name")
    last_name = first(row, "last_name")

    if not first_name and full_name:
        first_name = full_name.split()[0]
    if not last_name and full_name and len(full_name.split()) > 1:
        last_name = full_name.split()[-1]
    if not full_name and (first_name or last_name):
        full_name = " ".join(x for x in (first_name, last_name) if x)

    company_name = first(row, "current_company", "original_current_company")

    # Website - Company is the enriched company site and is the most reliable;
    # Final Domain URL is last because it carries bad SERP matches
    # (e.g. SSI -> ssa.gov/ssi).
    domain = None
    for c in ("Website - Company", "Website", "Official Website URL url",
              "Official Website URL", "NDIS Website URL website Url",
              "NDIS Website URL", "Final Domain URL"):
        domain = norm_domain(row[c]) if c in row.index else None
        if domain:
            break

    website = first(row, "Website - Company", "Website", "Official Website URL url",
                    "Official Website URL", "Final Domain URL")

    email = first(row, "Primary Email", "Final Work Email", "Email - Email",
                  "Email - Person", "email", "LH Email", "FM Email")
    email_status = norm_email_status(first(
        row, "Email Status - Email", "Email Status - Contact - Person", "Status"))
    email_quality = first(row, "Quality", "million verifer Email",
                          "MILION VERIFY Email", "Result")

    employees = int_or_none(first(row, "Employees"))

    company_key = domain or norm_name_key(company_name)

    return {
        # ---- identity
        "person_id": sid(linkedin or "", full_name or "", company_name or ""),
        "company_id": sid(company_key) if company_key else None,
        "company_key": company_key,
        # ---- name
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        # ---- linkedin profile
        "personal_linkedin_url": linkedin,
        "sales_nav_url": sales_nav,
        "headline": first(row, "headline"),
        "location_name": first(row, "location_name"),
        "state": state,
        "linkedin_plan_badge": plan_badge(
            row.get("badges_premium"), row.get("badges_job_seeker")),
        "is_open_to_work": (clean(row.get("badges_job_seeker")) or "").upper() == "TRUE",
        # ---- current role
        "current_company": company_name,
        "current_company_position": first(
            row, "current_company_position", "original_current_company_position",
            "current_company_custom_position"),
        "clean_current_position": first(row, "clean current position"),
        "position_tier": clean(row.get("Position Tier"), keep_none=True),
        "domain_position": first(row, "Domain | Position"),
        "start_date": first(row, "Start Date"),
        "time_since_start": first(row, "Time Since Start"),
        # ---- qualification signals
        "ndis_direct_support": yes_no(first(row, "NDIS Direct Support")),
        "ndis_direct_support_reasoning": first(
            row, "Reasoning NDIS Direct Support", "NDIS Direct Support"),
        "nursing_care_relevance": yes_no(first(
            row, "Nursing Care Relevance",
            "Does This organization provide nursing care")),
        "nursing_care_reasoning": first(
            row, "Does This organization provide nursing care",
            "Nursing Care Relevance"),
        "cald_services": first(row, "CALD Services"),
        "is_support_coordinator": bool(first(row, "Support Coordinator")),
        "support_coordinator_job_signal": first(
            row, "Support Coordinator", "Seek Signal Job Title",
            "Support Coordinator Jobs"),
        "seek_signal_job_title": first(row, "Seek Signal Job Title"),
        "icp_score": first(row, "ICP Score"),
        # ---- contact
        "official_website_url": website,
        "company_domain": domain,
        "primary_email": email,
        "email_status": email_status,
        "email_quality": email_quality,
        "has_email": bool(email),
        # ---- company snapshot carried on the person row
        "company_size": size_band(employees),
        "company_employee_total": employees,
        "company_industry": first(row, "Industry - Company"),
        "company_linkedin_url": first(row, "Company Linkedin Url", "Linkedin - Company"),
        # ---- campaign
        "campaign_label": first(row, "Campaign Label"),
        "outreach_channel": first(row, "Outreach Channel"),
        "smartlead_sequence": first(row, "Smartlead Sequence"),
        "ready_to_push": first(row, "Ready to Push"),
        "personalized_opening_line": first(row, "Personalized Opening Line"),
        "email_subject_line": first(row, "Email Subject Line variation 1"),
        # ---- lineage
        "source_file": source_file,
        "source_batch": f"Triple R {state} Campaign 3 Cold Export",
    }


# --------------------------------------------------------------------------
# company-level rollup
# --------------------------------------------------------------------------

def build_companies(people, raw_by_key):
    rows = []
    for key, grp in people[people["company_key"].notna()].groupby("company_key"):
        # Most-frequent name wins. Longest-wins would let a single mis-enriched
        # row rename the whole group (one stray "Settlement Services
        # International" hijacking the 27 Uniting people on uniting.org).
        counts = grp["current_company"].dropna().value_counts()
        name = None
        if len(counts):
            top = counts.max()
            name = max([n for n, c in counts.items() if c == top], key=len)
        variants = [n for n in counts.index if n != name]

        def pick(col):
            """Most common non-null value, falling back to first seen."""
            vals = grp[col].dropna()
            if not len(vals):
                return None
            vc = vals.value_counts()
            return vc.index[0]

        raw = raw_by_key.get(key, {})
        employees = pick("company_employee_total")
        employees = int(employees) if pd.notna(employees) and employees else None

        rows.append({
            "company_id": sid(key),
            "company_key": key,
            "company_name": name,
            "company_name_variants": "; ".join(variants[:8]) or None,
            "company_size": size_band(employees),
            "website": pick("official_website_url"),
            "domain": pick("company_domain") or key,
            "industry": pick("company_industry"),
            "founded_in": None,                     # not in source - Clay fills
            "founded_raw": raw.get("founded_raw"),  # mis-mapped source value, kept for audit
            "description": raw.get("description"),
            "company_type": None,                   # Clay fills
            "annual_revenue": None,                 # Clay fills
            "employee_total": employees,
            "company_email": None,                  # Clay fills (info@ / generic)
            "linkedin_url": pick("company_linkedin_url"),
            "linkedin_description": None,           # Clay fills
            "state": pick("state"),
            "ndis_direct_support": pick("ndis_direct_support"),
            "nursing_care_relevance": pick("nursing_care_relevance"),
            "position_tier_best": (
                sorted([t for t in grp["position_tier"].dropna().unique()
                        if t in ("A", "B", "C")])[0]
                if any(t in ("A", "B", "C") for t in grp["position_tier"].dropna())
                else None),
            "people_count": int(len(grp)),
            "support_coordinator_count": int(grp["is_support_coordinator"].sum()),
            "people_with_email_count": int(grp["has_email"].sum()),
            "source_batch": pick("source_batch"),
        })

    df = pd.DataFrame(rows)
    return df.sort_values(
        ["support_coordinator_count", "people_count", "company_name"],
        ascending=[False, False, True]).reset_index(drop=True)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

PEOPLE_ORDER = [
    "person_id", "company_id", "company_key",
    "first_name", "last_name", "full_name",
    "personal_linkedin_url", "sales_nav_url", "headline",
    "location_name", "state", "linkedin_plan_badge", "is_open_to_work",
    "current_company", "current_company_position", "clean_current_position",
    "position_tier", "domain_position", "start_date", "time_since_start",
    "ndis_direct_support", "ndis_direct_support_reasoning",
    "nursing_care_relevance", "nursing_care_reasoning", "cald_services",
    "is_support_coordinator", "support_coordinator_job_signal",
    "seek_signal_job_title", "icp_score",
    "official_website_url", "company_domain",
    "primary_email", "email_status", "email_quality", "has_email",
    "company_size", "company_employee_total", "company_industry",
    "company_linkedin_url",
    "campaign_label", "outreach_channel", "smartlead_sequence", "ready_to_push",
    "personalized_opening_line", "email_subject_line",
    "company_name_matches_domain", "source_file", "source_batch",
]

COMPANY_ORDER = [
    "company_id", "company_key", "company_name", "company_name_variants",
    "company_size", "website",
    "domain", "industry", "founded_in", "founded_raw", "description",
    "company_type", "annual_revenue", "employee_total", "company_email",
    "linkedin_url", "linkedin_description", "state",
    "ndis_direct_support", "nursing_care_relevance", "position_tier_best",
    "people_count", "support_coordinator_count", "people_with_email_count",
    "source_batch",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sydney", required=True)
    ap.add_argument("--vic", required=True)
    ap.add_argument("--out", default="../data")
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)

    sources = [
        (args.sydney, "NSW", os.path.basename(args.sydney)),
        (args.vic, "VIC", os.path.basename(args.vic)),
    ]

    people_rows, raw_frames, raw_by_key = [], [], {}

    for path, state, fname in sources:
        df = pd.read_csv(path, dtype=str, low_memory=False)
        df = df.dropna(how="all")
        df["__source_state"] = state
        df["__source_file"] = fname
        raw_frames.append(df)

        for _, row in df.iterrows():
            p = build_person(row, state, fname)
            if not (p["full_name"] or p["personal_linkedin_url"]):
                continue
            people_rows.append(p)

            key = p["company_key"]
            if key and key not in raw_by_key:
                raw_by_key[key] = {
                    "description": clean(row.get("Description")),
                    "founded_raw": clean(row.get("Size - Company")),
                }
            elif key and not raw_by_key[key].get("description"):
                raw_by_key[key]["description"] = clean(row.get("Description"))

    people = pd.DataFrame(people_rows)

    # dedupe: same person can appear in both exports / twice in one export
    before = len(people)
    people["__dk"] = people["personal_linkedin_url"].fillna(
        people["person_id"])
    people = people.sort_values(
        ["has_email", "position_tier"], ascending=[False, True])
    people = people.drop_duplicates("__dk", keep="first").drop(columns="__dk")
    people = people.sort_values(
        ["state", "current_company", "last_name"]).reset_index(drop=True)
    dropped = before - len(people)

    companies = build_companies(people, raw_by_key).reindex(columns=COMPANY_ORDER)

    # QA flag: this person's stated employer differs from the dominant employer
    # on their resolved domain, i.e. the source enrichment probably mismatched.
    dominant = dict(zip(companies["company_key"], companies["company_name"]))
    people["company_name_matches_domain"] = [
        None if not k else (norm_name_key(cn) == norm_name_key(dominant.get(k)))
        for k, cn in zip(people["company_key"], people["current_company"])
    ]

    people = people.reindex(columns=PEOPLE_ORDER)

    master = pd.concat(raw_frames, ignore_index=True, sort=False)

    people.to_csv(os.path.join(out, "people.csv"), index=False)
    companies.to_csv(os.path.join(out, "companies.csv"), index=False)
    master.to_csv(os.path.join(out, "master_combined.csv"), index=False)

    print(f"people.csv          {len(people):>6} rows  ({dropped} duplicates removed)")
    print(f"companies.csv       {len(companies):>6} rows")
    print(f"master_combined.csv {len(master):>6} rows x {len(master.columns)} cols")
    print(f"  with email        {int(people['has_email'].sum()):>6}")
    print(f"  support coords    {int(people['is_support_coordinator'].sum()):>6}")
    mism = (people["company_name_matches_domain"] == False).sum()
    print(f"  domain mismatches {int(mism):>6}  (flagged, not dropped)")
    return people, companies


if __name__ == "__main__":
    main()
