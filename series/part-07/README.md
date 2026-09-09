# Part 7 — The Regulator That Did Not Fire

Part 7 asks a different question from Parts 1–6.

If deliberative form can be measured, can it also be regulated?

T36 proposes an observe-only controller, the **OrbitalRegulator**, that watches trajectory dynamics and recommends intervention only when a specific pre-echo state is detected. It is not a truth detector, and in the experiments reported here it is not validated as a closed-loop controller.

The key result is negative but informative: the strongest preventive tier, Tier 3, did **not fire** on the default real-fleet configuration because the fleet did not occupy the divergence interval the controller was designed to defend.

This is not controller failure in the ordinary sense. It is a scope-condition failure: the controller's target state was not present in the measured operating region.

## Evidence map

- `orbital-regulator.md` — what the regulator measures and what Tier 3 requires.
- `observed-activity.md` — what actually fired in live and replay runs.
- `why-tier3-was-silent.md` — why the strongest tier did not activate.
- `claim-boundary.md` — what this does and does not establish.

## Reading rule

**Reachable under recalibration ≠ validated intervention.**

A controller can only regulate a state that the fleet actually occupies. If the target pre-echo region is absent, the correct conclusion is not to silently redefine the regime after the fact. The preconditions must be tested first.

This closes the first T36 arc with a change in emphasis: before trying to control reasoning trajectories, we first need to map which trajectories and transition regions real fleets can actually reach.
