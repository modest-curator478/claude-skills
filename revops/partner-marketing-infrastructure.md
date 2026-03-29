---
name: partner-marketing-infrastructure
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user wants to build, audit,
  or improve a partner marketing program. Trigger phrases include:
  "partner program," "channel partners," "reseller program," "integration
  partners," "technology partners," "co-sell," "partner pipeline,"
  "partner-sourced revenue," "partner tiers," "partner attribution,"
  "we want to build a partner program," or any request to structure
  the operational infrastructure behind a B2B partner or channel program.

  Also trigger when the user asks how to measure partner pipeline
  contribution, how to attribute revenue to partner-sourced deals,
  or how to build a joint go-to-market playbook with a specific partner.

  Do NOT trigger for co-marketing content creation, referral programs
  aimed at end customers, or affiliate programs. This skill is
  specifically about the operational and attribution infrastructure
  of a B2B partner or channel program, not the content that supports it.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Partner Marketing Infrastructure: Building and Attributing Partner Pipeline

This skill designs the operational infrastructure of a B2B partner
program: tier structure, pipeline attribution, joint go-to-market
execution, and measurement framework. Most partner programs fail not
because the partners are wrong but because the infrastructure is missing.
Partners without a clear tier structure get inconsistent treatment.
Partner-sourced deals without attribution get credited to the wrong
channel. Programs without a measurement framework get cut when budgets
tighten because no one can prove their value.

---

## HOW TO SET UP THIS SKILL

This skill works out of the box. For more specific output, provide:

- Type of partners: technology integrations, resellers, referral
  partners, system integrators, or a combination
- Current state: no program exists, a program exists but is informal,
  or a program exists and needs to be rebuilt
- Number of current or target partners
- Average deal size and sales cycle length for the core product
- Whether the CRM is HubSpot, Salesforce, or another system
- Whether sales has separate pipeline targets for partner-sourced deals

---

## The Four Partner Program Infrastructure Problems

Most partner programs that underperform have one of four structural
problems. Identify which applies before building anything.

---

### Problem 1: No tier structure, so all partners get the same treatment

The company has twenty partners. Three of them refer deals consistently.
Five refer a deal every few months. Twelve have never referred a deal but
attend the annual partner summit. All twenty receive the same co-marketing
budget, the same sales attention, and the same access to product roadmap
information.

The result: the three high-performing partners feel undervalued relative
to the investment required to maintain the program. The twelve inactive
partners consume resources without producing pipeline. Everyone is
dissatisfied.

Fix: Build a tier structure that allocates resources based on partner
performance and potential. Tiers define what partners receive (sales
support, co-marketing budget, product access, deal registration
protection) and what they are expected to produce in return (pipeline
volume, deal size, customer success outcomes).

---

### Problem 2: No pipeline attribution, so partner value is invisible

Partner-sourced deals close and get counted in the direct sales number.
No one tracks that the deal came through a partner referral. When the
question comes up in a board meeting, the answer is "we think partners
contributed something but we're not sure how much."

This is not a data problem. It is an infrastructure problem. The CRM
was never configured to capture deal source at the deal level with
enough specificity to differentiate partner-sourced, partner-influenced,
and direct deals.

Fix: Build deal source attribution into the CRM before partners start
referring deals. Define the three categories clearly, create the required
fields, build the workflow that routes partner-registered deals into the
right pipeline view, and train sales on the distinction. Do this before
the program launches, not after the first deals close.

---

### Problem 3: No joint go-to-market playbook, so each partner operates differently

Partner A sends referrals via email. Partner B uses the deal registration
portal. Partner C expects a co-sell motion where their rep joins the first
call. Partner D wants co-branded content. Each relationship was built
organically and operates differently, which means every partner requires
a custom operating model and no one on the team can manage more than five
partners without it becoming unmanageable.

Fix: Define a standard joint go-to-market playbook that covers: how
partners register deals, how sales engages on partner-sourced deals,
what co-sell looks like versus a pure referral, what co-marketing
assets are available and how partners access them, and what happens
when a partner-sourced deal is lost. Partners can deviate from the
standard but the standard exists and is the starting point.

---

### Problem 4: No measurement framework, so the program cannot defend its budget

The program has been running for eighteen months. Partner-sourced revenue
exists but has never been isolated from the total revenue number. When
budget cuts come, the partner program is easy to eliminate because no
one has a clear answer to the question: what would we lose if this
program did not exist?

Fix: Define the partner program measurement framework before the program
launches, not when it needs to defend itself. The framework should
separate partner-sourced revenue from partner-influenced revenue, track
LTV of partner-sourced customers versus direct customers, and calculate
the cost of partner-sourced revenue against the cost of direct demand
gen for the same dollar of pipeline.

---

## The Partner Program Infrastructure Framework

### Component 1: Tier structure design

Define two to four tiers. More than four tiers creates complexity without
differentiation. Fewer than two means the program has no way to reward
high-performing partners or manage underperforming ones.

**Tier criteria (what determines which tier a partner belongs to):**

Performance criteria: pipeline volume generated in the last twelve
months, closed revenue attributed to partner referrals, average deal
size of partner-referred opportunities, customer retention rate of
partner-sourced customers.

Potential criteria: partner's total addressable customer base that
overlaps with your ICP, partner's sales team size and capacity to
refer deals, partner's existing relationship depth with target accounts.

Commitment criteria: whether the partner has signed a partner agreement,
completed product certification, and has a designated partnership contact
who is responsive.

**Tier benefits (what each tier receives):**

Tier 1 (Strategic partners): dedicated partner success manager, co-sell
support on every deal, co-marketing budget allocation, early access to
product roadmap, deal registration protection with a defined SLA, joint
quarterly business reviews.

Tier 2 (Growth partners): shared partner success support, co-sell
support on deals above a defined ACV threshold, access to co-marketing
assets and templates, deal registration with standard SLA.

Tier 3 (Referral partners): self-service deal registration, access to
the partner portal and standard co-marketing assets, no dedicated support.

**Tier movement criteria:**
Define explicitly what it takes to move up or down. Partners should know
at the start of each quarter what they need to produce to maintain or
advance their tier. This prevents the awkward conversation when a Tier 1
partner underperforms and needs to be moved.

---

### Component 2: Pipeline attribution infrastructure

This is the most technically specific component. Build it correctly the
first time. Retrofitting attribution after deals have closed is
significantly harder.

**The three deal source categories:**

Partner-sourced: the partner identified the opportunity, introduced your
company, and registered the deal before your sales team had any contact
with the account. The partner is the origin of the deal.

Partner-influenced: your sales team identified the opportunity, but a
partner played a meaningful role in the sales process. An integration
partner whose product was already in use at the account. A reseller
whose relationship accelerated the decision. The partner did not originate
the deal but contributed to the close.

Direct: no partner involvement in either origination or influence.

**CRM configuration requirements:**

At the deal or opportunity level, create a required field for Deal Source
with the three categories above. Add a Partner Name field that links
to the partner record. Add a Deal Registration Date field that captures
when the partner submitted the deal. Add a Partner Contribution field
(for influenced deals) that captures what the partner contributed
and at what stage.

Build a workflow that routes deal registration submissions from the
partner portal or email into the CRM with the partner name, deal source,
and registration date pre-populated. Sales should never have to manually
attribute a partner deal. The attribution should be automatic from the
registration event.

**Revenue reporting by category:**

Set up three pipeline views: partner-sourced pipeline, partner-influenced
pipeline, and direct pipeline. These should be separate from the total
pipeline view but roll up into it. Track conversion rate, average deal
size, and sales cycle length separately for each category. Partner-sourced
deals often have different characteristics than direct deals, and those
differences are important for program management.

---

### Component 3: Joint go-to-market playbook

Define the standard operating model for partner collaboration. Every
partner starts with the standard playbook. Tier 1 partners may have
addendums that reflect their specific motion.

**Deal registration process:**
How does a partner register a deal? What information is required?
What is the SLA for sales to acknowledge and accept a registration?
What happens if sales already has the account in active prospecting?
Define the conflict resolution process before the first conflict happens.

**Co-sell motion definition:**
What does co-sell mean for your program? A strict definition: the
partner's rep is on the first call. A broader definition: the partner
provides an introduction and context but is not involved in the sales
process. Define which tier gets which co-sell model and what sales is
expected to do when a partner joins a call.

**Partner-sourced deal sales process:**
When sales receives a partner-sourced deal, what is different about
how they handle it? At minimum: they acknowledge the partner within
a defined SLA, they update the partner on deal status at defined
milestones, and they notify the partner when the deal closes or is
lost. None of this happens consistently without a defined process.

**Co-marketing asset access:**
What co-marketing assets are available to partners? Where do they
live? How do partners request custom assets? Who approves partner use
of the company logo, messaging, and brand guidelines? Define this
before partners start creating materials that are off-brand or
factually incorrect.

---

### Component 4: Measurement framework

**Primary metrics:**

Partner-sourced revenue: the total closed revenue attributed to
partner-sourced deals in a defined period. This is the headline number.

Partner program ROI: partner-sourced revenue divided by the total
cost of running the partner program (partner success headcount,
co-marketing spend, partner events, portal and tool costs). Compare
this to the cost of generating the same revenue through direct demand gen.

Partner pipeline coverage: the ratio of partner-sourced pipeline to
partner-sourced revenue target. If the target is $1M in partner-sourced
closed revenue and the pipeline is $2.5M, coverage is 2.5x. B2B SaaS
programs typically need 3x to 4x coverage depending on win rates.

**Secondary metrics:**

Partner activation rate: the percentage of program partners who have
referred at least one deal in the last ninety days. A program with
thirty partners and five active ones is not a thirty-partner program.

Average deal size by partner: high-performing partner programs often
produce larger deal sizes than direct channels because partners bring
credibility and warm introductions. Track this to identify which
partners are producing premium deals.

Time to close on partner-sourced deals: measure whether partner-sourced
deals close faster than direct deals. This is often true and is one
of the most compelling data points when justifying the program's budget.

LTV of partner-sourced customers: measure whether customers acquired
through partners have better retention and expansion rates. Also often
true, and also compelling.

**What not to measure:**

Number of partners signed: a vanity metric. A program with ten active
partners is better than one with fifty inactive partners.

Co-marketing impressions or content downloads: this measures activity,
not business outcomes. Only track if there is a clear link to pipeline.

---

## Deliver the Partner Program Infrastructure Plan

Output in this format:

```
PARTNER PROGRAM INFRASTRUCTURE PLAN
[Company or program name if provided]
Partner type: [technology, reseller, referral, or combination]
Built: [today's date]

PROBLEM DIAGNOSIS
[Which of the four structural problems applies, based on what the user
described. If the program is new, identify which problems are most
likely to emerge and why.]

TIER STRUCTURE

Tier 1 ([name]): [criteria for inclusion] | [benefits]
Tier 2 ([name]): [criteria for inclusion] | [benefits]
Tier 3 ([name]): [criteria for inclusion] | [benefits]

Tier movement criteria: [specific thresholds for moving up or down]
Review cadence: [when tier assignments are reviewed]

CRM ATTRIBUTION SETUP

Deal source categories: Partner-sourced / Partner-influenced / Direct
Required fields: [list with field type and whether required or optional]
Routing workflow: [how partner deal registrations flow into the CRM]
Conflict resolution rule: [what happens when sales already has the account]

JOINT GTM PLAYBOOK (STANDARD)

Deal registration process: [steps, required info, SLA]
Co-sell definition: [what it means and which tiers get it]
Partner communication SLA: [acknowledgment, status updates, close notification]
Co-marketing asset access: [where assets live and how partners request them]

MEASUREMENT FRAMEWORK

Primary metrics: [the three primary metrics with targets if known]
Reporting cadence: [how often and to whom]
Quarterly business review structure: [for Tier 1 partners]

LAUNCH SEQUENCE

Pre-launch (before accepting any deal registrations):
[CRM configuration, partner agreement, portal or process setup]

Soft launch (first 30 days with Tier 1 partners only):
[What to test and validate before opening to all tiers]

Full launch:
[When to expand and what the criteria are]

RISKS AND FAILURE MODES
[The two or three most likely reasons this program will underperform
and what to do proactively about each.]
```

---

## Output Rules

- Base the plan on the type of partners and sales motion the user
  described. A technology integration partner program has different
  infrastructure requirements than a reseller program.
- Be specific about CRM configuration. Vague recommendations like
  "track partner deals" are not useful. Name the fields, the workflow
  triggers, and the reporting views.
- If the program already exists and is underperforming, diagnose the
  structural gap before recommending additions.
- Do not recommend more tiers than necessary. Two tiers is often the
  right answer for an early-stage program.
- Note that this skill covers operational and attribution infrastructure
  only. Partner agreements, legal terms, and commission structures are
  outside scope and should be handled separately with legal and finance.
- Flag cannibalization risk in the output if the program involves resellers
  or co-sell partners who will be working the same accounts as the direct
  sales team. This is a predictable conflict that needs rules of engagement
  before the first conflict happens, not after.
- No em dashes. Use commas or periods.
