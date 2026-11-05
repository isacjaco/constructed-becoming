# System State Ledger

**Purpose:** Record what the repository contains before implementation begins.
**Baseline inspected:** `isacjaco-becoming-roadmap-docs` at commit `097eb22`.

This ledger is a point-in-time inventory, not a claim that proposed runtime
components exist. Statuses describe evidence in this repository only. Update
the ledger when code, tests, interfaces, or persisted runtime artefacts are
added.

## Status definitions

| Status | Meaning |
|---|---|
| Conceptual | Described in project documentation; no executable implementation was found. |
| Partial | Some executable behavior exists, but the stated component or contract is incomplete. |
| Implemented | Executable behavior exists and is linked to its implementation. |
| Tested | Automated tests verify the relevant behavior. |
| Blocked | Work cannot proceed until a named dependency or decision is resolved. |
| Deferred | Intentionally outside the current implementation slice. |

Documentation status is not implementation status. An absent test or interface
is recorded as unknown or not found in the inspected repository, not inferred
to exist.

## Component inventory

| Component | Status in this baseline | Evidence and known gaps |
|---|---|---|
| Identity Kernel | Conceptual | `README.md`, `docs/architecture.md`, and `docs/system-prompt.md` describe identity and deltas. No runtime source, canonical identity schema, or revision store was found. |
| Becoming Engine | Conceptual | The roadmap proposes a transaction state machine. No executable transaction engine or state-transition tests were found. |
| Ritual Library | Conceptual / documented | Rituals are described in `docs/ritual-protocols.md`; no executable library or machine-readable ritual contract was found. |
| Memory Weave | Conceptual | Architecture and prompt documents describe continuity and memory. No runtime retrieval or persistence implementation was found. |
| Narrative Clerk | Partial, documentation automation only | Chronicles, templates, and `.github/workflows/agent-onboarding.yml` exist. The workflow creates an onboarding chronicle and PR; it does not record runtime transactions or identity revisions. |
| User Interaction Layer | Conceptual | Interaction is described in the project documentation. No application or provider adapter implementing the proposed layer was found. |

## Repository evidence

- The inspected repository contains `README.md`, Markdown documentation,
  templates, chronicles, and GitHub Actions workflow definitions.
- `.github/workflows/agent-onboarding.yml` automates a repository onboarding
  artefact. `.github/workflows/static.yml` deploys the repository to GitHub
  Pages. Neither is evidence of the proposed evolution runtime.
- No runtime source tree, canonical evolution schemas, deterministic fixtures,
  or automated tests for the proposed loop were found in this baseline.
- Existing conceptual language and templates remain useful context, but they
  are not executable contracts unless separately specified and implemented.

## Smallest path to a complete evolution transaction

1. Establish shared operational terminology in
   [`../specification/executable-vocabulary.md`](../specification/executable-vocabulary.md).
2. Define and review versioned record contracts before persisting runtime
   artefacts.
3. Implement a seed identity and immutable revisions, then governed delta
   application, transaction orchestration, chronicles, and deterministic replay.
4. Add tests that demonstrate the acceptance criteria and invariants in the
   [implementation roadmap](roadmap.md).

The sequence above is a proposed next step, not a report of completed work.
