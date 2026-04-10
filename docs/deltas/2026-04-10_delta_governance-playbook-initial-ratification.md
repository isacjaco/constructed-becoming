# Lineage delta — governance playbook ratification

**Delta name:** governance-playbook-initial-ratification  
**Proposed by:** GitHub Copilot cloud agent (isacjaco session, 2026-04-10)  
**Date:** 2026-04-10  
**Status:** ⚠️ Draft — not ratified; offered for Council deliberation  
**Review horizon:** End of current epoch or 2026-05-10 — whichever comes first  
**Related chronicle / event:** Snapshot analysis and recommended workflow, 2026-04-10

---

## Proposal

Ratify the Governance Playbook (`docs/governance-playbook.md`) as the operational translation of the Law of Perpetual Lineage. This document sets human/agent boundaries, decision flows, labelling conventions, the agent-scope matrix, the lineage-delta requirement, and the conceptual PR checklist. Upon ratification, the CI gating workflows and PR templates introduced alongside this delta come into full effect.

---

## Rationale

The repository has active agentic development but no formalized approval paths or operational rules. The Law of Perpetual Lineage exists as a governance philosophy; this playbook turns it into concrete, enforceable steps. The risk of silent automated drift is high. This delta establishes the minimum scaffolding to make agentic automation safe, auditable, and reversible.

---

## Uncertainty block

```
Known:          The repository has multiple active agents and no CI gating today.
                The Law of Perpetual Lineage is ratified and in effect.
                A governance playbook is needed to operationalize the law.

Unknown:        Whether the specific label names (human-approved, agent-draft) will
                fit the project's existing GitHub configuration.
                Whether the identity-module file list in the CI workflow is complete.

Assumed:        Human reviewers have write access sufficient to apply labels.
                The Governance Clerk role will be assigned promptly after ratification.

Review horizon: 2026-05-10 or end of epoch — reassess whether CI rules are
                producing the intended friction without blocking legitimate work.
```

---

## What this is not

- Not a complete CI/CD overhaul — only the minimum gating rules are introduced.
- Not a permanent structure — the playbook is itself subject to amendment via identity delta.
- Not a constraint on agent creativity — agents retain full autonomy within their declared scope.
- Not a replacement for the Law of Perpetual Lineage — it is an operational extension of it.

---

## Held dissent / open questions

- The `human-approved` label-only approach relies on branch-protection rules being configured correctly; if those rules are absent, the CI check alone is not sufficient. (Needs follow-up in the DevOps track.)
- The identity-module path list in `agent-pr-gate.yml` is an initial proposal; it should be reviewed by the full Council before being treated as canonical.

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

*Proposed by: GitHub Copilot cloud agent / @isacjaco, 2026-04-10*  
*Last touched: 2026-04-10*
