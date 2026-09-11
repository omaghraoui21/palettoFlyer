# Projet Fable — générique d'Ultibro Breezhaler

Dossier de développement indépendant, produit sans réutiliser le dossier `developpement-ultibro.html` fourni par ailleurs.

- `DOSSIER.md` — le dossier complet (méthode, rétro-ingénierie, QTPP/CQA, risque, formulations, procédé, analytique, plan d'expériences, dimensionnement statistique, jalons, sources).
- `lactose/PROMPT.md` + `lactose/RESULTATS.md` + `lactose/candidats_lactose.csv` — protocole figé puis exécution de la sélection des lactoses (brevets, littérature primaire, fiches fournisseurs, grille de score).
- `tools/formulation.py` — bilan matière, correction de titre, recouvrement de surface et statistique de mélange.
- `tools/doe.py` — plan de criblage définitif (15 lots, 6 facteurs) et grandeurs de transposition du mélangeur.
- `tools/equivalence_power.py` — simulation Monte-Carlo de la puissance du critère EMA 85–118 %.
- `outputs/` — fichiers générés (CSV/JSON). Regénérer : `python3 tools/formulation.py && python3 tools/doe.py && python3 tools/equivalence_power.py`.

Pur Python 3, aucune dépendance. Usage R&D in vitro uniquement ; aucun lot fabriqué.
