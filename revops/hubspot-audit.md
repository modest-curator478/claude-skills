---
name: hubspot-audit
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user asks about auditing,
  cleaning up, reviewing, or improving their HubSpot instance. Trigger
  phrases include: "audit our HubSpot," "clean up HubSpot," "HubSpot
  is a mess," "inherited a HubSpot instance," "our workflows are broken,"
  "deal stages don't make sense," "leads aren't routing correctly,"
  "HubSpot hygiene," or any request to assess the health or structure
  of a HubSpot CRM.

  Also trigger when the user is starting a new role and mentions
  evaluating the existing HubSpot setup they inherited.

  Do NOT trigger for general HubSpot how-to questions or feature
  requests that are not about auditing an existing instance.
allowed-tools:
  - Read
  - Write
  - Edit
---

# HubSpot Instance Audit: Structural Health Review

This skill runs when the user needs to audit an existing HubSpot
instance. It produces a structured audit framework across six domains,
identifies the highest-impact problems first, and delivers a
prioritized remediation plan.

---

## HOW TO SET UP THIS SKILL

This skill works best when the user provides context about their
instance. Ask for the following if not already provided:

- How long the instance has been active
- Rough number of contacts, companies, and open deals
- Whether they inherited it or built it
- What Sales and Marketing teams are using it for
- Any known pain points

If no context is provided, run the audit framework as a diagnostic
checklist the user can work through manually.

---

## The Six Audit Domains

Run through each domain. For each, identify what to look for, what
the red flags are, and what good looks like.

---

### Domain 1: Deal pipeline and stage design

**What to look for:**
- How many deal stages exist and whether they reflect how sales
  actually works, not how someone wished it worked
- Whether stage names are action-oriented (what happens at this stage)
  or status-oriented (where the deal sits)
- Whether there is a clear exit criteria for each stage
- Whether deals are piling up in one or two stages, which signals
  a stage definition problem, not a sales problem
- Whether the pipeline has stages that no one uses

**Red flags:**
- More than 8 stages in a single pipeline
- Stage names like "In Progress" or "Active" with no definition
- A large percentage of deals stuck in the same stage for more than
  30 days
- Multiple pipelines that are nearly identical
- No close date discipline (all deals show the same default date)

**What good looks like:**
Each stage has a name that describes what sales did to get there,
a clear next action, and an exit criteria that both sales and marketing
agree on. Deal velocity is visible and not artificially inflated.

---

### Domain 2: Workflow and automation health

**What to look for:**
- How many active workflows exist
- How many are actually running vs. enrolled with zero contacts
- Whether workflows conflict with each other (contact enrolled in
  two workflows that send competing emails)
- Whether workflows have error handling or just silently fail
- Workflows built by people who no longer work at the company with
  no documentation

**Red flags:**
- Workflows with no description and no clear owner
- Enrollment triggers that are too broad (any contact who visits
  any page) producing noise
- Suppression lists that are out of date
- Workflows sending emails that are months or years old
- No testing or preview steps before live enrollment

**What good looks like:**
Every workflow has a name that describes what it does, an owner, an
enrollment trigger that is specific, and a suppression condition that
prevents the wrong contacts from entering. Old workflows are turned
off, not left running with zero enrollments.

---

### Domain 3: Lead lifecycle and routing

**What to look for:**
- Whether lifecycle stages are defined and enforced or just left
  at default
- Whether the progression from Subscriber to Lead to MQL to SQL
  is automated or manual
- Whether lead routing is based on rules or is still round-robin
  by default
- How long leads sit in MQL before being worked by sales
- Whether leads ever go backwards in lifecycle stage (SQL back to
  MQL) and whether that is intentional

**Red flags:**
- Thousands of contacts stuck at "Lead" with no progression logic
- No definition of what makes a contact an MQL
- Sales and marketing disagreeing on what an MQL means
- Leads assigned to reps who have left the company
- No SLA between marketing and sales for MQL follow-up

**What good looks like:**
Every lifecycle stage has a definition that sales and marketing have
agreed on in writing. Progression is automated where possible. Routing
assigns leads to the right rep based on territory, company size, or
vertical. There is a documented SLA for how fast sales works an MQL.

---

### Domain 4: Data hygiene and property health

**What to look for:**
- How many custom properties exist and how many are actually used
- Whether there are duplicate properties doing the same thing
  (Company Size and Number of Employees as separate fields)
- Whether critical fields have high null rates (no value in them)
- Whether contact and company records are being enriched or left
  as created
- Whether there are duplicate contacts or companies at scale

**Red flags:**
- Hundreds of custom properties with no documentation
- The same data point stored in multiple fields with inconsistent
  values
- Key segmentation fields empty on more than 40% of records
- No deduplication process in place
- Contacts from years ago with no activity and no suppression

**What good looks like:**
Properties are documented, used, and cleaned regularly. Duplicates
are caught at entry via form validation and cleaned on a schedule.
Critical fields for segmentation and reporting have high fill rates.
Old or irrelevant properties are archived, not deleted.

---

### Domain 5: Reporting and attribution

**What to look for:**
- Whether pipeline and revenue reports exist and are trusted by sales
- Whether marketing can tie campaign activity to pipeline and closed
  revenue
- Whether the dashboards are used or ignored
- Whether attribution models are set up or left at default
- Whether there is a shared revenue report that both sales and
  marketing review together

**Red flags:**
- Dashboards that were built once and never updated
- No campaign attribution on contacts or deals
- Sales using a spreadsheet for pipeline because HubSpot reports
  are not trusted
- Marketing reporting on leads but unable to show pipeline influence
- Multiple versions of "the number" depending on who you ask

**What good looks like:**
One shared pipeline report that sales and marketing both trust and
review in a weekly or monthly cadence. Marketing attribution is
connected to deal creation and closed revenue, not just lead volume.
Dashboards are maintained and reflect current priorities.

---

### Domain 6: Integration and data flow

**What to look for:**
- What tools are connected to HubSpot and whether the sync is
  bidirectional or one-way
- Whether Salesforce (if connected) has field mapping conflicts
- Whether form submissions are routing correctly
- Whether the website tracking code is installed and firing
- Whether any integrations have errored out and been silently
  failing

**Red flags:**
- Integrations connected but never audited since setup
- Data flowing one direction only when it should be bidirectional
- Form submissions not creating contacts or creating duplicates
- Website activity not tracking because the code is on some pages
  but not others
- Salesforce sync errors that no one is monitoring

**What good looks like:**
Every integration is documented with its sync direction, field
mapping, and owner. Errors are monitored and have an alert. Data
flows consistently and the same record looks the same in every
connected system.

---

## Step 3: Deliver the Audit Report

Output in this format:

```
HUBSPOT INSTANCE AUDIT
[Company or instance name if provided]
Audit date: [today's date]

INSTANCE OVERVIEW
[2-3 sentences summarizing what the instance appears to be used for
and the general health impression based on what the user shared.]

CRITICAL ISSUES (fix within 30 days)
[List only the issues that are actively causing pipeline or data
problems. Not cosmetic. Each item gets one sentence on the problem
and one sentence on the fix.]

HIGH PRIORITY (fix within 90 days)
[Issues that are not breaking anything today but will cause problems
at scale or during a future audit.]

LOW PRIORITY (fix when bandwidth allows)
[Cleanup and optimization items. Real but not urgent.]

RECOMMENDED REMEDIATION ORDER
1. [First thing to fix and why]
2. [Second]
3. [Third]
[Continue as needed]

ESTIMATED EFFORT
[Rough time estimate for the full remediation based on what was
described. Be honest if the instance sounds like a significant
rebuild vs. a light cleanup.]
```

---

## Output Rules

- Never invent data about the instance. Only assess what the user
  has described.
- If the user has not provided enough detail to assess a domain,
  include that domain as a question list for them to go investigate.
- Prioritize ruthlessly. Not everything is critical. Most audits
  have two or three things that actually matter and ten things that
  are just noise.
- No em dashes. Use commas or periods.
- Be direct about severity. If the instance sounds like it needs a
  rebuild, say so.
