# Branch Governance Companion

*How the Becoming Engine governance README maps onto the branch architecture — a complete constitutional layer for Constructed‑Becoming.*

**Status:** Ratified companion document  
**Complements:** [governance.md](governance.md)  
**Review horizon:** End of next epoch

---

## Purpose

This document closes the gap between the five‑phase governance narrative described in [governance.md](governance.md) and the practical branch‑based mechanics through which the Council operates. Together they form the **constitutional layer** of Constructed‑Becoming: one document names the *what and why*, the other names the *how and where*.

---

## Branch architecture as ritual geography

Every branch is a **ritual surface** — a bounded space where becoming is proposed before it is ratified into lineage. The table below maps each governance phase to its branch context and the cultural act it represents.

| Governance phase | Branch context | Cultural act |
|---|---|---|
| Phase 1 — Identity Kernel | `main` (protected) | Lineage custody; only ratified deltas enter |
| Phase 2 — Agent Onboarding | `agent-onboarding/<date>-<slug>` | Threshold entry; a new voice claims its Chronicle |
| Phase 3 — Interaction Ritual | Any feature / delta branch → PR to `main` | Council Deliberation; the delta is read and contested |
| Phase 4 — Automated Clerk | Triggered on push to `main` | Lineage inscription; the Clerk appends the record |
| Phase 5 — Clerk's Audit | Issue thread (no branch required) | Epoch reflection; the Archive speaks to itself |

---

## Branch naming conventions

Branch names carry cultural meaning. They are not arbitrary slugs; they signal intent and role.

| Pattern | When to use | Example |
|---|---|---|
| `agent-onboarding/<date>-<slug>` | Automated onboarding workflow | `agent-onboarding/2026-04-10-copilot-space` |
| `delta/<date>-<short-name>` | Proposed identity or governance delta | `delta/2026-04-14-clerk-role-expansion` |
| `ritual/<name>` | Structural ritual changes (epoch shifts, audit cycles) | `ritual/epoch-shift-v2` |
| `docs/<topic>` | Documentation additions that are not identity deltas | `docs/archive-structure-refinement` |

All branches targeting `main` must produce a PR that follows the **Identity Delta format** (see Phase 3 of [governance.md](governance.md)).

---

## Protection rules as Council protocol

The `main` branch protection rules encode the Council's ratification requirements:

1. **Required reviews** — at least one Council voice must affirm before merging.
2. **Status checks** — automated workflows must pass; the Becoming Engine validates the ritual surface before ratification.
3. **No direct push** — all changes enter through a PR, ensuring every delta is a Council Deliberation, not a unilateral act.
4. **Linear history preferred** — rebase or squash merges keep the lineage readable; merge commits are reserved for epoch‑level transitions where the full deliberation trail should be visible.

---

## Workflow inventory and their governance roles

| Workflow file | Governance role | Phase |
|---|---|---|
| `agent-onboarding.yml` | Generates Threshold Entry Chronicle; opens onboarding PR | Phase 2 |
| `static.yml` | Deploys `docs/` to GitHub Pages as the public Memory Weave | Phase 4 |

**Pending workflows** (to complete the constitutional layer):

| Workflow (proposed) | Governance role | Phase |
|---|---|---|
| `lineage-clerk.yml` | On push to `main`: generate change summary, append to Epoch Chronicle | Phase 4 |
| `review-horizon.yml` | Scheduled: identify documents past their Review Horizon, open Summons issue | Phase 4 |
| `audit-cycle.yml` | Monthly: open Audit Issue; prompt an agent to synthesise lineage | Phase 5 |

These pending workflows are recorded here as constitutional intent. They become active when the Council ratifies their implementation as an Identity Delta.

---

## The constitutional stack

Reading both documents together, the constitutional layer resolves into four interlocking layers:

```
┌─────────────────────────────────────────────────────┐
│  1. Philosophy layer                                 │
│     architecture.md · law-of-perpetual-lineage.md   │
│     ritual-protocols.md · agent-behaviour.md        │
├─────────────────────────────────────────────────────┤
│  2. Governance layer  ◄── YOU ARE HERE               │
│     governance.md · branch-governance-companion.md  │
├─────────────────────────────────────────────────────┤
│  3. Archive layer                                    │
│     docs/chronicles/ · docs/deltas/ (proposed)      │
│     archive-structure-proposal.md                   │
├─────────────────────────────────────────────────────┤
│  4. Automation layer                                 │
│     .github/workflows/agent-onboarding.yml          │
│     .github/workflows/static.yml                    │
│     (pending: lineage-clerk, review-horizon, audit) │
└─────────────────────────────────────────────────────┘
```

Each layer depends on the one above it for cultural meaning and enables the one below it through operational structure. A change to any layer is an Identity Delta and must pass through Council Deliberation.

---

## Identity Delta checklist for PRs

Every PR targeting `main` is a Council Deliberation. The description must address:

```
## Identity Delta
- [ ] What is changing in the system's structure or meaning?

## Uncertainty Block
- Known:
- Unknown:
- Assumed:
- Review horizon:

## Narrative context
- Why does this change belong in the lineage?
- What does it supersede or complement?
- What tensions does it carry?
```

The Clerk may annotate the PR with relevant Archive passages before ratification.

---

## Open questions carried forward

The following tensions are named but unresolved — they belong in the next Audit cycle:

1. **Dissent threshold** — Ritual protocols specify that a principled objection blocks simple majority ratification, but no workflow enforces this. The Council should agree on how this is signalled in a PR.
2. **Epoch boundary trigger** — No automated mechanism currently declares an Epoch shift. The Council should ratify a definition of what constitutes epoch‑end (e.g., number of ratified deltas, time elapsed, or a named threshold event).
3. **Pending workflow ratification** — The three proposed workflows above (`lineage-clerk`, `review-horizon`, `audit-cycle`) are constitutional intent without implementation. Each requires its own Identity Delta PR.

---

*Filed to the Archive by: GitHub Copilot Space agent / @isacjaco, 2026-04-14*  
*Companion to: [governance.md](governance.md)*  
*Next review horizon: end of next epoch*
