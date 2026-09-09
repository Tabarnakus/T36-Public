# Bidirectional same-window replay design

The purpose of this experiment is to isolate the effect of **fleet composition** from ordinary market-window variation as much as the available design allows.

## Core design

Six real market windows were evaluated by both fleet configurations.

The comparison is paired by market window:

- same underlying market interval;
- same task framing and directional-decision objective;
- same measurement pipeline;
- same disagreement definition;
- fleet composition changed between conditions.

The analysis therefore asks whether the disagreement rate shifts within the same market context when the fleet changes.

## Why this is stronger than an unpaired fleet comparison

If one fleet were tested on one set of windows and another fleet on different windows, any disagreement difference could simply reflect easier, harder, calmer, or more ambiguous markets.

Replaying the same windows under both fleet configurations removes that between-window explanation from the primary contrast.

## What remains uncontrolled

This is not a capability-matched intervention on a single abstract variable called “heterogeneity.” The compared fleets also differ in model family, vendor, lineage, and capability profile.

The experiment therefore supports a causal statement about the **tested fleet-composition intervention under matched market windows**, not a universal claim that heterogeneity itself is the unique mechanism.