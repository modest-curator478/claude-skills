# claude-skills: B2B Demand Gen, RevOps, and Marketing Leadership Skills for Claude

A library of Claude skills built for B2B demand gen leaders, RevOps practitioners, and marketing Directors. Covers HubSpot, ABM, intent data, pipeline health, win/loss analysis, offer negotiation, sales alignment, and small team management. Built from 20 years of running these programs, not reading about them.

Every skill in this repo encodes a real decision that practitioners face repeatedly and get wrong in predictable ways. The goal is not to explain how something works. The goal is to encode the judgment behind the work so Claude can operate as a genuinely useful thinking partner, not a prompt formatter.

**25 skills across 5 folders.**

---

## What Makes These Skills Different

Most Claude skills repos are frameworks dressed up as expertise. Challenge-solution-result structures. Generic negotiation tactics. Textbook pipeline stage definitions.

These skills are built around the decisions that generic frameworks skip:

- Which intent signal threshold routes to a rep versus a campaign, and why
- How to separate a product gap from a messaging gap in a win/loss debrief
- What to say when a consulting client pushes back on a finding you know is correct
- How to present a missed pipeline quarter without making it look like information management
- Why CRM closed/lost data is structurally unreliable before you run any analysis on it

If a section could appear in a "best practices" blog post, it was cut or rewritten until it could not.

---

## Folders

### `job-search/`
For active job searching at the Director level in B2B SaaS. Covers the research, outreach, and evaluation decisions that determine whether a process goes anywhere.

| Skill | What it does |
|---|---|
| `competitive-intelligence` | Deep company research before an interview or decision to apply |
| `resume-optimizer` | Score fit, select the right resume version, tailor for the specific role |
| `recruiter-outreach` | Director-level outreach that leads with proof, not personality |
| `offer-evaluation-negotiation` | Evaluate total compensation across all four components, design a specific counter, define a walk-away position |

---

### `revops/`
For the RevOps and demand gen practitioner building or inheriting systems. Covers the operational infrastructure that determines whether pipeline is predictable.

| Skill | What it does |
|---|---|
| `abm-campaign-builder` | Build a named account campaign from ICP to execution |
| `first-90-days-demand-gen-revops` | Diagnostic playbook for the first quarter in a new role |
| `free-trial-designer` | Design a free trial that converts, not just one that generates signups |
| `gtm-ai-adoption-rollout` | Lead a company-wide AI tool evaluation and rollout across a GTM team |
| `hubspot-audit` | Audit a HubSpot instance for workflow conflicts, data hygiene, and pipeline visibility gaps |
| `intent-data-activation` | Turn ZoomInfo, Bombora, or G2 signals into CRM workflows, rep alerts, and campaign enrollment with tier-based threshold logic |
| `martech-contract-auditor` | Audit and renegotiate MarTech contracts with specific renewal tactics |
| `partner-marketing-infrastructure` | Build the systems behind a partner program, not just the program strategy |
| `pipeline-health-reviewer` | Diagnose pipeline quality, velocity, and coverage gaps before the forecast conversation |
| `win-loss-analysis` | Run a structured deal outcome diagnostic that feeds back into ICP, messaging, and channel decisions |

---

### `leadership/`
For the Director navigating the human and organizational dynamics of the role: upward relationships, peer alignment, team management, and recurring accountability conversations.

| Skill | What it does |
|---|---|
| `managing-up` | Build the upward relationship with a CEO, CRO, or VP across four specific friction types |
| `marketing-budget-defense` | Defend marketing spend when funding is at risk |
| `marketing-qbr` | Prepare and deliver a quarterly business review that builds credibility, including how to handle a missed quarter |
| `sales-leader-alignment` | Diagnose and repair Sales-Marketing misalignment across four distinct types |
| `sales-marketing-sla` | Design a service level agreement that both teams will actually follow |
| `small-team-management` | Manage a team of two to six direct reports as a practitioner who came up through the function, not HR training |

---

### `writing/`
For writing that has to do a specific job: generate pipeline, document proof, or build credibility in a professional context.

| Skill | What it does |
|---|---|
| `b2b-case-study-writer` | Write a case study that functions as a sales asset, not content marketing decoration |
| `b2b-outreach-humanizer` | Rewrite AI-generated or template outreach so it reads like a person wrote it |
| `linkedin-post` | Write practitioner-level LinkedIn content that drives engagement without sounding like a thought leadership post |

---

### `consulting/`
For the independent practitioner delivering RevOps or HubSpot consulting work to external clients.

| Skill | What it does |
|---|---|
| `consulting-client-presentation` | Deliver findings and recommendations to a client in a way that maintains the relationship, handles bad news, manages scope, and closes with a clear next step |
| `consulting-engagement-setup` | Scope, price, and structure a consulting engagement from the first conversation |

---

## How to Use These Skills

**In Claude.ai (Pro, Max, Team, or Enterprise):**
Go to Settings > Capabilities > Skills and upload any skill file. Claude will activate the skill automatically when it detects a relevant request, or you can reference the skill by name.

**In Claude Projects:**
Add the skill file contents to your Project knowledge. Claude will apply the skill in every conversation within that Project.

**In Claude Code:**
```bash
# Clone the repo
git clone https://github.com/matellez/claude-skills.git

# Copy all skills to your global Claude skills directory
cp claude-skills/revops/* ~/.claude/skills/
cp claude-skills/leadership/* ~/.claude/skills/
cp claude-skills/job-search/* ~/.claude/skills/
cp claude-skills/writing/* ~/.claude/skills/
cp claude-skills/consulting/* ~/.claude/skills/

# Or install specific skills only
cp claude-skills/revops/intent-data-activation.md ~/.claude/skills/
```

---

## Who Built This

20 years running demand gen and RevOps programs at B2B SaaS companies. Pipeline from $8M to $14M. CPL from $340 to $85. Sales cycles from 8 months to 3. LTV:CAC from 1.8:1 to 5.2:1. HubSpot rebuilds, ABM programs, partner infrastructure, GTM AI rollouts.

These skills are built from that work, not from reading about it.

[linkedin.com/in/manuelvallestellez](https://linkedin.com/in/manuelvallestellez)

---

## Contributing

If you have practitioner experience in B2B marketing, demand gen, or RevOps and want to contribute a skill, open a PR. The bar is the same as above: encode judgment, not frameworks. If the content could appear in a blog post without modification, it needs more work.

---

## License

MIT
