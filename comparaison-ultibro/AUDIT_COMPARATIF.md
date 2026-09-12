# Audit Astra / Fable — constats qui changent une décision

12 septembre 2026. Voir la [méthode 3](DECISION_METHODE_3.md) pour les choix opératoires et la signification de [E]/[C]/[H]. Aucun essai physique n'a été réalisé pendant cette revue.

**Mise à jour de périmètre :** Omar confirme l'impossibilité actuelle de co-microniser et demande des API déjà micronisés chez leur fabricant. Le PI est donc exclu du programme actuel, y compris en sous-traitance. Ses bilans et publications restent analysés ci-dessous comme travaux historiques.

## Périmètre et suffisance des pièces

Le projet Fable est dans `omaghraoui21/palettoFlyer`, branche historique `hoplite/poseidonia-706c0148`. Le commit `bf9b1e07bf6e38d71ccc5fd4975ff82990f583f2` contient le protocole et son générateur de pesées ; `4702fff9bc24264f32d7c81146563b360ed6e42b` ajoute la présentation. La branche comparative part de ce dernier commit. La branche `main` contient un autre projet et n'est pas la source Ultibro.

Les fichiers demandés ont été lus intégralement : DOSSIER ; les quatre textes/jeux de données et le script du dossier lactose ; sélection/PROMPT et CANDIDAT ; formulation, doe, equivalence_power, select_candidate et batch_record ; protocole/PROMPT et PROTOCOLE_FB2 ; présentation/SCRIPT et son prompt, ainsi que les README et sorties CSV/JSON. Les caches binaires Python ont été conservés, sans les traiter comme des sources scientifiques.

Le ZIP Astra apporte le HTML complet, le bilan F0 et le plan de 19 lots. `MEMORY.md` est un fichier de contexte minimal, sans données expérimentales. Le PDF joint apporte cinq remarques ciblées. **Les pièces sont suffisantes pour la comparaison documentaire.** Il manque encore les données propres aux matières, machines et lots pour transformer la proposition en instruction de fabrication exécutable. [Inventaire et empreintes](INVENTAIRE_SOURCES.json).

## Constats prioritaires

| ID | Localisation et constat | Statut / conséquence |
|---|---|---|
| R01 | `PROTOCOLE_FB2.md`, EXP-07 et §8 : la priorité proposée en cas de pénurie de RLD favorise le dispositif candidat ; la référence est parfois définie avec le « même dispositif ». | [H] Inadapté à la comparaison produit commercial/test commercial. Garder Breezhaler comme ancre RLD ; transfert de poudre uniquement comme pont diagnostique. |
| R02 | `CANDIDAT.md`, protocole et présentation : FB-2 et FB-2-C ont tous deux le PI. | [C] Ce contraste teste le porteur et ne permet pas de décider « PI nécessaire ou non ». La méthode 3 utilise exclusivement les API micronisés chez le fabricant ; le PI est hors programme actuel. |
| R03 | Les deux dossiers prennent 0,14 % de MgSt comme départ. L'EPAR historique mentionne 0,15 % dans « Formulation excipients », p. 24. | [E] Deux indications documentaires différentes, aucune mesure du RLD actuel. Le point de départ de méthode 3 est 0,15 % [H], révisable avant fabrication ; aucun optimum revendiqué. [EPAR](https://www.ema.europa.eu/en/documents/assessment-report/ultibro-breezhaler-epar-public-assessment-report_en.pdf). |
| R04 | Procédés GEA à fort cisaillement, PI par jet mill ; moyens locaux : Inversina et API micronisés achetés. | [H] Les durées/vitesses GEA ne se transfèrent pas directement. Aucun lot du programme actuel ne nécessite une campagne de PI ou un jet mill. |
| R05 | `PROTOCOLE_FB2.md`, EXP-04 : conversion de toutes les coupures NGI avec un exposant universel 0,5. | [E] L'équation 2 de l'article utilise un exposant propre à l'étage. Employer la calibration au débit réel ; une approximation peut modifier la FPD calculée. [Rzewińska 2025](https://link.springer.com/article/10.1208/s12249-025-03182-9). |
| R06 | `batch_record.py` calcule sans valider les entrées ; l'écriture omet les masses ≤ 0. | [C] Le cas IND 0,986, GLY-Br du PI 0,10 et MgSt du PI 0,90 produit environ **−6,335 g** de MgSt externe, sans rejet. Le bilan algébrique semble encore fermé. Le nouveau calculateur bloque ce cas. |
| R07 | `PROTOCOLE_FB2.md`, prélèvement du prémélange avant ajout des actifs. | [C] Retirer 3 g de support d'une charge de 300 g, sans réconcilier, enrichit ensuite les actifs d'environ 1 %. Déduire les masses réellement retirées ; caractériser sur un placebo ou échantillon dédié si possible. |
| R08 | Choix final sur DD/FPD et score W, puis règle de départage du porteur. | [H] Une même FPD peut masquer des distributions différentes. Ne pas confondre Carr d'un lactose seul et aptitude réelle du mélange au remplissage. |

## Plans expérimentaux : ce que les calculs permettent réellement

**Astra, 19 lots [C].** Le CSV contient 16 combinaisons uniques et équilibrées de quatre facteurs, plus trois fabrications centrales. Les bilans ferment à l'arrondi près. Ce plan peut estimer les quatre effets principaux et les six interactions à deux facteurs. Les carrés des quatre facteurs sont identiques dans ce plan : les centres détectent une courbure globale, sans séparer quatre courbures individuelles. Il reste raisonnable si ces quatre facteurs et leurs interactions sont les questions prioritaires ; il n'est pas nécessaire pour un premier candidat.

**Fable, DSD [C].** La matrice de conférence est valide. Les 15 lignes correspondent à 13 réglages distincts, dont le centre répété trois fois. Le modèle intercept + six effets principaux + six carrés a un rang de 13 : deux degrés de liberté résiduels, tous d'erreur pure ; aucune capacité de test du manque d'ajustement pour ce modèle saturé aux réglages distincts. Le modèle quadratique complet a 28 colonnes mais un rang de 13. Les interactions ne sont pas toutes estimables simultanément ; une sélection parcimonieuse doit être justifiée, pas garantie par le nom DSD. Un AICc proche de la saturation dépend aussi du comptage des paramètres, dont la variance.

Deux incohérences supplémentaires : le centre DSD est **4 % de fines et 50 % de ML001**, alors que FB-2 est **0 % et 100 %**. Le plan n'est donc pas réellement centré sur FB-2. Et un mélange 50/50 de lots GLY de d90 différents n'a pas nécessairement le d90 moyen : mesurer sa distribution. Si ces lots diffèrent aussi en surface ou fournisseur, « effet d90 » et « effet lot matière » sont confondus.

**Conclusion [H] :** aucun des deux plans ne domine l'autre sur toutes les questions. Le gain vient surtout d'éviter un modèle dont les facteurs, les niveaux ou la voie de fabrication ne sont pas encore justifiés. [Calculs reproductibles](VERIFICATIONS.json).

## Sélection, lactose et modèles

- **MCDA [C/H]** : C2 obtient 3,94/5 et arrive premier dans environ 98,7 % des perturbations de poids du script. C'est une robustesse conditionnelle aux notes choisies, pas une probabilité de bioéquivalence. Baisser d'un point ses notes GLY et stabilité suffit à obtenir 3,59, sous C1 à 3,64. Les notes et l'élagage des candidats importent davantage que l'apparente précision du Monte-Carlo.
- **Scores lactose [C]** : avec les poids écrits, SV003 vaut **9**, pas 11 ; LH206 vaut **6**, pas 7. ML001 reste à 14. Cette correction ne transforme pas le classement en preuve expérimentale.
- **Identification des grades [H]** : le rapprochement de trois quantiles et d'une CDF interpolée produit des candidats plausibles. Il ne démontre pas l'identité de grades commerciaux anonymisés, ni une identité de lot. Les règles de score « simple versus mélange » ne suffisent pas à rendre les identifications fermes.
- **Physique [C/H]** : couverture de surface et fluctuations de comptage sont des modèles conditionnels à PSD, forme et rugosité. Ils ne démontrent pas l'impossibilité d'un mélange à faible cisaillement. Des agglomérats peuvent changer fortement la variance prédite.
- **Prédiction de l'article [E/H]** : ses entrées incluent les dépôts mesurés de l'autre actif ; ce n'est pas un prédicteur complet de recette avant tout NGI. Les lignes d'une formulation sont regroupées dans le partage des données : ne pas lui attribuer une fuite aléatoire entre lignes qui n'est pas décrite. L'importance d'une variable n'est pas une preuve causale. [Article, modélisation](https://link.springer.com/article/10.1208/s12249-025-03182-9).
- **Puissance [C/H]** : `equivalence_power.py` illustre utilement l'effet interlot sous son modèle log-normal. Il ne calcule pas la probabilité conjointe de réussir tous les étages, actifs et débits. Trois lots RLD ne donnent pas une estimation précise garantie de leur CV. La taille confirmatoire dépendra de la variabilité mesurée et du biais test/RLD.

## Réconciliation des ressources

Le protocole Fable est détaillé mais son budget doit être recalculé avant exécution :

- [C] 270 capsules = neuf boîtes de 30, pas dix. La comparaison 3 débits × (10 DD + 3 NGI) × 2 dispositifs consomme déjà 78 capsules par lot RLD, avant les essais destructifs complémentaires.
- [C] Si seuls les trois NGI à 30 L/min utilisent deux capsules, neuf profils consomment douze capsules, pas dix-huit. Le besoin dépend de la LOQ réelle.
- [C] 20 g de GLY + 1 g de MgSt = 21 g de charge avant pertes. « 5 % du bromure » représente 4,7619 % du PI binaire théorique, pas 5 % du PI.
- [C] À une densité apparente de 0,63 g/mL, 300 g occupent environ 0,476 L : 47,6 % d'un bol de 1 L, avant considération de son volume de travail. L'exemple de transposition à 195 g n'est pas une qualification d'une charge de 300 g.
- [C] Le stock annoncé de 100 capsules à E24 ne couvre pas à lui seul les essais initiaux, tous les prélèvements de stabilité et la réserve décrits. Une chromatographie simultanée des deux actifs ne nécessite pas deux injections par fraction.

## Traitement des cinq commentaires du PDF fourni

| Commentaire | Traitement dans la copie Astra revue |
|---|---|
| Brevet 5 % | Précision « exemple 2 » ; exemple 1 à 3,7 %. Le statut « Revoked » affiché par Google Patents est signalé comme indication non revalidée au registre officiel, sans conclusion de liberté d'exploitation. [Texte du brevet](https://patents.google.com/patent/EP2037879B1/en). |
| PSD GLY | Fenêtre interne distinguée des plages du tableau I : d50 1,20–4,62 µm ; d90 3,57–9,07 µm. |
| PSD lactose | d50 70–100 µm clairement interne ; tableau I environ 19,76–79,01 µm. [Tableau primaire](https://link.springer.com/article/10.1208/s12249-025-03182-9/tables/1). |
| Charbon | Exception explicite ajoutée pour l'actif déjà équivalent in vitro, conformément au §4.2.4. |
| CSV « anhydres » | Remplacement par titre des sels 100 % ; bases de calcul et chiffres conservés. |

Les cinq remarques sont fondées et intégrées. Leur verdict sur les calculs Astra est confirmé ; il ne valide pas la fabrication ni l'optimalité du plan de 19 lots. La copie revue porte en plus un renvoi à la méthode 3 et le signal EPAR 0,15 %. Les fichiers historiques restent conservés octet pour octet.
