---
name: intent-data-activation
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user is working with intent
  data signals from ZoomInfo, Bombora, G2, 6sense, Demandbase, or any
  similar platform, and needs to operationalize those signals into CRM
  workflows, campaign enrollment, rep alerts, or account prioritization.
  Trigger phrases include: "intent data," "ZoomInfo intent," "Bombora
  signals," "G2 buyer intent," "in-market accounts," "activating intent,"
  "intent signals aren't doing anything," "we're paying for intent data
  but not using it," "how do I route intent accounts," "intent-based
  campaigns," or any situation where the user has intent data and needs
  to turn it into action.

  Also trigger when the user is evaluating which intent signals to act
  on, designing CRM workflows to handle signal ingestion, or trying to
  measure whether their intent activation is producing results.

  Do NOT trigger for general ABM strategy, ZoomInfo data enrichment
  questions, or lead scoring without intent signals. This skill is
  specifically about the workflow layer between receiving an intent
  signal and taking an action.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Intent Data Activation: Turning Signals Into Actions That Generate Pipeline

Intent data earns its cost when it changes what happens next for a specific account. A signal without a workflow is just data. This skill encodes the workflow design decisions that connect a signal to a response, the threshold logic that determines which signals are worth acting on, the routing decisions that determine whether a signal goes to a rep or a campaign, and the measurement framework that tells you whether the activation is working.

---

## HOW TO SET UP THIS SKILL

Provide:

- Which intent data provider or providers you have: ZoomInfo Intent, Bombora, G2 Buyer Intent, 6sense, Demandbase, or other
- Your CRM: HubSpot, Salesforce, or other
- How intent data currently flows into your CRM, if at all
- Whether you have an SDR or BDR team handling outbound
- Your current ICP: the firmographic and behavioral profile of your best-fit accounts
- What, if anything, you are currently doing with intent signals

---

## The Core Problem: Intent Data Without Activation Logic

Intent signals decay fast. A Bombora Company Surge score that spikes on a Monday and is not acted on by Wednesday has already lost significant value. Accounts in active research mode are evaluating multiple vendors simultaneously. The team that responds first with relevant messaging wins more conversations than the team with the best product but the slowest activation.

---

## Step 1: Signal Triage Before Building Any Workflow

Signal quality by source type:

First-party signals (your own website, your own HubSpot or Salesforce data): Highest quality. An account visiting your pricing page three times in a week is a more reliable signal than an account showing Bombora surge on a topic adjacent to your category.

G2 Buyer Intent: High quality for software categories. An account actively reviewing products in your category on G2 has demonstrated vendor evaluation behavior.

Bombora Company Surge: Medium quality. Topic selection matters enormously. Broad topics produce noise. Narrow, category-specific topics produce signal.

ZoomInfo Intent: Variable quality. Treat it as a directional indicator to be validated against ICP fit before routing to reps.

The ICP filter must come before the intent filter. A high-intent signal from a company outside your ICP is not worth acting on at the rep level.

---

## Step 2: Threshold Design

Tier 1 (immediate rep response within 24 hours):
Account is in ICP. No open opportunity in CRM. Intent signal is first-party or G2 Buyer Intent active. Signal has been active for three or more days.

Tier 2 (campaign enrollment, SDR sequence within 48 hours):
Account is in ICP. No open opportunity. Bombora surge score above your chosen threshold (typically 60 or above on a 100-point scale). Or ZoomInfo intent score elevated on two or more relevant topics simultaneously.

Tier 3 (retargeting only, no direct outreach):
Account shows intent signal but does not fully match ICP. Or signal is weak or single-topic.

Existing customers and open opportunities: Flag for customer success or the account executive who owns the relationship.

---

## Step 3: Workflow Architecture in HubSpot or Salesforce

The workflow must: receive the signal, check ICP fit, apply threshold logic, route to the right response, and log the trigger for measurement.

HubSpot workflow structure:

Enrollment trigger: Company property updated by the intent data integration.

Step 1: Check company properties against ICP criteria. If not ICP fit, enroll in Tier 3 retargeting list. Exit workflow.

Step 2: Check for existing open deal. If open deal exists, create task for deal owner. Exit.

Step 3: Apply signal threshold logic. If Tier 1, create high-priority SDR task due within 24 hours. Log intent trigger in contact timeline. If Tier 2, enroll in outbound sequence or marketing nurture with intent-aware messaging. If Tier 3, add to retargeting audience only.

Step 4: Set a re-enrollment window. If the account takes no action and the signal persists for 14 days, re-evaluate.

The logging step is not optional. Every time the workflow fires, log the intent trigger, the tier it was routed to, and the date.

---

## Step 4: Messaging That Uses the Signal

Do not say: "I see you have been researching supply chain software." This signals surveillance, not relevance.

Do say: "We work with a lot of supply chain teams who are evaluating how to get better pipeline visibility right now."

G2 Buyer Intent: Lead with differentiation and proof. The account is already sold on the category. The question is why you versus the alternatives.

Bombora surge on a problem topic: Lead with problem validation and perspective, not a product pitch.

First-party high-intent (pricing page, demo page): Make it easy to take the next step. Short, direct, low friction.

---

## Step 5: Measuring Activation Effectiveness

Conversion rate by intent tier: If Tier 1 is not converting to opportunities at a meaningfully higher rate than Tier 2, your Tier 1 threshold is miscalibrated.

Signal-to-opportunity time: How many days between the first intent signal and opportunity creation. If this number is improving, your activation speed is working.

Run both reports quarterly. Adjust thresholds based on what you see.

---

## Common Activation Failures

The rep ignores intent alerts: Tighten Tier 1 threshold to reduce volume. Move alerts to the channel reps already use.

The workflow fires but nothing converts: Audit the last 30 Tier 1 accounts. Find the break in the chain before adjusting thresholds.

Intent data stops flowing into CRM: Native integrations break silently. Build a weekly check into your RevOps routine.

---

## Output Rules

- Never recommend activating intent signals without first defining ICP criteria.
- Be specific about CRM property names and workflow steps when the user has named their CRM.
- If the user does not have a native integration between their intent provider and CRM, address that before building workflow logic.
- The logging step is not optional. Flag it explicitly if the user does not mention measurement.
- No em dashes. Use commas or periods.
