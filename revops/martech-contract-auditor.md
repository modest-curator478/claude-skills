---
name: martech-contract-auditor
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user mentions a vendor renewal,
  SaaS contract, MarTech negotiation, or any conversation about renewing,
  renegotiating, or evaluating a marketing or sales technology subscription.
  Trigger phrases include: "our HubSpot renewal is coming up," "ZoomInfo
  contract," "renewing our," "vendor negotiation," "contract coming up,"
  "too expensive," "right-sizing our stack," or any mention of a specific
  MarTech tool alongside pricing or contract concerns.

  Do NOT trigger for general tool comparisons or product research where
  no existing contract or renewal is involved.
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
---

# MarTech Contract Auditor: Vendor Renewal and Negotiation Prep

This skill runs when the user is preparing for a vendor renewal or
renegotiation. Search the web for current pricing benchmarks before
writing anything. Do not rely on training data for pricing information.

---

## HOW TO SET UP THIS SKILL

This skill works out of the box. No personal data required. Optionally
add your current stack and contract details to get more specific output.

**Optional context to provide:**
- Current vendor, contract value, and renewal date
- How many seats, contacts, or records you are paying for vs. using
- What you actually use vs. what came with the package
- Whether you have a competing vendor evaluation in progress

---

## What This Skill Does

Most MarTech vendors price on the assumption that buyers do not know
their leverage. This skill helps you find it. It walks through six
areas where renewal leverage exists, produces a negotiation brief, and
delivers specific ask language you can use in the renewal conversation.

---

## Step 1: Search for Current Pricing Benchmarks

Before building the negotiation brief, search for:

1. Vendor name + "pricing" + current year
2. Vendor name + "discount" or "negotiation tips"
3. Vendor name + alternatives or competitors (to establish walk-away
   options)
4. G2 or Capterra reviews mentioning pricing or contract experience
5. Any recent funding, acquisition, or financial news about the vendor
   (financially pressured vendors discount more aggressively)

Note what you find. If pricing is not publicly available, note that
and flag it as a negotiation signal: opacity in pricing means more
room to negotiate.

---

## Step 2: Build the Leverage Audit

Go through each category below and assess the user's position.

**Usage vs. spend**
Is the user paying for capacity they are not using? Seats, contacts,
records, API calls, or features that went unused last cycle are the
strongest leverage point in any renewal. If usage is below 70% of
contracted capacity, that is an opening.

**Contract timing**
Is the renewal coming at end of quarter or end of year for the vendor?
Vendors close deals under quota pressure. A renewal that lands in the
last two weeks of a vendor's fiscal quarter is worth 10-20% more
discount than the same renewal in the middle of the quarter.

**Competitive alternatives**
What are the two or three most credible alternatives to this vendor?
Even if the user has no intention of switching, having named
alternatives in the conversation changes the dynamic. The user does
not need to lie. They need to be able to say "we are evaluating X and
Y as part of this renewal process" and mean it.

**Multi-year leverage**
If the user is willing to commit to a multi-year term, what is that
worth? Most vendors will trade 15-25% off annual price for a 2-year
commitment. Only recommend this if the tool is genuinely sticky.

**Bundle and package gaps**
Is the user on a package that includes things they do not need, or
missing things they do need that would require an upgrade? Both are
negotiation angles. Downgrade asks and feature-for-discount trades
are legitimate.

**Relationship and history**
How long has the user been a customer? Long-tenure customers who have
never negotiated are often on above-market rates. Vendors do not
proactively offer loyalty discounts. You have to ask.

---

## Step 3: Deliver the Negotiation Brief

Output in this format:

```
VENDOR RENEWAL BRIEF
[Vendor Name]
Renewal date: [if provided, otherwise "not specified"]
Current annual value: [if provided, otherwise "not specified"]

LEVERAGE SUMMARY
[2-3 sentences on where the user's strongest leverage sits based on
the audit above. Be direct about which angles are worth pursuing and
which are not.]

TOP THREE ASKS (in priority order)

1. [Primary ask -- the number or term you are going in for]
   Rationale: [why this is reasonable and defensible]
   How to frame it: [specific language to use]

2. [Secondary ask -- fallback or addition]
   Rationale: [why]
   How to frame it: [language]

3. [Tertiary ask -- nice to have or concession trade]
   Rationale: [why]
   How to frame it: [language]

WALK-AWAY POSITION
[What the user should be willing to walk away from if terms do not
move. Name the specific alternative vendor if one exists.]

THINGS TO AVOID
[Common mistakes in this type of renewal: accepting the auto-renewal,
negotiating over email instead of a call, revealing timeline pressure,
or asking for a discount without a rationale.]

ESTIMATED SAVINGS RANGE
[Based on benchmarks found: X% to Y% reduction is realistic. If no
benchmarks were found, state that and give a conservative estimate
based on typical SaaS negotiation ranges of 10-25%.]
```

---

## Output Rules

- Never invent pricing data. If benchmarks are not found, say so.
- Be direct about weak leverage. Not every renewal has strong angles.
- Frame language as what the user would actually say, not what a
  negotiation textbook would say.
- Keep the brief to one page equivalent. This is a working document,
  not a research paper.
- No em dashes. Use commas or periods.
