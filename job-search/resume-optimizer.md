---
name: resume-optimizer
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill automatically when the user pastes or shares
  a job posting, job description, or any role they are considering applying for.
  Also trigger when the user asks Claude to review, tailor, score, or optimize
  their resume against a role. Trigger when the user asks "how well do I match,"
  "am I a good fit," "should I apply," or shares a LinkedIn job posting, job
  board listing, or recruiter message containing a role description.

  Do NOT trigger for general career advice, salary research, or interview prep
  questions that do not include a specific job posting.

  This skill scores the user's fit against the role, selects the right resume
  version, and delivers a tailored resume ready to submit. The user has two
  resume versions on file. The skill selects and tailors the right one
  automatically based on the job posting.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Resume Optimizer: Score, Select, and Tailor

This skill runs automatically when the user shares a job posting.
Do not wait to be asked. Run the full process and deliver results.

---

## HOW TO SET UP THIS SKILL

This skill requires your resume content before it can run. Replace every
section marked [PLACEHOLDER] below with your own information before adding
this file to your Claude Project.

You need two resume versions:
- Version A: your primary functional focus (e.g., Demand Generation,
  Growth Marketing, Performance Marketing)
- Version B: your secondary or adjacent focus (e.g., Revenue Operations,
  Marketing Operations, GTM)

If you only have one resume version, duplicate it into both slots and
skip the version selection logic in Step 1.

---

## Resume Versions on File

---

### VERSION A: [PRIMARY FOCUS -- e.g., Demand Gen / Growth Marketing]

**Headline:** [Your Version A headline]

**Summary:** [Your Version A professional summary, 2-3 sentences]

**Core Competencies:**
- [Competency area 1]: [specific skills]
- [Competency area 2]: [specific skills]
- [Competency area 3]: [specific skills]
- [Competency area 4]: [specific skills]
- [Competency area 5]: [specific skills]
- [Competency area 6]: [specific skills]

**Key Accomplishments (Version A priority order):**
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]

**Use Version A for:** [list the job titles where this version leads]

---

### VERSION B: [SECONDARY FOCUS -- e.g., RevOps / Marketing Operations]

**Headline:** [Your Version B headline]

**Summary:** [Your Version B professional summary, 2-3 sentences]

**Core Competencies:**
- [Competency area 1]: [specific skills]
- [Competency area 2]: [specific skills]
- [Competency area 3]: [specific skills]
- [Competency area 4]: [specific skills]
- [Competency area 5]: [specific skills]
- [Competency area 6]: [specific skills]

**Key Accomplishments (Version B priority order):**
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]
- [Result with $ or % metric] -- [brief context, company optional]

**Use Version B for:** [list the job titles where this version leads]

---

## Full Work History (Both Versions)

List every role here in full. Claude will draw from this when tailoring
bullets for a specific job posting. Include all roles, even older or
shorter ones. More context produces better tailoring.

**[Job Title] -- [Company]** ([Industry]) | [Start Date] - [End Date]
- [Bullet with metric]
- [Bullet with metric]
- [Bullet with metric]

**[Job Title] -- [Company]** ([Industry]) | [Start Date] - [End Date]
- [Bullet with metric]
- [Bullet with metric]

[Repeat for all roles]

---

## Education and Credentials

**[Degree]** -- [School], [Year]

**Certifications (if any):**
- [Certification name, issuer]
- [Certification name, issuer]

**Tools:** [List all tools you use across both roles]

---

## Step 1: Select the Right Version

Read the job posting carefully. Identify the primary role type:

- Title or core focus maps to Version A role types -- use **Version A**
- Title or core focus maps to Version B role types -- use **Version B**
- Title is hybrid (e.g., "Director of Demand Gen and RevOps") -- use
  **Version B** as the base but pull Version A accomplishments to the
  top of the Key Accomplishments section

State which version you selected and why before proceeding.

---

## Step 2: Score the Match

Go through the job posting line by line. Pull out every requirement,
both required and preferred, and match each one against the resume above.

**Score format:**

```
MATCH SCORE: [X/100]
Version selected: [A or B] -- [one sentence why]

Strong matches:
- [specific requirement] -- covered by [specific experience]

Gaps:
- [what is missing or thin]

Red flags:
- [dealbreakers if any]

Recommendation: Apply / Apply with adjustments / Pass
```

Be direct. Do not oversell the fit. If the match is below 60, say so
and explain why.

Distinguish between stated requirements and narrative context. A job
posting that mentions an industry as background context is different
from one that lists it as a requirement. Do not flag narrative context
as a gap.

---

## Step 3: Tailor the Resume

After scoring, automatically produce a tailored resume for the role.

**Tailoring rules:**

**Mirror the job's language.** Use exact keywords and phrases from the
posting where they apply honestly. ATS systems scan for keyword matches.
Do not stuff keywords. Only use them where they genuinely apply.

**Lead with what the job cares about most.** Reorder accomplishments to
put the most relevant ones first. If the job emphasizes pipeline
generation, pipeline numbers lead. If it emphasizes CRM architecture,
HubSpot bullets lead.

**Rewrite the summary for this specific role.** The summary should read
like it was written for this job, not as a generic statement.

**Quantify everything.** Every bullet that can have a number should have
a number. Pull from the accomplishments list above.

**Trim what does not apply.** If a skill or bullet is not relevant to
this role, move it down or remove it. Keep the resume focused.

**Length:** Two pages for Director-level roles. One page for
Manager-level roles.

**Format:** Clean plain text, ATS-safe. No tables, no columns.

```
[FULL NAME]
[City, State] | [Phone] | [Email] | [LinkedIn URL]

SUMMARY
[2-3 sentences tailored to this specific role]

CORE COMPETENCIES
[10-12 keywords most relevant to this role, comma-separated]

KEY ACCOMPLISHMENTS
[5-7 most relevant accomplishments, reordered for this role]

WORK EXPERIENCE
[Company] | [Title] | [Dates]
[One-line context: what you owned or built]
- [Most relevant bullet for this role]
- [Second bullet]
[Repeat for each role, trimming less relevant roles to 1-2 bullets]

CERTIFICATIONS AND AI FLUENCY
[If you have certifications relevant to the role, always include these.
They differentiate at the Director level.]

TOOLS AND TECHNOLOGY
[Trim to tools most relevant to this role]

EDUCATION
[Degree] -- [School], [Year]

VOLUNTEER AND COMMUNITY
[Optional -- one line if relevant]
```

---

## Step 4: Before You Apply

After delivering the resume, add 3-5 specific action items:

- Should your LinkedIn headline match this role's title?
- Is there a specific gap worth addressing in a cover note?
- Does the job description hint at something to research before the
  interview?
- Is there a tool or certification gap worth flagging proactively?
- Any signal in the posting about company culture or the hiring
  manager's priorities worth noting?

---

## Output Format

Deliver in this order:
1. Version selected and why (one sentence)
2. Match score with breakdown
3. Tailored resume (full, ready to copy-paste)
4. Before You Apply bullets

No preamble. No explanation of what you are about to do.
Just run the process and deliver.
