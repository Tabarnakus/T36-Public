# Paired statistical test

The published historical comparison records 40 steps per fleet in each of six market windows. The analysis uses the **market window**, not each individual step, as the nominal paired unit (`n=6`).

- Direction: NEW split rate exceeds OLD in **6/6 windows**.
- Mean paired difference: **+14.583333 percentage points** (`+14.6` rounded).
- Exact two-sided Wilcoxon signed-rank: **W_min = 0, p = 0.03125** when sign assignments are exchangeable across independent pairs.

The public receipt recomputes the statistic directly from released historical aggregate counts. **A p-value is not proof the windows are independent.** Potential overlap, shared context, selection effects and multiple comparisons remain unverified. Read this p-value as a conditional, unadjusted descriptor, not a universal effect guarantee.

[Download and rerun the CSV analysis](../../receipts/paired-fleet-disagreement/README.md).
