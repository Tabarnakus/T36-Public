# T36 Doctrine: principles, checks and limits

Status: proposed public documentation revision, pending review. Audience: researchers and engineers. **Not a complete runtime specification.**

## What counts as evidence

**1+1=2:** facts require attributable sources; agreement among agents does not substitute for independent evidence. A public summary without raw data must be labeled accordingly. Neither a simulation, a passing unit test, nor an appealing analogy proves an empirical claim.

Use these distinct labels:

- **DESIGN PRINCIPLE:** rule proposed for engineering or governance, not automatically implemented.
- **MEASURED RESULT:** bounded observation with recorded sample, method and limitations.
- **REPRODUCED ANALYSIS:** someone can recompute a statistic from public inputs.
- **REPLICATED EXPERIMENT:** independent execution from sufficient raw inputs and frozen protocol.
- **OPEN HYPOTHESIS:** claim awaiting a suitable test.

## 1. Separate memory layers

| Layer | Responsibility | Ownership / boundaries |
|---|---|---|
| Agent-local | Working context and tentative hypotheses | Remains local to that agent; not a collective truth source |
| Institutional | Reviewed norms and approved policies | Controlled by explicit authorization |
| Append-only archive | Traceable historical evidence | Retain version and provenance; no silent rewrite |
| Collective memory (MC) | Narrow shared set of evidence-linked pinned facts | Admission checks and provenance required |

**Failure mode:** repeated agent opinions become institutional "facts" merely through reuse.

**Proposed control:** separate temporary hypotheses from explicit pins and keep all writes inspectable. This repository does not claim publicly verifiable deployment of all four layers.

**Relevant method:** [W3C PROV-O](https://www.w3.org/TR/prov-o/) formalizes relations among entities, activities and agents; it does not prove the T36 design.

## 2. Fence lineage before a shared write

A lineage fence is a proposed/implemented-in-private-project *validation boundary* that rejects a consolidated write when required provenance or identifiers are missing. In public examples, a pin should identify the claim, evidence source, domain, and supersession relationship where applicable.

Policy: fail closed on missing required fields; report `UNKNOWN` rather than guessing. An authorized retry may resolve missing context, but cannot invent a source.

**Failure mode:** source-free claims propagate into shared memory and later look independently confirmed.

**Evidence status:** public documentation describes this rule. No public experimental estimate of echo-reduction caused by the fence is yet provided. The aggregate fleet receipt measures a different treatment, fleet composition.

**Relevant method:** [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) establishes a provenance representation standard; it is not proof of a fence's efficacy.

## 3. Version and supersede, never silently erase

Every correction should preserve the prior version or an immutable reference to it and record what superseded it. A hash supports integrity relative to the recorded bytes, not correctness of the original assertion.

**Failure mode:** hidden overwrites make contradictions and post-hoc adjustments impossible to audit.

**Proposed verification:** deliberately mutate a pinned record; require a changed content hash and an explicit supersession event. Public demonstration code may verify this mechanical invariant, but does not establish scientific predictive value.

**Relevant method:** [Git object data model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects), which provides content-addressed history concepts. Application retention and access control are separate obligations.

## 4. External adjudication, with domain-specific labels

A fleet must not decide whether its own consensus was right solely by agreeing with itself.

In the market-based T36 experiments, models recorded directional choices before the outcome. A **later realized cryptocurrency market movement** provided a domain-specific outcome label at fixed horizons. A human separately adjudicated process risk, approval and governance. These two jobs are not one "market + human" truth score.

**Failure mode:** the same model family produces an answer, judges the answer and thereby launders internal agreement into external truth.

**Boundaries:** crypto-market outcome cannot validate medical advice, mathematical proofs or general reasoning; human review can also err. A model evaluator may be used for convenience but is not independent ground truth by default.

**Relevant method:** [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), a governance/measurement framework, not a market-adjudication protocol.

## 5. Monitor disagreement, echo and consensus separately

Disagreement is not necessarily good, and agreement is not necessarily correct. More deliberation rounds (`T↑`) or more agents can make interactions more complicated without demonstrating better outcomes.

Our [paired-fleet receipt](./receipts/paired-fleet-disagreement/README.md) reanalyses six recorded market windows: the comparison changes fleet composition; 6/6 windows show more native directional disagreement in the recorded NEW roster relative to OLD, with a +14.6 pp mean paired shift and exact Wilcoxon p=0.03125. This is **not evidence that the lineage fence improved anything** and **not evidence for a six-agent risk peak**.

**Failure modes:** conformity and premature consensus, noisy disagreement mistaken for diversity, confounded fleet comparisons, and misleading after-the-fact thresholds.

**External research context:** [Bellina et al., Conformity and Social Impact on AI Agents](https://arxiv.org/abs/2601.05384) reports conformity effects in specific studied models/tasks, not T36 measurements. See [Part 3](./series/part-03/README.md) and [Part 6](./series/part-06/README.md) for bounded T36 null results.

## Write path and review statuses

Proposed public sequence: **Finder → Reader → Verification (GREEN/YELLOW/RED) → Synthesis → human authorization**.

- **GREEN** means evidence passed a specified review; its source/criteria must be inspectable.
- **YELLOW** means unresolved, not accepted as verified doctrine.
- **RED** means rejected under specified review criteria.
- **UNKNOWN** is the proper outcome when retrieval or validation cannot resolve an assertion.

No claim of any numerical model-confidence threshold follows from these labels. Critically, **a GREEN label without a receipt is only a reported status**, not public reproducible evidence.

## Claims we explicitly do not make

- There is no validated universal maximum or "risk peak" of six agents.
- The six-window fleet-composition observation does not prove elimination of echo chambers or improvement in truth.
- A passing code test is not independent replication of an experiment.
- Private production code is not implicitly public, audited or certified.
- External papers motivate questions and methods; they do not validate T36 by association.

See [Glossary](./GLOSSARY.md) and [Research references](./RESEARCH-REFERENCES.md).
