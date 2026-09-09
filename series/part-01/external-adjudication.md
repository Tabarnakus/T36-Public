# External Adjudication

## Plain-language version

A group of AI agents cannot be allowed to declare its own consensus "correct" merely because the agents agree.

For the market-grounded T36 experiments, the adjudicator is a later market outcome. The agents deliberate using information available at the decision point; the future price movement is observed afterward.

This creates a temporal separation:

**deliberation → recorded decision → future observation → adjudication**

## Why use a market?

Short-horizon cryptocurrency data provides three useful experimental properties:

- the observation available to the agents can be bounded in time;
- the agents' judgment can be recorded before the future outcome occurs;
- the later price movement is external to the deliberating fleet.

The market is therefore used as an **external outcome source**, not as an internal evaluator and not as an agent vote.

## Directional adjudication

At a fixed evaluation horizon, the realized price movement supplies the external direction. A recorded directional consensus can then be compared with that realized direction and classified as externally vindicated or externally refuted under the experiment's directional rule.

The important methodological invariant is that the fleet does not assign its own verdict after seeing its deliberation.

## What this does not establish

Market adjudication is domain-specific. A result in this environment should not automatically be generalized to medicine, law, factual QA, mathematics, or other domains with different external judges.

The purpose of the market experiment is narrower: test whether internal deliberative dynamics carry information about an outcome that is decided outside the multi-agent system.

## Implementation provenance

The private experimental harness is observe-only: it reads market data, records agent outputs and dynamical measurements, and logs later market outcomes. It does not place orders, trade, or access a wallet.

Only the public methodological description required to evaluate the X-series claims is reproduced here; private orchestration and unrelated research code remain outside this repository.
