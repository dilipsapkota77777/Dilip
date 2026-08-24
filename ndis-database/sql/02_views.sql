-- =====================================================================
-- Triple R NDIS outreach database - the two preview modes
--   ndis.v_people    -> People / individual data set
--   ndis.v_companies -> Company data set
-- plus the extraction views you asked for by name.
-- Run after 01_schema.sql.
-- =====================================================================

-- ---------------------------------------------------------------------
-- PREVIEW MODE 1 : PEOPLE
-- Every person, with their company data joined on. Column order matches
-- the Excel "People View" sheet exactly, so Clay maps 1:1.
-- ---------------------------------------------------------------------
create or replace view ndis.v_people as
select
    p.person_id,
    p.first_name,
    p.last_name,
    p.full_name,
    p.personal_linkedin_url,
    p.headline,
    p.location_name,
    p.state,
    p.linkedin_plan_badge,
    p.current_company,
    p.current_company_position,
    p.clean_current_position,
    coalesce(c.website, p.official_website_url)  as official_website_url,
    coalesce(c.domain,  p.company_domain)        as domain,
    p.position_tier,
    p.ndis_direct_support,
    p.ndis_direct_support_reasoning,
    p.nursing_care_relevance,
    p.is_support_coordinator,
    p.support_coordinator_job_signal,
    p.seek_signal_job_title,
    p.start_date,
    p.time_since_start,
    p.primary_email,
    p.email_status,
    p.email_quality,
    -- one column that answers "can I send to this person right now"
    case
        when p.primary_email is null                       then 'no_email'
        when p.email_status  = 'valid'                     then 'sendable'
        when p.email_quality = 'good'                      then 'sendable'
        when p.email_status in ('invalid', 'unavailable')  then 'do_not_send'
        else 'unverified'
    end                                          as send_readiness,
    coalesce(c.company_size,    p.company_size)     as company_size,
    coalesce(c.employee_total,  p.company_employee_total) as employee_total,
    coalesce(c.industry,        p.company_industry) as industry,
    coalesce(c.linkedin_url,    p.company_linkedin_url) as company_linkedin_url,
    p.company_id,
    p.company_name_matches_domain,
    p.campaign_label,
    p.outreach_channel,
    p.source_batch
from ndis.people p
left join ndis.companies c on c.company_id = p.company_id;

-- ---------------------------------------------------------------------
-- PREVIEW MODE 2 : COMPANIES
-- One row per organisation. No people columns - people roll up to counts.
-- ---------------------------------------------------------------------
create or replace view ndis.v_companies as
select
    c.company_id,
    c.company_name,
    c.company_name_variants,
    c.company_size,
    c.website,
    c.domain,
    c.industry,
    c.founded_in,
    c.description,
    c.linkedin_description,
    c.company_type,
    c.annual_revenue,
    c.employee_total,
    c.company_email,
    c.linkedin_url,
    c.state,
    c.ndis_direct_support,
    c.nursing_care_relevance,
    c.position_tier_best,
    c.people_count,
    c.support_coordinator_count,
    c.people_with_email_count,
    -- how much of this account is actually reachable
    case when c.people_count > 0
         then round(100.0 * c.people_with_email_count / c.people_count)
         else 0 end                              as email_coverage_pct,
    c.source_batch
from ndis.companies c;

-- ---------------------------------------------------------------------
-- THE MAIN JOB: support-coordinator emails for a given organisation.
-- ---------------------------------------------------------------------
create or replace view ndis.v_support_coordinator_emails as
select
    c.company_name,
    c.domain,
    c.industry,
    c.state,
    p.full_name,
    p.clean_current_position,
    p.primary_email,
    p.email_status,
    p.personal_linkedin_url,
    p.position_tier,
    p.time_since_start
from ndis.people p
join ndis.companies c on c.company_id = p.company_id
where p.is_support_coordinator
  and p.primary_email is not null
order by c.company_name, p.full_name;

-- Convenience function: the exact ask, "support coordinator emails of that
-- organisation". Matches on domain OR name, case-insensitive, partial.
--   select * from ndis.support_coordinators('uniting');
--   select * from ndis.support_coordinators('abilityoptions.org.au');
create or replace function ndis.support_coordinators(org text)
returns table (
    company_name text,
    full_name    text,
    position_title text,
    email        text,
    email_status text,
    linkedin     text
) language sql stable as $$
    select c.company_name,
           p.full_name,
           p.clean_current_position,
           p.primary_email,
           p.email_status,
           p.personal_linkedin_url
    from ndis.people p
    join ndis.companies c on c.company_id = p.company_id
    where p.is_support_coordinator
      and p.primary_email is not null
      and (c.domain       ilike '%' || org || '%'
        or c.company_name ilike '%' || org || '%')
    order by p.full_name;
$$;

-- ---------------------------------------------------------------------
-- Push-ready list: tier A/B support coordinators with a sendable email.
-- This is what goes to Smartlead.
-- ---------------------------------------------------------------------
create or replace view ndis.v_ready_to_send as
select *
from ndis.v_people
where send_readiness = 'sendable'
  and is_support_coordinator
  and position_tier in ('A', 'B')
order by state, current_company, full_name;

-- ---------------------------------------------------------------------
-- Enrichment worklist: what Clay still needs to fill.
-- ---------------------------------------------------------------------
create or replace view ndis.v_enrichment_gaps as
select
    c.company_id,
    c.company_name,
    c.domain,
    c.people_count,
    (c.founded_in       is null) as needs_founded_in,
    (c.description      is null) as needs_description,
    (c.employee_total   is null) as needs_employee_total,
    (c.company_email    is null) as needs_company_email,
    (c.linkedin_url     is null) as needs_linkedin_url,
    (c.industry         is null) as needs_industry,
    (c.annual_revenue   is null) as needs_annual_revenue
from ndis.companies c
where c.founded_in is null
   or c.description is null
   or c.employee_total is null
   or c.company_email is null
   or c.linkedin_url is null
   or c.industry is null
order by c.people_count desc;

-- ---------------------------------------------------------------------
-- Grants: service_role (what Clay uses) reads every view.
-- ---------------------------------------------------------------------
grant usage on schema ndis to service_role;
grant select on all tables in schema ndis to service_role;
grant execute on function ndis.support_coordinators(text) to service_role;
