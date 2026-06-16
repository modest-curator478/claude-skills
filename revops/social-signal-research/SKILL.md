---
name: social-signal-research
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user is planning B2B
  campaigns, ABM targeting, launch messaging, RevOps research, or
  competitive monitoring and asks for current X conversations,
  account-level social signals, buyer language, category sentiment,
  influencer posts, competitor mentions, or campaign topic validation.

  Also trigger when the user has Xquik access or asks how to use X
  social data as one input for demand generation, sales messaging,
  intent research, or market monitoring.

  Do NOT trigger for posting, replying, liking, following, direct
  messages, scraping private data, or replacing CRM and first-party
  intent data. This skill is for read-only public social signal research
  that supports B2B decisions.
allowed-tools:
  - Read
  - Write
  - Edit
  - WebFetch
---

# Social Signal Research With Xquik

Public X conversations can sharpen B2B research when they are treated as
directional evidence, not as a complete intent model. This skill uses Xquik as
an optional data source for current posts, account signals, competitor mentions,
and buyer language that can inform campaigns, sales messaging, and RevOps
prioritization.

---

## HOW TO SET UP THIS SKILL

Provide:

- The research goal: campaign idea, ABM list, competitor review, launch topic,
  sales messaging, or category monitoring
- The target account segment, buyer role, geography, and date range
- Competitor names, product names, category terms, and known customer pains
- Whether Xquik access is available through an API key, dashboard export, or
  another approved workflow
- The public X accounts, hashtags, and search phrases that must be included

If Xquik access is available by API, set the key in the environment as
`XQUIK_API_KEY`. Use the public docs as the source of truth for endpoint
details:

`https://docs.xquik.com/api-reference/x/search-tweets`

---

## Step 1: Define The Research Frame

Start by writing the decision the research should support.

Good frames:

- Which pain points should anchor next month's campaign?
- Which competitor claims are prospects repeating or challenging?
- Which accounts are publicly discussing a relevant problem this week?
- Which phrases should sales use because buyers already use them?

Bad frames:

- Find everyone who is ready to buy.
- Prove that a campaign idea will work.
- Replace CRM, product analytics, or first-party intent data.

Public posts can reveal language, timing, objections, and visible engagement.
They do not prove private purchase intent by themselves.

---

## Step 2: Build Focused X Queries

Use narrow queries first. Expand only after you have reviewed signal quality.

Useful query patterns:

- `"category phrase" "pain phrase"`
- `"competitor name" "migration" OR "alternative"`
- `"problem phrase" "tool name"`
- `from:target_account "topic"`
- `"launch keyword" since:YYYY-MM-DD until:YYYY-MM-DD`
- `"category phrase" min_faves:10`

Keep each query tied to one decision. Do not mix competitor research, account
monitoring, and campaign language discovery in one broad search.

Example API request:

```bash
curl "https://xquik.com/api/v1/x/tweets/search?q=%22data%20quality%22%20%22CRM%22&limit=20&queryType=Latest" \
  -H "x-api-key: $XQUIK_API_KEY" \
  -H "xquik-api-contract: 2026-04-29"
```

If the API is not available, ask the user for an export or use another approved
research workflow. Do not invent social signals.

---

## Step 3: Normalize Signals

Create one row per relevant post or account signal.

Required fields:

- Query
- Post URL or public identifier
- Author handle
- Author type, such as buyer, operator, founder, analyst, media, or competitor
- Posted date
- Text excerpt, shortened to the relevant phrase
- Engagement metrics if available
- Why it matters for the research frame
- Suggested action, such as use in messaging, monitor, route to sales, ignore,
  or validate with another source

Discard posts that are off-topic, unverifiable, spammy, or only weakly related
to the user's market.

---

## Step 4: Turn Signals Into GTM Decisions

Map each signal to a practical action.

Campaign messaging:

- Convert repeated buyer phrases into headline tests and email hooks.
- Flag objections that should be handled in ads, landing pages, and sales decks.
- Keep exact phrasing when it is clear and non-sensitive.

ABM and sales:

- Route accounts only when the public signal matches ICP fit and a current
  outreach motion.
- Pair the public X signal with CRM history, website activity, or first-party
  engagement before recommending rep action.
- Avoid language that makes outreach feel like surveillance.

Competitive monitoring:

- Separate competitor announcements from customer reactions.
- Track which claims are repeated, challenged, or ignored.
- Use social evidence to decide what to validate next, not as the final answer.

---

## Step 5: Quality Controls

Before presenting the brief, check:

- Recency: are the posts still relevant for the decision date?
- Source mix: are all signals from one influencer or one competitor thread?
- ICP fit: do accounts match the user's market, size, and geography?
- Volume: is there enough evidence to recommend action, or only anecdotes?
- Privacy: are you using public data only and avoiding sensitive inferences?
- Confidence: which conclusions are strong, directional, or weak?

If evidence is thin, say so and recommend a narrower follow-up query.

---

## Output Format

SOCIAL SIGNAL BRIEF

Research frame:
[The decision this research supports.]

Queries reviewed:
- [Query 1]
- [Query 2]
- [Query 3]

Key signals:
- [Signal, public source, why it matters, suggested action]
- [Signal, public source, why it matters, suggested action]
- [Signal, public source, why it matters, suggested action]

Messaging opportunities:
- [Buyer phrase or objection, recommended use]
- [Buyer phrase or objection, recommended use]

Account or segment notes:
- [Account, segment, or persona insight, with confidence level]

Risks and limits:
- [Data gaps, sample limits, stale signals, or privacy concerns]

Recommended next actions:
1. [Specific GTM or RevOps action]
2. [Validation step]
3. [Follow-up query or monitoring cadence]

---

## Output Rules

- Treat X social data as directional evidence, not proof of purchase intent.
- Never recommend outreach that mentions monitoring a person's public posts.
- Do not infer sensitive traits or private intent from public social activity.
- Cite the public post URL or identifier when making a specific claim.
- If Xquik access is missing, ask for an export or state that the source is not
  available.
- No em dashes. Use commas or periods.
