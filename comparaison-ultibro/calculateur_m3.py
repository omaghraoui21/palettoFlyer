"""Bilan théorique IND/GLY : unités explicites, titres en sel sur produit tel quel.

Ne qualifie ni une balance, ni une charge de mélangeur, ni une fabrication.
Pas de correction automatique de pertes, d'eau ou de surdosage.
Python standard uniquement. Exécuter avec -B pour préserver les sources historiques.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

# Masses molaires g/mol calculées avec C=12.011, H=1.008, N=14.007,
# O=15.999, Br=79.904. Cohérence avec formulation.py, sans l'importer.
F_IND = 508.571 / 392.499
F_GLY = 398.341 / 318.437


def _number(name, value, low, high=None, strict_low=False):
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ValueError(f"{name}: nombre requis")
    if not math.isfinite(value) or value < low or (strict_low and value == low):
        raise ValueError(f"{name}: valeur hors domaine")
    if high is not None and value > high:
        raise ValueError(f"{name}: valeur supérieure à {high}")
    return float(value)


def calculate(*, batch_g, fill_mg, titre_ind, titre_gly,
              mgst_mode, mgst_value, fines_pct=0, ml001_fraction=1,
              gly_route="directe", mgst_fraction_pi=0, min_weigh_g=None):
    """titres = g de sel / g de matière telle quelle ; fractions entre 0 et 1.

    mgst_mode : 'pct_poudre' (% m/m total) ou 'ug_par_gelule' (total absolu).
    fines_pct : % m/m de la poudre ; ml001_fraction : fraction du porteur restant.
    PI : titre_gly et mgst_fraction_pi doivent être mesurés séparément.
    La masse de MgSt désigne l'excipient qualifié, pas le magnésium élémentaire.
    """
    batch_g = _number("batch_g", batch_g, 0, strict_low=True)
    fill_mg = _number("fill_mg", fill_mg, 0, strict_low=True)
    titre_ind = _number("titre_ind", titre_ind, 0, 1, True)
    titre_gly = _number("titre_gly", titre_gly, 0, 1, True)
    fines_pct = _number("fines_pct", fines_pct, 0, 100)
    ml001_fraction = _number("ml001_fraction", ml001_fraction, 0, 1)
    mgst_fraction_pi = _number("mgst_fraction_pi", mgst_fraction_pi, 0, 1)
    mgst_value = _number("mgst_value", mgst_value, 0)
    if gly_route not in ("directe", "PI"):
        raise ValueError("gly_route: directe ou PI")
    if gly_route == "directe" and mgst_fraction_pi != 0:
        raise ValueError("Voie directe : MgSt incorporé au PI impossible")
    if titre_gly + mgst_fraction_pi > 1 + 1e-12:
        raise ValueError("Titre GLY-Br + fraction MgSt du PI > 100 %")
    if mgst_mode not in ("pct_poudre", "ug_par_gelule"):
        raise ValueError("Choisir explicitement la convention de MgSt")
    if mgst_mode == "pct_poudre" and mgst_value > 100:
        raise ValueError("MgSt > 100 %")
    units = batch_g * 1000 / fill_mg
    ind = units * 110 * F_IND / 1e6 / titre_ind
    gly_material = units * 50 * F_GLY / 1e6 / titre_gly
    mgst_pi = gly_material * mgst_fraction_pi
    mgst_total = (batch_g * mgst_value / 100 if mgst_mode == "pct_poudre"
                  else units * mgst_value / 1e6)
    mgst_external = mgst_total - mgst_pi
    if mgst_external < -1e-12:
        raise ValueError("Le PI apporte plus de MgSt que la cible totale")
    mgst_external = max(0.0, mgst_external)  # seulement bruit numérique < 1 pg
    fines = batch_g * fines_pct / 100
    carrier = batch_g - ind - gly_material - mgst_external - fines
    if carrier <= 0:
        raise ValueError("Bilan impossible : porteur résiduel nul ou négatif")
    masses = {
        "IND_maleate_g": ind,
        "GLY_matiere_g": gly_material,
        "MgSt_externe_g": mgst_external,
        "lactose_fin_g": fines,
        "ML001_g": carrier * ml001_fraction,
        "SV003_g": carrier * (1 - ml001_fraction),
    }
    if not all(math.isfinite(x) and x >= 0 for x in masses.values()):
        raise ValueError("Bilan non fini ou négatif")
    below = []
    if min_weigh_g is not None:
        min_weigh_g = _number("min_weigh_g", min_weigh_g, 0, strict_low=True)
        below = [k for k, v in masses.items() if 0 < v < min_weigh_g]
    checks = {
        "unites_theoriques": units,
        "masse_totale_g": sum(masses.values()),
        "IND_base_ug_par_gelule": ind * titre_ind / F_IND / units * 1e6,
        "GLY_base_ug_par_gelule": gly_material * titre_gly / F_GLY / units * 1e6,
        "MgSt_total_pct": mgst_total / batch_g * 100,
        "MgSt_total_ug_par_gelule": mgst_total / units * 1e6,
        "MgSt_dans_PI_g": mgst_pi,
        "masses_sous_poids_minimal": below,
        "poids_minimal_renseigne": min_weigh_g is not None,
        "statut": "BILAN_THEORIQUE_NON_LIBERATOIRE",
    }
    return {"masses_g": masses, "controles": checks}


def examples():
    common = dict(batch_g=300, fill_mg=25, titre_ind=1, titre_gly=1,
                  mgst_mode="pct_poudre", mgst_value=0.15)
    # Réserves conditionnelles, pas quatre lots à commander d'emblée.
    return {
        "M3-A": calculate(**common),
        "M3-C": calculate(**common, ml001_fraction=0.5),
        "M3-F3": calculate(**common, fines_pct=3),
        "M3-F6": calculate(**common, fines_pct=6),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inputs", type=Path, help="JSON contenant les arguments explicites de calculate")
    p.add_argument("--examples", action="store_true", help="Scénarios théoriques 300 g / 25 mg / titres 100 %")
    p.add_argument("--csv", type=Path, help="Nouveau fichier CSV ; refuse d'écraser un fichier")
    args = p.parse_args()
    if bool(args.inputs) == bool(args.examples):
        p.error("Choisir --inputs OU --examples")
    result = examples() if args.examples else {"calcul": calculate(**json.loads(args.inputs.read_text()))}
    if args.csv:
        with args.csv.open("x", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["Scenario_theorique", "Composant", "Masse_g", "Statut"])
            for name, data in result.items():
                for comp, mass in data["masses_g"].items():
                    w.writerow([name, comp, f"{mass:.8f}", data["controles"]["statut"]])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
