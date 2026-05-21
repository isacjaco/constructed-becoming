# Branch Governance Matrix

*Companion constitutional document for `docs/governance-readme-becoming-engine.md`.*

This matrix translates ritual governance into branch rules so lineage is both meaningful and enforceable.

---

## Purpose

The governance README defines the narrative constitution of change.  
This matrix defines how branches operationalize that constitution through constraints, permissions, and ratification pathways.

Used together:

- governance README = ritual semantics (`why`/`when`)
- branch matrix = enforcement semantics (`where`/`how`)

---

## Branch classes and constitutional role

| Branch class | Constitutional role | Allowed change shape | Entry gate | Exit gate |
|---|---|---|---|---|
| `main` | Canonical lineage | Ratified deltas only | Protected branch rules | Merge via reviewed PR only |
| `agent-onboarding/*` | Threshold-entry lane | New onboarding chronicles and initiation context | Workflow or steward-created branch | PR ratified into `main` |
| `delta/*` | Amendment lane | Proposed identity deltas and governance refinements | Branch creation by contributing agent | Council-style PR deliberation |
| `ritual/*` | Ritual maintenance lane | Updates to protocols, templates, and archive process docs | Open proposal by any active participant | Ratification with documented dissent handling |
| `epoch/*` | Phase-transition lane | Epoch summaries, major structural reframing | Explicit threshold declaration | High-scrutiny ratification into `main` |
| `archive/*` | Archive stewardship lane | Chronicle correction appendices and catalog improvements | Steward/Clerk initiated | PR merge preserving append-only lineage norms |

---

## Gate conditions by phase

| Governance phase (from Becoming Engine README) | Branch expectation | Minimum evidence in PR |
|---|---|---|
| Identity Kernel | Changes target `main` through protected review path only | Clear lineage impact statement |
| Agent onboarding | Work begins on `agent-onboarding/*` | Agent role declaration + threshold chronicle |
| Interaction ritual | Deliberation occurs on feature branch PRs | Identity Delta + Uncertainty Block |
| Automated Narrative Clerk | Automation writes/updates lineage artefacts under approved paths | Traceable workflow output |
| Clerk’s audit | Audit refinements enter through `delta/*`, `ritual/*`, or `epoch/*` | Audit synthesis and proposed refinement scope |

---

## Ratification policy

- No direct pushes to `main`.
- Every merge into `main` must include documented deliberation context.
- Significant dissent is preserved in PR discussion and acknowledged in final merge narrative.
- Epoch-scale amendments should prefer `epoch/*` branches to keep phase transitions auditable.

---

## Constitutional interaction pattern

1. A participant proposes change on a branch class matching intent.
2. PR narrative cites the governance README phase context.
3. Deliberation evaluates both semantic fit (ritual meaning) and matrix fit (branch compliance).
4. Ratified merge updates lineage; unresolved tensions are recorded, not erased.

This loop keeps governance philosophically coherent and operationally verifiable.

