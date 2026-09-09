# X Series — Part 3: The First Surprise

Part 3 asks whether any measured internal signature separates consensus cases that are later **vindicated** from those later **refuted** by the external market outcome.

The answer in the tested data is **no**.

A separation criterion had been fixed before reading this result:

> **The 95% bootstrap confidence interval for silhouette separation must have a lower bound of at least 0.15.**

Across the tested concept-space and response-space instruments, no instrument met that criterion at any adjudication horizon.

One response-space trajectory descriptor produced a numerically interesting ranking result:

- **AUC = 0.713**
- **silhouette = -0.026**
- **95% bootstrap CI = [-0.026, 0.059]**
- **Mann–Whitney p = 0.084**
- **N = 32** at H=3

Because the pre-specified separation criterion was not met, this value is reported as a **replication target**, not as a discovery.

## Evidence map

- [`separation-criterion.md`](./separation-criterion.md) — the fixed decision rule.
- [`h3-results.md`](./h3-results.md) — locked-corpus H=3 results.
- [`auc-vs-silhouette.md`](./auc-vs-silhouette.md) — why AUC 0.713 did not override the separation criterion.
- [`claim-boundary.md`](./claim-boundary.md) — what this null result does and does not establish.

## Reading rule

A promising number is not automatically a finding.

**pre-specified criterion first, interpretation second**
