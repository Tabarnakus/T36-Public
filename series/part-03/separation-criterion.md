# Separation Criterion

Part 3 tests whether internal deliberative measurements separate consensus cases that are later vindicated from those later refuted by the external adjudicator.

For each instrument and horizon, the analysis uses:

- silhouette coefficient between the two externally labeled groups;
- 95% confidence intervals from **600 bootstrap resamples**;
- area under the ROC curve (AUC);
- a Mann–Whitney rank test.

The decision rule was fixed before reading the Part 3 result:

> **A result meets the separation criterion only if the lower bound of the 95% bootstrap confidence interval for silhouette reaches 0.15.**

The threshold was inherited from earlier analyses of the system and applied unchanged here.

This matters because it prevents a numerically attractive statistic from replacing the rule after the result is known.

## Why silhouette is central here

The question in Part 3 is not merely whether one scalar can weakly rank two groups. It is whether the internal measurement produces a sufficiently separable structure between externally vindicated and externally refuted cases.

AUC and rank tests are therefore reported as complementary diagnostics, but they do not override the locked silhouette criterion.
