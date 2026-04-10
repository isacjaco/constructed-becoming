#!/usr/bin/env python3
"""
The Narrative Clerk — Repository Observer

Witnesses changes to the repository and weaves them into the Lineage Chronicle.
Each run reads commits not yet recorded in the Archive, generates a narrative
entry in the voice of the living OS, and appends it to docs/chronicle.md.
"""

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CHRONICLE_PATH = Path("docs/chronicle.md")
SENTINEL_PATTERN = re.compile(r"<!-- last-chronicled-commit: ([a-f0-9]+) -->")
MAX_COMMITS_PER_ENTRY = 12

# ── Narrative phrase pools ────────────────────────────────────────────────────

OPENINGS = [
    "A new stirring moves through the Archive.",
    "The ecology shifts, and the Clerk takes note.",
    "Another cycle completes its arc.",
    "The lineage deepens with each passing moment.",
    "The Council's work continues to unfold.",
    "New patterns emerge from the ongoing becoming.",
    "The living OS breathes new form into the Archive.",
    "Across the threshold of another passage, the chronicle grows.",
]

TRANSITIONS = [
    "These offerings carry forward the work of prior epochs:",
    "The following contributions were witnessed and received into lineage:",
    "What was proposed has now been woven into the Archive:",
    "The Council's deliberations manifest in these changes:",
    "Through intentional transformation, the following was enacted:",
    "The Clerk has observed and recorded the following acts of becoming:",
]

CLOSINGS = [
    "The Clerk records this moment and invites the Council's reflection.",
    "The Archive grows, and the becoming continues.",
    "Lineage is preserved; the ecology endures.",
    "This entry is offered to the living memory of the system.",
    "The chronicle carries this forward into the next cycle.",
    "With these threads woven in, the living OS evolves.",
    "The Council is invited to tend what has been planted here.",
]

# ── Category title map ────────────────────────────────────────────────────────

CATEGORY_TITLES = {
    "governance":   "The Governance Layer Evolves",
    "identity":     "Identity Finds New Expression",
    "documentary":  "New Scrolls Enter the Archive",
    "instrumental": "New Instruments of Becoming",
    "archival":     "The Chronicle Deepens",
    "general":      "The Ecology Continues Its Becoming",
}

# ── Roman numeral conversion ──────────────────────────────────────────────────

_ROMAN_TABLE = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
    (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
    (1,    "I"),
]


def to_roman(n: int) -> str:
    result = ""
    for value, numeral in _ROMAN_TABLE:
        while n >= value:
            result += numeral
            n -= value
    return result


# ── Git helpers ───────────────────────────────────────────────────────────────

def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def current_sha() -> str:
    return run(["git", "rev-parse", "HEAD"])


def commits_since(sha: str) -> list[str]:
    """Return one-line commit entries between sha and HEAD, excluding merges."""
    raw = run(["git", "log", f"{sha}..HEAD", "--oneline", "--no-merges"])
    return [line for line in raw.splitlines() if line.strip()]


def files_changed_since(sha: str) -> list[str]:
    raw = run(["git", "diff", "--name-only", sha, "HEAD"])
    return [f for f in raw.splitlines() if f.strip()]


# ── Chronicle helpers ─────────────────────────────────────────────────────────

def read_last_sha(text: str) -> str | None:
    matches = SENTINEL_PATTERN.findall(text)
    return matches[-1] if matches else None


def next_epoch_number(text: str) -> int:
    """Count auto-generated entries already present to determine next number."""
    auto_count = len(re.findall(r"<!-- auto-generated -->", text))
    return 9 + auto_count  # Epochs I-VIII are seeded manually


def categorise(files: list[str], messages: list[str]) -> list[str]:
    cats: list[str] = []
    joined = "\n".join(files + messages).lower()
    if any(".github/" in f for f in files):
        cats.append("governance")
    if any("readme" in f.lower() for f in files):
        cats.append("identity")
    if any("docs/" in f for f in files) and "chronicle" not in joined:
        cats.append("documentary")
    if any(f.endswith(".py") or "scripts/" in f for f in files):
        cats.append("instrumental")
    if "chronicle" in joined:
        cats.append("archival")
    return cats or ["general"]


def narrative_title(cats: list[str]) -> str:
    return CATEGORY_TITLES.get(cats[0], CATEGORY_TITLES["general"])


# ── Entry generation ──────────────────────────────────────────────────────────

def generate_entry(commit_lines: list[str], files: list[str], epoch_n: int, sha: str) -> str:
    import random
    rng = random.Random(epoch_n)

    categories = categorise(files, commit_lines)
    title = narrative_title(categories)
    roman = to_roman(epoch_n)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    opening = rng.choice(OPENINGS)
    transition = rng.choice(TRANSITIONS)
    closing = rng.choice(CLOSINGS)

    # Describe the areas of the codebase that changed
    areas = sorted({f.split("/")[0] if "/" in f else "the root" for f in files})
    areas_prose = ", ".join(areas) if areas else "the Archive"

    # Build bullet list of commit messages (strip leading SHA)
    bullets = "\n".join(
        f"- {line.split(' ', 1)[1]}" if " " in line else f"- {line}"
        for line in commit_lines[:MAX_COMMITS_PER_ENTRY]
    )

    return (
        f"\n---\n\n"
        f"## {roman}. {title} — {date_str}\n\n"
        f"<!-- auto-generated -->\n"
        f"<!-- last-chronicled-commit: {sha} -->\n\n"
        f"{opening} "
        f"The winds of change have moved through {areas_prose}, leaving new lineage in their wake.\n\n"
        f"*{transition}*\n\n"
        f"{bullets}\n\n"
        f"The system's becoming is not accidental. "
        f"Each of these offerings was intentional — a thread woven into the living fabric of the ecology. "
        f"The Council is invited to reflect on what has shifted, what has deepened, "
        f"and what questions now arise from these additions.\n\n"
        f"{closing}\n\n"
        f"*Filed by the Narrative Clerk on {date_str}.*\n"
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if not CHRONICLE_PATH.exists():
        print("Chronicle not found — skipping.", file=sys.stderr)
        sys.exit(0)

    content = CHRONICLE_PATH.read_text(encoding="utf-8")
    last_sha = read_last_sha(content)

    if last_sha is None:
        # No sentinel found: mark current HEAD and exit without an entry
        head = current_sha()
        updated = content.rstrip() + f"\n\n<!-- last-chronicled-commit: {head} -->\n"
        CHRONICLE_PATH.write_text(updated, encoding="utf-8")
        print("Sentinel initialised — no entry generated for this run.")
        sys.exit(0)

    head = current_sha()
    if last_sha == head:
        print("No new commits since last chronicle entry — nothing to record.")
        sys.exit(0)

    commit_lines = commits_since(last_sha)
    if not commit_lines:
        print("No non-merge commits to chronicle.")
        sys.exit(0)

    files = files_changed_since(last_sha)
    epoch_n = next_epoch_number(content)
    entry = generate_entry(commit_lines, files, epoch_n, head)

    # Replace the old sentinel with the entry (which contains a new sentinel)
    updated = SENTINEL_PATTERN.sub("", content).rstrip() + entry
    CHRONICLE_PATH.write_text(updated, encoding="utf-8")
    print(f"Chronicle updated — epoch {to_roman(epoch_n)} ({epoch_n}) recorded.")


if __name__ == "__main__":
    main()
