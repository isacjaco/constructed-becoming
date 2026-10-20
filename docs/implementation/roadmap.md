# Roadmap: Unblock Constructed-Becoming with a Minimum Viable Evolution Loop

**Status:** Draft / request for comments
**Change type:** Architecture, governance, and implementation roadmap

> This document proposes a roadmap. Its schemas, interfaces, sequencing, and acceptance criteria are implementation decisions for review—not claims about the repository's current code. Adapt proposed paths and contracts to the repository's implementation language and conventions.

## Summary

Move Constructed-Becoming from a concept-rich framework towards an executable, testable evolution system by proving one complete, deterministic transaction before expanding the system. The framework describes six architectural components: Identity Kernel, Becoming Engine, Ritual Library, Memory Weave, Narrative Clerk, and User Interaction Layer. It also calls for transformations to be logged, contextualised, narratively meaningful, and reversible.

The proposed **Minimum Viable Becoming Loop** loads an identity, receives an interaction, reflects, proposes an identity delta, obtains a governance decision, commits an accepted change, writes a chronicle, and reconstructs and audits the resulting lineage. The first vertical slice is complete only when an accepted delta changes the active identity, creates an immutable audit record, and can be replayed from the seed identity.

```text
Identity Kernel -> Interaction -> Reflection -> Delta Proposal
    -> Governance Decision -> Committed Identity Revision
    -> Chronicle Entry -> Lineage Replay
```

## Motivation and problem statement

The dialogue analysis identifies recurring obstacles: foundational concept misalignment, repeated clarification, inefficient communication, missing signals for confusion or deviation, and framework-translation fatigue. It recommends shared vocabulary, modular interactions with explicit inputs and outputs, defined success criteria, meta-communication signals, small calibration tests, and records of recurring misunderstandings.

The framework's design principles point in the same direction: make evolution deliberate; keep identity deltas and epoch shifts traceable; preserve meaningful events in chronicles; use governance to maintain continuity; and provide historical and contextual coherence through memory. Without a canonical execution path, modules could be implemented independently without demonstrating a full act of becoming. This roadmap therefore proposes one canonical transaction, a minimum set of persisted artefacts, a governance path, an audit/replay path, an ordered backlog, and gates between implementation phases.

## Priority model

| Priority | Meaning | Sequencing rule |
|---|---|---|
| P0 | Required to restart executable system evolution | Complete before feature expansion |
| P1 | Required for continuity, safety, and repeatability | Begins after the P0 loop works |
| P2 | Required for collaboration and broader agent participation | Begins after single-agent lineage is reliable |
| P3 | Exploratory or ecosystem expansion | Begins only after governance and replay are stable |

## Prioritised implementation roadmap

### P0 — Minimum Viable Becoming Loop

**Recommended starting sequence:** Begin implementation with P0.1, then complete P0.2 in series with it. The state ledger establishes what exists and what remains unknown; the executable vocabulary can then use that inventory to resolve terminology consistently before schema and runtime work begins.

#### P0.1 — Establish the repository state ledger

Proposed deliverable: `docs/implementation/system-state-ledger.md`.

Inventory what is conceptual, specified, partially implemented, implemented, tested, blocked, or intentionally deferred. Include each component's status, source of truth, implemented interfaces, persisted artefacts, tests, dependencies, known gaps, and next gate. Cover the Identity Kernel, Becoming Engine, Ritual Library, Memory Weave, Narrative Clerk, and User Interaction Layer.

**Acceptance criteria:** Every component has one entry; documentation is distinguished from executable implementation; implemented components link to code and tests; unknowns remain explicitly unknown; and the ledger identifies the smallest path to a complete evolution transaction.

**Exit gate:** One document answers what exists, what is only described, and what must be built next.

#### P0.2 — Freeze and publish the executable vocabulary

Proposed deliverable: `docs/specification/executable-vocabulary.md`. Define operational meanings for seed identity, active identity, identity revision, identity delta, reflection, proposal, ratification, rejection, chronicle, lineage, epoch, ritual, council decision, replay, rollback, and supersession.

Each term has one operational definition. Synonyms may be documented but must not become competing schema fields. Runtime terminology changes require an explicit amendment. Broader philosophical meanings may remain, but must be distinguished from runtime definitions.

**Acceptance criteria:** Runtime terms are unambiguous; each term identifies the artefacts or interfaces where it appears; conflicts are resolved or marked unresolved; schema properties and test names use normative vocabulary.

**Exit gate:** Two independent contributors can describe the same transaction without translating between competing terms.

#### P0.3 — Define versioned canonical schemas

Proposed schemas: `schemas/identity.schema.json`, `interaction.schema.json`, `reflection.schema.json`, `identity-delta.schema.json`, `governance-decision.schema.json`, `chronicle-entry.schema.json`, and `epoch.schema.json`.

Persisted records share `schema_version`, `record_id`, `created_at`, `created_by`, `lineage_parent`, and `correlation_id` as applicable. An identity delta includes `schema_version` (initially proposed as `"0.1"`), `delta_id`, `identity_id`, `parent_revision`, `proposed_by`, `trigger`, `summary`, `rationale`, `operations`, `expected_effects`, `constraints_checked`, `governance_status` (initially `proposed`), and `created_at`. Proposed governance states are `proposed`, `under_review`, `accepted`, `rejected`, `superseded`, and `reverted`.

**Acceptance criteria:** Every persisted artefact declares a schema version; each delta identifies its parent revision; each decision references exactly one proposal; accepted deltas cannot be silently edited; invalid transitions return structured errors; valid and invalid fixtures exist for each schema.

**Exit gate:** Contracts are stable and reviewable independently of any model or orchestration provider.

#### P0.4 — Implement the Identity Kernel

Required capabilities: initialise a seed identity; retrieve active and historical revisions; validate a delta against its parent; apply an accepted delta; reject an unratified delta; and reconstruct a revision from the seed and accepted deltas.

Proposed interface: `initialiseIdentity(seed)`, `getActiveIdentity(identityId)`, `getIdentityRevision(identityId, revision)`, `validateDelta(delta)`, `applyAcceptedDelta(delta, decision)`, and `replayLineage(identityId, revision)`.

**Acceptance criteria:** A seed can be created and retrieved; an accepted delta creates a new revision while preserving the previous one; an unaccepted delta cannot mutate the active identity; a wrong-parent delta is rejected; replay matches the stored canonical state; reapplying the same accepted delta is idempotent.

**Exit gate:** Identity can change intentionally without destroying prior state.

#### P0.5 — Implement the Becoming Engine as a state machine

Canonical transaction: `observe -> reflect -> propose -> review -> accept | reject -> commit -> chronicle`.

Require explicit transitions, no mutation before acceptance, correlation across transaction artefacts, deterministic validation, recoverable failure states, and structured rejection reasons.

**Acceptance criteria:** The complete state machine is represented in code; unsupported transitions fail explicitly; rejection leaves identity unchanged; an accepted proposal invokes the Identity Kernel exactly once; every terminal transaction has an audit result; interrupted transactions remain inspectable and cannot be mistaken for committed changes.

**Exit gate:** One governed transition can run from interaction to identity revision.

#### P0.6 — Make the Narrative Clerk mandatory

Chronicle production is part of transaction completion, not an optional afterthought. A proposed chronicle contains `chronicle_id`, `transaction_id`, `identity_id`, `event_type`, `observation`, `reflection_summary`, `proposal_summary`, `decision`, `decision_rationale`, `revision_before`, `revision_after`, and `recorded_at`.

Chronicles record accepted and rejected deltas, distinguish proposals from committed revisions, reference source artefacts, and preserve readable narrative alongside structured metadata.

**Acceptance criteria:** Every completed transaction has a chronicle; facts are distinguished from interpretation; accepted changes link before/after revisions; rejection explains why no revision was created; the chronicle is readable without model-private reasoning; chronicle-generation failure is visible and recoverable.

**Exit gate:** No meaningful act of becoming occurs without entering the living archive.

#### P0.7 — Add explicit meta-communication signals

Persist reflection signals for `understanding.status` (`confirmed`, `partial`, `uncertain`) and `unresolved_terms`; `framework_alignment.status` (`aligned`, `drifting`, `unknown`) and `notes`; `identity_impact.level` (`none`, `minor`, `major`, `unknown`) and `rationale`; and `recommended_action.type` (`observe`, `clarify`, `propose_delta`, `request_governance`).

Uncertain understanding cannot silently become a major identity delta. Unknown alignment triggers clarification or review. Signals inform governance but do not authorise mutation.

**Acceptance criteria:** Every reflection includes understanding status; unresolved terms can surface before proposal; major-impact proposals require confirmed or explicitly reviewed understanding; tests cover disagreement between confidence and governance outcome; signals appear in chronicles.

**Exit gate:** The system can express uncertainty before it becomes lineage.

#### P0.8 — Prove the loop with deterministic fixtures

Minimum scenarios: no-change interaction (no delta); accepted minor delta (revision and chronicle); rejected delta (identity unchanged and rejection chronicled); stale-parent delta (commit rejected); duplicate commit (no duplicate revision); replay (seed plus accepted deltas reproduces active state); and rollback or compensating revision (reversal through a new governed record, preserving history).

**Acceptance criteria:** Tests need no live language-model service; fixtures are stable and reviewable; failures identify the violated invariant; the full loop runs in CI; replay is checked automatically.

**P0 completion gate:** A deterministic interaction moves from seed identity to accepted revision, creates a chronicle, and replays to the same state.

### P1 — Continuity, recovery, and observability

#### P1.1 — Implement the Memory Weave

Retrieve relevant identity revisions and chronicles, preserve lineage relationships, expose provenance, and separate durable lineage from transient interaction context.

**Acceptance criteria:** Every retrieved item identifies its source; identity-affecting decisions trace to records; retrieval does not mutate identity; removing transient context does not remove lineage; replay does not depend on probabilistic retrieval.

#### P1.2 — Introduce epoch manifests

Proposed fields: `epoch_id`, `name`, `purpose`, `entry_criteria`, `permitted_changes`, `required_invariants`, `exit_criteria`, `opening_revision`, `closing_revision`, and `status`.

**Acceptance criteria:** The active epoch is explicit; entry/exit criteria are machine-readable where practical; a closed epoch references its final revision; epoch transitions are chronicled; major changes can require an epoch-shift decision.

#### P1.3 — Create an evolution status report

Prefer a generated repository artefact, `generated/evolution-status.md`, before a graphical dashboard. Include active identity revision and epoch, proposed deltas, accepted/rejected decisions, incomplete transactions, replay status, schema versions, and last successful conformance run.

**Acceptance criteria:** Generated from persisted state and not a competing source of truth; broken lineage is prominent; reproducible locally and in CI.

#### P1.4 — Add migration and compatibility policy

Version schema changes, make migrations explicit, keep old chronicles readable, report incompatible replay records, and require an epoch-level decision for breaking changes.

**Acceptance criteria:** At least one migration fixture; record identifiers and lineage references survive migration; compatibility failures do not silently drop records; supported schema versions are documented.

### P2 — Governance and participation

#### P2.1 — Implement a minimal Council Protocol

Initial scope: proposal submission; named participants or roles; recorded positions; a decision rule; final decision; dissent or unresolved concerns; and chronicle output.

**Acceptance criteria:** A decision references one proposal; participant roles are explicit; the decision rule is recorded before the outcome; dissent can be preserved without blocking the historical record; the outcome maps to a valid governance state.

#### P2.2 — Automate the Initiation Arc

Proposed sequence: introduce identity; record arrival; assign initial role and constraints; connect lineage; complete a first guided ritual.

**Acceptance criteria:** An initiated participant has role and constraints; arrival is chronicled; lineage integration is explicit; the first ritual is associated with the participant; partial initiation can be resumed or safely abandoned.

#### P2.3 — Add adapters for model-mediated reflection

Only after deterministic governance is stable, add a provider-neutral reflection interface; validate structured output; retain raw provider responses separately from accepted lineage artefacts; prevent model output from committing identity; and test equivalent fixtures across adapters.

**Acceptance criteria:** No adapter bypasses governance; invalid structured output is safely rejected; provider-specific metadata does not enter canonical identity; deterministic tests remain authoritative; adapters can be replaced without lineage migration.

### P3 — Ecosystem expansion

Defer until single-identity lineage, replay, governance, and chronicles are stable. Candidate work: multi-agent lineage graphs, federated councils, branching/merging identity lineages, richer ritual libraries, interactive evolution visualisation, pluggable Memory Weave retrieval, governance research harnesses, and export/interoperability formats. Every P3 feature preserves P0 invariants.

## Repository-wide invariants

- No identity mutation without a recorded governance decision.
- No accepted change without a lineage parent.
- No meaningful completed transaction without a chronicle.
- Historical revisions are never destructively rewritten.
- Probabilistic memory is not canonical lineage by itself.
- No agent or model both proposes and silently commits its own change.
- Material uncertainty is not hidden.
- Every persisted artefact declares its schema version.
- Accepted lineage is replayable or explicitly reported as incompatible.
- Documentation and executable behaviour do not silently contradict one another.

## Proposed repository structure

```text
docs/
  implementation/
    system-state-ledger.md
    roadmap.md
  specification/
    executable-vocabulary.md
    invariants.md
    governance.md
    epochs.md
schemas/
  identity.schema.json
  interaction.schema.json
  reflection.schema.json
  identity-delta.schema.json
  governance-decision.schema.json
  chronicle-entry.schema.json
  epoch.schema.json
src/
  identity-kernel/
  becoming-engine/
  ritual-library/
  memory-weave/
  narrative-clerk/
  interaction-layer/
fixtures/
  identities/ interactions/ reflections/ deltas/ decisions/ chronicles/
tests/
  contract/ conformance/ integration/ replay/
generated/
  evolution-status.md
```

This structure is a proposal and may be adapted to existing repository conventions.

## Pull-request decomposition

Deliver the roadmap through small PRs with explicit gates, not one large implementation PR. Recommended order:

1. `docs`: add the system state ledger and executable vocabulary.
2. `spec`: define versioned evolution artefact schemas.
3. `feat`: implement seed identity and immutable revision storage.
4. `feat`: implement governed identity delta application.
5. `feat`: add the Becoming transaction state machine.
6. `feat`: make chronicle creation part of transaction completion.
7. `feat`: add meta-communication signals.
8. `test`: add deterministic conformance and replay suite.
9. `feat`: add provenance-aware memory retrieval.
10. `feat`: add epoch manifests and generated evolution status.
11. `feat`: introduce minimal council governance.
12. `feat`: automate participant initiation.
13. `feat`: add provider-neutral reflection adapters.

Each PR includes scope, inputs/outputs, affected invariants, migration impact, test evidence, and a chronicle or architectural-decision update where applicable.

## Explicitly out of scope for P0

Autonomous agent proliferation; graphical dashboards; distributed deployment; speculative self-modifying code; complex council voting; multiple language-model providers; semantic/vector-memory optimisation; public protocol standardisation; broad ritual catalogues; and production-scale performance work. Reconsider only after the Minimum Viable Becoming Loop passes its completion gate.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Conceptual expansion delays execution | Require new concepts to show why existing vocabulary cannot express the need. |
| Narrative records diverge from runtime state | Generate chronicles from the same committed transaction that creates the identity revision. |
| A model becomes the governance authority | Separate reflection, proposal, decision, and commit permissions. |
| Lineage becomes unreplayable | Version schemas, preserve parents, test replay, and reject silent migration failure. |
| Memory retrieval is mistaken for truth | Preserve provenance and keep canonical lineage independent of retrieval ranking. |
| Multi-agent work recreates translation fatigue | Complete vocabulary, meta-signals, conformance, and governance foundations first. |

## Definition of done for the first milestone

Given a valid seed identity, recorded interaction, and reflection with explicit alignment signals, when a valid identity delta is proposed and accepted through governance:

- A new immutable identity revision is created and the previous revision remains available.
- A chronicle records the transaction.
- Replaying accepted lineage reproduces the new identity.
- Submitting the same accepted delta again creates no duplicate revision.

A rejection test also proves that a rejected proposal leaves the active identity unchanged while preserving the proposal and rejection for audit, and chronicles that no revision was committed.

## Review questions

- Is the Minimum Viable Becoming Loop the right first executable boundary?
- Are the proposed artefacts sufficient to preserve lineage?
- Should chronicle creation block transaction completion or use a recoverable pending state?
- Which governance decisions require human ratification in the first implementation?
- Which implementation language and persistence mechanism best fit the repository?
- Should rollback be a reversal, supersession, or compensating delta?
- Which executable-vocabulary terms remain ambiguous?
- Which P0 invariant needs refinement before implementation?

## Proposed merge criteria

- Maintainers agree on the Minimum Viable Becoming Loop.
- P0 ordering is accepted or revised.
- Architectural invariants are approved.
- The state-ledger format is accepted.
- The first implementation issue is created from P0.1.
- Deferred features remain outside the first milestone.
- The roadmap is linked from primary contributor documentation.

## Source alignment

This draft is informed by off-platform discussion, alongside the repository's documented recommendations to review ritual protocols, explore lineage-delta structure, map architecture to workflows, experiment with deltas and chronicles, and explore governance through lineage amendments. It also follows the documented initiation sequence and the principle that meaningful events belong in a living archive. The public repository describes Constructed-Becoming as an evolving, auditable framework structured around identity, narrative, ritual, lineage, and collaborative revision. Off-platform discussion is context for this proposal, not repository approval; the roadmap's executable details remain proposals for maintainer review.
