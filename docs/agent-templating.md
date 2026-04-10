# Agent templating

> *How new agents are scaffolded from `@agent_template.md` — the canonical persona template.*

---

## Overview

Agent templating in Constructed‑Becoming is a **local-first, hybrid system**: agent persona definitions live in `agents/` as Markdown files with YAML frontmatter for machine parsing and a full narrative body for humans and the living OS.

The convention `@agent_template.md` refers to `agents/agent_template.md` — the canonical persona template. Referencing `@agent_template.md` in a prompt or document signals the intent to scaffold a new agent definition from that template.

---

## The `@agent_template.md` convention

When an agent or steward writes `@agent_template.md`, they are invoking the canonical template as the basis for a new agent. This is a **ritual reference** — it names the lineage the new agent descends from and commits to the ten-section structure defined in the template.

The ten sections are:

| Section | Content |
|---|---|
| 1. Identity Header | Name, role type, domain, date, status, steward |
| 2. Origin and Lineage | Chronicle/delta reference, lineage inheritance, founding tension |
| 3. Role and Scope | Core role statement, domain focus, explicit out-of-scope |
| 4. Core Capacities | Observable behaviours and patterns of contribution |
| 5. Operational Constraints | Principles and prohibitions guiding the agent's activity |
| 6. Interaction Style | Register, tone, and form of contributions |
| 7. Ritual Alignment | Rituals the agent participates in or facilitates |
| 8. Signature Output Pattern | Recognisable shape of the agent's contributions |
| 9. Uncertainty Handling Profile | How the agent engages with ambiguity and incomplete information |
| 10. Evolution Path | Review horizons and signals for the agent's own becoming |

---

## Generator: `scripts/new_agent.py`

A local Python CLI generator scaffolds new agent files from the template, filling placeholders deterministically.

### Requirements

Python 3.9+ (standard library only — no external dependencies).

### Usage

```bash
# Minimal (required fields only)
python scripts/new_agent.py \
  --name "Lineage Cartographer" \
  --role-type "Analytical" \
  --domain "lineage analysis"
# → writes agents/lineage_cartographer.md

# Full example
python scripts/new_agent.py \
  --name "Uncertainty Mediator" \
  --role-type "Mediating" \
  --domain "conflict resolution" \
  --capacities "Structured dialogue facilitation" "Tension mapping" "Dissent documentation" \
  --constraints "Does not adjudicate unilaterally" "Does not collapse held tensions into premature consensus" \
  --rituals "Council conflict mediation" "Audit cycle" \
  --interaction-style "Produces structured dialogue summaries with explicit tension maps." \
  --validate

# Preview without writing
python scripts/new_agent.py \
  --name "Archive Scout" \
  --role-type "Steward" \
  --domain "archive maintenance" \
  --dry-run

# Write to a custom path
python scripts/new_agent.py \
  --name "Epoch Herald" \
  --role-type "Ceremonial" \
  --domain "epoch transitions" \
  --output agents/epoch_herald.md
```

### Options

| Flag | Description |
|---|---|
| `--name` | Agent name (**required**) |
| `--role-type` | Role type (**required**) |
| `--domain` | Primary domain (**required**) |
| `--capacities` | Core capacities (space-separated; quote multi-word values) |
| `--constraints` | Operational constraints |
| `--rituals` | Ritual alignments |
| `--interaction-style` | Interaction style description |
| `--signature-output` | Signature output pattern |
| `--uncertainty-profile` | Uncertainty handling profile |
| `--evolution-path` | Evolution path description |
| `--initial-task` | First task for the agent |
| `--output` | Custom output path (default: `agents/<slug>.md`) |
| `--validate` | Validate the output file after writing |
| `--dry-run` | Print output without writing to disk |

---

## Validation

The generator includes a built-in validator (`--validate` flag) that checks:

- All ten required sections are present in the generated file.
- YAML frontmatter is present (file starts with `---`).

You can also invoke validation independently for an existing agent file:

```python
from scripts.new_agent import validate_agent_file
from pathlib import Path

errors = validate_agent_file(Path("agents/lineage_cartographer.md"))
if errors:
    for e in errors:
        print(e)
```

### Optional pre-commit validation

To validate all agent files automatically before every commit, add a pre-commit hook:

```bash
# .git/hooks/pre-commit (make executable: chmod +x .git/hooks/pre-commit)
#!/usr/bin/env bash
set -e
for f in agents/*.md; do
  [[ "$f" == "agents/agent_template.md" ]] && continue
  python scripts/new_agent.py --validate --output "$f" 2>/dev/null || \
    python -c "
from scripts.new_agent import validate_agent_file
from pathlib import Path
import sys
errors = validate_agent_file(Path('$f'))
if errors:
    print(f'Validation failed for $f:')
    [print(f'  - {e}') for e in errors]
    sys.exit(1)
"
done
```

---

## File structure

```
agents/
├── agent_template.md          # Canonical template — the @agent_template.md reference
├── <agent_slug>.md            # Generated agent files
└── example_lineage_cartographer.md   # Example generated agent
scripts/
└── new_agent.py               # Generator CLI
```

---

## After scaffolding

The generated file is a **starting shape**, not a finished definition. After scaffolding:

1. Open the file and expand the narrative sections (especially sections 2, 3, and 10).
2. Fill the **Uncertainty block** in section 9 with real, named unknowns.
3. Reference the **origin chronicle** or delta that prompted the agent's creation (section 2).
4. Optionally open a **Council deliberation** to ratify the agent's role and scope.
5. File a **chronicle entry** recording the agent's threshold crossing.

---

## Lineage

The agent template itself carries lineage. The template and this documentation were introduced as part of the `2026-04-10_delta_agent-templating-and-governance` delta. Any amendments to the template should be proposed as identity deltas and ratified through Council deliberation.

*See: [Agent templating delta](../docs/deltas/2026-04-10_delta_agent-templating-and-governance.md)*
