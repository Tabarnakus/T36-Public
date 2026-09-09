# OrbitalRegulator

The OrbitalRegulator is a proposed **observe-only** intervention architecture. It monitors deliberative dynamics and returns recommendations; in the experiments reported here, those recommendations are not delivered back to the agents.

Its strongest preventive tier is Tier 3.

Tier 3 requires all of the following:

1. Tier 2 is armed from a sufficiently negative recent slope in inter-agent divergence.
2. The current divergence lies in the pre-echo interval:

   `0 < lambda_perp < 0.15`

3. Engagement exceeds the gate:

   `tau > 0.40`

The intended interpretation is preventive rather than corrective: the system must still have measurable divergence left to lose, while already moving toward collapse.

The gate values and timing were calibrated on a synthetic campaign rather than fitted to the real LLM corpus. This makes the controller's applicability an empirical question, not an assumption.

The regulator therefore has explicit scope conditions:

- the fleet must reach a defensible healthy regime;
- a traversable pre-echo interval must exist;
- the reference distance used by `lambda_perp` must be anchorable to that regime.

If those conditions fail, the controller has no validated state to defend.
