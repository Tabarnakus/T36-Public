# Part 8 — The Map Did Not Earn an Ncrit

Part 8 asks whether the restricted trajectory map stabilizes strongly enough, under the frozen Gate 8.4 rule, to justify a defensible critical reference-population size `N_crit`.

The answer is **NULL**.

Gate 8.4 and its follow-up Gate 8.4b were evaluated without threshold retuning, seed removal, representation transfer, or extrapolation beyond the frozen N-grid.

The result is not a disguised PASS and not a structural FAIL.

It is a frozen NULL.

## What passed

- DKW condition: PASS across the full tested grid.
- Censor ceiling `c <= 0.60`: PASS across the full tested grid.
- Censor stability: PASS from `N = 250` onward.

## What prevented Ncrit

The relative plateau rule required three consecutive `PASS_total` plateaus.

Isolated `PASS_total` values occurred at:

- `N = 400`
- `N = 630`
- `N = 1250`
- `N = 2000`

Never three consecutively.

Therefore no defensible `N_crit` was identified under the frozen rule.

## Frozen decision

**Gate 8.4 parent: `N_crit = NULL`.**

**Gate 8.4b: `N_crit = NULL`.**

Gate 8.4 remains immutable and is not reinterpreted after the follow-up run.

## What this does not establish

This result does **not** show that the trajectory map is structurally impossible.

It does **not** show that the original NULL was merely caused by a sparse grid or too few seeds.

It does **not** identify the latent breakpoint tail beyond `gamma_max`.

It does **not** establish representation transfer.

## Prohibited operations confirmed

- MiniLM: not invoked
- Q0.0 representation transfer: not run
- Gate 8.4 mutation: none
- Plateau / alpha / censor ceiling / N / seed retuning: none
- Seed removal: none

## Next question

The next question is separate from Gate 8.4:

> Does any trajectory structure survive a real change of representation?

Control remains downstream.

## Evidence map

- `gate-8.4b-result.md` — scientific result and frozen decision.
- `claim-boundary.md` — what the NULL result allows and forbids us to claim.
