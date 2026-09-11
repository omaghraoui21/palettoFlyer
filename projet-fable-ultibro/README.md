# Projet Fable — générique d'Ultibro Breezhaler

Dossier de développement indépendant, produit sans réutiliser le dossier `developpement-ultibro.html` fourni par ailleurs.

- `DOSSIER.md` — le dossier complet (méthode, rétro-ingénierie, QTPP/CQA, risque, formulations, procédé, analytique, plan d'expériences, dimensionnement statistique, jalons, sources).
- `lactose/PROMPT.md` + `lactose/RESULTATS.md` + `lactose/candidats_lactose.csv` — protocole figé puis exécution de la sélection des lactoses (brevets, littérature primaire, fiches fournisseurs, grille de score).
- `lactose/IDENTIFICATION_RZEWINSKA.md` + `lactose/identify_grades.py` — méthodologie et résultats d'identification des grades DFE Pharma derrière les 10 PSD du tableau I de Rzewińska 2025 (ajustement grade seul / mélange binaire).
- `selection/PROMPT.md` + `selection/CANDIDAT.md` + `tools/select_candidate.py` — protocole figé puis sélection multicritère du candidat de départ (FB-2) et de son challenger, avec analyse de sensibilité aux poids.
- `protocole/PROMPT.md` + `protocole/PROTOCOLE_FB2.md` + `tools/batch_record.py` — protocole opératoire complet (16 expériences) de FB-2 / FB-2-C et générateur de fiche de pesée à partir des CoA.
- `tools/formulation.py` — bilan matière, correction de titre, recouvrement de surface et statistique de mélange.
- `tools/doe.py` — plan de criblage définitif (15 lots, 6 facteurs) et grandeurs de transposition du mélangeur.
- `tools/equivalence_power.py` — simulation Monte-Carlo de la puissance du critère EMA 85–118 %.
- `outputs/` — fichiers générés (CSV/JSON). Regénérer : `python3 tools/formulation.py && python3 tools/doe.py && python3 tools/equivalence_power.py`.

Pur Python 3, aucune dépendance. Usage R&D in vitro uniquement ; aucun lot fabriqué.
