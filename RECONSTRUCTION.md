# Reconstruction

Goal: an unrelated third party should be able to rebuild Constructed‑Becoming from this repository alone. If a step below cannot be followed from the files listed, a dependency is undocumented and should be recorded as a gap.

## Core files required

- `README.md`
- `docs/core-definitions.md`
- `docs/architecture.md`
- `docs/law-of-perpetual-lineage.md`
- `docs/agent-initiation.md`
- `docs/ritual-protocols.md`
- `docs/templates/`
- `schemas/`

## Core concepts required

Identity, Becoming, Lineage, Node, Chain, Chronicle, Evidence, Transition, as defined in `docs/core-definitions.md`.

## Bootstrap sequence

1. Read `README.md`, then `docs/core-definitions.md`.
2. Read `docs/architecture.md` and `docs/law-of-perpetual-lineage.md`.
3. Create the directory layout: `docs/`, `docs/chronicles/`, `docs/templates/`, `schemas/`.
4. Copy the templates from `docs/templates/`.

## Lineage sequence

1. Record a seed identity as the first node.
2. Mark each change with a transition ritual (`docs/ritual-protocols.md`).
3. Write a chronicle from `docs/templates/chronicle-template.md` for each transition.
4. Link the new node to its predecessor.

## Validation sequence

1. Every node validates against `schemas/NODE.schema.json`.
2. Every chain validates against `schemas/CHAIN.schema.json`.
3. Every lineage validates against `schemas/LINEAGE.schema.json`.
4. Every transition has at least one chronicle as evidence.

The schemas are currently empty skeletons, so steps 1–3 are not yet enforceable.

## Acceptance criteria

Reconstruction is ready to pass when an independent reader can:

1. Follow the README links to every referenced document from a clean checkout.
2. Identify which terms are established and which are proposed without inferring fields the repository does not specify.
3. Rebuild the documented directory layout and follow the bootstrap and lineage sequences using only repository files.
4. Trace each transition from its predecessor to its successor, in order, without dangling or duplicated node references.
5. Locate at least one extant chronicle or other cited artefact as evidence for each transition, and confirm the evidence refers to that transition.
6. Validate node, chain, and lineage records against the schemas once their fields and relationship rules have been formalised.

The first three criteria can be checked against the current documentation. Criteria 4–6 require a formal record shape and cannot be considered passed until the schema definitions and corresponding validation tests exist. The current schema placeholders intentionally impose no record fields.

## Known gaps

- Node, Chain, and Evidence are proposed terms with no field-level specification.
- No automated validation exists yet.
