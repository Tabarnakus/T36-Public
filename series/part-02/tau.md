# τ — Engagement / Influence Proxy

## Plain-language question

**Does an agent's current position appear aligned with context produced by its peers in the previous round?**

In the implementation used here, τ is a cosine-similarity engagement coefficient:

```text
τ_t(i) = cosine_similarity(
    e_t(i),
    mean_j≠i(e_(t-1)(j))
)
```

It compares the focal agent's current embedding with the mean of the other agents' previous-round embeddings.

The coefficient lies in `[-1, 1]` under cosine similarity.

## Interpretation

Higher τ means the focal agent's current representation is more aligned with the peers' immediately preceding context.

That makes τ useful as an **engagement / following proxy** when interpreted alongside inter-agent divergence. It helps distinguish agents that remain different while engaging with peers from agents that simply remain disconnected.

## Important limitation

τ is not proof of causal influence.

Semantic similarity can arise from shared prompts, shared priors, common evidence, lexical overlap, or other common causes. The metric therefore measures an observable signature consistent with engagement; stronger causal claims require experimental controls.

## Boundary

High engagement does not imply correctness. Agents can influence one another toward a false consensus. Low engagement does not imply error.

As with λ∥ and λ⊥, τ describes the deliberative process. External validity remains a separate measurement.
