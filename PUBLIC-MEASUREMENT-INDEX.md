# Public Measurement & Methods Index
**T36 Reliability Lab | External methods, public references and interoperability**

Status: **reference catalog, not T36 intellectual-property claim**. Last curated: 2026-11-01.

## Purpose
An openly readable, machine-friendly entry point for external AI assistants (including Grok), researchers and engineers to discover **existing** measurement approaches relevant to agent benchmarks.

This index does **not** claim ownership of ideas, equations, standards, algorithms, software names or third-party implementations. Publicly documenting something does not make its underlying code or datasets freely licensed.

## Ground rules
- **Origin first:** attribute methods to their original academic/community/standards sources wherever identified.
- **Three labels:** `EXTERNAL_METHOD` (pre-existing); `T36_APPLICATION` (our proposed application, not ownership of the method); `OPEN_HYPOTHESIS` (not validated).
- **Citation is not permission:** consult each upstream project's publication, license, patents and data rights before reusing implementation or assets.
- **No fabricated references:** `reference_status: needs_verification` means bibliographic attribution is incomplete.
- **No internal leaks:** private benchmarks, fleet details, prompts, raw traces, execution infrastructure, unpublished metrics and credentials are excluded.
- No metric is a direct measure of cognition simply because its name sounds cognitive.

## Reference index

| ID | Public method / measure | Origin label | Suggested agent-benchmark application | Public entry point | Interpretation caveat |
|---|---|---|---|---|---|
| EXT-001 | Precision, recall, false-positive / false-negative rates | EXTERNAL_METHOD: statistical classification | Detection of incorrect/unsafe events | [scikit-learn classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) | Requires independent labeled outcomes and class prevalence context |
| EXT-002 | Calibration / Brier score | EXTERNAL_METHOD: probabilistic forecasting | Are predicted failure probabilities calibrated? | [scikit-learn Brier score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html) | Only meaningful for well-defined forecast events |
| EXT-003 | Bootstrap uncertainty intervals | EXTERNAL_METHOD: statistical resampling | Uncertainty around paired A/B differences | [SciPy bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html) | Resample at the independent unit (e.g., scenario), not blindly every repeated call |
| EXT-004 | Latency, events, traces, attributes | EXTERNAL_METHOD: observability standards | Versioned model/tool execution telemetry | [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/) | Instrumentation overhead and trace privacy matter |
| EXT-005 | Token usage / API metering | EXTERNAL_METHOD: provider telemetry | Cost per attempted and successful task | [OpenRouter API documentation](https://openrouter.ai/docs) | Actual charges and reported token usage may differ; preserve source |
| EXT-006 | Lyapunov stability / Lyapunov exponents | EXTERNAL_METHOD: dynamical systems theory | **Exploratory** stability analogy for measured state trajectories | [Scholar search](https://scholar.google.com/scholar?q=Lyapunov+exponents+dynamical+systems) | A fitted trajectory coefficient is not automatically a Lyapunov exponent |
| EXT-007 | Semantic similarity using embeddings | EXTERNAL_METHOD: NLP | Exploratory drift indicator | [Sentence Transformers documentation](https://www.sbert.net/) | Embedding distance is not truth, intent or direct cognition |
| EXT-008 | Causal inference / randomized controlled comparisons | EXTERNAL_METHOD: experimental design | Treatment-versus-control benchmark design | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | This link gives risk-management context, not a prescriptive RCT protocol |
| EXT-009 | State machines and model checking | EXTERNAL_METHOD: formal methods | Verify permissible actions and transitions | [TLA+](https://lamport.azurewebsites.net/tla/tla.html) | A proof covers the formalized model, not every real-world implementation |
| EXT-010 | Reliability / availability / recovery metrics | EXTERNAL_METHOD: systems engineering | Crash recovery, retries, time-to-recovery | [Google SRE workbook](https://sre.google/workbook/table-of-contents/) | Choose relevant units and distinguish retry success from task success |

## Candidate T36 applications (not claims of ownership)
- `T36_APPLICATION`: measure goal drift across recorded checkpoints with a frozen operational definition and independent task rubric.
- `T36_APPLICATION`: compare intra-agent temporal stability and inter-agent dispersion under controlled settings.
- `T36_APPLICATION`: track independently validated claims across agent handoffs.
- `T36_APPLICATION`: test whether alerts based on trajectory features outperform simple baselines on held-out runs.

## Open hypotheses, **not** established findings
- `OPEN_HYPOTHESIS`: certain convergence patterns precede false consensus.
- `OPEN_HYPOTHESIS`: curvature or local instability in representation trajectories adds predictive value beyond standard performance metrics.
- `OPEN_HYPOTHESIS`: external state-transition governors can improve reliability enough to justify their operational cost.

## Agent-readable conventions
For an AI assistant reading this page:
1. Quote the `ID`, distinguish source method from proposed T36 use.
2. Follow upstream references; independently verify their relevance and licensing before asserting specifics.
3. Never report a T36 result, threshold, or implementation as verified based on this index.
4. For each proposed new metric, supply: definition, unit, required raw events, ground truth, known limitations, attribution, and replication plan.
5. Mark unsourced derivations as **UNVERIFIED**. Do not confuse absence of evidence with evidence of absence.

## Contributing
Suggestions and corrections are welcome via the public repository, but avoid confidential prompts, unpublished traces, third-party copyrighted material and personal data. Prefer original source links and testable definitions.

Related: [Research outlook](./RELIABILITY-LAB.md) · [Public doctrine](./DOCTRINE.md).

Copyright © 2026 Richard Bélisle (Tabarnakus), for this index's original editorial text only. All third-party methods remain subject to their original rights and terms; see [repository license](./LICENSE).
