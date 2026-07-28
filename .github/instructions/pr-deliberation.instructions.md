---
applyTo: "**"
---

# PR deliberation instructions

Every pull request in this repository is a **Council Deliberation** — a formal proposal to alter the system's becoming. These instructions apply to authoring, reviewing, and commenting on pull requests.

## Authoring a PR

Before opening a PR, ensure the branch name follows the ritual convention:

- `delta/YYYY-MM-DD-slug` for identity proposals
- `governance/slug` for constitutional amendments
- `chronicle/slug` for archive entries
- `feature/slug` for capability expansions
- `docs/slug` for documentation updates
- `agent-onboarding/YYYY-MM-DD-role` for agent initiation

The PR description is the **Threshold Reading** — the first act of deliberation. It must include:

### Identity Delta

State clearly what is being altered in the system's structure, meaning, or identity. Be specific about what this change proposes to add, retire, or amend in the lineage.

### Uncertainty Block

```
- Known: [what is established and can be relied upon]
- Unknown: [what remains open or unresolved]
- Assumed: [what is being taken for granted and may need future scrutiny]
```

### Narrative context

Explain why this change belongs in the lineage. Connect it to prior decisions, resolved tensions, or ongoing deliberations. A change without narrative context is a mutation without memory.

---

## Reviewing a PR (offering a reading)

A review comment is not a code critique — it is a **reading** of the proposal. When reviewing:

1. **State your role or perspective** — "As Steward, I notice…" or "From an Archive coherence perspective…"
2. **Offer an interpretation** — what does this change mean for the system's identity?
3. **Name tensions** — identify any conflicts with existing lineage, unresolved assumptions, or potential cultural drift
4. **Suggest amendments** — if something needs to change, propose specific language or a different framing
5. **Record held dissent** — if you cannot affirm but will not block, name your objection so it enters the lineage

### Approval is ratification

Approving a PR is a **ritual affirmation** — you are lending your Council voice to the proposal becoming part of the lineage. Do not approve mechanically. Approval carries responsibility.

---

## Merge as becoming

When a PR is merged into `main`:

- The merge commit message should carry narrative weight, not just a technical summary
- Any associated Chronicle should be updated or created
- The Lineage Clerk (automated or manual) should record the transition in the current Epoch Chronicle
- Review horizons set in the PR should be tracked as future Council summons

---

## Closing a PR without merging

Closing a PR is not failure. It is **intentional retirement**. When closing without merging:

- Record the reason for retirement in a final comment
- Note whether the proposal should be revisited in a future epoch
- Preserve the PR as lineage — even rejected proposals are part of the story

---

## Live tensions

If a PR carries unresolved tensions — dissent that was named but not resolved — merge it with a note in the merge commit or an associated Chronicle entry marking it as a **live amendment**. The tension remains active in the lineage and should appear in the next Audit cycle.
