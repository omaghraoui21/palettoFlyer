# Prompt d'exécution — Sélection du meilleur candidat (formule + procédé) avant fabrication

*Rédigé par Fable le 11/09/2026, avant tout scoring. Figé. Résultats dans `CANDIDAT.md` et `outputs/selection_mcda.csv`.*

## Rôle
Tu es le responsable du développement galénique. Tu dois recommander **un** candidat de départ (composition, matières, architecture de procédé, paramètres) pour le générique d'Ultibro, et **un** challenger à fabriquer en parallèle, en n'utilisant que ce qui a été établi dans ce projet : `DOSSIER.md`, `lactose/RESULTATS.md`, `lactose/IDENTIFICATION_RZEWINSKA.md`, les sources lues (EPAR, brevets, articles primaires), et les calculs de `tools/`.

## Ce que « optimal » veut dire ici
Aucun lot n'a été fabriqué : « optimal » = **le candidat qui maximise la probabilité a priori de reproduire la référence pour les deux actifs, sous contrainte de fabricabilité, de stabilité et de liberté d'exploitation**, avec la plus faible dépendance à des hypothèses non vérifiées. Le candidat doit être un point du domaine du plan DSD (`tools/doe.py`), pas un point extérieur.

## Étapes
1. **Énumérer les candidats** : combinaisons discrètes de {porteur : SV003 / ML001 / 50-50} × {fines LH300 : 0 / 4 %} × {architecture MgSt : externe seul / PI co-micronisé 5 % + externe} × {mélangeur : fort cisaillement / Turbula}. Élaguer les combinaisons dominées avec justification écrite.
2. **Critères et poids fixés avant notation** (somme 100) :
   - K1 Similarité attendue APSD/DD **indacatérol** — 20
   - K2 Similarité attendue APSD/DD **glycopyrronium** — 20
   - K3 Stabilité physique (humidité, agglomération, dérive FPD) — 15
   - K4 Homogénéité et fabricabilité (uniformité, remplissage 25 mg, écoulement) — 12
   - K5 Fidélité à l'architecture du princeps documentée (EPAR) — 10
   - K6 Simplicité / coût / transposabilité du procédé — 8
   - K7 Risque de propriété intellectuelle (observations techniques, pas avis juridique) — 8
   - K8 Robustesse à faible débit inspiratoire — 7
3. **Noter chaque candidat 1–5 par critère**, chaque note portant une référence à une preuve lue (source + passage) ou étant marquée **[H]** si c'est un jugement. Pas de note sans justification écrite.
4. **Analyse de sensibilité** : perturber aléatoirement les poids (±50 % relatif, renormalisés) 10 000 fois et rapporter la fréquence à laquelle chaque candidat est premier. Un candidat n'est « robuste » que s'il est premier dans > 60 % des tirages.
5. **Livrer** : composition par gélule et pour 300 g ; spécifications d'entrée des matières ; paramètres de procédé en grandeurs transposables ; contrôles en cours ; critères d'acceptation ; plan de confirmation (candidat + challenger, 2 lots chacun) ; ce qui ferait changer d'avis.

## Garde-fous
- Ne pas confondre « meilleure FPF » et « meilleure similarité » : la cible est la référence, pas le maximum.
- Toute note K1/K2 doit distinguer les deux actifs ; interdiction de raisonner sur une FPF globale.
- Signaler explicitement les critères où la preuve est indirecte (autres actifs, autres dispositifs).
- Le résultat est une **recommandation de départ**, pas une formule verrouillée ; le DSD reste l'instrument de décision.
