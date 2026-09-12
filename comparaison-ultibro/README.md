# Ultibro — comparaison Astra / Fable

Branche de travail indépendante : `redteam/astra-fable-methode-3`.

1. Lire la [décision et le programme adaptatif](DECISION_METHODE_3.md).
2. Consulter l'[audit comparatif](AUDIT_COMPARATIF.md), le [prompt exécuté](GOAL_PROMPT.md) et le [journal des décisions](JOURNAL_DECISIONS.csv).
3. Ouvrir le [dossier Astra revu, HTML autonome](../projet-astra-ultibro/version-revue/developpement-ultibro.html) et ses [corrections](../projet-astra-ultibro/version-revue/CORRECTIONS.md).
4. Retrouver les [sources Astra originales](../projet-astra-ultibro/source-originale/), le [projet Fable historique](../projet-fable-ultibro/README.md) et la [revue PDF fournie](sources/revue-fable-fournie.pdf).

**Résultat documentaire :** une première voie directe, puis un contraste ou une répétition selon ses résultats. Voie courte conditionnelle de 3–4 lots pour obtenir un candidat prometteur ; aucune équivalence démontrée, aucun lot réellement fabriqué.

## Calculs reproductibles

Depuis la racine du dépôt, Python standard uniquement :

```bash
python -B comparaison-ultibro/audit_calculs.py
python -B comparaison-ultibro/calculateur_m3.py --examples
python -B comparaison-ultibro/calculateur_m3.py --inputs comparaison-ultibro/entrees_exemple.json
```

Les deux dernières commandes affichent des bilans théoriques. `--csv nouveau-fichier.csv` crée un CSV et refuse d'écraser un fichier existant. Voir les [exemples de compositions](FORMULATIONS_THEORIQUES.csv). Les titres sont en sels sur produit tel quel ; ne pas appliquer une seconde correction d'eau. Choisir explicitement une teneur totale de MgSt en % poudre ou en µg/capsule. Le poids minimal et la charge du mélangeur restent à qualifier.

Le contrôle couvre les bilans, entrées impossibles, changement de masse, PI, plans, scores et conservation des sources. [Résultats enregistrés](VERIFICATIONS.json) et [inventaire avec empreintes](INVENTAIRE_SOURCES.json).

La branche conserve chaque fichier historique. Les seules additions sont `projet-astra-ultibro/` et `comparaison-ultibro/`. Aucun changement de la branche principale, du dossier Fable ou du ZIP source. Le HTML est consultable localement ; l'intégration Git n'active pas un hébergement web.
