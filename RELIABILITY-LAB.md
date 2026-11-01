# Beyond the Final Answer: Measuring AI Agent Reliability

**Can we detect when an AI agent is drifting, becoming overconfident, or reinforcing an error before the final answer fails?**

That is the research question behind the **T36 Reliability Lab** concept.

AI agents are increasingly asked to complete long tasks, use tools, maintain state and collaborate. A convincing final answer does not necessarily tell us whether the underlying process was reliable.

We want to study the **trajectory of the work**, not just its final output.

## The research directions

### 1. Reproducible agent benchmarks
Compare the same model under different controlled workflows. Freeze tasks and evaluation criteria before running experiments; preserve version information, costs, failures and disagreements. A successful test harness is not evidence that any protocol improves a model.

### 2. A library of reproducible failures
Turn well-documented failures into regression tests: goal drift, unsupported claims, context contamination, improper tool assumptions, authorization errors and recovery breakdowns. Useful negative results are research assets.

### 3. Reliability monitoring
Explore whether repeated tests and execution traces can reveal regressions across model or workflow versions. Separate measurable task success from mere adherence to instructions.

### 4. Cognitive Weather (concept)
A public, evidence-linked observatory of how agent configurations behave across standardized tasks. No fabricated rankings or universal intelligence scores; only scoped measurements, uncertainty and methodological limitations.

### 5. Independent control layers (research direction)
Investigate whether external checks, state transitions and permission boundaries can prevent certain agent failures. Such controllers would need explicit invariants and independent verification; probabilistic confidence alone cannot guarantee safety.

### 6. Dynamics of cognitive trajectories (long-horizon hypothesis)
Explore whether convergence, divergence, influence and goal-drift signals can predict failures **before** they appear in final outputs. Predictive value, transferability and causal interpretation remain open questions.

## How we intend to distinguish evidence from ideas

| Label | Meaning |
|---|---|
| **Concept** | An idea worth exploring, not an implemented feature |
| **Prototype** | A functioning artifact without established external reliability |
| **Benchmark result** | A scoped, versioned observation with methodology and limitations |
| **Replicated result** | A result reproduced under separately documented conditions |
| **Open hypothesis** | A claim whose validity has not yet been demonstrated |

We will not present theoretical analogies as established physical laws of AI reasoning. Consensus among agents does not establish factual correctness. A negative result does not disappear because it is inconvenient.

## What is available today?

This repository provides public T36 research notes, definitions, methodological boundaries and related documentation. The reliability product described here is a **research and engineering direction**, not an announced commercial release.

See the [public research series](./series/part-01/README.md) and [research doctrine](./DOCTRINE.md) for background.

Private runtime code, raw experimental traces, credentials, internal configurations and unreleased evaluations are **not** part of this public repository.

## Who might find this useful?

- Developers running long-lived agents and tool-using workflows
- Researchers working on agent evaluation, robustness and multi-agent dynamics
- Teams looking for reproducible regression tests
- People interested in control theory applied carefully to AI systems

## Follow or collaborate

Interested in measurable agent reliability rather than benchmark theater?

Read the public material, challenge a falsifiable claim, suggest an objective test or share a reproducible failure case **without confidential data**.

Find project updates at [@Tabarnackus on X](https://x.com/Tabarnackus).

**Our guiding question:** What would it take to know that an AI system is getting *more reliable*, rather than merely sounding more confident?

---

*Research outlook • November 2026. Ideas above are not claims of validated predictive capability or production safety.*

*Copyright © 2026 Richard Bélisle (Tabarnakus). Subject to this repository's [license](./LICENSE) and [notice](./NOTICE.md).*
