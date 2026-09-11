"""Identification des grades DFE Pharma derrière des triplets (d10, d50, d90).

Méthode : chaque grade de référence est représenté par une courbe cumulée Q3(ln d)
interpolée linéairement entre points d'ancrage ; un mélange binaire est la somme
pondérée en masse des cumulées ; les percentiles du mélange sont obtenus par
inversion. Le score est la RMS des écarts log(d_obs/d_pred) sur les 3 percentiles.
On compare : (a) grade seul, (b) meilleur mélange binaire (pas de 5 %).

Références : PSD « typiques » des pages produit DFE (11/09/2026), spécification
ML001 (PD-0063) et PSD mesurées par Karabulut et al., RDD 2022 (tableau 1).
Usage : python3 identify_grades.py
"""
from __future__ import annotations

import math

# (d10, d50, d90) en µm. Source dans le commentaire.
GRADES = {
    "Respitose SV003":  (35, 60, 95),      # DFE typ. ; Karabulut : 30.45/60.17/100.74
    "Respitose SV010":  (45, 110, 175),    # DFE typ.
    "Respitose ML001":  (5, 50, 150),      # DFE typ. ; spec 3-7/37-61/124-194 ; Karabulut 5.55/49.0/143.1
    "Respitose ML006":  (2.74, 17.02, 45.91),  # Karabulut (pas de PSD typ. publiée sur le site)
    "Lactohale 100":    (55, 130, 220),    # DFE typ.
    "Lactohale 200":    (10, 70, 140),     # DFE typ. ; Karabulut 13.39/68.95/148.7
    "Lactohale 201":    (5, 20, 55),       # DFE typ. ; Karabulut 4.67/23.89/63.88
    "Lactohale 206":    (35, 85, 150),     # DFE typ. ; Karabulut 30.11/83.2/161.85
    "Lactohale 210":    (5, 15, 40),       # DFE typ. (brochure : 3/15/44)
    "Lactohale 220":    (3, 13, 34),       # brochure DFE blend products 02/2022
    "Lactohale 230":    (1.4, 8.4, 23),    # estore DFE (brochure : 2/8/23)
    "Lactohale 300":    (1.0, 3, 9),       # DFE typ. x50/x90 ; d10 = hypothèse
}

# Spécification laser ML001 (fiche PD-0063) pour un test d'appartenance strict.
ML001_SPEC = {"d10": (3, 7), "d50": (37, 61), "d90": (124, 194)}

OBS = [
    (4.80, 44.24, 144.96), (4.23, 34.98, 99.65), (3.35, 37.49, 142.00),
    (10.52, 74.45, 145.61), (3.66, 19.76, 84.32), (5.67, 41.58, 127.00),
    (5.19, 37.35, 118.16), (4.18, 30.26, 121.27), (12.95, 79.01, 159.97),
    (6.80, 48.95, 138.38),
]

Z = [0.0, 0.10, 0.50, 0.90, 1.0]


def anchors(d10, d50, d90):
    # Queues : 0 % à d10/5, 100 % à d90*1.8 (hypothèse de forme, identique pour tous).
    return [math.log(d10 / 5), math.log(d10), math.log(d50), math.log(d90), math.log(d90 * 1.8)]


def cumulative(x, anc):
    if x <= anc[0]:
        return 0.0
    if x >= anc[-1]:
        return 1.0
    for i in range(len(anc) - 1):
        if anc[i] <= x <= anc[i + 1]:
            t = (x - anc[i]) / (anc[i + 1] - anc[i])
            return Z[i] + t * (Z[i + 1] - Z[i])
    return 1.0


def percentiles_of_mix(components):
    """components = [(fraction, anchors), ...] -> (d10, d50, d90)."""
    lo = min(a[0] for _, a in components)
    hi = max(a[-1] for _, a in components)
    def q(x):
        return sum(f * cumulative(x, a) for f, a in components)
    out = []
    for target in (0.10, 0.50, 0.90):
        a, b = lo, hi
        for _ in range(40):  # bissection : Q3 est monotone
            m = (a + b) / 2
            if q(m) < target:
                a = m
            else:
                b = m
        out.append(math.exp((a + b) / 2))
    return tuple(out)


def score(obs, pred):
    return math.sqrt(sum(math.log(o / p) ** 2 for o, p in zip(obs, pred)) / 3)


def identify(obs):
    anc = {g: anchors(*v) for g, v in GRADES.items()}
    singles = sorted((score(obs, GRADES[g]), g) for g in GRADES)
    best_mix = (9e9, None, None, None, None)
    names = list(GRADES)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            for k in range(1, 20):
                f = k / 20
                pred = percentiles_of_mix([(f, anc[a]), (1 - f, anc[b])])
                s = score(obs, pred)
                if s < best_mix[0]:
                    best_mix = (s, a, b, f, pred)
    return singles, best_mix


def in_ml001_spec(obs):
    return all(lo <= v <= hi for v, (lo, hi) in zip(obs, ML001_SPEC.values()))


if __name__ == "__main__":
    print(f"{'ligne':>5} {'d10':>6} {'d50':>6} {'d90':>7} | {'grade seul (RMS log)':<34} | {'spec ML001':<10} | meilleur mélange binaire (RMS log)")
    for n, o in enumerate(OBS, 1):
        singles, mix = identify(o)
        s1, g1 = singles[0]
        s2, g2 = singles[1]
        ms, a, b, f, pred = mix
        gain = "  <- mélange nettement meilleur" if ms < 0.6 * s1 and s1 > 0.10 else ""
        print(f"{n:>5} {o[0]:>6.2f} {o[1]:>6.2f} {o[2]:>7.2f} | {g1} ({s1:.3f}) ; 2e {g2} ({s2:.3f})".ljust(90)
              + f" | {'oui' if in_ml001_spec(o) else 'non':<10} | {f*100:.0f} % {a} + {100-f*100:.0f} % {b} ({ms:.3f}) -> pred {pred[0]:.1f}/{pred[1]:.1f}/{pred[2]:.1f}{gain}")


def all_plausible(obs, tol=0.10):
    """Toutes les hypothèses (grade seul ou mélange binaire) sous le seuil de RMS log."""
    anc = {g: anchors(*v) for g, v in GRADES.items()}
    hits = [(score(obs, GRADES[g]), g, None, 1.0) for g in GRADES]
    names = list(GRADES)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            for k in range(1, 20):
                f = k / 20
                s = score(obs, percentiles_of_mix([(f, anc[a]), (1 - f, anc[b])]))
                hits.append((s, a, b, f))
    hits = sorted(h for h in hits if h[0] <= tol)
    # une seule entrée par couple (a,b) : la meilleure fraction
    seen, out = set(), []
    for h in hits:
        key = (h[1], h[2])
        if key in seen:
            continue
        seen.add(key)
        out.append(h)
    return out


if __name__ == "__main__":
    print("\n=== Hypothèses plausibles par ligne (RMS log <= 0.10 ; grade seul = pas de 2e composant) ===")
    for n, o in enumerate(OBS, 1):
        hs = all_plausible(o)
        txt = " ; ".join(f"{a}" + (f" {f*100:.0f}% + {b}" if b else "") + f" ({s:.3f})" for s, a, b, f in hs[:6])
        print(f"{n:>2}: {txt if txt else 'aucune sous 0.10'}")
