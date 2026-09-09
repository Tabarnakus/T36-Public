# Why Tier 3 Was Silent

Tier 3 did not fail because the engagement gate was too strict. The blocking condition was the divergence window.

The observed real-fleet band on this domain lies predominantly below zero, with a reported median `lambda_perp = -0.171`, while Tier 3 requires:

`0 < lambda_perp < 0.15`

In other words, the controller was designed to fire in a pre-echo region that the tested fleet did not occupy under the default calibration.

There is a second measurement issue. On short technical rationales, raw `tau` sits on a lexical similarity floor near `0.698`, so the original `tau > 0.40` gate is satisfied almost whenever text is present. It therefore does not meaningfully discriminate engagement in this setting without lexical-floor correction and rescaling.

Under a fully recalibrated offline configuration, using corrected engagement and a shifted divergence scale, Tier 3 becomes reachable and fires on **17 of 117 replayed steps**.

That result must be interpreted narrowly:

- it shows reachability under an alternative scale choice;
- it does not validate the controller;
- the replay remains observe-only;
- the intervention is not delivered to the agents;
- no external outcome is measured against the recommendation.

So the scientific result is not “the regulator works.” It is that controller applicability itself depends on whether the fleet occupies the state space the controller assumes.
