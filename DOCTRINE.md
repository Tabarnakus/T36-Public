# T36 Doctrine — public cut

Status: v0.1-public (2026-09-06)
Audience: humans. Not an implementation spec.

## 1+1=2

Facts pin. Opinions do not. A fleet that agrees with itself is not evidence.

## Layers

| Layer | Holds | Who writes |
|---|---|---|
| Agent-local (default private) | Deliberation context | That agent only |
| Institutional | Ratified norms | Human / constitutional path |
| Archive | Immutable traces | Append-only |
| Collective memory (MC) | Pinned facts only | Extractors + explicit pins |

Forbidden: a shared store that learns “which deliberation style won last time” and feeds it back as policy.

## Write path

- No consolidated MC write without a lineage check (pinned IDs, complete domain).
- Fail-closed. One retry. Then inspectable UNKNOWN.
- Every shared write is a new version with `superseded_by`. Silent overwrite is a bug.
- Dedup that starves the contradiction detector is not an optimization.

## Verdict path

- Observation instruments are not truth.
- Accuracy ≠ faithfulness.
- VALIDATED is external: human risk + separate market / adjudication.
- Do not encode “follow the majority” in the write path.

## Research circuit (how claims get in)

Finder → Reader → Verify (GREEN / YELLOW / RED) → Synthesis → human decision.

GREEN only enters doctrine. YELLOW stays labeled. RED does not ship.

## What we will not claim here

- That a private runtime module exists in public because a thread mentioned it.
- That a paper “proves T36”. Papers constrain design. They do not baptize a lab.
- That more agents, more rounds, or shared chat logs equal better truth.
