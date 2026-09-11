"""Fiche de pesée et dossier de lot pour FB-2 / FB-2-C.

Entrées : masse de lot, titres réels (CoA) du PI (en GLY-Br, tel quel), de l'IND
maléate (en sel, tel quel), teneur réelle en MgSt du PI, fraction de porteur broyé.
Sorties : CSV avec masses cibles, tolérances de pesée, contrôles de calcul.

Tolérances : la tolérance relative sur chaque actif est bornée par (a) la précision
de la balance (poids minimal qualifié, U = 0,1 % [Q]) et (b) une contribution
<= 0,5 % à la dose ; pour excipients, ±1 %. Usage : python3 tools/batch_record.py
"""
from __future__ import annotations

import csv
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from formulation import F_GLY, F_IND  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")

FILL_MG = 25.0
MGST_TOTAL_PCT = 0.14
IND_BASE_UG = 110.0
GLY_BASE_UG = 50.0


def batch_record(name: str, batch_g: float, potency_ind_salt: float, pi_gly_br_content: float,
                 pi_mgst_content: float, milled_fraction: float, fines_pct: float = 0.0):
    """potency_* en fraction (0.982 = 98,2 %). pi_gly_br_content = g GLY-Br / g PI ;
    pi_mgst_content = g MgSt / g PI (les deux mesurés sur le lot de PI)."""
    units = batch_g * 1000 / FILL_MG
    ind_salt_pure = IND_BASE_UG * F_IND / 1e6 * units          # g de sel à 100 %
    gly_salt_pure = GLY_BASE_UG * F_GLY / 1e6 * units
    ind_weigh = ind_salt_pure / potency_ind_salt
    pi_weigh = gly_salt_pure / pi_gly_br_content
    mgst_in_pi = pi_weigh * pi_mgst_content
    mgst_total = batch_g * MGST_TOTAL_PCT / 100
    mgst_ext = mgst_total - mgst_in_pi
    fines = batch_g * fines_pct / 100
    carrier = batch_g - ind_weigh - pi_weigh - mgst_ext - fines
    milled = carrier * milled_fraction
    sieved = carrier - milled
    rows = [
        ("Maléate d'indacatérol micronisé", ind_weigh, 0.005, f"titre sel tel quel {potency_ind_salt*100:.2f} %"),
        ("PI (GLY-Br + MgSt co-micronisé)", pi_weigh, 0.005,
         f"GLY-Br {pi_gly_br_content*100:.2f} % ; MgSt {pi_mgst_content*100:.2f} % du PI"),
        ("MgSt externe (LIGAMED MF-2-V-BI)", mgst_ext, 0.01, f"MgSt total {mgst_total:.5f} g = {MGST_TOTAL_PCT} %"),
        ("Lactose micronisé LH300 (fines ajoutées)", fines, 0.01, f"{fines_pct} % m/m"),
        ("Respitose ML001 (porteur broyé)", milled, 0.01, f"{milled_fraction*100:.0f} % du porteur"),
        ("Respitose SV003 (porteur tamisé)", sieved, 0.01, f"{(1-milled_fraction)*100:.0f} % du porteur"),
    ]
    checks = {
        "units_theoriques": units,
        "IND_base_ug_par_gelule": ind_weigh * potency_ind_salt / F_IND / units * 1e6,
        "GLY_base_ug_par_gelule": pi_weigh * pi_gly_br_content / F_GLY / units * 1e6,
        "MgSt_total_pct": (mgst_in_pi + mgst_ext) / batch_g * 100,
        "total_g": sum(r[1] for r in rows),
    }
    return rows, checks


def write(name, rows, checks, batch_g):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"fiche_pesee_{name}.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow([f"Fiche de pesée {name} — lot théorique {batch_g:.1f} g — R&D in vitro uniquement, aucune administration humaine"])
        w.writerow(["Composant", "Masse cible (g)", "Tolérance (g)", "Min (g)", "Max (g)", "Base de calcul", "Masse pesée", "Balance / opérateur / heure"])
        for label, m, tol_rel, note in rows:
            if m <= 0:
                continue
            tol = max(m * tol_rel, 0.0005)  # jamais sous 0,5 mg [Q]
            w.writerow([label, f"{m:.5f}", f"±{tol:.5f}", f"{m - tol:.5f}", f"{m + tol:.5f}", note, "", ""])
        w.writerow([])
        w.writerow(["Contrôle", "Valeur", "Attendu"])
        w.writerow(["Unités théoriques", f"{checks['units_theoriques']:.0f}", "12 000 pour 300 g"])
        w.writerow(["IND base µg/gélule", f"{checks['IND_base_ug_par_gelule']:.3f}", "110,000"])
        w.writerow(["GLY base µg/gélule", f"{checks['GLY_base_ug_par_gelule']:.3f}", "50,000"])
        w.writerow(["MgSt total %", f"{checks['MgSt_total_pct']:.4f}", "0,1400"])
        w.writerow(["Total g", f"{checks['total_g']:.5f}", f"{batch_g:.5f}"])
    return path


if __name__ == "__main__":
    # Exemple : CoA IND 98,6 % ; PI dosé à 94,9 % GLY-Br et 4,9 % MgSt.
    for name, milled in (("FB2", 1.0), ("FB2C", 0.5)):
        rows, checks = batch_record(name, 300.0, 0.986, 0.949, 0.049, milled)
        p = write(name, rows, checks, 300.0)
        print(p)
        for r in rows:
            if r[1] > 0:
                print(f"  {r[0]:42s} {r[1]:10.5f} g")
        print("  ", {k: round(v, 4) for k, v in checks.items()})
