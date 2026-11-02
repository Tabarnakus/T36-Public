# Bidirectional same-window replay design

The **recorded intervention** compares two named, three-model rosters, `OLD` and `NEW`, on six market windows (three selected from each source cohort). Both rosters have members from multiple model families.

For each window, the historical analysis reports the same market context, task framing, measurement pipeline and 40 steps per roster, while the **fleet roster** changes.

This is stronger than comparing unrelated market windows, but **not** a single-variable manipulation of "heterogeneity": model identity, training lineage, capabilities, vendors and routing differ. The raw historical logs were not independently inspected in this public audit, so exact window non-overlap, execution-order effects and source-event integrity remain unverified.

**The robust unit of interpretation is an observed contrast between these specific OLD/NEW fleet configurations, not a general law of multi-agent diversity.** See [Receipt 01](../../receipts/paired-fleet-disagreement/README.md) for the released aggregate reanalysis.
