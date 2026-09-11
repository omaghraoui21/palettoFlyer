"""Analyse multicritère (somme pondérée) des candidats formule+procédé, avec
analyse de sensibilité aux poids par Monte-Carlo. Pur Python.

Les notes (1-5) et leurs justifications sont dans selection/CANDIDAT.md ; ce
fichier ne fait que les porter et les agréger. Usage : python3 tools/select_candidate.py
"""
from __future__ import annotations

import csv
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")

WEIGHTS = {"K1_IND": 20, "K2_GLY": 20, "K3_stabilite": 15, "K4_fabricabilite": 12,
           "K5_fidelite_EPAR": 10, "K6_simplicite": 8, "K7_PI": 8, "K8_faible_debit": 7}
assert sum(WEIGHTS.values()) == 100

# Candidats non dominés (l'élagage est justifié dans CANDIDAT.md § 1).
#             K1 K2 K3 K4 K5 K6 K7 K8
CANDIDATES = {
    "C1  ML001 | 0 % LH300 | MgSt externe 0.14 % | fort cisaillement":        (4, 3, 3, 4, 3, 5, 5, 3),
    "C2  ML001 | 0 % LH300 | PI 5 % + MgSt ext. | fort cisaillement":         (4, 4, 4, 4, 5, 3, 3, 4),
    "C3  50/50 SV003-ML001 | 0 % LH300 | PI 5 % + ext. | fort cisaillement":  (3, 4, 4, 5, 5, 3, 3, 3),
    "C4  SV003 | 4 % LH300 | PI 5 % + MgSt ext. | fort cisaillement":         (3, 4, 3, 3, 4, 2, 3, 3),
    "C5  ML001 | 4 % LH300 | MgSt externe 0.14 % | fort cisaillement":        (4, 3, 2, 3, 2, 4, 5, 4),
    "C6  SV003 | 0 % LH300 | MgSt externe 0.14 % | fort cisaillement":        (2, 2, 3, 5, 3, 5, 5, 2),
    "C7  ML001 | 0 % LH300 | PI 5 % + MgSt ext. | Turbula":                  (3, 3, 4, 3, 4, 4, 3, 3),
}


def score(notes, weights):
    return sum(n * w for n, w in zip(notes, weights.values())) / sum(weights.values())


def sensitivity(n_sim=10000, seed=7, rel=0.5):
    rng = random.Random(seed)
    wins = {c: 0 for c in CANDIDATES}
    for _ in range(n_sim):
        w = {k: v * rng.uniform(1 - rel, 1 + rel) for k, v in WEIGHTS.items()}
        best = max(CANDIDATES, key=lambda c: score(CANDIDATES[c], w))
        wins[best] += 1
    return {c: v / n_sim for c, v in wins.items()}


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    base = {c: score(n, WEIGHTS) for c, n in CANDIDATES.items()}
    sens = sensitivity()
    rows = sorted(CANDIDATES, key=lambda c: -base[c])
    with open(os.path.join(OUT, "selection_mcda.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["candidat", *WEIGHTS, "score_pondere_sur_5", "freq_premier_MC"])
        for c in rows:
            w.writerow([c, *CANDIDATES[c], f"{base[c]:.3f}", f"{sens[c]:.3f}"])
    for c in rows:
        print(f"{base[c]:.3f}  P(1er)={sens[c]:.2f}  {c}")
