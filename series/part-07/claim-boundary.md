# Claim Boundary

## Supported by the reported evidence

- The OrbitalRegulator can be instrumented in observe-only mode on real multi-agent deliberation traces.
- Under the default tested configuration, Tier 3 did not fire in either the live interactive runs or the offline replay.
- The blocking condition was the `lambda_perp` pre-echo interval, not evidence of a successful intervention.
- A recalibrated offline configuration can make Tier 3 reachable.
- Controller applicability is therefore fleet- and calibration-dependent.

## Not established

The evidence does **not** establish that:

- the OrbitalRegulator improves deliberation quality;
- Tier 3 prevents echo collapse;
- Tier 3 improves external validity;
- the synthetic thresholds transfer universally to real LLM fleets;
- recalibration constitutes validation;
- a controller should be deployed on a fleet that does not occupy the assumed healthy/pre-echo regime.

## Strongest interpretation

This part is a scope-condition result, not an intervention-success result.

The proposed controller was aimed at a transition region that the tested fleet did not naturally traverse under the default calibration. That is a reason to map reachable trajectories and transition regions before attempting closed-loop control.

The next scientific question is therefore cartographic before it is regulatory: **what trajectory regions do real fleets actually occupy, how do they move between them, and which transitions are reproducible enough to justify intervention?**
