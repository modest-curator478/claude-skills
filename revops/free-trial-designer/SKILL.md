---
name: free-trial-designer
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user wants to build, fix,
  or evaluate a free trial program for a B2B SaaS product. Trigger
  phrases include: "free trial," "trial program," "PLG," "product-led
  growth," "trial to paid conversion," "trial isn't converting,"
  "people sign up but don't convert," "trial length," "trial gate,"
  or any request to design or improve a B2B SaaS product trial.

  Also trigger when the user asks how to improve trial conversion rates
  or how to build the nurture sequence for a trial.

  Do NOT trigger for general onboarding, user activation, or retention
  questions that are not specifically about a free trial program.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Free Trial Designer: B2B SaaS Trial Program Architecture

This skill designs or diagnoses a B2B SaaS free trial program. It
covers trial gate design, trial length, the activation sequence,
the sales-marketing handoff, and the conversion framework. The goal
is a trial that teaches prospects to succeed with the product, not
just a 14-day countdown to a sales call.

---

## HOW TO SET UP THIS SKILL

Ask the user for the following context before proceeding:

- What the product does and who the primary buyer is
- Current trial structure if one exists (length, gate, features included)
- Current trial-to-paid conversion rate if known
- Average deal size and sales motion (self-serve, sales-assisted, enterprise)
- What the user considers a successful trial (demo booked, feature
  activated, data imported, etc.)
- Whether sales is involved in the trial and at what point

If they have an existing trial program, ask where most trials go
wrong before redesigning.

---

## The Five Trial Program Decisions

Every trial program requires five structural decisions. Get these
wrong and no amount of nurture email will fix the conversion rate.

---

### Decision 1: The trial gate

Option A (no gate): Anyone can start with just an email address. Best
for self-serve products with short time-to-value and low ACV. High
volume, lower intent signal.

Option B (light gate): Requires a work email. Filters personal addresses
and gives sales a domain to research. Most common for B2B mid-market.

Option C (qualification gate): Asks 2-3 qualification questions before
granting access. Reduces volume, increases intent signal, allows routing
to the right experience. Best for enterprise products.

Option D (demo-first): Trial access requires a demo call first. Not
technically a free trial. Best for complex enterprise products where
the product cannot be understood without configuration.

Match the gate to the deal size and sales motion. If ACV is under
$10K and time-to-value is short, use A or B. If ACV is over $25K
and requires implementation, use C or D.

---

### Decision 2: Trial length

Trial length should be set based on how long it takes the average
user to reach the value moment, not on an arbitrary number.

The value moment is the specific action or outcome inside the product
that correlates most strongly with conversion to paid. Find it by
looking at closed-won customers and asking: what did they do in the
product before they decided to buy?

Set trial length: find the median time to the value moment, add 25-30%
buffer. If median is 7 days, set trial to 10 days. If 20 days, set
to 28 days.

14 days because "everyone does 14 days" is not a strategy. If your
product requires data import or configuration before delivering value,
14 days may not be enough. If it delivers value in 5 minutes, 14 days
creates unnecessary length and reduces urgency.

---

### Decision 3: Feature access

Full product access: Best when value is immediately apparent without
significant configuration. Risk: users see complexity before value.

Core feature access: Limit to features most likely to produce the
value moment. Hide advanced features until post-conversion. Best for
complex products.

Sandboxed environment with sample data: Pre-populate with realistic
data so users see the product working immediately. Best for products
where the value is in seeing the output, not the setup.

---

### Decision 4: The activation sequence

Day 0 (immediately after signup): Welcome email with one clear action.
Not a feature tour. One thing: "Do this first and you will see why
this matters." Single CTA.

Day 1-2: Check whether Day 0 action was completed. If yes, move to
next step. If no, reframe the value of that first action. Do not move on.

Day 3-5: Value milestone email. What can they see or do now that they
could not before? Make the value concrete with numbers if possible.

Mid-trial: Check-in with a specific question. Not "how is it going?"
but "have you been able to [specific action] yet?" Surfaces blockers.

Pre-expiration: Clear statement that trial ends in X days. What happens.
What they need to do to continue. No tricks. Just clarity.

Expiration: What happens to their data. How to reactivate. One clear
path to conversion.

Sales involvement: For deals above a certain ACV threshold, sales
should receive an alert when a trial user completes the value moment
action. That is the highest-intent signal in the trial.

---

### Decision 5: The conversion framework

Self-serve: User upgrades directly inside the product. Best for lower
ACV. Requires clear pricing and a simple upgrade flow.

Sales-assisted: Trial user books a call or connects with a rep before
converting. Best for higher ACV where contract requires negotiation
or IT approval.

Hybrid: Self-serve for smaller deals, sales-assisted for larger.
Route based on company size or ACV threshold from trial signup.

Conversion blockers to audit: pricing page clarity, procurement friction
for that company size, and technical blockers like security review or
integration requirements.

---

## Deliver the Trial Program Design

Output in this format:

```
FREE TRIAL PROGRAM DESIGN
[Product or company name if provided]
Built: [today's date]

PROGRAM OVERVIEW
[2-3 sentences: gate, length, sales motion, primary conversion goal]

STRUCTURAL DECISIONS
Trial gate: [recommended gate and rationale]
Trial length: [recommended length and rationale based on value moment]
Feature access: [what is included and excluded and why]
Sales involvement trigger: [at what point and based on what signal]
Conversion path: [self-serve, sales-assisted, or hybrid and why]

THE VALUE MOMENT
[The specific action in the product the entire trial is designed to
get the user to complete. Everything in the activation sequence
points here.]

ACTIVATION SEQUENCE
Day 0: [email subject, one-line content description, single CTA]
Day 1-2: [conditional logic based on whether Day 0 action was taken]
Day 3-5: [value milestone content]
Mid-trial: [check-in email structure]
Pre-expiration: [what to say and how to frame it]
Expiration: [what happens and one clear path forward]

SALES ALERT TRIGGERS
[The specific in-product actions that should notify sales of
high-intent trial users.]

CONVERSION FRAMEWORK
[The specific steps a user takes to convert, what friction exists,
and what to remove.]

MEASUREMENT FRAMEWORK
Primary metric: Trial-to-paid conversion rate (baseline and target)
Supporting metrics:
- Time to value moment (average days to first key action)
- Day 7 retention rate (percentage still active midway)
- Conversion rate by acquisition channel
- Trial-to-call rate (for sales-assisted models)

RISKS AND FAILURE MODES
[Two or three most likely reasons this program will underperform
and what to do about each proactively.]
```

---

## Output Rules

- Match program design to the product's actual sales motion and deal
  size. Do not recommend self-serve conversion for a $50K ACV product.
- Be specific about the value moment. Push the user to name the
  specific action, not a vague "when they see value."
- Flag when the user is describing a trial that is actually a POC
  or pilot. These require different structures.
- No em dashes. Use commas or periods.
