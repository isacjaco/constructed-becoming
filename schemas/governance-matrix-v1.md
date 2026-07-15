# Governance matrix v1

**Status:** Reconciled readability refactor  
**Intent ref:** `INT-007-governance-matrix-refactor`  
**Scope:** Clarify responsibilities without changing operational meaning

---

## Interpretation

| Branch | Core responsibility | Reads from | Produces | Annotation | Example |
|---|---|---|---|---|---|
| Philosopher | Clarifies purpose, constraints, assumptions, and unresolved questions before change begins. | User intent, prior lineage, governing constraints | Clarification messages, framing assumptions, scope boundaries | This branch stabilises meaning before implementation diverges. | `MSG-401` frames the refactor as clarity-only, forbids semantic drift, and leaves no open questions. |

## Generation

| Branch | Core responsibility | Reads from | Produces | Annotation | Example |
|---|---|---|---|---|---|
| Architect | Translates interpreted intent into workstreams, coordination rules, and reconciliation guidance. | Clarification messages, active governance artifact, branch-level capacities | Work plans, dependency rules, arbitration guidance | The Architect may sponsor parallel approaches so long as schema stability is preserved. | `MSG-402` assigns section reordering to Implementer-01 and annotation enrichment to Implementer-02. |
| Implementer | Proposes concrete artifact changes that satisfy the current intent and declared constraints. | Architectural plan, target artifact, local context | Proposed deltas, revised artifact drafts | Multiple implementers may legitimately generate divergent deltas against the same artifact. | `LDS-0007` proposes reordering for readability, while `LDS-0008` proposes inline annotations without reordering. |

## Verification

| Branch | Core responsibility | Reads from | Produces | Annotation | Example |
|---|---|---|---|---|---|
| Verification Branch | Detects conflicts, checks schema stability, and escalates unresolved divergence. | Proposed deltas, target artifact, governing rules | Escalations, validation findings, reconciliation triggers | Verification arbitrates for coherence, not authorship ownership. | `MSG-403` flags the conflict between two deltas targeting `schemas/governance-matrix-v1.md` and recommends a non-disruptive baseline plus annotations. |

---

## Responsibility notes

- **Section order is part of schema stability in v1.** Readability improvements may enrich the existing layout, but they must not reorder top-level sections in this version.
- **Parallel deltas are permitted.** Divergence becomes a governance event when multiple changes target the same artifact in incompatible ways.
- **Arbitration follows stability precedence.** When readability and structural disruption conflict, the schema-stable interpretation wins for the current major version.
- **Examples are explanatory only.** They illustrate the branch role and must not alter the meaning of the matrix.

---

## Reconciled outcome

The reconciled v1 position keeps the original section order:

1. Interpretation
2. Generation
3. Verification

Under this baseline, the artifact may be clarified with inline annotations and examples, but structural reordering is deferred to a future major version.
