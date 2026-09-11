"""Bilan matière, correction de titre et physique du mélange adhésif.

Pur Python (pas de dépendance). Toutes les hypothèses sont explicites et
surchargeables. Usage : python3 tools/formulation.py  -> écrit outputs/*.
"""
from __future__ import annotations

import csv
import json
import math
import os
from dataclasses import dataclass, asdict

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")

# --- Constantes physico-chimiques -------------------------------------------
# Masses molaires calculées à partir des formules brutes (IUPAC 2021, arrondi).
ATOMIC = {"C": 12.011, "H": 1.008, "N": 14.007, "O": 15.999, "Br": 79.904}


def molar_mass(formula: dict[str, int]) -> float:
    return sum(ATOMIC[k] * v for k, v in formula.items())


M_IND = molar_mass({"C": 24, "H": 28, "N": 2, "O": 3})            # indacatérol
M_IND_MAL = M_IND + molar_mass({"C": 4, "H": 4, "O": 4})          # maléate
M_GLY = molar_mass({"C": 19, "H": 28, "N": 1, "O": 3})            # cation
M_GLY_BR = M_GLY + ATOMIC["Br"]                                   # bromure
M_LACTOSE_ANH = molar_mass({"C": 12, "H": 22, "O": 11})
M_LACTOSE_H2O = M_LACTOSE_ANH + molar_mass({"H": 2, "O": 1})

F_IND = M_IND_MAL / M_IND   # µg de sel par µg de base
F_GLY = M_GLY_BR / M_GLY


@dataclass
class Formula:
    """Composition d'une unité (mg) et d'un lot (g)."""
    name: str
    fill_mg: float
    ind_base_ug: float = 110.0
    gly_base_ug: float = 50.0
    mgst_pct: float = 0.14          # % m/m sur poudre totale
    fines_pct: float = 0.0          # lactose micronisé ajouté, % m/m
    potency_ind: float = 1.0        # titre du sel tel quel (fraction)
    potency_gly: float = 1.0
    pi_mgst_ratio: float = 0.0      # MgSt co-micronisé / bromure (0 = pas de PI)

    def per_unit_mg(self) -> dict[str, float]:
        ind = self.ind_base_ug * F_IND / 1000 / self.potency_ind
        gly = self.gly_base_ug * F_GLY / 1000 / self.potency_gly
        mgst = self.fill_mg * self.mgst_pct / 100
        fines = self.fill_mg * self.fines_pct / 100
        carrier = self.fill_mg - ind - gly - mgst - fines
        d = {
            "indacaterol_maleate": ind,
            "glycopyrronium_bromide": gly,
            "magnesium_stearate_total": mgst,
            "lactose_fines_added": fines,
            "lactose_carrier": carrier,
            "total": self.fill_mg,
        }
        if self.pi_mgst_ratio:
            gly_salt_pure = self.gly_base_ug * F_GLY / 1000
            mgst_in_pi = gly_salt_pure * self.pi_mgst_ratio
            d["pi_glycopyrronium_mgst"] = gly + mgst_in_pi
            d["mgst_in_pi"] = mgst_in_pi
            d["mgst_external"] = mgst - mgst_in_pi
        return d

    def batch_g(self, batch_g: float) -> dict[str, float]:
        units = batch_g * 1000 / self.fill_mg
        return {k: v * units / 1000 for k, v in self.per_unit_mg().items()} | {"units": units}


# --- Physique du mélange adhésif ---------------------------------------------
@dataclass
class Powder:
    name: str
    d50_um: float
    true_density_g_cm3: float
    shape_factor: float = 1.0   # 1 = sphère ; >1 = surface réelle / surface sphère équivalente

    def mass_per_particle_g(self) -> float:
        d_cm = self.d50_um * 1e-4
        return self.true_density_g_cm3 * math.pi / 6 * d_cm ** 3

    def specific_surface_m2_g(self) -> float:
        # 6/(rho d) pour des sphères (m²/kg -> /1000 pour m²/g), fois un facteur de rugosité.
        return 6 / (self.true_density_g_cm3 * 1000 * self.d50_um * 1e-6) / 1000 * self.shape_factor

    def projected_area_per_mass_m2_g(self) -> float:
        # aire projetée (pi d^2/4) / masse -> 1.5/(rho d), en m²/g
        return 1.5 / (self.true_density_g_cm3 * 1000 * self.d50_um * 1e-6) / 1000


def coverage_analysis(formula: Formula, carrier: Powder, ind: Powder, gly: Powder, mgst: Powder) -> dict:
    """Recouvrement théorique de la surface du porteur par les fines (API + MgSt).

    Régime « mélange adhésif » si le recouvrement est très inférieur à 100 % :
    les sites actifs du porteur dominent, d'où le rôle du MgSt et des fines.
    """
    u = formula.per_unit_mg()
    carrier_area = u["lactose_carrier"] / 1000 * carrier.specific_surface_m2_g()
    areas = {
        "indacaterol_maleate": u["indacaterol_maleate"] / 1000 * ind.projected_area_per_mass_m2_g(),
        "glycopyrronium_bromide": u["glycopyrronium_bromide"] / 1000 * gly.projected_area_per_mass_m2_g(),
        "magnesium_stearate_total": u["magnesium_stearate_total"] / 1000 * mgst.projected_area_per_mass_m2_g(),
    }
    n_carrier = u["lactose_carrier"] / 1000 / carrier.mass_per_particle_g()
    n_ind = u["indacaterol_maleate"] / 1000 / ind.mass_per_particle_g()
    n_gly = u["glycopyrronium_bromide"] / 1000 / gly.mass_per_particle_g()
    return {
        "carrier_surface_m2_per_unit": carrier_area,
        "coverage_pct": {k: 100 * v / carrier_area for k, v in areas.items()},
        "coverage_pct_total": 100 * sum(areas.values()) / carrier_area,
        "carrier_particles_per_unit": n_carrier,
        "ind_particles_per_carrier_particle": n_ind / n_carrier,
        "gly_particles_per_carrier_particle": n_gly / n_carrier,
    }


def random_mixing_cv(dose_mass_ug: float, unit: Powder) -> float:
    """CV (%) d'un mélange aléatoire parfait (Poisson) selon la taille de l'unité
    de mélange : particule primaire ou agglomérat. Montre que l'homogénéité est
    gouvernée par la désagglomération, pas par la statistique des particules.
    """
    n = dose_mass_ug * 1e-6 / unit.mass_per_particle_g()
    return 100 / math.sqrt(n)


def write_outputs():
    os.makedirs(OUT, exist_ok=True)
    fb1 = Formula("FB-1 (référence interne)", fill_mg=25.0, mgst_pct=0.14)
    fb1_pi = Formula("FB-1-PI (GLY co-micronisé 5 % MgSt)", fill_mg=25.0, mgst_pct=0.14, pi_mgst_ratio=0.05)
    fb1_alt = Formula("FB-1b (remplissage 23.75 mg, hypothèse lactose déclaré en monohydrate)", fill_mg=23.75, mgst_pct=0.14)
    fb1_coa = Formula("FB-1 corrigée CoA (IND 98.2 %, GLY 99.1 %)", fill_mg=25.0, mgst_pct=0.14,
                      potency_ind=0.982, potency_gly=0.991)

    rows = []
    for f in (fb1, fb1_pi, fb1_alt, fb1_coa):
        unit = f.per_unit_mg()
        batch = f.batch_g(300)
        for k, v in unit.items():
            rows.append([f.name, k, f"{v:.6f}", f"{batch[k]:.5f}"])
    with open(os.path.join(OUT, "bilan_matiere.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Formule", "Composant", "mg/unite", "g/lot_300g"])
        w.writerows(rows)

    # Hypothèses granulométriques par défaut (à remplacer par les CoA / mesures).
    carrier = Powder("lactose porteur broyé", d50_um=60, true_density_g_cm3=1.54, shape_factor=2.5)
    ind = Powder("IND maléate micronisé", d50_um=2.0, true_density_g_cm3=1.30)
    gly = Powder("GLY bromure micronisé", d50_um=2.0, true_density_g_cm3=1.35)
    mgst = Powder("MgSt", d50_um=6.0, true_density_g_cm3=1.05)
    cov = coverage_analysis(fb1, carrier, ind, gly, mgst)

    mixing = {
        "cv_random_pct_ind_primary_2um": random_mixing_cv(fb1.per_unit_mg()["indacaterol_maleate"] * 1000, ind),
        "cv_random_pct_gly_primary_2um": random_mixing_cv(fb1.per_unit_mg()["glycopyrronium_bromide"] * 1000, gly),
        "cv_random_pct_gly_agglomerates_30um": random_mixing_cv(
            fb1.per_unit_mg()["glycopyrronium_bromide"] * 1000, Powder("agglomérat GLY", 30, 0.6)),
        "cv_random_pct_gly_agglomerates_100um": random_mixing_cv(
            fb1.per_unit_mg()["glycopyrronium_bromide"] * 1000, Powder("agglomérat GLY", 100, 0.6)),
        "cv_random_pct_mgst_primary_6um": random_mixing_cv(fb1.per_unit_mg()["magnesium_stearate_total"] * 1000, mgst),
    }

    lactose_mono = fb1.per_unit_mg()["lactose_carrier"] + fb1.per_unit_mg()["lactose_fines_added"]
    summary = {
        "molar_masses": {"IND": M_IND, "IND_maleate": M_IND_MAL, "GLY": M_GLY, "GLY_bromide": M_GLY_BR,
                         "lactose_anhydrous": M_LACTOSE_ANH, "lactose_monohydrate": M_LACTOSE_H2O},
        "salt_factors": {"IND": F_IND, "GLY": F_GLY},
        "salt_per_unit_ug": {"IND_maleate": 110 * F_IND, "GLY_bromide": 50 * F_GLY},
        "lactose_per_unit_mg_FB1": {"monohydrate": lactose_mono,
                                    "anhydrous_equivalent": lactose_mono * M_LACTOSE_ANH / M_LACTOSE_H2O},
        "coverage": cov,
        "mixing_cv": mixing,
        "assumptions": {"carrier": asdict(carrier), "ind": asdict(ind), "gly": asdict(gly), "mgst": asdict(mgst)},
    }
    with open(os.path.join(OUT, "physique_melange.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)
    return summary


if __name__ == "__main__":
    s = write_outputs()
    print(json.dumps(s, indent=2, ensure_ascii=False))
