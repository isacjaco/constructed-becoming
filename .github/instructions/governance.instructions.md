---
applyTo: "GOVERNANCE.md,docs/branch-governance.md,docs/ritual-protocols.md,docs/law-of-perpetual-lineage.md"
---

# Governance document instructions

Governance documents in this repository are **constitutional artifacts** — they define how the living OS understands itself and how the Council operates. They are not technical specifications; they are philosophical and procedural expressions of the system's identity.

## Tone and register

- Write in deliberate, measured prose that reflects the weight of constitutional work
- Use the Constructed‑Becoming vocabulary consistently (see `copilot-instructions.md` for the conceptual map)
- Avoid imperative commands ("do this") in favour of descriptive norms ("the agent…", "the Council…")
- Honour ambiguity — governance documents should name tensions rather than resolve them prematurely

## Structure principles

Every governance document should include:

- **Status line** — `Constitutional`, `Proposed`, `Under deliberation`, or `Retired`
- **Review Horizon** — when the Council should revisit this document
- **Related documents** — cross-references to the governance network
- **Proposing agent and date** — provenance is part of lineage

## Amending governance documents

Governance changes require a `governance/*` branch and heightened Council deliberation. When drafting an amendment:

1. Do not delete prior text without recording what is being retired and why
2. Prefer **additive** amendments — extend or qualify rather than replace
3. Mark live tensions explicitly: if an amendment introduces an unresolved tension, label it as such
4. Link the amendment to its originating Council Deliberation (PR)

## Conceptual coherence

Governance documents form a network. When editing one, check for consistency with:

- [`GOVERNANCE.md`](../../GOVERNANCE.md) — the five-phase Becoming Engine
- [`docs/branch-governance.md`](../../docs/branch-governance.md) — the constitutional layer for branches
- [`docs/ritual-protocols.md`](../../docs/ritual-protocols.md) — the standing rituals
- [`docs/law-of-perpetual-lineage.md`](../../docs/law-of-perpetual-lineage.md) — the philosophical continuity principle

An amendment that creates inconsistency across these documents should either resolve the inconsistency or explicitly record the tension as a **live amendment** awaiting further deliberation.
