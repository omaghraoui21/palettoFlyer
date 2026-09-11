"""Puissance du critère in vitro EMA (IC 90 % du rapport des moyennes géométriques
dans 85–118 %) par simulation Monte-Carlo, avec variabilité inter-lot et intra-lot.

But : dimensionner le nombre de lots et d'unités AVANT l'étude pivot et montrer
que la variabilité inter-lot (pas le nombre d'inhalateurs) est le facteur limitant.
Pur Python. Usage : python3 tools/equivalence_power.py
"""
from __future__ import annotations

import csv
import math
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")

# Quantiles t(0.95) pour df 1..30 ; au-delà, approximation normale.
T95 = [None, 6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812,
       1.796, 1.782, 1.771, 1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725,
       1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703, 1.701, 1.699, 1.697]


def t95(df: int) -> float:
    return T95[df] if df <= 30 else 1.645 + 1.2 / df


def simulate(true_ratio: float, cv_batch: float, cv_unit: float, n_batches: int, n_units: int,
             n_sim: int, rng: random.Random, analysis: str) -> float:
    """Probabilité que l'IC 90 % du rapport T/R tombe dans [0.85, 1.18].

    analysis = "batch_means" : l'unité statistique est la moyenne de lot (conservateur).
    analysis = "pooled"      : toutes les unités regroupées (ignore la corrélation intra-lot).
    """
    s_b = math.sqrt(math.log(1 + cv_batch ** 2))
    s_u = math.sqrt(math.log(1 + cv_unit ** 2))
    lo, hi = math.log(0.85), math.log(1.18)
    ok = 0
    for _ in range(n_sim):
        def product(mu):
            batches = []
            for _b in range(n_batches):
                b = rng.gauss(mu, s_b)
                batches.append([rng.gauss(b, s_u) for _u in range(n_units)])
            return batches
        ref, test = product(0.0), product(math.log(true_ratio))
        if analysis == "batch_means":
            r = [sum(b) / n_units for b in ref]
            t = [sum(b) / n_units for b in test]
            df = 2 * n_batches - 2
        else:
            r = [x for b in ref for x in b]
            t = [x for b in test for x in b]
            df = len(r) + len(t) - 2
        mr, mt = sum(r) / len(r), sum(t) / len(t)
        var = (sum((x - mr) ** 2 for x in r) + sum((x - mt) ** 2 for x in t)) / df
        half = t95(df) * math.sqrt(var * (1 / len(r) + 1 / len(t)))
        d = mt - mr
        if d - half >= lo and d + half <= hi:
            ok += 1
    return ok / n_sim


def write_outputs(n_sim: int = 2000, seed: int = 11):
    os.makedirs(OUT, exist_ok=True)
    rng = random.Random(seed)
    scenarios = []
    for cv_batch in (0.04, 0.08, 0.12):
        for cv_unit in (0.10, 0.20):
            for n_batches, n_units in ((3, 10), (3, 20), (5, 10), (6, 10)):
                for true_ratio in (1.00, 1.05, 1.10):
                    row = {"cv_batch": cv_batch, "cv_unit": cv_unit, "n_batches": n_batches,
                           "n_units": n_units, "true_ratio": true_ratio}
                    row["power_batch_means"] = simulate(true_ratio, cv_batch, cv_unit, n_batches, n_units,
                                                        n_sim, rng, "batch_means")
                    row["power_pooled"] = simulate(true_ratio, cv_batch, cv_unit, n_batches, n_units,
                                                   n_sim // 4, rng, "pooled")
                    scenarios.append(row)
    with open(os.path.join(OUT, "puissance_equivalence_in_vitro.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(scenarios[0]), delimiter=";")
        w.writeheader()
        for s in scenarios:
            w.writerow({k: (f"{v:.3f}" if isinstance(v, float) else v) for k, v in s.items()})
    return scenarios


if __name__ == "__main__":
    for s in write_outputs():
        print(s)
