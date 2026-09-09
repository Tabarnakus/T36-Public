# AUC 0.713 vs Silhouette -0.026

The ten-dimensional trajectory descriptor is the one Part 3 quantity that looks numerically interesting at first glance:

- **AUC = 0.713**
- **silhouette = -0.026**
- **95% bootstrap CI = [-0.026, 0.059]**
- **Mann–Whitney p = 0.084**
- **N = 32**

These statistics answer different questions.

## AUC

AUC asks whether a score tends to rank one externally labeled group above the other.

A moderate AUC can therefore arise from a weak monotone tendency even when the groups do not form cleanly separated regions in feature space.

## Silhouette

Silhouette asks whether the labeled groups form separable clusters relative to their within-group and between-group geometry.

Here, the silhouette is slightly negative and its confidence interval remains far below the pre-specified 0.15 lower-bound criterion.

## Why this was not called a discovery

The rank test does not reach conventional significance at this sample size (`p = 0.084`), and the locked separation criterion is not met.

The appropriate interpretation is therefore:

> **interesting enough to replicate with more data, not strong enough to claim as a discovery.**

Reporting the AUC rather than omitting it preserves the potentially useful signal while keeping the evidential standard unchanged after seeing the result.
