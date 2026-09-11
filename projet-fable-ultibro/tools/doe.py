"""Plan d'expériences séquentiel et règles de transposition d'échelle du mélange.

Phase 1 : Definitive Screening Design (Jones & Nachtsheim 2011) à 6 facteurs,
construit sur la matrice de conférence C6 -> 13 lots (dont centre) + 2 centres.
Avantages vs factoriel 2^4 complet : effets principaux orthogonaux aux
interactions d'ordre 2, courbure estimable par facteur, 15 lots au lieu de 19,
deux facteurs de plus (PSD du glycopyrronium, type de porteur).
Le facteur F (fraction de porteur broyé) découle de lactose/RESULTATS.md.
Phase 2 : augmentation en plan composite centré sur les 2-3 facteurs retenus.
"""
from __future__ import annotations

import csv
import math
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")

# Matrice de conférence d'ordre 6 (symétrique, C·Cᵗ = 5·I).
C6 = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, -1, -1, 1],
    [1, 1, 0, 1, -1, -1],
    [1, -1, 1, 0, 1, -1],
    [1, -1, -1, 1, 0, 1],
    [1, 1, -1, -1, 1, 0],
]


def check_conference(c):
    n = len(c)
    for i in range(n):
        for j in range(n):
            dot = sum(c[i][k] * c[j][k] for k in range(n))
            expected = n - 1 if i == j else 0
            assert dot == expected, (i, j, dot)


FACTORS = {
    # nom: (bas, centre, haut, unité)
    "A_fines_pct": (0.0, 4.0, 8.0, "% lactose micronisé ajouté"),
    "B_mgst_pct": (0.08, 0.14, 0.20, "% MgSt total"),
    "C_precoat_tip_speed": (2.0, 4.0, 6.0, "m/s, vitesse périphérique, 2 min"),
    "D_final_blend_time": (1.0, 3.0, 5.0, "min à vitesse périphérique 2.4 m/s"),
    "E_gly_d90": (3.5, 5.0, 6.5, "µm, d90 du lot de GLY (2 lots + mélange 50/50)"),
    "F_carrier_milled_pct": (0, 50, 100, "% de porteur broyé (ML001-type) dans le porteur, complément tamisé (SV003-type)"),
}


def dsd_runs(seed: int = 2026) -> list[dict]:
    check_conference(C6)
    cols = list(FACTORS)
    rows = []
    k = len(cols)
    for r in C6:
        rows.append(r[:k])
        rows.append([-x for x in r[:k]])
    rows.append([0] * k)  # centre intrinsèque du DSD
    rows += [[0] * k, [0] * k]  # deux centres supplémentaires -> erreur pure
    runs = []
    for i, coded in enumerate(rows, 1):
        run = {"essai": f"D{i:02d}", "type": "centre" if not any(coded) else "sommet"}
        for name, c in zip(cols, coded):
            lo, mid, hi, _ = FACTORS[name]
            run[name + "_code"] = c
            run[name] = {-1: lo, 0: mid, 1: hi}[c]
        runs.append(run)
    rnd = random.Random(seed)
    rnd.shuffle(runs)
    # Ancrer un centre au début et un à la fin pour suivre la dérive.
    centres = [r for r in runs if r["type"] == "centre"]
    others = [r for r in runs if r["type"] != "centre"]
    ordered = [centres[0]] + others[:6] + [centres[1]] + others[6:] + [centres[2]]
    for k, r in enumerate(ordered, 1):
        r["ordre"] = k
    return ordered


# --- Transposition du mélange à fort cisaillement -----------------------------
def blender_metrics(bowl_volume_l: float, impeller_d_m: float, rpm: float, fill_fraction: float,
                    bulk_density_g_ml: float, t_min: float) -> dict:
    tip = math.pi * impeller_d_m * rpm / 60
    froude = (2 * math.pi * rpm / 60) ** 2 * (impeller_d_m / 2) / 9.81
    mass_g = bowl_volume_l * 1000 * fill_fraction * bulk_density_g_ml
    # Puissance dissipée ~ rho·N^3·D^5 (turbulent) ; rapportée à la masse : N^3·D^5/m.
    n = rpm / 60
    specific_power_index = n ** 3 * impeller_d_m ** 5 / (mass_g / 1000)
    return {"tip_speed_m_s": tip, "froude": froude, "mass_g": mass_g, "revolutions": rpm * t_min,
            "specific_energy_index": specific_power_index * t_min * 60}


def scale_rpm_constant_tip_speed(rpm_small: float, d_small: float, d_large: float) -> float:
    return rpm_small * d_small / d_large


def write_outputs():
    os.makedirs(OUT, exist_ok=True)
    runs = dsd_runs()
    cols = ["ordre", "essai", "type"] + [f for f in FACTORS] + [f + "_code" for f in FACTORS]
    with open(os.path.join(OUT, "plan_dsd_15_lots.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(cols)
        for r in runs:
            w.writerow([r[c] for c in cols])
        w.writerow(["#", "Facteurs", *[f"{k}: {v[0]} / {v[1]} / {v[2]} ({v[3]})" for k, v in FACTORS.items()]])

    # Exemple : GEA 1 L (turbine ~85 mm) -> 5 L (turbine ~150 mm), hypothèses géométriques.
    small = blender_metrics(1.0, 0.085, 2500, 0.30, 0.65, 2.0)
    large_same_rpm = blender_metrics(5.0, 0.150, 2500, 0.30, 0.65, 2.0)
    rpm_l = scale_rpm_constant_tip_speed(2500, 0.085, 0.150)
    large_tip = blender_metrics(5.0, 0.150, rpm_l, 0.30, 0.65, 2.0)
    with open(os.path.join(OUT, "transposition_melangeur.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["cas", *small.keys()])
        w.writerow(["1 L, 2500 rpm, 2 min", *[f"{v:.3g}" for v in small.values()]])
        w.writerow(["5 L, 2500 rpm (même rpm)", *[f"{v:.3g}" for v in large_same_rpm.values()]])
        w.writerow([f"5 L, {rpm_l:.0f} rpm (même vitesse périphérique)", *[f"{v:.3g}" for v in large_tip.values()]])
    return runs, small, large_same_rpm, large_tip


if __name__ == "__main__":
    runs, *m = write_outputs()
    for r in runs:
        print(r["ordre"], r["essai"], r["type"], [r[f + "_code"] for f in FACTORS])
    for x in m:
        print(x)
