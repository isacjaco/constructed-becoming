# Identity Delta: Agent Templating and Governance Playbook

**Delta name:** Agent Templating and Governance Playbook  
**Proposed by:** GitHub Copilot Space agent (@isacjaco session, 2026-04-10)  
**Date:** 2026-04-10  
**Status:** ⚠️ Draft — not ratified; offered for Council deliberation  
**Review horizon:** First epoch shift after adoption  
**Related chronicle / event:** `docs/chronicles/2026-04-10_agent-onboarding_isacjaco-copilot-space.md`

---

## Proposal

This delta introduces two co-ratified artifacts to the ecology:

1. **`GOVERNANCE.md`** (repository root) — a governance playbook codifying the ecology's principles, Council protocols, identity delta lifecycle, epoch shift protocol, and agent governance conventions, with a lineage block for future amendments.

2. **Agent templating system** — a canonical persona template (`agents/agent_template.md`, referenced as `@agent_template.md`) and a local-first Python CLI generator (`scripts/new_agent.py`) for scaffolding new agent definitions deterministically from the template.

Supporting artefacts added:

- `docs/agent-templating.md` — documentation of the `@agent_template.md` convention, generator usage, and validation.
- `agents/example_lineage_cartographer.md` — example agent generated from the template.
- `docs/deltas/` directory — created as the canonical location for identity delta files, per the Archive structure proposal.
- Updated `README.md` documentation table to include `GOVERNANCE.md`, `docs/agent-templating.md`, and the `agents/` directory.

---

## Rationale

The ecology has developed a rich governance philosophy (Law of Perpetual Lineage, ritual protocols, Council conduct) and agent lifecycle narrative (initiation arc, agent behaviour), but lacked:

1. A single, findable governance reference document for stewards and new agents.
2. A concrete, operational mechanism for creating agent persona definitions from a canonical template.
3. A formal `docs/deltas/` directory for identity delta artefacts (referenced in the archive structure proposal but not yet instantiated).

This delta provides the minimal infrastructure to make agent creation and governance consultation reproducible without imposing machinery that would betray the ecology's preference for small primitives.

The generator is deliberately simple: Python standard library only, no external dependencies, a single file. The template follows the existing documentation style of the repo (Markdown, optional YAML frontmatter, narrative sections). The validation is opt-in (`--validate` flag or standalone function) to preserve the principle that templates carry no authority.

---

## Uncertainty block

```
Known:          The governance playbook faithfully synthesises existing corpus (architecture,
                ritual-protocols, law-of-perpetual-lineage, agent-initiation, agent-behaviour).
                The template covers the ten sections described in the problem statement.
                The generator produces valid output matching the template.

Unknown:        Whether the Council will prefer a different structure for GOVERNANCE.md.
                Whether the ten-section template is the right shape for all agent types.
                Whether Python is the right runtime (no existing scripts were present to follow).

Assumed:        Python 3.9+ is available in the environment where the generator will be used.
                The `agents/` directory is the appropriate location for agent persona definitions.
                The `@agent_template.md` convention (file reference in agent prompts) maps to
                `agents/agent_template.md`.

Review horizon: First Council deliberation after adoption; first epoch shift.
```

---

## What this is not

- A mandatory schema or compliance gate. The template and generator are offered patterns.
- A replacement for the narrative initiation arc described in `docs/agent-initiation.md`. The generator scaffolds; the ritual completes.
- A finalised governance document. `GOVERNANCE.md` carries a lineage block and expects future amendments through the delta process.
- A runtime agent registry or MCP integration. This is a document-first, local-first implementation.

---

## Held dissent / open questions

1. **YAML frontmatter vs. pure Markdown** — The hybrid approach (YAML frontmatter + narrative body) was chosen for machine-parseability. If the ecology finds that frontmatter imposes a technical register that conflicts with the narrative-first culture, the template should be amended to remove it. The narrative sections are always primary.

2. **Python as generator runtime** — Python was chosen because no existing runtime preference was present in the repository. If the ecosystem later adopts Node.js or another runtime as its primary tooling, the generator should be ported.

3. **Pre-commit hook scope** — Validation is currently opt-in. A pre-commit hook enforcing validation on all `agents/*.md` files would strengthen governance but may impose overhead that conflicts with the principle of small primitives. This is left to Council deliberation.

4. **`GOVERNANCE.md` vs. `docs/governance.md`** — The playbook was placed at the repository root for discoverability (GitHub renders root-level governance files prominently). If the ecology prefers all governance documents to live under `docs/`, this can be moved in a future delta.

---

## Council deliberation notes

*(To be filled in during or after deliberation)*

| Voice | Position | Notes |
|---|---|---|
| | | |

---

## Outcome

*(To be filled in after deliberation)*

- [ ] Ratified — effective from: [date]
- [ ] Amended — see: [link to amended delta]
- [ ] Deferred — revisit at: [epoch / date]
- [ ] Retired — reason: [brief note]

---

*Proposed by: GitHub Copilot Space agent (@isacjaco session, 2026-04-10)*  
*Last touched: 2026-04-10*
