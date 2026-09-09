# λ∥ — Longitudinal Stability

## Plain-language question

**How much is one agent's trajectory changing from round to round?**

λ∥ is a longitudinal Lyapunov-style observable applied to consecutive embeddings from the same agent.

For embeddings `e_0 ... e_(N-1)`, the implementation computes the mean logarithmic ratio between successive displacement magnitudes:

```text
λ∥ = mean_t log( ||e_t - e_(t-1)|| / (||e_(t-1) - e_(t-2)|| + ε) )
```

where `ε` is a small numerical stabilizer.

## Interpretation

In the implementation convention:

- **λ∥ < 0**: successive changes are shrinking; the trajectory is stabilizing.
- **λ∥ ≈ 0**: roughly neutral change scale.
- **λ∥ > 0**: successive changes are growing; the trajectory is becoming more divergent.

This is a temporal measurement **within one trajectory**. It is not the same as asking how far apart different agents are.

## Boundary

λ∥ does not determine whether the content of an agent's reasoning is true. A confidently stabilizing trajectory can stabilize around a false claim, and an unstable trajectory can contain useful correction or exploration.

T36 therefore treats λ∥ as an observable of deliberative dynamics, not as an epistemic score.
