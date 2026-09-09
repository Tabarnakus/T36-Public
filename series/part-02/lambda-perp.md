# Lambda transverse: inter-agent divergence

## Plain-language question

**How far apart are the agents at the same point in the deliberation?**

Lambda transverse is computed from pairwise distances between agent representations in a shared embedding space.

For N agent embeddings at the same round, the implementation averages the logarithm of each pairwise distance after normalization by a reference distance.

## Interpretation

Under this implementation convention:

- larger values correspond to greater separation among agent representations;
- strongly negative values correspond to agents collapsing toward the same region of representation space.

This therefore measures **inter-agent geometry**, not correctness.

## Why it needs context

High divergence can mean productive diversity, persistent disagreement, noise, or incompatible reasoning. Low divergence can mean legitimate convergence or premature collapse.

For that reason, this observable is not interpreted alone. T36 pairs geometry with other observables such as tau and, separately, with external adjudication.

## Boundary

Agents can converge on a shared false claim or remain separated while one agent is correct. This metric has no built-in access to factual truth.

Its job is narrower: describe the geometry of the deliberation so that the relationship, if any, between that geometry and external validity can be tested rather than assumed.
