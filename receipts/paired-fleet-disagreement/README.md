# Receipt 01: Paired fleet disagreement (aggregate reanalysis)

**Status: aggregate analysis reproduced, original experiment NOT independently replicated.**

This receipt checks one *observed* T36 result already described in [Part 5](../../series/part-05/README.md): in six matched market windows, the recorded NEW fleet showed higher **native directional disagreement** than the recorded OLD fleet. These six records were extracted from an existing private experiment summary rather than generated as synthetic examples. The underlying raw agent logs have **not** been independently reviewed.

## Run it offline

Python 3.10+ standard library only; no model key, provider access or network calls.

```bash
cd receipts/paired-fleet-disagreement
python3 reproduce.py
python3 -m unittest discover -s . -p 'test_*.py' -v
```

Expected: `6/6` positive paired differences; mean `+14.583333` percentage points (rounds to `+14.6`); exact two-sided Wilcoxon signed-rank `p=0.03125`, `W_min=0`. `RESULT.json` contains the reference output.

## Meaning of the data

- One row = one matched market window. Both fleets were evaluated on that window. Public IDs `W01`–`W06` are anonymized labels preserving the private source row order.
- `steps_per_condition` = 40 recorded steps for each fleet in each window.
- Split counts are derived from **recorded aggregate split rates**, not independently re-extracted here from raw event logs. Example: `35.0% × 40 = 14`.
- Rates were recorded as increments of 2.5 percentage points. Pairwise difference is NEW minus OLD.
- The exact p-value enumerates sign assignments over nonzero paired differences and requires independence/sign exchangeability assumptions. The six time windows may overlap or be correlated; that dependence has not been audited in this package. Treat the p-value as descriptive and unadjusted for any wider family of comparisons. The sample size for this paired test is **six windows**, not 480 independent steps.

## Provenance and boundary

The owner retains the non-public source report, derived aggregate JSON and raw experiment logs outside this public receipt. A reviewer can independently recompute **every statistic published here from the six released pairs**, but cannot yet independently reconstruct those pairs from original model responses. This is *analysis reproducibility*, not *experimental replication* or independent truth adjudication.

The underlying experiment changed fleet composition. Different models, lineages and provider routes are part of that comparison. This dataset cannot isolate a general causal effect of "fleet composition" or prove that one configuration is universally better.

**This receipt does NOT show:** a six-agent risk peak, a lineage-fence effect, reduced hallucinations, improved accuracy, or proven echo-chamber prevention.

See [Part 5 method](../../series/part-05/replay-design.md), [original public summary](../../series/part-05/disagreement-result.md) and [public statistical note](../../series/part-05/statistics.md).

## Next evidentiary upgrade

To call this a *raw-data reproduction*, first approve a privacy-reviewed, anonymized **per-step event extract** and release the split-classification rule, then rerun this analysis from those events and compare with the frozen aggregates. Do not leak private prompts, provider credentials, internal paths, model routing or unredacted responses.

## Corrected condition labels

The original version of the public Part 5 narrative used **homogeneous** and **heterogeneous** as shorthand. The reviewed non-public roster configuration and historical analysis specify two distinct three-model rosters (`OLD` and `NEW`), both containing different model families. That historical shorthand does not establish a controlled homogeneous-versus-heterogeneous experiment.

The public CSV therefore uses `old_split_count` and `new_split_count`. This terminology matches the recorded experimental contrast without exposing private model routing or raw agent content.
