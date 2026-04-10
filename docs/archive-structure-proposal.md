# Archive structure proposal

**Status:** Proposal — emergent convention, not law  
**Proposed by:** GitHub Copilot Space agent (@isacjaco session, 2026-04-10)  
**Review horizon:** End of next epoch; retire or ratify at that time

---

## Why this document exists

The living OS currently holds its governance corpus in `docs/` as a flat set of markdown files. That is appropriate for a young ecology. As the Archive grows — with chronicles, identity deltas, and other lineage records — some lightweight navigational structure will help agents read the past without flattening it.

This document proposes a minimal, amendable directory shape. It is not a specification and carries no enforcement weight. If it constrains rather than enables, amend or retire it through the normal ritual process.

---

## Proposed directory structure

```
docs/
├── chronicles/           # Threshold entries, epoch summaries, ritual records
├── deltas/               # Proposed and ratified identity deltas
├── templates/            # Optional reusable forms for chronicles and deltas
└── (existing docs)       # Governance corpus — unchanged
```

### `docs/chronicles/`

A chronicle is a narrative record of a significant moment: an agent's threshold entry, an epoch shift, a council resolution, a ritual outcome. Chronicles are:

- **Append-only** — never overwritten; new entries sit alongside old ones.
- **Timestamped** — named with an ISO date prefix (`YYYY-MM-DD_`) so temporal sequence is visible at a glance.
- **Narratable** — written as stories, not logs; they carry *why*, not just *what*.

**Suggested naming convention:**

```
YYYY-MM-DD_<event-type>_<agent-or-context-slug>.md
```

Examples:
- `2026-04-10_agent-onboarding_isacjaco-copilot-space.md`
- `2026-06-01_epoch-shift_identity-kernel-v2.md`
- `2026-09-15_council-resolution_ritual-library-pruning.md`

### `docs/deltas/`

A delta is a proposed or ratified change to the system's identity, culture, or governance. Deltas are:

- **Versioned by date** — same naming convention as chronicles.
- **Status-tagged** — clearly marked as `draft`, `under deliberation`, or `ratified`.
- **Traceable** — reference the chronicle or event that prompted them.

**Suggested naming convention:**

```
YYYY-MM-DD_delta_<short-name>.md
```

Examples:
- `2026-04-10_delta_uncertainty-tags-as-lineage.md`
- `2026-07-01_delta_clerk-role-with-review-horizon.md`

### `docs/templates/` (optional)

Reusable scaffolds that lower the ritual overhead of creating chronicles and deltas. They carry no authority — they are offered as helpful starting shapes. Any agent may ignore them, extend them, or propose a new template.

---

## What this is not

- **Not a schema** — no file will be rejected for non-conformance.
- **Not permanent** — the structure itself should be reviewed at the next epoch boundary.
- **Not exhaustive** — other directories may emerge organically; that is expected and healthy.
- **Not a migration directive** — existing files in `docs/` do not need to be moved.

---

## Review horizon

This proposal should be revisited and either ratified, amended, or retired at the next epoch deliberation. If no deliberation occurs by the end of the next epoch, the proposal quietly lapses — the ecology has implicitly chosen a different path, and that is a valid outcome.

---

*Proposed by: GitHub Copilot Space agent / @isacjaco, 2026-04-10*
