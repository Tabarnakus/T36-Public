#!/usr/bin/env python3
"""Offline, dependency-free reanalysis of published T36 paired aggregate counts.

These OLD/NEW historical fleet counts are derived aggregate observations, not synthetic examples. This script
DOES NOT reproduce the original API runs or independently validate the source logs.
"""
from __future__ import annotations
import csv
import itertools
import json
from fractions import Fraction
from pathlib import Path

CSV = Path(__file__).parent / 'data' / 'sanitized-window-counts.csv'


def load_rows(path: Path = CSV):
    with path.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        expected = ['window', 'steps_per_condition', 'old_split_count', 'new_split_count']
        if reader.fieldnames != expected:
            raise ValueError('Unexpected CSV schema')
        out = []
        ids = set()
        for r in reader:
            w = r['window']
            if not w or w in ids:
                raise ValueError('Missing or duplicate window ID')
            ids.add(w)
            n, a, b = (int(r[k]) for k in expected[1:])
            if not 0 < n <= 100_000 or not (0 <= a <= n and 0 <= b <= n):
                raise ValueError('Impossible counts or denominator')
            out.append((w, n, a, b))
    if not out:
        raise ValueError('No paired observations')
    return out


def exact_wilcoxon_two_sided(deltas):
    """Enumerate 2**n sign assignments on nonzero differences.

    Average ranks for tied absolute differences. Assumes independent pairs and
    sign exchangeability under the null; returns exact conditional p-value.
    """
    nonzero = [Fraction(d) for d in deltas if d]
    if not nonzero:
        raise ValueError('All-zero differences: no signed-rank test')
    if len(nonzero) > 20:
        raise ValueError('Exact sign enumeration limited to n<=20')
    absvals = list(map(abs, nonzero))
    ranks = []
    for a in absvals:
        lower = sum(x < a for x in absvals)
        equal = sum(x == a for x in absvals)
        ranks.append(Fraction(2 * lower + equal + 1, 2))
    total = sum(ranks)
    positive = sum(rank for rank, d in zip(ranks,nonzero) if d > 0)
    observed_min = min(positive,total-positive)
    extreme = 0
    for mask in itertools.product([False, True],repeat=len(ranks)):
        wplus = sum(rank for rank,yes in zip(ranks,mask) if yes)
        if min(wplus,total-wplus) <= observed_min:
            extreme += 1
    return {'W_min': float(observed_min),
            'p_two_sided_exact': float(Fraction(extreme,2**len(nonzero))),
            'nonzero_pairs':len(nonzero)}


def analyze(rows):
    deltas = [Fraction(b-a,n) for _,n,a,b in rows]
    stat = exact_wilcoxon_two_sided(deltas)
    return {
      'source_level': 'sanitized experimental aggregates; original logs private/not independently replicated',
      'n_pairs': len(rows),
      'steps_per_condition': [n for _,n,_,_ in rows],
      'old_split_counts': [a for _,_,a,_ in rows],
      'new_split_counts': [b for _,_,_,b in rows],
      'delta_percentage_points': [round(100*float(x),3) for x in deltas],
      'new_higher_pairs': sum(d>0 for d in deltas),
      'mean_paired_delta_percentage_points': round(100*float(sum(deltas)/len(deltas)),6),
      'wilcoxon_W_min':stat['W_min'],
      'wilcoxon_exact_two_sided_p':stat['p_two_sided_exact'],
      'interpretation': 'Descriptive paired shift in recorded disagreement; no universal causal or truth claim',
    }

if __name__ == '__main__':
    print(json.dumps(analyze(load_rows()),indent=2,ensure_ascii=False))
