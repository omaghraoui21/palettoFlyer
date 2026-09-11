# Générique d'Ultibro Breezhaler (indacatérol 110 µg / glycopyrronium 50 µg, poudre pour inhalation en gélule)

## Dossier de développement pharmaceutique — approche Fable, version 1.0 du 11/09/2026

> Portée : préformulation, plan de développement et stratégie d'équivalence pour un laboratoire équipé.
> Aucun lot n'a été fabriqué ni testé. Rien ici n'est destiné à une administration humaine.
> Les chiffres calculés sont reproductibles par `tools/*.py` ; les hypothèses sont marquées **[H]**, les faits sourcés **[S-n]**.

---

## 0. Ce qui distingue cette approche

Je ne pars pas d'une « formule F0 » à reproduire, mais d'une question : **quelles grandeurs physiques gouvernent la performance du princeps, et lesquelles pouvons-nous mesurer avant de fabriquer ?** Le dossier s'organise donc en QbD inversé :

1. Rétro-ingénierie quantitative des documents publics (§ 2) — en séparant ce qu'ils prouvent de ce qu'ils suggèrent.
2. Profil cible (QTPP) et attributs critiques (CQA) formulés comme des **écarts test/référence**, pas comme des valeurs absolues (§ 3).
3. Analyse de risque mécanistique reliant attributs matières et paramètres procédé aux CQA, avec des ordres de grandeur calculés (recouvrement de surface, statistique de mélange) (§ 4).
4. Formulations de départ définies comme **un domaine**, pas un point : la teneur en fines et le MgSt sont des facteurs du plan, pas des constantes héritées (§ 5).
5. Procédé exprimé en grandeurs transposables (vitesse périphérique, Froude, taux de remplissage, énergie spécifique), pas en tr/min (§ 6).
6. Plan d'expériences séquentiel à criblage définitif (15 lots, 5 facteurs) puis surface de réponse (§ 8).
7. Dimensionnement statistique de l'étude d'équivalence **avant** de choisir la formule, par simulation (§ 9) : c'est là que la plupart des projets DPI échouent, pas au laboratoire de formulation.

---

## 1. Faits établis par les documents publics

| Fait | Source | Ce qu'il implique pour nous |
|---|---|---|
| 143 µg de maléate d'indacatérol ≡ 110 µg d'indacatérol ; 63 µg de bromure de glycopyrronium ≡ 50 µg de glycopyrronium par gélule ; dose délivrée 85/43 µg | [S-1] | Contenu nominal fixé ; la dose délivrée de référence doit être **mesurée**, pas reprise du RCP |
| « 23,5 mg de lactose (sous forme monohydratée) » | [S-1] | Voir § 2.1 : deux scénarios de remplissage compatibles |
| Excipients : lactose monohydraté, stéarate de magnésium ; gélule HPMC taille 3 ; blister PA/Alu/PVC-Alu | [S-1][S-2] | Plateforme Q1 connue |
| Le glycopyrronium est transformé en **intermédiaire pharmaceutique (PI)** dans les 4 premières des 13 étapes ; l'indacatérol micronisé, le lactose et **du MgSt additionnel** sont ajoutés ensuite ; équilibrage des gélules avant blister | [S-2] p. 13–14 | Le MgSt est réparti en deux fractions ; le PI est très probablement un co-broyage GLY + MgSt (cf. brevet [S-6]) |
| Le produit a été développé à partir de Seebri ; **la FPF d'indacatérol est plus élevée en association** qu'en monothérapie, ce qui a motivé la baisse de 150 à 110 µg | [S-2] p. 13 | Notre cible de FPF pour IND est celle d'Ultibro, **supérieure** à celle d'Onbrez : une plateforme lactose seule (type Onbrez) sera probablement insuffisante pour IND |
| Les deux substances sont non hygroscopiques, mais le produit fini est sensible à l'humidité (FPM) | [S-2] p. 10–15 | L'eau agit sur les interfaces, pas sur le solide massif : contrôler HR de fabrication et équilibrage |
| Étude publique la plus proche : 70 mélanges à 0,14 % MgSt, 300 g en cuve GEA 1 L, prétraitement lactose+MgSt 2500 tr/min 2 min puis actifs 1500 tr/min 3 min, NGI 100 L/min via RS01 | [S-3] | Point de départ crédible pour le procédé ; ses PSD (tableau I) bornent le domaine matières |
| Co-micronisation GLY + 1–20 % MgSt (préférence 3–5 %), exemples à 3,7 % et 5 % ; brevet EP **révoqué** (statut Google Patents au 11/09/2026) | [S-6] | Piste technique documentée ; statut à confirmer par un conseil en PI, pays par pays |
| Guide EMA d'équivalence Rev. 2 en vigueur depuis le 01/02/2026 : IC 90 % dans 85–118 % par étage/groupe, ≥ 3 lots × ≥ 10 unités, 3 débits, associations fixes (§ 4.2.4) | [S-4] | Le critère est **statistique et par actif** : voir § 9 |
| Précédent : Indacaterol/Glycopyrronium Polpharma, hybride art. 10(3), approuvé 18/06/2025 avec deux études PK (avec/sans charbon), marges Cmax élargies | [S-5] | L'équivalence purement in vitro n'a pas été obtenue par ce précédent : budgéter la PK |

---

## 2. Rétro-ingénierie : ce que les chiffres disent vraiment

### 2.1 Masse de remplissage — deux scénarios, un test décisif

Les RCP de la famille Breezhaler donnent des masses de lactose qui, croisées, contraignent le remplissage :

| Produit | Lactose déclaré | Actif (sel) | Somme lactose + sel |
|---|---|---|---|
| Onbrez 150 µg | 24,8 mg (« lactose ») | 0,194 mg | 24,99 mg |
| Onbrez 300 µg | 24,6 mg | 0,389 mg | 24,99 mg |
| Seebri 50 µg | 23,6 mg (« sous forme monohydratée ») | 0,063 mg | 23,66 mg + MgSt |
| Ultibro | 23,5 mg (« sous forme monohydratée ») | 0,143 + 0,063 mg | 23,71 mg + MgSt |

Onbrez : la différence de 0,2 mg de lactose entre 150 et 300 µg égale la différence de sel (0,194 mg) → **remplissage constant à 25,0 mg**, lactose déclaré tel quel. [S-7]

Seebri/Ultibro : la baisse de 0,1 mg de lactose correspond, à l'arrondi près, à l'ajout de 0,143 mg de maléate d'indacatérol → même remplissage pour les deux, à ±0,05 mg. Mais la valeur absolue admet deux lectures :

- **Scénario A [H]** — lactose déclaré en **équivalent anhydre** : 23,5 mg × 360,31/342,30 = 24,74 mg de monohydrate ; + 0,206 mg de sels + ~0,035 mg MgSt → **24,98 ≈ 25,0 mg** de remplissage. Cohérent avec Onbrez.
- **Scénario B [H]** — lactose déclaré en masse de monohydrate : remplissage ≈ **23,75 mg**, soit un changement de masse de dose par rapport à Onbrez.

Les deux sont arithmétiquement cohérents. La distinction se tranche en **une journée** : pesée nette du contenu de 30 gélules de référence sur 3 lots (J1, § 11). Je ne fige donc pas 25 mg ; `tools/formulation.py` produit FB-1 (25,0 mg) et FB-1b (23,75 mg).

### 2.2 Ce qu'on ne peut pas déduire des documents publics
Proportion de lactose fin, grade(s) de lactose, quantité exacte de MgSt et sa répartition PI/externe, PSD des actifs, conditions d'équilibrage. Ces inconnues deviennent soit des **mesures sur le princeps** (PSD du lactose après dissolution sélective des actifs ; dosage du MgSt par ICP-Mg ; eau par Karl Fischer ; Raman/SEM-EDX pour la localisation du MgSt), soit des **facteurs du plan** (§ 8).

### 2.3 Rapport des doses délivrées
85/110 = 77 % pour IND, 43/50 = 86 % pour GLY [S-1]. Une rétention différentielle de 9 points entre deux actifs de PSD voisines n'est pas triviale : elle signale des interactions différentes avec le porteur, la gélule et le dispositif. La formulation doit reproduire **ce différentiel**, ce qui interdit de raisonner sur un « FPF global ».

---

## 3. Profil cible (QTPP) et attributs critiques

| CQA | Cible | Pourquoi | Méthode |
|---|---|---|---|
| Dose délivrée (DD), par actif | Rapport T/R des moyennes dans 0,85–1,15 ; IC 90 % à l'étude pivot | Critère 7 du guide [S-4] | DUSA, 3 débits |
| APSD complète, par actif, 3 débits | IC 90 % dans 85–118 % par étage/groupe | § 5.1 [S-4] | NGI + préséparateur, débit calibré |
| Dépendance au débit (FPD vs √ΔP) | Pente similaire à la référence | § 5.2.1 [S-4] ; conditionne la PK | 3 pertes de charge, 2–6 kPa |
| Uniformité de dose délivrée | Ph. Eur. 0671 (préparations pour inhalation) / spécification interne RSD ≤ 5 % | Prérequis à toute comparaison | 10 unités début/milieu/fin |
| Teneur et homogénéité de mélange | 95–105 %, RSD ≤ 3 % à l'échelle 25 mg | Détecte la ségrégation | Prélèvement voleur qualifié, LC |
| Stabilité APSD/DD | Dérive ≤ celle de la référence à 6 mois 40/75 | Le produit est sensible à l'humidité [S-2] | ICH, blister final |
| Impuretés | Ph. Eur./ICH Q3B, profil ≤ référence | L'indacatérol porte une amine secondaire : risque de réaction de Maillard avec le lactose (sucre réducteur), à évaluer en stress | LC-UV/MS |
| Fonction gélule/dispositif | Perforation nette, sans fragment, rétention < 10 % | Rétention gouverne 15–25 % de la dose | Pesée gélule vide, inspection |

---

## 4. Analyse de risque mécanistique

### 4.1 Ordres de grandeur (calculés, hypothèses dans `outputs/physique_melange.json`)

Pour une gélule FB-1 avec un porteur de d50 60 µm (facteur de rugosité 2,5) [H] :

- Surface du porteur : **≈ 40 cm² par gélule** (≈ 0,16 m²/g) ; ≈ 140 000 particules de porteur.
- Recouvrement par aire projetée : IND ≈ 2,0 %, GLY ≈ 0,9 %, MgSt ≈ 0,2 % → **≈ 3 % au total**. Régime de mélange adhésif dilué : les fines occupent les sites les plus énergétiques du porteur, et la performance dépend de la **distribution d'énergie de surface** du lactose, pas de sa surface totale.
- ≈ 180 particules d'IND et ≈ 80 de GLY par particule de porteur : la compétition IND/GLY pour les sites actifs est réelle ; c'est le mécanisme plausible de la hausse de FPF d'IND en association [S-2] et de l'interaction réciproque rapportée par [S-3].
- Le MgSt à 0,14 % ne couvre que 0,2 % du porteur **s'il reste particulaire**. Son effet connu de « dry coating » exige qu'il soit étalé en film par cisaillement : **le prétraitement à fort cisaillement est donc un paramètre critique, pas une commodité.** Le MgSt ajouté dans un mélangeur à faible cisaillement (Turbula) n'aura pas le même effet à composition égale.

### 4.2 Statistique de mélange
CV théorique d'un mélange aléatoire parfait à l'échelle d'une dose de 62,5 µg de GLY :
- particules primaires 2 µm : **0,03 %** ;
- agglomérats de 30 µm : 1,2 % ; de 100 µm : **7 %**.

L'homogénéité à l'échelle de la dose n'est donc jamais limitée par la statistique des particules : elle est limitée par la **désagglomération des actifs micronisés** et par la ségrégation post-mélange. Conséquence : (i) contrôle de l'état d'agglomération des actifs à la réception (PSD à plusieurs pressions de dispersion) ; (ii) énergie du mélange final suffisante pour casser les agglomérats sans arracher le MgSt ; (iii) manipulations minimales après mélange.

### 4.3 Matrice CMA/CPP → CQA (risque a priori : H haut, M moyen, F faible)

| Attribut / paramètre | DD | APSD IND | APSD GLY | Uniformité | Stabilité | Justification |
|---|---|---|---|---|---|---|
| PSD GLY (d90, span) | M | F | **H** | M | H | Facteur dominant de [S-3] pour GLY ; GLY plus cohésif/agglomérant |
| PSD IND | F | **H** | F | F | M | [S-3] |
| PSD lactose porteur (d10, fines natives) | M | **H** | **H** | M | M | d10 du lactose ressort pour GLY et la PSD du porteur pour IND [S-3] |
| Lactose fin ajouté (0–8 %) | M | H | H | F | M | Saturation des sites actifs ; effet non monotone attendu |
| MgSt total et localisation (PI vs externe) | M | H | **H** | F | **H** | Anti-adhérent et barrière humidité ; stabilité des surfaces |
| Énergie du prétraitement | F | H | H | F | M | Étalement du MgSt ; attrition du lactose si excessive |
| Énergie du mélange final | F | M | M | **H** | F | Désagglomération vs arrachage du MgSt |
| HR pendant fabrication et équilibrage | M | M | M | F | **H** | [S-2] ; capillarité et électrostatique |
| Gélule (HPMC, teneur en eau, perforation) | **H** | M | M | M | M | Rétention dans la gélule |
| Dispositif (résistance, géométrie) | **H** | **H** | **H** | F | F | Doit être figé avant la phase 2 |
| Remplissage (compaction, masse) | M | M | M | **H** | F | Compaction → agglomérats de dose |

---

## 5. Formulations de départ

Composition de référence interne **FB-1** (25,0 mg ; 0,14 % MgSt [S-3] ; **0 % de fines ajoutées**, le lactose fin étant un facteur du plan et non une constante) ; calcul sur sels à titre 100 %, corrigé ensuite par le CoA (facteur = M_sel/M_base ÷ titre en sel tel quel ; si le CoA exprime le titre en base, ne pas appliquer le facteur de sel).

| Composant | mg / gélule | g / lot 300 g (12 000 unités) |
|---|---|---|
| Maléate d'indacatérol micronisé | 0,142530 | 1,71036 |
| Bromure de glycopyrronium micronisé | 0,062546 | 0,75055 |
| Stéarate de magnésium (total) | 0,035000 | 0,42000 |
| Lactose monohydraté porteur, q.s. | 24,759924 | 297,11909 |
| **Total** | **25,000** | **300,000** |

Variantes calculées dans `outputs/bilan_matiere.csv` :
- **FB-1-PI** : même composition, MgSt réparti 0,003127 mg dans le PI (5 % du bromure, ex. 2 de [S-6]) + 0,031873 mg externe ; PI théorique 0,065673 mg à 95,24 % de bromure.
- **FB-1b** : remplissage 23,75 mg (scénario B du § 2.1), à ne fabriquer que si la pesée du princeps l'impose.
- **FB-1 corrigée CoA** : exemple à 98,2 % / 99,1 %.

Constantes : M(IND) 392,50 ; M(maléate) 508,57 ; M(GLY⁺) 318,44 ; M(bromure) 398,34 g/mol → 142,53 µg et 62,546 µg de sels par gélule, cohérents avec les 143/63 µg arrondis du RCP. Lactose FB-1 : 24,76 mg de monohydrate = 23,52 mg d'équivalent anhydre (cohérent avec le scénario A).

Pourquoi **pas** de lactose fin dans la référence interne : Onbrez et Seebri sont formulés sur la même plateforme ; rien dans [S-2] ne mentionne deux grades de lactose ; et [S-3] montre que les fines natives (d10 du lactose) portent déjà l'effet. Fixer 6 % de fines avant de savoir si le princeps en contient est une hypothèse coûteuse à défaire. Le plan explore 0–8 %.

### Matières premières — fenêtre exploratoire et contrôles

| Matière | Fenêtre [H], bornée par [S-3] tableau I | Contrôles à la réception |
|---|---|---|
| GLY bromure micronisé | d50 1,2–3,0 µm ; d90 3,6–6,5 µm ; **2 lots à d90 distincts** (facteur E) | PSD (3 pressions de dispersion), XRPD (forme A), eau, impuretés, surface spécifique, état d'agglomération |
| IND maléate micronisé | d50 1,4–2,4 µm ; d90 2,7–5,0 µm | Idem + pureté chirale, fraction amorphe (DSC/DVS) |
| Lactose porteur, grade inhalation | Deux grades de d50 ≈ 50–60 µm : tamisé sans fines (x10 ≈ 35) et broyé à fines intrinsèques (x10 ≈ 5) — voir `lactose/RESULTATS.md` | PSD, % < 4,5 et < 15 µm, SSA, span, morphologie SEM, eau, amorphe (DVS), fraction β |
| Lactose micronisé (fines ajoutées) | x50 ≈ 3 µm, x90 ≈ 9 µm (type Lactohale 300) ; fines ≥ 3 µm préférées aux ultrafines (Grasmeijer 2014) | PSD, eau, amorphe |
| MgSt, grade inhalation (végétal) | d50 5–10 µm | PSD, surface spécifique, ratio stéarate/palmitate, hydratation (XRPD), impuretés |
| Gélule HPMC taille 3 pour inhalation | Teneur en eau 4–6 % [H] | Masse, eau, perforation sur le dispositif cible |

---

## 6. Procédé : décisions et grandeurs transposables

### 6.1 Arbre de décision de l'architecture
```
Pesée du princeps (J1) ──► remplissage 25,0 ou 23,75 mg
        │
        ▼
Phase 0 : FB-1 et FB-1-PI, 2 lots indépendants chacun
        │
        ├─ FB-1 atteint DD et APSD GLY à ±15 % de la réf. à 3 débits ──► voie "MgSt externe seul" (plus simple, moins de PI)
        ├─ seul FB-1-PI y parvient, ou stabilité GLY meilleure à 4 sem. ──► voie PI (qualifier le co-broyage)
        └─ aucun ──► revoir PSD GLY et lactose avant tout plan
```

### 6.2 Paramètres exprimés pour être transposés
Le point de [S-3] (GEA 1 L, 2500 tr/min, turbine ≈ 85 mm [H]) correspond à une **vitesse périphérique ≈ 11 m/s** et un Froude ≈ 300. Passer à une cuve de 5 L (turbine ≈ 150 mm) **au même tr/min** porte la vitesse périphérique à 19,6 m/s et multiplie l'indice d'énergie spécifique par 3,4 ; à vitesse périphérique constante (≈ 1 420 tr/min), on la divise par 1,6 (`outputs/transposition_melangeur.csv`). Aucune règle unique ne conserve tout : je propose de conserver **la vitesse périphérique** pour le prétraitement (étalement du MgSt, gouverné par le cisaillement local) et **le nombre de révolutions × taux de remplissage** pour le mélange final (gouverné par la convection), puis de vérifier par les CQA.

| Étape | Paramètre | Point central | Grandeur de transposition |
|---|---|---|---|
| Désagglomération du lactose | Tamis 250 µm ou broyeur conique doux | — | Contrôler la PSD avant/après (pas d'attrition) |
| Chargement | Lactose en 2 couches, MgSt entre les couches | Taux de remplissage 30–40 % de la cuve | Constant à l'échelle |
| Prétraitement | Vitesse périphérique 4 m/s [H, facteur C : 2–6 m/s] ; 2 min | Hacheur arrêté | Vitesse périphérique constante |
| Ajout des actifs | Arrêt ; actifs déposés en sandwich entre deux portions de porteur prétraité ; pertes de transfert réconciliées | — | — |
| Mélange final | Vitesse périphérique 2,4 m/s ; 3 min [facteur D : 1–5 min] | Température du lit < 30 °C | Révolutions × taux de remplissage |
| Repos / dé-électrisation | 30 min en récipient antistatique fermé, HR 35–45 % | — | — |
| Remplissage | Doseur à vide/tambour, compaction minimale ; 25,0 mg ± 3 % | Poids net 100 % contrôlé | — |
| Équilibrage | 24 h et 72 h à 22 °C / 40 % HR [H, à comparer à un témoin scellé immédiatement] | — | — |
| Conditionnement | Blister PA/Alu/PVC-Alu, scellage qualifié | — | — |

Environnement : 20–25 °C, 30–45 % HR, enregistré en continu ; les actifs ne sont ni séchés ni tamisés isolément.

### 6.3 Ce que [S-3] ne permet pas d'affirmer
Son indicateur d'« énergie de mélange » (Eq. 1) est un produit dimensionnel de la masse, du cube de la vitesse, du carré du rayon et du temps ; il est utile **au sein d'un même mélangeur**, pas pour comparer deux géométries. D'où l'usage de grandeurs adimensionnelles ci-dessus.

---

## 7. Stratégie analytique

Ordre de priorité : **la référence d'abord**. Aucune formulation n'est jugée avant que la variabilité de la référence soit connue (≥ 5 lots, 3 débits, DD + APSD par actif), car c'est elle qui dimensionne l'étude d'équivalence (§ 9).

| Mesure | Mise en œuvre | Décision qu'elle permet |
|---|---|---|
| Pesée nette du contenu | 30 gélules × 3 lots de référence | Trancher § 2.1 |
| Dosage MgSt dans le princeps | ICP-OES Mg après minéralisation | Borner le facteur B |
| PSD du lactose du princeps | Dissolution sélective des actifs (solvant à définir : les actifs sont solubles dans MeOH/ACN, le lactose peu) puis diffraction laser ; contrôler l'absence de dissolution partielle du lactose | Fixer le grade de porteur et la présence de fines |
| Localisation du MgSt | Raman/SEM-EDX sur poudre princeps vs FB-1 vs FB-1-PI | Interpréter la voie PI |
| Teneur et homogénéité | LC, 10 prélèvements de 25 mg + gélules début/milieu/fin | Distinguer mélange, ségrégation, remplissage |
| DD | DUSA, 4 L, 3 débits (30/60/90 L/min ou 2/4/6 kPa selon résistance) | Critères 7 et 8 [S-4] |
| APSD | NGI + préséparateur, cut-off recalculés au débit, FPD < 5 µm par interpolation de la cumulée ; bilan massique 85–115 % | § 5.1 [S-4] |
| Résistance du dispositif | R = √ΔP/Q | Choix option 1/2 pour la dépendance au débit |
| Eau | KF (poudre) ; gélule séparément | Stabilité |
| Impuretés | LC-UV/MS, stress 40/75 ouvert 1 mois | Compatibilité |

Méthode LC de départ : RP C18, KH₂PO₄ 20 mM pH 3,5 / ACN-MeOH 9:1 en gradient, 210 nm, extraction eau/MeOH/ACN 3:1:1 [S-3] ; à valider (spécificité vs lactose et MgSt, récupération sur chaque surface du NGI, LOQ ≤ 2 % de la dose sur les étages 6–7 et MOC pour les deux actifs, ce qui est exigeant pour GLY à 43 µg délivrés).

---

## 8. Plan expérimental séquentiel

### Phase 0 — Méthodes et référence (semaines 1–8)
Qualification DD/APSD/LC ; caractérisation de ≥ 5 lots de référence ; pesée du contenu ; **FB-2 (ML001, PI 5 % + MgSt externe) et son challenger FB-2-C (porteur 50/50 ML001–SV003) × 2 lots** — sélection justifiée dans `selection/CANDIDAT.md`, qui remplace la comparaison FB-1/FB-1-PI initiale ; stabilité ouverte 4 semaines. **Sortie :** architecture (PI ou non), remplissage, résistance du dispositif candidat, estimation des CV inter-lot et intra-lot de la référence.

### Phase 1 — Criblage définitif, 6 facteurs, 15 lots (semaines 9–20)
Plan de Jones-Nachtsheim construit sur la matrice de conférence C6 : 12 sommets + 3 centres (`outputs/plan_dsd_15_lots.csv`, propriétés vérifiées : effets principaux orthogonaux entre eux et aux interactions d'ordre 2 ; 5 lots par niveau par facteur).

| Facteur | − | 0 | + |
|---|---|---|---|
| A · lactose micronisé ajouté | 0 % | 4 % | 8 % |
| B · MgSt total | 0,08 % | 0,14 % | 0,20 % |
| C · vitesse périphérique du prétraitement (2 min) | 2 m/s | 4 m/s | 6 m/s |
| D · durée du mélange final (2,4 m/s) | 1 min | 3 min | 5 min |
| E · d90 du lot de GLY | 3,5 µm | 5,0 µm (mélange 50/50) | 6,5 µm |
| F · fraction de porteur broyé (ML001-type) dans le porteur, complément tamisé (SV003-type) | 0 % | 50 % | 100 % |

Le facteur F et le grade des fines proviennent de l'étude documentaire `lactose/RESULTATS.md` (prompt figé dans `lactose/PROMPT.md`) : deux porteurs de même d50 (~50–60 µm) mais contrastés sur d10, fines intrinsèques et rugosité, attributs identifiés comme causaux par Rzewińska 2025, Kinnunen 2014 et Bungert 2021.

Pourquoi ce plan plutôt qu'un factoriel 2⁴ complet à 19 lots : deux facteurs de plus (la PSD du GLY, dominante selon [S-3], et le type de porteur) pour 4 lots de moins, la courbure estimable par facteur (les effets fines/MgSt sont attendus non monotones), et une projection directe vers un plan composite si 2–3 facteurs dominent. Le prix : les interactions d'ordre 2 sont partiellement confondues entre elles (pas avec les effets principaux) ; c'est acceptable en criblage.

Réponses par lot : DD et FPD < 5 µm pour chaque actif à 30 et 90 L/min (3 NGI), rétention gélule + dispositif, RSD de DD, RSD de teneur, écoulement. **Réponse composite pré-spécifiée :** pire écart |ln(T/R)| parmi {DD, FPD} × {IND, GLY} × {30, 90 L/min} — à minimiser. Analyse : régression sur effets principaux + termes quadratiques, sélection par AICc, lot = unité expérimentale ; les centres donnent l'erreur pure et la dérive temporelle.

### Phase 2 — Surface de réponse (semaines 21–30)
Composite centré sur les 2–3 facteurs retenus, 3 centres, 11–17 lots ; dispositif commercial figé ; 3 débits. Sortie : domaine de fonctionnement où **les deux actifs** satisfont simultanément ±10 % sur DD et FPD, avec marge pour la variabilité inter-lot.

### Phase 3 — Confirmation et robustesse (semaines 31–44)
3 lots au point retenu avec 2 lots de chaque matière ; défis : HR 30/50 %, temps d'attente 0/24/72 h, cadence de remplissage, 1,5 kg. Stabilité 1/3/6 mois 25/60 et 40/75. Sortie : lots représentatifs pour l'étude pivot.

---

## 9. Équivalence : dimensionner avant de croire

Le critère du guide [S-4] est un IC 90 % du rapport des moyennes géométriques dans 85–118 %, par étage/groupe, par actif et par débit, avec ≥ 3 lots × ≥ 10 unités. J'ai simulé la probabilité de succès (`outputs/puissance_equivalence_in_vitro.csv`, 2 000 tirages par scénario) en distinguant deux analyses : sur **moyennes de lot** (l'unité statistique est le lot, conservateur) et **regroupée** (toutes les unités, ignore la corrélation intra-lot).

| CV inter-lot | CV intra-lot | Lots × unités | Vrai rapport | P(succès), moyennes de lot | P(succès), regroupée |
|---|---|---|---|---|---|
| 4 % | 10 % | 3 × 10 | 1,00 | 0,87 | 0,99 |
| 4 % | 10 % | 3 × 10 | 1,10 | 0,40 | 0,73 |
| **8 %** | 10 % | **3 × 10** | **1,00** | **0,34** | 0,90 |
| 8 % | 10 % | 3 × 20 | 1,00 | 0,36 | 0,94 |
| 8 % | 10 % | 6 × 10 | 1,00 | 0,85 | 0,99 |
| 12 % | 10 % | 3 × 10 | 1,00 | 0,11 | 0,71 |
| 12 % | 10 % | 6 × 10 | 1,00 | 0,42 | 0,90 |

Conclusions opérationnelles :
1. **Doubler les unités par lot ne sert presque à rien ; ajouter des lots change tout.** Avec 8 % de CV inter-lot, passer de 3 × 10 à 3 × 20 gagne 2 points ; passer à 6 × 10 gagne 50 points.
2. Un vrai rapport de 1,10 — pourtant « dans ±15 % » — n'a que 40–70 % de chances de passer : la cible de développement doit être un rapport de **1,00 ± 0,05**, pas ±15 %.
3. L'écart entre les deux colonnes est l'enjeu du protocole statistique : le guide exige un protocole pré-spécifié ; le choix de l'unité statistique (lot vs inhalateur) doit être justifié auprès du CHMP en avis scientifique **avant** la phase 3, sinon on découvre le problème à la lecture des résultats.
4. La variabilité inter-lot de la **référence** entre dans le même calcul : d'où les ≥ 5 lots de référence en phase 0 et le choix de lots proches de la médiane (§ 5.2.3 [S-4]).

Regroupement d'étages : pré-spécifié sur les données pilotes, uniquement pour les étages < 5 % de la DD de référence, ≥ 4 groupes, ≤ 3 étages par groupe, FPD représentée par ≥ 2 groupes [S-4]. Pour GLY à 43 µg délivrés, les étages 6–7 et le MOC seront probablement à regrouper ; la LOQ de la méthode conditionne donc le plan statistique.

### Plan B : pharmacocinétique
Si un actif échoue in vitro, **les deux** sont évalués en PK [S-4 § 4.2.4]. Architecture attendue (à confirmer en avis scientifique) : GLY — absorption pulmonaire rapide, AUC₀₋₃₀ min et Cmax sans charbon comme substituts d'efficacité, AUC₀₋t pour la sécurité [S-4 § 6.2.2, S-5] ; IND — contribution digestive non négligeable, étude avec charbon pour l'efficacité (sauf si IND est l'actif déjà équivalent in vitro, auquel cas l'étude avec charbon devient inutile [S-4 § 4.2.4]). IC 90 % dans 80,00–125,00 % ; le précédent [S-5] a obtenu un élargissement pour Cmax sur justification de variabilité intra-individuelle, ce qui ne se planifie pas a priori. Étude croisée répliquée, 40–60 volontaires sains [H], LC-MS/MS avec LLOQ de l'ordre du pg/mL pour GLY [H].

---

## 10. Dispositif, gélule, réglementaire

- **Dispositif** : figer avant la phase 2 un inhalateur monodose à faible résistance (RS01 ou équivalent) dont la résistance mesurée est à ±15 % du Breezhaler (option 2 du § 5.2.1 sinon option 1 à 3 pertes de charge). Le Breezhaler sert de banc en phase 0 uniquement. Marquage CE du dispositif selon le règlement (UE) 2017/745 (produit combiné, art. 117).
- **Gélule HPMC** : qualifier la perforation sur le dispositif cible (fragments, taux d'ouverture), l'eau et la rétention ; HPMC et gélatine ne sont pas interchangeables pour la rétention électrostatique.
- **Voie réglementaire** : viser l'article 10(1) si tous les critères in vitro sont remplis ; prévoir l'hybride 10(3) comme dans [S-5]. Demander un avis scientifique CHMP après la phase 1 avec les données de référence et le protocole statistique.
- **Propriété intellectuelle** : EP2037879 (co-micronisation GLY/MgSt) est révoqué selon Google Patents [S-6], mais la famille comporte d'autres membres nationaux et des brevets de formulation d'association et de dispositif existent ; une recherche de liberté d'exploitation par pays est indispensable avant la phase 2. Ce dossier ne fournit aucun avis juridique.

---

## 11. Jalons et volumes

| Jalon | Contenu | Critère de passage | Lots (300 g) |
|---|---|---|---|
| J0 | Sourcing (2 lots GLY, 1 IND, 2 lactoses, 1 MgSt), dispositif candidat, FTO préliminaire | Matières et référence disponibles | 0 |
| J1 | Méthodes qualifiées ; ≥ 5 lots de référence caractérisés ; pesée du contenu | CV inter-lot référence connu ; remplissage tranché | 0 |
| J2 | FB-1 / FB-1-PI × 2 ; stabilité 4 semaines | Une architecture retenue ; homogénéité RSD ≤ 3 % | 4 |
| J3 | DSD 15 lots | Modèle avec R² ajusté ≥ 0,7 sur la réponse composite ; facteurs dominants identifiés | 15 |
| J4 | RSM + dispositif figé | Domaine où |ln(T/R)| ≤ 0,05 sur toutes les réponses | 11–17 |
| J5 | 3 lots de confirmation, 1,5 kg, stabilité 6 mois, avis scientifique | Protocole pivot approuvé | 3 + 2 |
| J6 | Lots pivots et étude d'équivalence | IC 90 % conformes ou PK lancée | 3 (pilote industriel) |

Total ≈ 35–40 lots de 300 g (≈ 12 kg de poudre) avant les lots pivots ; ≈ 60–70 g d'IND et ≈ 30 g de GLY, hors PI et hors pertes.

---

## 12. Limites explicites

- Les grandeurs du § 4.1 dépendent d'hypothèses de PSD, densité et rugosité ; elles fixent des ordres de grandeur, pas des valeurs.
- Le diamètre de turbine du GEA 1 L est supposé ; la transposition du § 6.2 doit être recalculée avec la géométrie réelle.
- La simulation du § 9 suppose des distributions log-normales indépendantes et une variance commune test/référence ; elle sert à dimensionner, pas à remplacer le protocole statistique.
- Les fenêtres matières sont bornées par une seule publication [S-3] ; elles ne sont pas des spécifications.
- Aucun accès aux dossiers confidentiels ; aucun essai réalisé.

---

## 13. Sources (consultées le 11/09/2026)

- **[S-1]** RCP Ultibro Breezhaler, EMA (information produit) et emc n° 3496 — sections 2, 3, 6.
- **[S-2]** EMA, CHMP Assessment Report Ultibro Breezhaler, EMA/CHMP/296722/2013, 25/07/2013 — p. 10–15 (substances, PI, 13 étapes, équilibrage, sensibilité à l'humidité, ajustement de dose d'indacatérol).
- **[S-3]** Rzewińska A. et al., *Factors Influencing the Dispersibility of Glycopyrronium Bromide and Indacaterol Maleate – Combined In Vitro and In Silico Study*, AAPS PharmSciTech 26:230 (2025), doi:10.1208/s12249-025-03182-9 — matériaux, tableau I, procédé, LC, NGI.
- **[S-4]** EMA, *Guideline on the requirements for demonstrating therapeutic equivalence between OIP for asthma and COPD*, CPMP/EWP/4151/00 Rev. 2, adopté 14/07/2025, en vigueur 01/02/2026 — § 4.2.4, 5.1, 5.2, 6.
- **[S-5]** Swedish MPA, Public Assessment Report *Indacaterol/Glycopyrronium Polpharma*, SE/H/2564/01/DC, finalisé 18/06/2025.
- **[S-6]** EP2037879 A1/B1 (Novartis), *Compositions of glycopyrronium salt for inhalation* — revendications 6–7, exemples 1–2 ; statut « Revoked » sur Google Patents.
- **[S-7]** RCP Onbrez Breezhaler 150/300 µg (emc n° 7794) ; RCP Seebri Breezhaler 44 µg (emc n° 2840) — section 2.
- EMA, *Guideline on the pharmaceutical quality of inhalation and nasal medicinal products*, EMEA/CHMP/QWP/49313/2005 Rev. 1, en vigueur 01/02/2026.
- Jones B., Nachtsheim C.J., *A Class of Three-Level Designs for Definitive Screening in the Presence of Second-Order Effects*, J. Qual. Technol. 43(1), 2011 — construction du DSD.
