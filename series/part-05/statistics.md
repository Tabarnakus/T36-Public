# Paired statistical test

The published historical comparison records 40 steps per fleet in each of six market windows. The analysis uses the **market window**, not each individual step, as the nominal paired unit (`n=6`).

- Direction: NEW split rate exceeds OLD in **6/6 windows**.
- Mean paired difference: **+14.583333 percentage points** (`+14.6` rounded).
- Exact two-sided Wilcoxon signed-rank: **W_min = 0, p = 0.03125** when sign assignments are exchangeable across independent pairs.

The public receipt recomputes the statistic directly from released historical aggregate counts. **Leave-one-window-out sensitivity:** dropping any single window leaves five positive differences, but the exact two-sided signed-rank p-value becomes **0.0625** in every one of the six leave-one-out checks. This illustrates the fragility of conventional 0.05 significance at n=6; it is not a validation of window independence.

**A p-value is not proof the windows are independent.** Potential overlap, shared context, selection effects and multiple comparisons remain unverified. Read this p-value as a conditional, unadjusted descriptor, not a universal effect guarantee.

[Download and rerun the CSV analysis](../../receipts/paired-fleet-disagreement/README.md).
