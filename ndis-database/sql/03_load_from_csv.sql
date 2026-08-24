-- =====================================================================
-- Load the CSVs. Two options - pick one.
-- =====================================================================
--
-- OPTION A - Supabase dashboard (no tooling needed)
--   1. Run 01_schema.sql, then 02_views.sql.
--   2. Table Editor -> ndis.companies -> Insert -> Import data from CSV
--      -> upload data/companies.csv
--   3. Same for ndis.people -> data/people.csv
--   Import companies FIRST: people.company_id references it.
--
-- OPTION B - psql from your machine (faster, repeatable)
--   Grab the connection string from
--   Supabase -> Project Settings -> Database -> Connection string -> URI
--
--     psql "$SUPABASE_DB_URL" -f 01_schema.sql
--     psql "$SUPABASE_DB_URL" -f 02_views.sql
--     psql "$SUPABASE_DB_URL" -v ON_ERROR_STOP=1 -f 03_load_from_csv.sql
--
--   The \copy lines below assume you run psql from the sql/ directory.
-- =====================================================================

\copy ndis.companies (company_id,company_key,company_name,company_name_variants,company_size,website,domain,industry,founded_in,founded_raw,description,company_type,annual_revenue,employee_total,company_email,linkedin_url,linkedin_description,state,ndis_direct_support,nursing_care_relevance,position_tier_best,people_count,support_coordinator_count,people_with_email_count,source_batch) from '../data/companies.csv' with (format csv, header true, null '');

\copy ndis.people (person_id,company_id,company_key,first_name,last_name,full_name,personal_linkedin_url,sales_nav_url,headline,location_name,state,linkedin_plan_badge,is_open_to_work,current_company,current_company_position,clean_current_position,position_tier,domain_position,start_date,time_since_start,ndis_direct_support,ndis_direct_support_reasoning,nursing_care_relevance,nursing_care_reasoning,cald_services,is_support_coordinator,support_coordinator_job_signal,seek_signal_job_title,icp_score,official_website_url,company_domain,primary_email,email_status,email_quality,has_email,company_size,company_employee_total,company_industry,company_linkedin_url,campaign_label,outreach_channel,smartlead_sequence,ready_to_push,personalized_opening_line,email_subject_line,company_name_matches_domain,source_file,source_batch) from '../data/people.csv' with (format csv, header true, null '');

-- sanity check
select 'companies' as t, count(*) from ndis.companies
union all
select 'people', count(*) from ndis.people
union all
select 'support coords with email', count(*) from ndis.v_support_coordinator_emails;
