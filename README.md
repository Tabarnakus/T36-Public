# T36 Public

**Measuring reliability in multi-agent AI without confusing agreement with truth.**

**1+1=2.** Agreement is observable. Truth needs an independent check.

T36 is an independent research and engineering project exploring how AI agents disagree, converge, drift, and pass information through shared memory. When a fleet reaches consensus, has it found evidence, or built **an echo with extra steps**?

**Start here:** [Eight research parts](./series/README.md) · [Receipt 01: reproduce the numbers](./receipts/paired-fleet-disagreement/README.md) · [Glossary](./GLOSSARY.md)

## Eight parts. Recorded results, including the nulls.

| Part | What happened | Explore |
|---|---|---|
| **1 · The question** | Freeze the agents' decision, then compare it with a later market outcome. | [External adjudication](./series/part-01/README.md) |
| **2 · The instruments** | Track temporal change (λ∥), divergence (λ⊥), and an influence proxy (τ). | [Dynamics](./series/part-02/README.md) |
| **3 · First surprise** | **Null result:** no tested signature met the frozen separation threshold. H=3 included 32 cases. | [Locked test](./series/part-03/README.md) |
| **4 · The wrong region?** | Real-fleet regime silhouette **0.005**, below the practical **0.15** criterion. | [Regime accessibility](./series/part-04/README.md) |
| **5 · Change the fleet** | In **6/6** paired windows, NEW showed more native directional disagreement than OLD: **+14.6 percentage points** on average. | [Fleet contrast](./series/part-05/README.md) |
| **6 · Form is not validity** | Deliberation structure changed, but improved market-following accuracy was **not demonstrated**. | [Outcome comparison](./series/part-06/README.md) |
| **7 · The silent regulator** | Preventive Tier 3 did not activate in the default real-fleet operating region. | [Controller scope](./series/part-07/README.md) |
| **8 · A frozen null** | No defensible critical reference-population size: **`N_crit = NULL`** under the fixed Gate 8.4/8.4b rule. | [Frozen gate](./series/part-08/README.md) |

Each part includes the methods, evidence, and conditions under which its conclusions hold. These are bounded observations, not a universal reliability score.

## Check the evidence yourself

[**Receipt 01: paired fleet disagreement**](./receipts/paired-fleet-disagreement/README.md) publishes six sanitized historical aggregate pairs, an offline Python reproduction, tests, and SHA-256 checksums.

```bash
cd receipts/paired-fleet-disagreement
python3 reproduce.py
python3 -m unittest discover -s . -p 'test_*.py' -v
```

Expected: **6/6** positive paired differences, **+14.583333 pp** mean, exact two-sided signed-rank **p = 0.03125**. At six windows, this is a fragile finding: deleting any one yields **p = 0.0625**. The [receipt](./receipts/paired-fleet-disagreement/README.md) explains the assumptions and the distinction between recomputing aggregates and independently reproducing model runs.

**Next evidentiary upgrade:** a privacy-reviewed, per-step extract that lets outsiders reconstruct the six published aggregates.

## The engineering idea

**Provenance before propagation.** Treat a shared-memory write as a controlled operation, not as automatic proof. Keep source, version, supersession and independent adjudication visible.

**No silent threshold retuning.** A null result stays null until a separately specified experiment earns a different result.

Read the [doctrine](./DOCTRINE.md), [research references](./RESEARCH-REFERENCES.md), and [public measurement methods index](./PUBLIC-MEASUREMENT-INDEX.md).

## Also in this repository

[Gladi~US~](./gladius/README.md) is an adaptive human-AI collaboration workflow. The [Reliability Lab](./RELIABILITY-LAB.md) describes future engineering directions; it is not a shipped validation result.

**Research timeline:** [September–November 2026 milestones](./CHANGELOG.md).

The operational runtime, private prompts, raw response logs and credentials remain private.

**X:** [@Tabarnackus](https://x.com/Tabarnackus) · **Copyright © 2026 Richard Bélisle (Tabarnakus)** · [License](./LICENSE) · [Notice](./NOTICE.md)
