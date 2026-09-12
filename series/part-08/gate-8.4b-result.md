# Gate 8.4b Scientific Result

## Decision

`N_crit (8.4b) = NULL`

Parent Gate 8.4 remains `N_crit = NULL` and is not reinterpreted.

## Frozen run conditions

- Instrument: `trajectory_mapping.gate84`
- Frozen manifest: `a14a3b3a56f7fbab0b7cf389c302985d2420e48cf8aae8920c8087b90bf30918`
- Seeds: `S = 30`
- N-grid: frozen
- `gamma in [0, 2]`, step `0.01`
- No MiniLM
- No threshold retuning
- No seed removal
- No extrapolation beyond `N = 2500`

## Decision logic

No sequence of three consecutive `PASS_total` plateaus was found.

- `PASS_DKW = true` across the full grid.
- Censor ceiling `c <= 0.60` = true across the full grid.
- Censor stability `max(c) - min(c) <= 2 epsilon_N` = true from `N = 250` onward.
- The blocking condition is the relative plateau threshold `0.05` combined with persistence `= 3`.

Isolated `PASS_total` values:

| N | PASS_total |
|---:|:---:|
| 400 | PASS |
| 630 | PASS |
| 1250 | PASS |
| 2000 | PASS |

Never three consecutively.

## Boundary observations

Observed breakpoint fraction was approximately `0.55–0.56`.

Mean censoring remained approximately `0.44` even at `gamma_max = 2`.

The latent tail beyond `gamma_max` is not identified.

## Interpretation

The follow-up does not confirm that the original Gate 8.4 NULL was caused by a sparse grid or too-small S.

It also does not establish structural failure.

Gate 8.4b is a new experiment. Gate 8.4 remains immutable.

The correct public status is therefore:

**NULL under the frozen rule.**
