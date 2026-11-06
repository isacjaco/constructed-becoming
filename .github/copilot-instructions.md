# Copilot instructions

## Project context

Constructed-Becoming is a model-agnostic, documentation-first framework for agentic systems that develop identity and continuity through narrative, ritual, memory, and governance. Its Living OS architecture describes relationships among the Identity Kernel, Becoming Engine, Ritual Library, Memory Weave, Narrative Clerk, and user interaction; the repository primarily documents these concepts rather than implementing them as software.

The `docs/` corpus includes conceptual architecture, agent behaviour and initiation, ritual protocols, lineage principles, chronicles, and reusable templates. Treat proposals and templates according to their stated status: for example, `docs/archive-structure-proposal.md` is explicitly a proposal, not an enforced directory convention. Do not present a concept, proposed structure, or future extension as an implemented feature or adopted rule unless the current repository establishes that status.

The repository has no application build, test, or lint command defined. The GitHub Pages workflow deploys the repository on pushes to `main`; the agent-onboarding workflow creates a chronicle from `docs/templates/onboarding-prompt.md` and opens a pull request. Neither workflow validates an implemented data schema.

## Working with documentation

- Read the relevant current documents and README before editing. Ground descriptions of existing structure, policy, and implementation in files present on the checked-out branch. If a requested disposition or fact cannot be verified, identify it as unresolved rather than inventing paths, prior decisions, or implementation state.
- Convert the user's request into a checklist of required content and preserved details before drafting. Validate that each requirement is substantively covered; do not make a change solely to satisfy a literal-heading or formatting check when the requested content is already clearly present.
- Keep proposals, examples, and future extensions distinct from adopted conventions. Preserve supplied terminology, examples, and rationale unless the user asks for changes.
- For documentation changes, review the final diff, run `git diff --check`, and verify any changed relative links and structured examples (such as fenced JSON). There is no repository-defined documentation test or Markdown linter.

## Reviewing pull-request feedback

Inspect the live comment or review thread, its context, and existing replies before changing files or responding. Distinguish actionable requests from acknowledgments such as “ok”; if an acknowledgment has already been handled, do not make unrelated edits or post a duplicate reply. For actionable feedback, check it against the original request and repository evidence, make only the in-scope correction, and reply in the existing thread.
