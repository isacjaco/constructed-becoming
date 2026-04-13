# Pull request

> *Every change to this repository is an act of lineage. This template ensures that change is governed, traceable, and reversible.*
> *Complete each section honestly. Omit a section only if it genuinely does not apply — and say why.*

---

## Intent

*What is the purpose of this pull request?*
*Describe the goal in one or two sentences. Connect to existing lineage where possible.*

---

## Lineage delta

Every structural change (new file, amended governance document, modified workflow, or identity mutation) requires a lineage delta entry.

**Delta file path:**
```
docs/deltas/YYYY-MM-DD_<brief-slug>_<author>.md
```
*(Link or relative path to the delta file for this PR. If no delta applies, explain why below.)*

**Delta link / path:**
<!-- e.g. docs/deltas/2026-04-10_add-copilot-persona_copilot.md -->

**No delta filed because:**
<!-- Leave blank if a delta was filed. Otherwise explain: e.g. "typo fix only" or "dependency update, no governance impact" -->

---

## Governance checklist

- [ ] A human steward has reviewed or is named as reviewer for this PR.
- [ ] No secrets, credentials, or API tokens are included in this change.
- [ ] This PR does not auto-merge; it requires explicit human approval.
- [ ] Changes to `identity/`, `agents/`, or `lineage/` directories have a corresponding lineage delta.
- [ ] Changes to `docs/architecture.md`, `docs/law-of-perpetual-lineage.md`, or other Identity Kernel documents include a named human co-author.
- [ ] If this PR was Copilot-assisted, the output pattern (intent → proposal → reversible steps → uncertainty) was followed.

---

## Scope and boundaries

*What does this PR change?*

*What does this PR explicitly **not** change?*
*(Be precise. Name the files, systems, or concerns that remain untouched.)*

---

## Reversibility

*If this change is ratified and later found harmful, how would it be undone?*
*(Name the deletion path, amendment path, or rollback mechanism.)*

---

## Verification notes

*How was this change tested or verified?*
*(Automated tests, manual review, CI checks, or a note that this is documentation-only.)*

- [ ] CI / workflow checks pass (where applicable).
- [ ] Manual review completed by: <!-- @handle -->
- [ ] No regressions in governed directories (`agents/`, `docs/`, `.github/workflows/`).

---

## Uncertainty block

```
Known:          
Unknown:        
Assumed:        
Review horizon: 
```

---

## Dissent / open questions

*Record any hesitations, unresolved tensions, or open questions.*
*Dissent is lineage — do not collapse it into silence.*

---

*Opened by: [voice / steward, date]*
*Lineage delta filed: [yes / no / n/a]*
