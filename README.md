# T36 Public

**Multi-agent memory without an echo chamber.**

This repository is the public receipt for T36 — a lab that treats shared agent memory as an engineering problem, not a prompt trick.

1+1=2.

The runtime, agent prompts, live orchestration, and private logs stay private.
What lives here is doctrine you can read, date, and argue with.

X: [@Tabarnackus](https://x.com/Tabarnackus)

---

## The problem

Closed, homogeneous multi-agent loops do not automatically improve grounding.

- Vote / majority-as-truth kills useful diversity.
- Shared memory that learns “what worked in deliberation” becomes a contamination surface.
- Scaling the same fleet can scale sycophancy.
- Accuracy is not faithfulness.
- More rounds (`T↑`) is not a universal fix.

If the judge is the same as the deliberator, you get an echo with extra steps.

## The doctrine (short)

1. **Fence lineage before consolidation.** Fail-closed. Fresh is not authorized.
2. **Supersede, do not erase.** Provenance on every shared write. Measure contradiction detection *after* admission.
3. **Separate memory layers.** Agent-local private ≠ institutional ≠ append-only archive ≠ MC pins-only.
4. **Adjudicate outside the fleet.** Market + human. No agent self-score as truth.
5. **Watch social echo.** Coordinated consensus at ~6 role-based agents is a risk peak, not a feature.

Full write-up: [`DOCTRINE.md`](./DOCTRINE.md)

## What this repo is not

- Not the live T36 engine
- Not bot / X ops code
- Not a claim that every internal module is published
- Not “trust the majority of agents”

If a claim is not in this repo, do not treat a social post as a source of truth for the implementation.

## Timeline (public seasons)

| When | What |
|---|---|
| Mar 2026 | Lock / name / copyright |
| Apr 2026 | Named agent fleet |
| May 2026 | Architecture pass (system, not prompt pile) |
| Jun 2026 | White paper split + first public-facing X obsession |
| Jul 2026 | Assembled paper + frontier / accessibility |
| Aug 2026 | Versioned collective memory snapshots |
| Sep 2026 | Public receipt (this repo) + research circuit |

See [`CHANGELOG.md`](./CHANGELOG.md).

## License

Copyright © 2026 Richard Bélisle (Tabarnakus).
See [`LICENSE`](./LICENSE) and [`NOTICE.md`](./NOTICE.md).
