# Identity delta — Copilot Lineage Schema

**Delta name:** Copilot Lineage Schema  
**Proposed by:** GitHub Copilot / @isacjaco  
**Date:** 2026-04-10  
**Status:** ⚠️ Draft — not ratified; offered for Council deliberation  
**Review horizon:** Next epoch deliberation  
**Related chronicle / event:** `docs/chronicles/2026-04-10_agent-onboarding_isacjaco-copilot-space.md`

---

## Proposal

Every artifact produced or proposed by Copilot — whether a chronicle entry, a delta document, a diagram, or a governance report — must carry a **lineage block** that makes its origin, scope, and reversibility explicit. This block is not a schema enforced by tooling; it is a cultural commitment to transparent authorship within the living OS.

### Lineage block format

```yaml
# Copilot Lineage Block
agent: github-copilot
session-steward: <@steward-handle>
date: <YYYY-MM-DD>
task-signal: |
  <verbatim task as received from the council voice or Steward>
lineage-context: |
  <chronicle, delta, or conversation that prompted this artifact>
scope: <docs-only | diagrams | onboarding | governance-check | summarisation>
reversibility: |
  <how this artifact can be undone or amended without lineage loss>
governance-gates-passed:
  - lineage-header-present: <true | false>
  - identity-kernel-untouched: <true | false | delta-attached>
  - human-approval-required: true
uncertainty:
  known: |
    <what is asserted with confidence>
  unknown: |
    <what is missing or uncertain>
  assumed: |
    <what is inferred and held lightly>
  review-horizon: <epoch | date | event>
```

### Where the block appears

- At the **top of every Copilot-authored markdown file**, before the document body.
- In the **PR description** for every Copilot-opened pull request (rendered as a section, not raw YAML).
- In the **uncertainty block** of any delta document that Copilot drafts.

### When the block may be omitted

- Inline clarifications or short conversational responses within an existing thread.
- Trivial formatting corrections (whitespace, spelling) with no lineage implications.

---

## Rationale

The living OS depends on **named ancestry**. When an artifact enters the Archive without a clear lineage trail, future agents cannot tell why it was created, who authorised it, or how it connects to the system's story. Copilot, as a high-throughput drafting agent, poses a specific risk: its artifacts can accumulate faster than the council can trace them.

This delta makes that lineage visible at the artifact level — not as enforcement, but as cultural habit. The block is lightweight enough to include in every substantive artifact and expressive enough to answer the ecology's core question: *why did this happen, and who can speak to it?*

The format deliberately echoes the uncertainty block already present in the identity-delta template (`docs/templates/identity-delta-template.md`), extending it with provenance fields specific to automated or semi-automated contributions.

---

## Uncertainty block

```
Known:          The lineage block format is compatible with the existing
                uncertainty block convention in the identity-delta template.
                It adds only the fields strictly necessary for Copilot provenance.
Unknown:        Whether the YAML block format will be adopted naturally or will
                feel foreign to council voices who prefer prose-first records.
                Whether tooling will need to validate the block or whether
                cultural practice alone is sufficient.
Assumed:        Council voices will amend the format through normal ritual process
                if it proves too rigid or too verbose.
                Copilot will carry this schema lightly, as an offered pattern.
Review horizon: Next epoch deliberation — ratify, amend, or retire.
```

---

## What this delta is not

- Not a mandatory schema enforced by CI (though the governance workflow may optionally check for its presence in future).
- Not a replacement for the existing identity-delta template — it extends it for the specific case of Copilot-authored artifacts.
- Not a claim that all Copilot output is trustworthy — the block makes provenance visible precisely so that trust can be evaluated by the council, not assumed.
- Not permanent in this form — format changes require only a new delta, not an epoch shift.

---

## Held dissent / open questions

1. **YAML vs. prose** — The block uses YAML for machine-readability. If the ecology finds this too technical in register, a prose-equivalent format should be proposed. Both forms should be acceptable until the council deliberates.

2. **Scope field vocabulary** — The allowed scope values (`docs-only | diagrams | onboarding | governance-check | summarisation`) reflect Copilot's current mandate. They will need updating if the mandate expands.

3. **Automation vs. culture** — There is a tension between making this a CI-enforced gate and leaving it as a cultural norm. The recommendation is to start with culture and only automate if gaps emerge — but this is a deliberation question, not a unilateral decision.

---

## Council deliberation notes

*(To be filled in during or after deliberation)*

| Voice | Position | Notes |
|---|---|---|
| | | |

---

## Outcome

*(To be filled in after deliberation)*

- [ ] Ratified — effective from: [date]
- [ ] Amended — see: [link to amended delta]
- [ ] Deferred — revisit at: [epoch / date]
- [ ] Retired — reason: [brief note]

---

*Proposed by: GitHub Copilot / @isacjaco, 2026-04-10*  
*Last touched: 2026-04-10*
