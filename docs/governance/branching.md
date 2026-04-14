# Branch Governance  
*A constitutional guide for how change moves through the Constructed‑Becoming ecosystem.*

Constructed‑Becoming treats branches not as technical conveniences but as **ritual surfaces** where identity, lineage, and experimentation meet. Each branch type expresses a different mode of becoming: canonical, exploratory, or integrative. Together they form a coherent system that preserves continuity while enabling evolution.

---

## Branch roles

### 🜁 Lineage branch — `main`  
The canonical identity surface. All changes that reach this branch become part of the project's enduring lineage. Mutation is only permitted through reviewed, validated, narratively‑anchored pull requests.

Key properties:
- Pull requests required  
- Full governance validation (manifest + lineage)  
- Signed commits  
- Linear history  
- No bypass, no force pushes, no deletions  

This branch is the **memory** of the ecosystem.

---

### 🜂 Experimental branches — `experiment/*`  
The playground for agents and humans to explore, rewrite, discard, and prototype. These branches are intentionally permissive to support rapid iteration and divergent thinking.

Key properties:
- Direct commits allowed  
- Minimal checks (build + lint)  
- Non‑linear history  
- Force pushes and deletions allowed  
- Bypass allowed  

These branches are the **dreaming** of the ecosystem.

---

### 🜄 Staging branch — `staging`  
The convergence layer where multiple experimental lines are integrated, stabilised, and prepared for ascent into lineage. It balances flexibility with discipline.

Key properties:
- Pull requests required  
- Governance manifest validation  
- Linear history  
- No bypass, no force pushes, no deletions  

This branch is the **threshold** between experimentation and identity.

---

## Flow of change

The ecosystem follows a three‑stage movement:

```
experiment/*   →   staging   →   main
   dreaming        integration     lineage
```

### 1. Experimentation  
Agents and humans explore ideas freely in `experiment/*`. History may be rewritten, branches may be discarded, and prototypes may be generated without ceremony.

### 2. Integration  
When an experimental line stabilises, it is merged into `staging` through a pull request. This is where:
- tests must pass  
- governance manifests must validate  
- conversations must resolve  
- integration conflicts must be addressed  

### 3. Lineage ascent  
Once integrated and stable, changes move from `staging` to `main` through a lineage‑grade pull request. This step requires:
- narrative context  
- lineage delta  
- signed commits  
- full governance validation  

This is the ritual moment where change becomes identity.

---

## Change workflow

### 1. Initiation  
A contributor (human or agent) identifies a change and creates an `experiment/*` branch.

### 2. Drafting  
Work proceeds freely. Agents may generate drafts, rewrite history, or restructure content.

### 3. Integration PR  
When ready, the contributor opens a pull request from `experiment/*` → `staging`.  
The PR must include:
- a narrative explanation of intent  
- a summary of changes  
- any uncertainty markers  
- a governance manifest update if relevant  

### 4. Governance checks  
Automated agents validate:
- build, lint, test  
- manifest structure  
- dependency integrity  

Humans review conceptual and narrative alignment.

### 5. Staging merge  
Once approved, the PR merges into `staging`.  
This branch accumulates stable, integrated work.

### 6. Lineage PR  
When staging is ready for ascent, a PR from `staging` → `main` is opened.  
This PR must include:
- a lineage delta  
- a narrative of how the change fits the project's evolution  
- confirmation that all governance checks pass  

### 7. Ritual merge  
After human approval, the change enters `main` and becomes part of the project's enduring identity.

---

## Proposal prompt for contributors

This is the standard prompt contributors should use when proposing changes. It ensures every proposal arrives in a lineage‑ready format.

```
# Constructed‑Becoming Change Proposal

## 1. Intent
What change is being proposed, and why does it matter?

## 2. Context
What background, problem, or opportunity does this change respond to?

## 3. Change Summary
List the concrete modifications introduced by this proposal.

## 4. Lineage Impact
How does this change affect identity, structure, or narrative continuity?

## 5. Uncertainties
What aspects require review, clarification, or further exploration?

## 6. Governance Artifacts
- Manifest updates (if any)
- Lineage delta (if targeting `main`)
- Diagrams or models (optional)

## 7. Branch Path
Which branch is this proposal targeting?
- experiment/* → staging
- staging → main
```
