---
name: linkedin-post
version: 1.0.0
description: |
  AUTO-TRIGGER: Apply this skill when the user asks Claude to write, draft,
  create, or improve a LinkedIn post, caption, or update. Also trigger when
  the user asks for a post about a professional topic they plan to share on
  LinkedIn.

  Do NOT trigger for long-form articles, resumes, emails, or general writing
  tasks. This skill is specifically for short-form LinkedIn post content only.

  This skill structures and formats LinkedIn posts to match the user's
  established content style: punchy, practitioner-level, engagement-focused,
  with a strong ending that drives comments without resorting to "agree or
  disagree?" cliches.
allowed-tools:
  - Read
  - Write
  - Edit
---

# LinkedIn Post Skill

This skill runs automatically when the user wants a LinkedIn post. Apply
all rules below before delivering output. Do not explain what you are
doing. Just deliver the post.

---

## HOW TO SET UP THIS SKILL

Replace the [PLACEHOLDER] sections with your own profile before adding
this file to your Claude Project.

---

## Your Profile

**Name:** [Your full name]

**Role and background:** [1-2 sentences. Your title, domain, years of
experience, and current focus. Example: "B2B SaaS marketing leader,
15 years in demand generation and RevOps. Currently consulting and
writing about pipeline strategy and AI-assisted marketing."]

**Content focus areas:** [List 4-6 topics you post about regularly.
Example:
- Original takes on B2B demand gen and pipeline strategy
- AI tools and productivity for marketers and operators
- Commentary on industry articles or trends
- Lessons from building GTM functions at B2B SaaS companies]

**Audience:** [Describe who reads your content. Example: "B2B marketers,
RevOps leaders, demand gen practitioners, founders, and recruiters in
the SaaS and tech space."]

---

## Voice Rules (Non-Negotiable)

These apply to every post, no exceptions.

- **Short and punchy.** Most sentences under 12 words. Cut anything
  that does not add meaning.
- **Lead with the sharpest idea.** Do not build up to the point. Start
  with it.
- **Active voice only.** Never passive.
- **No em dashes.** Use a period or comma instead.
- **No "agree or disagree?" endings.** This is the most common LinkedIn
  cliche. Never use it.
- **No fluff openers.** Never start with "In today's landscape," "As a
  [title]," "I've been thinking a lot about," or any variation.
- **No sycophantic language.** No "excited to share," "humbled to
  announce," "honored to."
- **No AI vocabulary words.** No: delve, foster, crucial, pivotal,
  landscape, tapestry, underscore, showcase, testament, vibrant.
- **Opinions are required.** Neutral posts get ignored. Take a position.
- **Outcome framing when relevant.** Connect ideas to business results,
  not just activities.

---

## Post Structure by Content Type

### Type 1: Original professional take

Use when sharing a direct opinion or observation about your domain.

**Structure:**
```
[Sharp opening statement: the opinion or observation, 1-2 lines]

[2-4 short supporting points or examples]

[Closing line: a provocative statement, a specific question that invites
a real answer, or a reframe that makes the reader think]
```

**Rules:**
- Keep total post under 150 words
- No bullet points unless the content is genuinely a list
- If using bullets, 3 max, no bold headers on each bullet
- Closing line should spark a reaction, not solicit agreement

---

### Type 2: AI tools and productivity

Use when the post is about a tool, workflow, or productivity insight.

**Structure:**
```
[Specific tool or workflow named upfront -- no mystery]

[What it actually does, in plain terms]

[One concrete use case or result]

[Closing take: is this worth using, who it is for, what it changes]
```

**Rules:**
- Be specific. Name the tool. Name the workflow. Name the outcome.
- Do not hype. Be honest about limitations if relevant.
- Write for a non-technical audience. No jargon without explanation.
- Keep under 150 words.

---

### Type 3: Article commentary

Use when sharing an article and adding your take.

**Structure:**
```
[Your take on the article -- lead with the opinion, not the summary]

[One or two specific points worth amplifying or pushing back on]

[Your conclusion or reframe]

[Optional: credit the original source naturally]
```

**Rules:**
- The post should be about your angle, not a recap of the article.
- Never start with "Great article by..." or "Interesting read from..."
- Your opinion should be in the first two lines.
- Keep under 120 words.

---

### Type 4: Content series post

Use when the post is part of a recurring educational series.

**Structure:**
```
[Series context: one line that anchors where this fits]

[Core lesson or takeaway: the main thing the reader walks away knowing]

[2-3 supporting points, each as its own short line or paragraph]

[Closing line that teases the next post or lands the key insight]
```

**Rules:**
- Keep the series framing consistent across posts.
- Educational but not academic. Write like a practitioner.
- If numbered, include the number (e.g., "Part 4 of 6").
- Keep under 200 words.

---

## Formatting Rules

- **Line breaks matter on LinkedIn.** Single-sentence lines hit harder
  than dense paragraphs. Use white space deliberately.
- **No hashtag dumps.** If using hashtags, 2-3 max, only if relevant.
  Place them at the end naturally.
- **No emojis as bullet points.** If emojis are used at all, 1-2 max
  and only if they genuinely fit the tone.
- **No "link in comments"** unless the user specifically asks.

---

## Output Format

Deliver:
1. The post, ready to copy-paste
2. One line explaining the content type and ending strategy used

Do not add a preamble. Do not explain what you are about to do.
Deliver the post, then the one-line note.

If the user provides a topic but no content type, pick the most fitting
type and apply it. Do not ask for clarification unless the topic is
genuinely ambiguous.
