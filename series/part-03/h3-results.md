# Locked H=3 Results

The table below reports the locked corpus at **H = 3**, with:

- **N = 32** total specimens
- **19 market-vindicated consensus cases**
- **13 market-refuted consensus cases**

| Instrument | Space | Silhouette | 95% bootstrap CI | AUC | Mann–Whitney p |
|---|---|---:|---|---:|---:|
| `premise_coherence` | concept | -0.013 | [-0.236, 0.087] | 0.587 | 0.38 |
| `premise_contradiction` | concept | -0.065 | [-0.323, 0.300] | 0.510 | 0.12 |
| `covert_contradiction` | concept | -0.053 | [-0.193, 0.020] | 0.510 | 0.33 |
| λ⊥ (step) | response | +0.005 | [-0.027, 0.121] | 0.514 | 0.091 |
| trajectory descriptor (10-D) | response | -0.026 | [-0.026, 0.059] | 0.713 | 0.084 |

## Decision against the fixed criterion

The required condition was:

> lower bound of the 95% silhouette interval ≥ 0.15

None of the instruments satisfied it.

The same qualitative null held on the expanded corpus and at **H = 1** and **H = 5**.

## Important nuance

For four of the five instruments shown above, the upper confidence bound remains below 0.15, which argues against a separation of the pre-specified magnitude in this sample.

`premise_contradiction` is different: its interval extends to 0.300, so the data are too imprecise to exclude a moderate effect for that instrument. This is a power limitation, not evidence of a positive result.
