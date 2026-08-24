#!/usr/bin/env bash
# Push the NDIS database to Supabase in one command.
#
#   export SUPABASE_DB_URL='postgresql://postgres.<ref>:<password>@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
#   ./push_to_supabase.sh
#
# Get the URL from: Supabase -> Project Settings -> Database -> Connection string -> URI
# Use the SESSION pooler (port 5432), not the transaction pooler (6543) - \copy needs it.
#
# Safe to re-run: schema uses IF NOT EXISTS, and the load truncates first.

set -euo pipefail

SQL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../sql" && pwd)"
DATA_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../data" && pwd)"

if [[ -z "${SUPABASE_DB_URL:-}" ]]; then
    echo "ERROR: SUPABASE_DB_URL is not set." >&2
    echo "  Supabase -> Project Settings -> Database -> Connection string -> URI" >&2
    exit 1
fi

for f in people.csv companies.csv; do
    [[ -f "$DATA_DIR/$f" ]] || { echo "ERROR: missing $DATA_DIR/$f" >&2; exit 1; }
done

run() { psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 "$@"; }

echo "==> Connecting"
run -tc "select 'connected to ' || current_database() || ' as ' || current_user;"

echo "==> 01_schema.sql   (tables, indexes, RLS)"
run -q -f "$SQL_DIR/01_schema.sql"

echo "==> 02_views.sql    (v_people, v_companies, extraction views)"
run -q -f "$SQL_DIR/02_views.sql"

echo "==> Loading data    (truncate + copy)"
run -q -c "truncate ndis.people, ndis.companies cascade;"

# Take the column list from the CSV header itself. Naming the columns explicitly
# is required: the tables also carry created_at/updated_at, which the CSVs do not,
# so a bare \copy would expect every column in table order and fail.
load() {
    local table="$1" file="$2" cols
    cols=$(head -1 "$file" | tr -d '\r')
    run -q -c "\copy ndis.$table ($cols) from '$file' with (format csv, header true, null '')"
    echo "    $table loaded"
}
load companies "$DATA_DIR/companies.csv"
load people    "$DATA_DIR/people.csv"

echo "==> Verifying"
run -c "
select 'companies'                 as table, count(*) from ndis.companies
union all select 'people',                    count(*) from ndis.people
union all select 'support coords w/ email',   count(*) from ndis.v_support_coordinator_emails
union all select 'ready to send',             count(*) from ndis.v_ready_to_send;"

echo
echo "Done. Try it:"
echo "  select * from ndis.support_coordinators('uniting');"
