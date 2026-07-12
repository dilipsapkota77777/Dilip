"""
IT Together — SEEK Signal Scraper
Run this on your local machine (not in the cloud environment).

Requirements:
    pip install playwright
    playwright install chromium

Run:
    python3 seek_scraper_local.py

Output:
    seek_signal_raw.csv      — all results with exclusion flags
    seek_signal_sendable.csv — clean list ready for Clay import
"""

import csv
import time
import os
from collections import Counter
from playwright.sync_api import sync_playwright

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

SEARCHES = [
    {"query": "IT Manager",           "signal": "IT_MANAGER_HIRE",  "campaign": "IT-CFO-AUS"},
    {"query": "IT Support Officer",   "signal": "IT_SUPPORT_HIRE",  "campaign": "IT-CEO-AUS"},
    {"query": "Systems Administrator","signal": "SYSADMIN_HIRE",    "campaign": "IT-CEO-AUS"},
    {"query": "Help Desk Technician", "signal": "HELPDESK_HIRE",    "campaign": "IT-CEO-AUS"},
    {"query": "Network Administrator","signal": "NETWORK_HIRE",     "campaign": "IT-CEO-AUS"},
    {"query": "IT Coordinator",       "signal": "IT_COORD_HIRE",    "campaign": "IT-CEO-AUS"},
    {"query": "Head of IT",           "signal": "HEAD_IT_HIRE",     "campaign": "IT-CFO-AUS"},
    {"query": "Cybersecurity Analyst","signal": "CYBER_HIRE",       "campaign": "IT-CEO-AUS"},
]

RECRUITER_KEYWORDS = [
    "recruit", "staffing", "labour hire", "labor hire", "talent",
    "hudson", "hays", "robert half", "manpower", "randstad",
    "people2people", "michael page", "adecco", "kelly services",
    "chandler macleod", "pgc", "fuse", "davidson", "finite",
    "red earth", "healthcare australia", "skilled", "programmed"
]

IT_COMPANY_KEYWORDS = [
    "managed it", "managed services", " msp", "it solutions", "it services",
    "cybersecurity", "tech solutions", "technology solutions",
    "cloud services", "it consulting", "digital solutions", "infosys",
    "accenture", "wipro", "tata consultancy", "datacom", "empired",
    "fujitsu", "ntt", "dxc", "unisys", "logicalis", "kinetic it",
    "brennan", "macquarie cloud", "invarosoft", "versent"
]


def scrape_seek(page, query, signal, campaign, max_pages=5):
    results = []
    for page_num in range(1, max_pages + 1):
        url = (
            f"https://www.seek.com.au/jobs"
            f"?q={query.replace(' ', '+')}"
            f"&l=All+Australia"
            f"&dateRange=30d"
            f"&worktype=242"
            f"&page={page_num}"
        )
        print(f"  [{query}] Page {page_num}...")
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(2500)

            jobs = page.evaluate("""
                () => {
                    const results = [];
                    const cards = document.querySelectorAll('article[data-job-id]');
                    cards.forEach(card => {
                        const titleEl = card.querySelector('[data-automation="jobTitle"]')
                                     || card.querySelector('h3 a')
                                     || card.querySelector('h2 a');
                        const companyEl = card.querySelector('[data-automation="jobCompany"]')
                                       || card.querySelector('[class*="company"]');
                        const locationEl = card.querySelector('[data-automation="jobLocation"]')
                                        || card.querySelector('[class*="location"]');
                        const dateEl = card.querySelector('[data-automation="jobListingDate"]')
                                    || card.querySelector('time');
                        results.push({
                            job_id:      card.getAttribute('data-job-id') || '',
                            job_title:   titleEl   ? titleEl.innerText.trim()   : '',
                            company_name:companyEl ? companyEl.innerText.trim() : '',
                            location:    locationEl? locationEl.innerText.trim(): '',
                            date_posted: dateEl    ? (dateEl.innerText || dateEl.getAttribute('datetime') || '').trim() : '',
                        });
                    });

                    // Fallback — newer SEEK layouts
                    if (results.length === 0) {
                        document.querySelectorAll('[data-testid="job-card"], [class*="JobCard"]').forEach(card => {
                            const t = card.querySelector('h3, h2, [class*="title"]');
                            const c = card.querySelector('[class*="company"], [class*="advertiser"]');
                            const l = card.querySelector('[class*="location"]');
                            if (t || c) {
                                results.push({
                                    job_id: '',
                                    job_title: t ? t.innerText.trim() : '',
                                    company_name: c ? c.innerText.trim() : '',
                                    location: l ? l.innerText.trim() : '',
                                    date_posted: '',
                                });
                            }
                        });
                    }
                    return results;
                }
            """)

            if not jobs:
                print(f"  No cards found on page {page_num} — stopping.")
                break

            for job in jobs:
                if job.get("job_title") and job.get("company_name"):
                    job["search_query"] = query
                    job["signal"] = signal
                    job["campaign_track"] = campaign
                    job["signal_source"] = "SEEK_IT_HIRE"
                    job["signal_tier"] = "Tier 1"
                    results.append(job)

            print(f"  Found {len(jobs)} listings.")

            next_btn = page.query_selector('[data-automation="pagination-next"], [aria-label="Next page"]')
            if not next_btn:
                break
            time.sleep(1.5)

        except Exception as e:
            print(f"  Error: {e}")
            break

    return results


def flag_row(row):
    company = row.get("company_name", "").lower()
    if any(k in company for k in RECRUITER_KEYWORDS):
        return "Yes", "RECRUITER"
    if any(k in company for k in IT_COMPANY_KEYWORDS):
        return "Yes", "IT_COMPANY"
    if row.get("company_name", "").strip().lower() in ["confidential", "unknown", ""]:
        return "Yes", "NO_COMPANY_NAME"
    return "No", ""


def clean_and_dedup(results):
    seen = set()
    cleaned = []
    for row in results:
        exclude, reason = flag_row(row)
        row["exclude"] = exclude
        row["exclude_reason"] = reason
        key = f"{row['company_name'].lower().strip()}|{row['job_title'].lower().strip()}"
        if key not in seen:
            seen.add(key)
            cleaned.append(row)
    return cleaned


def save_csv(rows, filename):
    if not rows:
        print(f"  Nothing to save for {filename}")
        return
    fields = [
        "job_title", "company_name", "location", "date_posted",
        "search_query", "signal", "campaign_track", "signal_source",
        "signal_tier", "exclude", "exclude_reason", "job_id"
    ]
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"  Saved {len(rows)} rows -> {path}")
    return path


def main():
    print("=" * 60)
    print("IT Together — SEEK Signal Scraper")
    print("=" * 60)

    all_results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        ctx = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 900},
            locale="en-AU",
        )
        page = ctx.new_page()
        page.route("**/*.{png,jpg,jpeg,gif,webp,svg,woff,woff2,ttf}", lambda r: r.abort())

        for s in SEARCHES:
            print(f"\nSearching: {s['query']}")
            rows = scrape_seek(page, s["query"], s["signal"], s["campaign"], max_pages=5)
            all_results.extend(rows)
            time.sleep(2)

        browser.close()

    print(f"\nTotal raw: {len(all_results)}")
    cleaned = clean_and_dedup(all_results)

    sendable  = [r for r in cleaned if r["exclude"] == "No"]
    excluded  = [r for r in cleaned if r["exclude"] == "Yes"]

    print(f"Unique rows: {len(cleaned)}")
    print(f"  Sendable:  {len(sendable)}")
    print(f"  Excluded:  {len(excluded)}")

    print("\nSaving...")
    save_csv(cleaned,  "seek_signal_raw.csv")
    save_csv(sendable, "seek_signal_sendable.csv")

    print("\n--- BY QUERY ---")
    for q, n in sorted(Counter(r["search_query"] for r in sendable).items(), key=lambda x: -x[1]):
        print(f"  {q:<35} {n}")

    print("\n--- SAMPLE (first 15) ---")
    for r in sendable[:15]:
        print(f"  {r['company_name']:<40} | {r['job_title']:<30} | {r['location']}")

    print("\nNext step: import seek_signal_sendable.csv into Clay")
    print("Then run the enrichment stack from clay-segmentation.md")


if __name__ == "__main__":
    main()
