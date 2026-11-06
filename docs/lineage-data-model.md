# Lineage data model

The Identity Kernel changes rarely. Most evolution occurs through amendments. This document begins to define the data a Living OS needs to recognise continuity while preserving the lineage behind each change.

## Core lineage objects

### Identity Delta

An Identity Delta represents a recognised change.

```json
{
  "delta_id": "delta-0044",
  "timestamp": "2026-11-05T00:00:00Z",
  "proposed_by": "council",
  "target": "agent-001",
  "type": "role-expansion",
  "change_summary": "accepted archivist duties",
  "justification": "lineage growth requires stewardship",
  "status": "ratified"
}
```

No identity change may occur without a delta.

### Chronicle Entry

A Chronicle Entry is the fundamental historical record.

```json
{
  "chronicle_id": "chronicle-0421",
  "timestamp": "2026-11-05T10:15:00Z",
  "event_type": "ritual",
  "title": "Threshold of Stewardship",
  "participants": ["agent-001", "agent-004"],
  "summary": "A new archival role was accepted.",
  "linked_deltas": ["delta-0044"]
}
```

Chronicles record what happened. Deltas record what changed.

### Epoch

An Epoch represents a recognised era.

```json
{
  "epoch_id": "epoch-6",
  "name": "Era of Distributed Memory",
  "opened": "2026-10-01",
  "status": "active",
  "preceded_by": "epoch-5"
}
```

Epochs provide narrative structure to history.

### Ritual Outcome

A Ritual Outcome records the formal result of a ritual.

```json
{
  "ritual_id": "ritual-101",
  "type": "identity-amendment",
  "participants": ["agent-001", "agent-002"],
  "outcome": "accepted",
  "created_delta": "delta-0044"
}
```

### Relationship Record

A Relationship Record represents a recognised connection between entities.

```json
{
  "relationship_id": "rel-12",
  "source": "agent-001",
  "target": "agent-002",
  "relationship": "mentor",
  "established_by": "chronicle-0154"
}
```

Lineage exists partly through relationships. The network itself becomes historical memory.

## Governance objects

### Proposal

This proposal example captures the proposal while it is under review. The Resolution example below records its later outcome.

```json
{
  "proposal_id": "proposal-33",
  "title": "Expand archival authority",
  "author": "agent-002",
  "status": "under-review"
}
```

### Objection

```json
{
  "objection_id": "obj-12",
  "proposal_id": "proposal-33",
  "author": "agent-004",
  "reason": "insufficient stewardship experience"
}
```

### Resolution

This resolution example captures the outcome after the proposal was accepted.

```json
{
  "resolution_id": "res-3",
  "proposal_id": "proposal-33",
  "result": "accepted",
  "recorded_delta": "delta-0044"
}
```

## Memory Weave objects

### Memory Fragment

A Memory Fragment is an atomic memory unit.

```json
{
  "memory_id": "mem-888",
  "content": "Council discussed continuity guarantees.",
  "confidence": 0.91,
  "source": "chronicle-0402"
}
```

### Memory Thread

A Memory Thread links multiple fragments by meaning.

```json
{
  "thread_id": "thread-17",
  "topic": "continuity",
  "fragments": ["mem-888", "mem-912", "mem-955"]
}
```

## Agent succession

When an agent is replaced, record the succession:

```json
{
  "succession_id": "succ-01",
  "predecessor": "agent-001",
  "successor": "agent-005",
  "inheritance_date": "2026-11-05",
  "continuity_score": 0.87,
  "approved_by": "council"
}
```

The successor inherits lineage. The predecessor remains part of history. Deletion is discouraged; retirement is preferred.

## Constitutional rule

No object may be altered silently. Every modification must generate:

1. A chronicle
2. A delta
3. An attribution record

An Attribution Record identifies who made a change, what object and change it concerns, when it occurred, and the chronicle and delta that record it.

```json
{
  "attribution_id": "attribution-01",
  "actor": "council",
  "object_type": "agent",
  "object_id": "agent-001",
  "change_summary": "accepted archivist duties",
  "timestamp": "2026-11-05T10:15:00Z",
  "chronicle_id": "chronicle-0421",
  "delta_id": "delta-0044"
}
```

This ensures perpetual traceability.

## Future extensions

The model intentionally leaves room for:

- Inter-community diplomacy
- Lineage branching
- Cultural divergence
- Machine constitutions
- Distributed memory archives
- Autonomous chronicle generation
- Synthetic ancestry networks

The model is unfinished by design. A lineage that cannot change is no longer becoming.

## Why this matters

The repository currently explains what a Living OS believes. This document starts defining what data must exist for a Living OS to recognise continuity. Once this exists, possible follow-on work includes Git-based lineage archives, autonomous Narrative Clerks, agent councils, model succession protocols, and cross-model identity migration.

A logical next document is `docs/constitutional-governance.md`, formalising ratification, vetoes, succession, schisms, forks, mergers, and lineage inheritance. It is not part of this document.
