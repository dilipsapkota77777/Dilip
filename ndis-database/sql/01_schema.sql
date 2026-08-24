-- =====================================================================
-- Triple R NDIS outreach database - schema
-- Source: Clay master-table cold exports, Campaign 3 (Sydney/NSW + VIC)
-- Run this first, in the Supabase SQL editor.
-- =====================================================================

create schema if not exists ndis;

-- ---------------------------------------------------------------------
-- companies : one row per organisation, keyed on normalised domain
-- ---------------------------------------------------------------------
create table if not exists ndis.companies (
    company_id                text primary key,
    company_key               text not null unique,   -- normalised domain, else name key
    company_name              text,
    company_name_variants     text,                   -- other spellings seen on this domain
    company_size              text,                   -- band: 11-50, 51-200, ...
    website                   text,
    domain                    text,
    industry                  text,
    founded_in                integer,                -- EMPTY in source - Clay fills
    founded_raw               text,                   -- mis-mapped source value, audit only
    description               text,
    company_type              text,                   -- EMPTY in source - Clay fills
    annual_revenue            text,                   -- EMPTY in source - Clay fills
    employee_total            integer,
    company_email             text,                   -- EMPTY in source - Clay fills
    linkedin_url              text,
    linkedin_description      text,                   -- EMPTY in source - Clay fills
    state                     text,
    ndis_direct_support       text,                   -- Yes / No / Unclear
    nursing_care_relevance    text,                   -- Yes / No / Unclear
    position_tier_best        text,                   -- best tier among its people
    people_count              integer default 0,
    support_coordinator_count integer default 0,
    people_with_email_count   integer default 0,
    source_batch              text,
    created_at                timestamptz default now(),
    updated_at                timestamptz default now()
);

-- ---------------------------------------------------------------------
-- people : one row per person, FK to companies
-- ---------------------------------------------------------------------
create table if not exists ndis.people (
    person_id                     text primary key,
    company_id                    text references ndis.companies(company_id) on delete set null,
    company_key                   text,

    -- name
    first_name                    text,
    last_name                     text,
    full_name                     text,

    -- profile
    personal_linkedin_url         text,
    sales_nav_url                 text,
    headline                      text,
    location_name                 text,
    state                         text,
    linkedin_plan_badge           text,               -- Premium / Free / Free (Open to Work)
    is_open_to_work               boolean default false,

    -- current role
    current_company               text,
    current_company_position      text,
    clean_current_position        text,
    position_tier                 text,               -- A / B / C / none
    domain_position               text,               -- "domain | position" composite
    start_date                    text,               -- source is "May 2024" style
    time_since_start              text,               -- "2 years"

    -- qualification signals
    ndis_direct_support           text,
    ndis_direct_support_reasoning text,
    nursing_care_relevance        text,
    nursing_care_reasoning        text,
    cald_services                 text,
    is_support_coordinator        boolean default false,
    support_coordinator_job_signal text,
    seek_signal_job_title         text,
    icp_score                     text,

    -- contact
    official_website_url          text,
    company_domain                text,
    primary_email                 text,
    email_status                  text,               -- valid / unavailable / invalid / risky
    email_quality                 text,               -- good / ...
    has_email                     boolean default false,

    -- company snapshot carried on the person row
    company_size                  text,
    company_employee_total        integer,
    company_industry              text,
    company_linkedin_url          text,

    -- campaign
    campaign_label                text,
    outreach_channel              text,
    smartlead_sequence            text,
    ready_to_push                 text,
    personalized_opening_line     text,
    email_subject_line            text,

    -- QA + lineage
    company_name_matches_domain   boolean,            -- false = source enrichment mismatch
    source_file                   text,
    source_batch                  text,
    created_at                    timestamptz default now(),
    updated_at                    timestamptz default now()
);

-- ---------------------------------------------------------------------
-- indexes - tuned for the lookups you actually run
-- ---------------------------------------------------------------------
create index if not exists idx_people_company_id    on ndis.people (company_id);
create index if not exists idx_people_company_key   on ndis.people (company_key);
create index if not exists idx_people_email         on ndis.people (lower(primary_email));
create index if not exists idx_people_state         on ndis.people (state);
create index if not exists idx_people_tier          on ndis.people (position_tier);
create index if not exists idx_people_coordinator   on ndis.people (is_support_coordinator)
    where is_support_coordinator;
create index if not exists idx_people_domain        on ndis.people (company_domain);
create index if not exists idx_people_linkedin      on ndis.people (personal_linkedin_url);

create index if not exists idx_companies_domain     on ndis.companies (domain);
create index if not exists idx_companies_state      on ndis.companies (state);
create index if not exists idx_companies_industry   on ndis.companies (industry);

-- full-text search over names, so "search my database" works from Clay/Supabase
create index if not exists idx_companies_name_trgm
    on ndis.companies using gin (to_tsvector('english', coalesce(company_name, '')));
create index if not exists idx_people_name_fts
    on ndis.people using gin (to_tsvector('english',
        coalesce(full_name, '') || ' ' || coalesce(headline, '')));

-- ---------------------------------------------------------------------
-- keep updated_at honest
-- ---------------------------------------------------------------------
create or replace function ndis.touch_updated_at() returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

drop trigger if exists trg_people_touch on ndis.people;
create trigger trg_people_touch before update on ndis.people
    for each row execute function ndis.touch_updated_at();

drop trigger if exists trg_companies_touch on ndis.companies;
create trigger trg_companies_touch before update on ndis.companies
    for each row execute function ndis.touch_updated_at();

-- ---------------------------------------------------------------------
-- RLS: locked to service_role by default. Clay connects with the service
-- key, so it keeps full access; anon/authenticated get nothing until you
-- decide otherwise.
-- ---------------------------------------------------------------------
alter table ndis.people    enable row level security;
alter table ndis.companies enable row level security;

drop policy if exists svc_all_people on ndis.people;
create policy svc_all_people on ndis.people
    for all to service_role using (true) with check (true);

drop policy if exists svc_all_companies on ndis.companies;
create policy svc_all_companies on ndis.companies
    for all to service_role using (true) with check (true);
