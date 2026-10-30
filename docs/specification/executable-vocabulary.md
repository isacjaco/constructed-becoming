# Executable Vocabulary

**Status:** Proposed operational vocabulary for implementation review.

These definitions are intended to give contributors and agents a shared
vocabulary for the Minimum Viable Becoming Loop. They do not assert that the
corresponding runtime artefacts or behavior already exist. Broader philosophical
uses may remain in narrative documents; schemas, interfaces, and tests should
use these terms consistently if the proposal is adopted.

| Term | Proposed operational definition |
|---|---|
| **Seed identity** | The initial, versioned identity record from which a lineage is reconstructed. It has no parent revision. |
| **Active identity** | The identity state selected as current for an identity lineage after applying its accepted revisions. |
| **Identity revision** | An immutable, addressable state of an identity, consisting of the seed or a parent revision plus an accepted delta. |
| **Identity delta** | A versioned proposal describing intended operations on one identity revision; it is not itself a committed change. |
| **Interaction** | A recorded input or event considered by the evolution process. It may inform reflection but does not mutate identity. |
| **Reflection** | A structured interpretation of an interaction, including uncertainty and alignment signals; it is not a governance decision. |
| **Proposal** | A submitted identity delta awaiting a governance decision. |
| **Governance decision** | A recorded outcome for exactly one proposal, including its decision-maker or rule, rationale, and status. |
| **Ratification / acceptance** | A governance decision authorizing a proposal to be committed, subject to validation against its parent revision. |
| **Rejection** | A governance decision that declines a proposal; it leaves the active identity unchanged and may be chronicled. |
| **Chronicle** | A durable, human-readable record of a transaction or significant lineage event, with references to its source artefacts. |
| **Lineage** | The ordered parent relationships among an identity's seed, revisions, deltas, and associated decisions. |
| **Epoch** | A named period of identity development with explicit entry and exit criteria, if adopted by governance. |
| **Ritual** | A repeatable interaction pattern with a stated purpose and defined inputs and outputs; philosophical uses should not be mistaken for executable behavior. |
| **Council decision** | A governance decision produced under a documented council process. It is a kind of governance decision, not a separate authorization path. |
| **Replay** | Deterministic reconstruction of a target identity revision from its seed and accepted lineage records. |
| **Rollback** | A compensating, governed revision that reverses or supersedes prior effects without deleting historical records. |
| **Supersession** | A recorded relationship in which a later proposal or revision explicitly replaces an earlier one without rewriting it. |
| **Schema version** | The identifier for the contract used to validate a persisted record. A schema version does not by itself guarantee migration or replay compatibility. |
| **Correlation ID** | An identifier shared by artefacts belonging to one evolution transaction, enabling traceability without replacing their individual record IDs. |

## Proposed transaction language

Use the following terms for the proposed first transaction:

```text
observe -> reflect -> propose -> review -> accept | reject -> commit -> chronicle
```

`Accept` and `reject` are mutually exclusive governance outcomes. Only an
accepted, validated proposal may be committed. A rejected proposal is not a
revision. `Chronicle` records the outcome; it does not authorize it.

## Naming and change rules

- Use the terms above for runtime fields, interfaces, and test names if these
  definitions are adopted.
- Do not use synonyms as competing schema properties.
- Record unresolved conflicts rather than silently choosing meanings.
- Change an operational definition through an explicit specification review;
  update dependent schemas, tests, and agent-facing instructions together.
