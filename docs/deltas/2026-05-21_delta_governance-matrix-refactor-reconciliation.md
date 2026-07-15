# Governance matrix refactor reconciliation

**Delta name:** Governance matrix readability reconciliation  
**Proposed by:** Architect-01 / Implementer-02  
**Date:** 2026-05-21  
**Status:** Ratified through arbitration baseline  
**Review horizon:** Next MAJOR governance-matrix version  
**Related chronicle / event:** `EX-007-divergent-parallel-deltas-with-conflict-arbitration`

---

## Proposal

Preserve the existing section order of `schemas/governance-matrix-v1.md` and improve readability only through inline annotations, grouped notes, and examples.

This reconciles two parallel deltas that targeted the same artifact:

- `LDS-0007` — reorder sections and grouped responsibilities for readability
- `LDS-0008` — add inline annotations and examples without reordering

---

## Rationale

The governance matrix refactor was explicitly scoped to clarity without semantic change. Because `LDS-0007` would alter operational placement by reordering top-level sections, it created a stability conflict with the existing v1 structure. `LDS-0008` improved comprehension without changing ordering, so it became the safer baseline under the arbitration rule of **schema stability precedence**.

The reconciled lineage therefore adopts annotation enrichment and defers structural reordering to a future MAJOR version.

---

## Uncertainty block

```text
Known:          the original intent forbids semantic and schema-breaking changes
Known:          both divergent deltas targeted the same artifact
Known:          arbitration selected the non-disruptive baseline and allowed annotations
Unknown:        whether a future MAJOR version should adopt a reordered governance matrix
Assumed:        examples and annotations do not alter the matrix's operational meaning
Review horizon: next MAJOR governance-matrix version
```

---

## Divergent lineage

### Message lineage

| ID | Phase | Summary |
|---|---|---|
| `MSG-401` | Interpretation | Clarifies that the refactor is for clarity only, with no new branches, semantic changes, or schema-breaking changes. |
| `MSG-402` | Generation | Splits work into parallel strategies: section reordering and annotation enrichment. |
| `MSG-403` | Verification | Escalates the conflict and proposes preserving a non-disruptive structural baseline before layering annotations. |
| `MSG-404` | Generation | Arbitrates the outcome: no reordering in v1, annotations allowed, structural change deferred to a future MAJOR version. |

### Delta lineage

| Delta | Agent | Status | Summary |
|---|---|---|---|
| `LDS-0007` | Implementer-01 | Superseded in part | Reordered Interpretation, Generation, and Verification sections for readability. |
| `LDS-0008` | Implementer-02 | Baseline parent | Added explanatory notes and examples under each branch without reordering. |
| `LDS-0009` | Implementer-02 | Reconciled | Refined annotations and examples while confirming that the original section order remained unchanged. |

---

## What this is not

- Not a new governance branch
- Not a semantic rewrite of branch responsibilities
- Not a schema migration for v1
- Not a rejection of future structural change in a MAJOR version

---

## Held dissent / open questions

- The readability gains proposed by `LDS-0007` may still be valuable, but they require a versioned structural change rather than a clarity-only refactor.
- A future MAJOR version should explicitly evaluate whether section ordering is normative structure or presentation detail.

---

## Outcome

- [x] Ratified — effective from: 2026-05-21
- [ ] Amended — see: 
- [ ] Deferred — revisit at: 
- [ ] Retired — reason: 

---

*Ratified from `LDS-0008` as the reconciled parent lineage.*  
*Reconciled delta:* `LDS-0009` — “Finalize governance matrix annotations without structural reordering.”  
*Rationale:* Apply enrichment strategy under arbitration while preserving schema stability.
