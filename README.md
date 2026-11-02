# T36 Public

**Measuring reliability in multi-agent AI without confusing agreement with truth.**

T36 is an independent research and engineering project examining multi-agent disagreement, drift, memory provenance and external validation. This repository publishes **methods, bounded results and reproducibility materials**. The operational runtime, private prompts and raw response logs are not public.

**Start here:** [research results, Parts 1–8](./series/README.md) | [reproducible aggregate receipt](./receipts/paired-fleet-disagreement/README.md) | [glossary](./GLOSSARY.md)

> A documented result is not necessarily independently replicated. A successful software test does not establish scientific validity.

## Results: eight-part research series

| Part | What the public evidence establishes or leaves open | Details |
|---|---|---|
| **1. External adjudication** | Defines how recorded agent consensus is compared with later cryptocurrency-market outcomes; not a general truth oracle. | [Part 1](./series/part-01/README.md) |
| **2. Deliberation instruments** | Introduces longitudinal change (λ∥), inter-agent divergence (λ⊥) and an influence proxy (τ), none of which independently measure truth. | [Part 2](./series/part-02/README.md) |
| **3. Locked separation test** | **Null against the frozen threshold:** no tested instrument met the required silhouette CI lower bound of 0.15. H=3 contained **32 cases**; AUC 0.713 was not sufficient. | [Part 3](./series/part-03/README.md) |
| **4. Regime accessibility** | Synthetic calibration did not establish transferable real-fleet regime separation; the reported pooled silhouette was 0.005, below the threshold. | [Part 4](./series/part-04/README.md) |
| **5. Fleet-composition contrast** | The recorded NEW roster showed more native directional disagreement than the OLD roster in **6/6** matched market windows (**+14.6 percentage points on average**), with important sample and confounding limits. | [Part 5](./series/part-05/README.md) |
| **6. Form versus outcome** | The reported OLD/NEW cohorts showed different deliberation structure but no demonstrated gain in consensus-following market accuracy; every reported horizon/fleet cell was below 50%. | [Part 6](./series/part-06/README.md) |
| **7. Regulator scope** | The preventive Tier 3 controller did not activate in the default real-fleet configuration; closed-loop effectiveness remains unvalidated. | [Part 7](./series/part-07/README.md) |
| **8. Frozen Gate 8.4/8.4b** | **`N_crit = NULL`** under the frozen plateau-persistence rule. Neither proof of structural impossibility nor a successful validation. | [Part 8](./series/part-08/README.md) |

These are **scoped research reports**, not a single validated predictive or reliability system. Read each part's evidence map and claim boundary before generalizing.

## Run a real-data aggregate reanalysis

[**Receipt 01: paired fleet disagreement**](./receipts/paired-fleet-disagreement/README.md) contains six **sanitized, non-synthetic aggregate observations**, a CSV, a Python reproduction script, unit tests and expected output. The script independently recalculates **6/6 positive paired differences**, **+14.583333 percentage points** (NEW minus OLD) on average and an exact paired signed-rank **p = 0.03125** from the published values.

**Replication boundary:** the underlying agent-event logs are private and were not independently audited. This is a reproduction of an **aggregate analysis**, **not** reconstruction of all original events or replication of model runs. The six windows may be correlated; the reported p-value is conditional on independent/sign-exchangeable paired differences. It is not proof that a unique heterogeneity mechanism was identified, that echo chambers were eliminated or that model accuracy improved.

**Part 3 data availability:** the public H=3 summary includes 19 market-vindicated and 13 market-refuted cases, but does **not** provide 32 case-level feature vectors, outcomes and bootstrap sampling units. We cannot truthfully offer a reproducible Part 3 bootstrap without such a privacy-reviewed case-level export. **No synthetic reconstruction is substituted for missing observations.**

## Doctrine and engineering boundaries

1. **Provenance before shared-memory writes.** A lineage fence is an authorization rule, not an evidence-of-truth certificate.
2. **Version shared records instead of silently overwriting them.** Keep corrections and contradictions inspectable.
3. **Separate agent-local, institutional, archival and pinned collective memory.**
4. **Adjudicate outside the deliberating fleet.** The market supplies domain-specific delayed labels; humans determine acceptable risk and authorization.
5. **Treat convergence and agent count as variables to investigate, not validated universal risk thresholds.** No demonstrated six-agent risk peak is claimed.

These are research/engineering principles, not claims that the private runtime has been independently audited.

Read [the expanded doctrine](./DOCTRINE.md), [glossary](./GLOSSARY.md) and [research references](./RESEARCH-REFERENCES.md).

## Other public work

- [Gladi~US~](./gladius/README.md): adaptive human-AI collaboration workflow; its validation is separate from T36.
- [Reliability Lab research outlook](./RELIABILITY-LAB.md): research direction, not a shipped product.
- [Public Measurement & Methods Index](./PUBLIC-MEASUREMENT-INDEX.md): third-party methods and attribution, not T36 ownership claims.

## Public timeline

- **September 6, 2026:** initial public doctrine, scope and licensing.
- **September 9, 2026:** Parts 1–7 added as research/evidence packets.
- **September 12, 2026:** Part 8 null-result documentation and Gladi~US~ v1.1.
- **November 1, 2026:** Reliability Lab research outlook and public methods index.
- **November 2, 2026:** Receipt 01 aggregate reanalysis, series navigation and documentation revisions.

See [the changelog](./CHANGELOG.md) for dated repository milestones.

## Privacy, links and rights

Private orchestration, unpublished raw agent traces, credentials, internal bot configurations and operational thresholds stay private. A public receipt's missing raw records are disclosed rather than silently replaced. Publishing aggregate statistics does not establish independent reproduction of the original experiment.

X: [@Tabarnackus](https://x.com/Tabarnackus).

Copyright © 2026 Richard Bélisle (Tabarnakus). See [LICENSE](./LICENSE) and [NOTICE.md](./NOTICE.md).
