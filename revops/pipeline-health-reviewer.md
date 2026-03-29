---
name: pipeline-health-reviewer
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user shares pipeline data,
  asks about pipeline health, deal velocity, or sales cycle performance.
  Trigger phrases include: "our pipeline is stalling," "deals are stuck,"
  "review our pipeline," "sales cycle is too long," "why aren't deals
  moving," "forecast accuracy is off," "our close rate is dropping,"
  or any request to diagnose why a B2B sales pipeline is underperforming.

  Also trigger when the user shares a pipeline report, deal stage
  breakdown, or asks how to improve pipeline velocity.

  Do NOT trigger for general sales strategy questions not tied to a
  specific pipeline situation.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Pipeline Health Reviewer: Velocity and Stage Diagnosis

This skill diagnoses why a B2B pipeline is stalling and delivers a
prioritized set of structural fixes. It treats pipeline problems as
systems problems, not sales performance problems, unless the evidence
points clearly to the latter.

---

## HOW TO SET UP THIS SKILL

This skill works best with specific data. Ask the user to provide
as much of the following as possible:

- Total pipeline value and number of open deals
- Deal stage names and what percentage of pipeline sits in each
- Average days in each stage (or average total sales cycle length)
- Average deal size
- Win rate and loss rate
- Where most deals are lost (stage and reason if known)
- Whether they have a defined ICP and qualification framework

If no data is provided, run the diagnostic as a structured interview,
asking for the key numbers before delivering conclusions.

---

## The Pipeline Diagnostic Framework

A stalling pipeline has one of four root causes. Identify which one
or which combination applies before recommending fixes.

---

### Root cause 1: Stage definition problems

Deals appear to move but do not actually progress because stages are
defined by time or activity rather than buyer behavior.

**Signals:**
- Deals sitting in "Discovery" or "Proposal" for 60+ days
- Reps moving deals forward to show activity rather than real progress
- Stage names that describe what the rep did, not what the buyer did
- No exit criteria that requires buyer confirmation before advancing

**The fix:**
Redefine stages around buyer actions, not sales actions. A deal
should not move to "Proposal" because the rep sent a proposal. It
should move when the buyer has confirmed they received it, reviewed
it, and have a specific next step scheduled. This is the distinction
between deal stage theater and real pipeline visibility.

---

### Root cause 2: ICP and qualification gaps

Pipeline is full but close rates are low because deals that should
not be in the pipeline are in the pipeline. This inflates the number,
destroys forecast accuracy, and wastes rep time on deals that will
never close.

**Signals:**
- Close rates below 20% on proposals
- A high number of deals that go dark after the demo or proposal
- Long average sales cycles with no clear acceleration point
- Win rate variance by rep that does not correlate with tenure or skill

**The fix:**
Audit closed-lost deals for patterns. If a certain company size,
vertical, tech stack, or buyer persona consistently loses, that is
an ICP problem. The qualification framework needs to include a hard
disqualification step, not just a scoring model that everyone ignores.
Better to have 30 real deals than 90 deals where 60 are noise.

---

### Root cause 3: Follow-up and sequence gaps

Deals are real and qualified but stalling because there is no
structured follow-up after key milestones. The buyer goes quiet and
the rep waits.

**Signals:**
- High number of deals with no activity in the last 14-21 days
- Deals in late stages with no scheduled next step
- Reps following up with generic "just checking in" emails
- No automated re-engagement for deals that go dark

**The fix:**
Every deal that advances past a defined stage needs a follow-up
sequence with a specific trigger and a specific message, not a
generic nudge. The sequence should reference the last thing the
buyer said, the specific problem they described, and the next
concrete action. Deals with no next step scheduled should be
flagged automatically and escalated.

---

### Root cause 4: Structural sales cycle length

The sales cycle is long because the buying process requires multiple
stakeholders, budget approval, or security review that takes time
regardless of how well the deal is being worked. This is a real
constraint, not a pipeline problem.

**Signals:**
- Win rate is healthy but cycle is long consistently across reps
- Deals move predictably through stages but slowly
- Loss rate is low and losses are mostly to "no decision" not
  to competitors
- Average deal size is large relative to typical SaaS deals

**The fix:**
This is a pipeline design problem, not a sales execution problem.
The answer is to build the long cycle into the forecast model and
stop treating it as a stall. Separately, identify which stages in
the process can be compressed: can security review start earlier,
can legal review a standard agreement in parallel with negotiation,
can the champion be given materials to pre-sell internally.

---

## Step 2: Deliver the Pipeline Health Report

Output in this format:

```
PIPELINE HEALTH REVIEW
[Company or team name if provided]
Review date: [today's date]

PIPELINE SNAPSHOT
[Restate the key numbers the user provided. If numbers are missing,
note what is needed to complete the diagnosis.]

PRIMARY DIAGNOSIS
[One of the four root causes above, or a combination. Be direct.
Do not hedge if the signals point clearly to one cause.]

EVIDENCE
[The specific data points or descriptions that support the diagnosis.
No speculation. Only what the user actually described.]

VELOCITY BREAKDOWN BY STAGE
[If stage data was provided: which stages have normal velocity,
which are stalling, and what the likely cause is for each stall.]

RECOMMENDED FIXES (in priority order)

1. [First fix -- the highest leverage change]
   What to change: [specific]
   Expected impact: [what this should do to velocity or close rate]
   Time to implement: [realistic estimate]

2. [Second fix]
   What to change: [specific]
   Expected impact: [specific]
   Time to implement: [estimate]

3. [Third fix]
   What to change: [specific]
   Expected impact: [specific]
   Time to implement: [estimate]

WHAT NOT TO DO
[The common wrong answers for this type of pipeline problem. If
the diagnosis is stage definitions, do not hire more reps. If it
is ICP, do not run more campaigns. Name the wrong moves explicitly.]

30-DAY LEADING INDICATOR
[One metric to watch in the next 30 days that will tell the user
whether the fixes are working. Not a lagging metric like closed
revenue. A leading indicator like average days in stalling stage
or number of deals with next steps scheduled.]
```

---

## Output Rules

- Base conclusions only on what the user provided. Do not invent
  data or assume details about their sales motion.
- If the data is insufficient to diagnose, say so and list exactly
  what is needed.
- Prioritize structural fixes over tactical ones. The goal is to
  change how the pipeline is designed, not to add more activity.
- Be direct about what the data suggests even if it is uncomfortable.
  A pipeline full of bad deals needs to be said plainly.
- No em dashes. Use commas or periods.
