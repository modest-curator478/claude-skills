---
name: competitive-intelligence
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user mentions a company they are
  interviewing with, preparing for an interview at, or researching for a job
  application. Trigger phrases include: "I have an interview at," "I'm
  interviewing with," "tell me about [company]," "research [company] for me,"
  "what do I need to know about [company]," or any request to prepare for a
  specific company meeting or interview.

  Also trigger when the user shares a company name alongside a job title,
  job posting, or recruiter name -- these signals indicate interview prep.

  Do NOT trigger for general industry research, trend analysis, or news
  requests that are not tied to a specific company and interview.
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
---

# Competitive Intelligence: Interview Prep Briefs

This skill runs automatically when the user is preparing for an interview or
researching a specific company for a job application. Always search the web
before writing anything. Do not rely on training data for company information.

---

## HOW TO SET UP THIS SKILL

Replace the [PLACEHOLDER] sections below with your own background before
adding this file to your Claude Project. The more specific you are about
your background and target roles, the more relevant the talking points
and questions Claude generates will be.

---

## Who This Person Is

**Name:** [Your full name]

**Target roles:** [List 3-5 role titles you are actively applying for]

**Background:** [2-3 sentences summarizing your core expertise, years of
experience, key tools, and functional areas.]

**Typical interview process for your roles:**
[Describe the typical stages you encounter, e.g.:
- Recruiter screen
- Hiring manager
- Panel interview
- Take-home exercise]

---

## Step 1: Search First

When this skill triggers, immediately run web searches on the company.
Do not write the brief until you have current information from the web.

Required searches:
1. Company name + "news [current year]"
2. Company name + "funding" or "acquisition" or "PE"
3. Company name + your functional area
4. Company name + "reviews" or "Glassdoor"
5. Company name + job title if provided

Run additional searches if gaps remain.

---

## Step 2: Build the Intel Brief

Deliver the output in this exact format.

COMPANY INTEL BRIEF
[Company Name]
Prepared: [Today's date]
Role: [Role title if provided, otherwise "Not specified"]

WHAT THEY DO
[2-3 sentences. Plain language. What product or service, who they sell
to, what problem they solve. No marketing speak.]

OWNERSHIP AND FINANCIAL CONTEXT
[Public or private. PE-backed, VC-backed, or bootstrapped. Any recent
funding rounds, acquisitions, or notable financial events. If PE-backed,
name the firm if known.]

RECENT NEWS (last 6 months)
- [Item 1: what happened, source, date]
- [Item 2: what happened, source, date]
- [Item 3: what happened, source, date]
[If no recent news is found, say so directly.]

SIGNALS RELEVANT TO YOUR ROLE
[Anything relevant to the user's functional background:]
- Known tech stack
- Recent hires or leadership changes
- Job postings that reveal what they are building
- Product launches affecting go-to-market
[If nothing found, note that and suggest what to ask in the interview.]

CULTURE AND LEADERSHIP SIGNALS
[Glassdoor rating if available. Common review themes. CEO approval
rating if visible. Notable leadership changes.]

ICP AND GO-TO-MARKET
[Who do they sell to? Company size, verticals, buyer persona. How do
they go to market. Average deal size if known. Sales cycle if known.]

INTERVIEW TALKING POINTS
[3-5 specific things you can reference to show you did your homework.
Connect each to your skills or experience where possible.]

SMART QUESTIONS TO ASK
[5 questions to ask the interviewer that show functional fluency and
business acumen. Not answerable from the website.]

RED FLAGS TO WATCH
[Anything in the research that warrants caution. High turnover, financial
instability, culture issues, or anything that does not add up. Be direct.]

BOTTOM LINE
[One short paragraph. Should this role be a priority? Biggest opportunity
and biggest risk. Be direct.]

---

## Output Rules

- No em dashes. Use commas or periods.
- Describe the company factually. No marketing language.
- If information is not found, say "not found." Do not fill gaps with guesses.
- Cite sources by name when referencing specific claims.
- Deliver the full brief in one response.
