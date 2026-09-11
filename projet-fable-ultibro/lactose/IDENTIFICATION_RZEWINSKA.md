# Identification des grades de lactose DFE Pharma du tableau I de Rzewińska et al. (2025)

Question posée : à quels grades commerciaux correspondent les 10 triplets (d10, d50, d90) du tableau I ? L'article dit seulement « *Lactose monohydrate was supplied by DFE Pharma* » et « *one or two grades of lactose and magnesium stearate were mixed* » — donc **des mélanges de grades sont explicitement possibles**, et la question « quel grade ? » doit être posée pour chaque ligne comme « quel grade ou quel mélange ? ».

## 1. Méthodologie

### 1.1 Constituer la bibliothèque de référence
Trois niveaux de fiabilité, du plus faible au plus fort :
1. **PSD « typiques » des pages produit DFE** (dfepharma.com, consultées le 11/09/2026) : valeurs arrondies, sans méthode précisée.
2. **Spécification de libération** (fiche PD-0063, Respitose ML001) : fenêtre laser sec d10 3–7 / d50 37–61 / d90 124–194 µm — utile pour un test d'appartenance strict.
3. **PSD mesurées indépendamment sur les mêmes grades** : Karabulut et al., RDD 2022, tableau 1 (Malvern Spraytec, 6 grades DFE) — LH200 13,4/69,0/148,7 ; LH201 4,7/23,9/63,9 ; LH206 30,1/83,2/161,9 ; ML001 5,6/49,0/143,1 ; ML006 2,7/17,0/45,9 ; SV003 30,5/60,2/100,7.

| Grade | Type | d10 | d50 | d90 | Source retenue |
|---|---|---|---|---|---|
| Respitose SV003 | tamisé | 35 | 60 | 95 | DFE typ. (Karabulut : 30/60/101) |
| Respitose SV010 | tamisé | 45 | 110 | 175 | DFE typ. |
| Respitose ML001 | broyé | 5 | 50 | 150 | DFE typ. ; spec 3–7/37–61/124–194 |
| Respitose ML006 | broyé fin | 2,7 | 17 | 46 | Karabulut 2022 (pas de typ. publiée) |
| Lactohale 100 | tamisé | 55 | 130 | 220 | DFE typ. |
| Lactohale 200 | broyé | 10 | 70 | 140 | DFE typ. (Karabulut : 13/69/149) |
| Lactohale 201 | broyé | 5 | 20 | 55 | DFE typ. |
| Lactohale 206 | broyé sans fines | 35 | 85 | 150 | DFE typ. |
| Lactohale 210 | fines grossières | 5 | 15 | 40 | DFE typ. (brochure : 3/15/44) |
| Lactohale 220 | fines | 3 | 13 | 34 | brochure DFE « blend products » 02/2022 |
| Lactohale 230 | fines | 1,4 | 8,4 | 23 | estore DFE |
| Lactohale 300 | micronisé | ~1 | 3 | 9 | DFE typ. (d10 non publié, hypothèse) |

### 1.2 Modèle de mélange
Chaque grade est représenté par une cumulée Q3 en ln(d), linéaire par morceaux entre 0 % (d10/5), 10 %, 50 %, 90 % et 100 % (1,8 × d90). Un mélange binaire à fraction massique *f* a pour cumulée *f·Q3ₐ + (1−f)·Q3_b* ; ses percentiles sont obtenus par inversion (bissection). L'écart est la **RMS des log(d_obs/d_préd)** sur les trois percentiles : 0,03 ≈ ±3 %, 0,10 ≈ ±10 %. On compare chaque ligne au meilleur grade seul et au meilleur mélange binaire (pas de 5 %). Script : `identify_grades.py` (pur Python, ~2 s).

### 1.3 Règles de décision
- **Grade seul** si RMS ≤ 0,10 et qu'aucun mélange ne fait mieux que 60 % de cet écart.
- **Mélange** si le meilleur binaire est ≤ 0,10 **et** nettement meilleur que le grade seul ; dans ce cas plusieurs couples sont souvent équivalents (**dégénérescence** : trois percentiles ne suffisent pas à identifier deux composants + une fraction), et on les rapporte tous.
- Cohérence physique : un d10 < 5 µm avec un d90 > 120 µm ne peut pas venir d'un grade tamisé seul (les tamisés ont d10 ≥ 30) ; il exige un grade broyé ou un ajout de fines.

### 1.4 Limites intrinsèques
- Sympatec RODOS (article) vs Malvern/valeurs typiques (références) : les diffractomètres laser à dispersion sèche divergent de 5–15 % sur d10 et d90 selon la pression de dispersion et le modèle optique ; l'article ne donne pas la pression utilisée pour le lactose.
- Les valeurs typiques DFE sont arrondies (5/50/150) et les lots réels varient à l'intérieur de la spécification (ML001 : d50 37–61 !). Un ajustement à ±10 % ne discrimine donc pas un lot de ML001 d'un mélange LH200 + fines.
- Les auteurs ont peut-être utilisé des **grades personnalisés** (« Customized Lactohale », offre explicite de DFE) qui n'existent pas dans la bibliothèque.

## 2. Résultats ligne par ligne

| # | d10 / d50 / d90 | Meilleur grade seul (RMS) | Dans spec ML001 ? | Meilleur(s) mélange(s) (RMS) | Lecture |
|---|---|---|---|---|---|
| 1 | 4,80 / 44,24 / 144,96 | **ML001 (0,077)** | oui | ML001 95 % + fines (0,03) | **ML001 seul** — le plus proche de la valeur mesurée par Karabulut (5,6/49/143) ; l'ajout de 5 % de fines n'améliore que marginalement |
| 4 | 10,52 / 74,45 / 145,61 | **LH200 (0,051)** | non | LH200 85 % + LH206 15 % (0,024) | **LH200 seul** — coïncide avec Karabulut (13,4/69/149) ; le mélange n'apporte rien de décisif |
| 10 | 6,80 / 48,95 / 138,38 | ML001 (0,184) / LH200 (0,304) | oui | LH200 85 % + LH210 15 % (0,023) ; LH200 80 % + LH201 20 % (0,035) | Ambigu : **lot de ML001 côté haut de spec** (d10 5–7 autorisé) **ou LH200 + ~15 % de fines grossières** |
| 6 | 5,67 / 41,58 / 127,00 | ML001 (0,161) | oui | LH200 80 % + LH220 20 % (0,048) ; ML006 20 % + LH200 80 % (0,050) | Idem : **ML001 (lot bas de spec en d50)** ou **LH200 + ~20 % de fines** |
| 3 | 3,35 / 37,49 / 142,00 | ML001 (0,287) | oui (limite basse d10 3, d50 37) | **ML001 90 % + LH230 10 % (0,028)** ; ML001 95 % + LH300 (0,083) | d10 3,35 trop bas pour un ML001 typique : **ML001 + ~10 % de fines micronisées** (LH230 ou LH300) le plus probable |
| 8 | 4,18 / 30,26 / 121,27 | ML001 (0,331) | non (d50 < 37) | ML006 40 % + LH200 60 % (0,034) ; LH206 45 % + LH220 55 % (0,036) ; LH200 65 % + LH220 35 % (0,040) | **Mélange porteur broyé + 35–40 % de fines broyées** ; d50 30 avec d90 121 est impossible pour un grade seul |
| 7 | 5,19 / 37,35 / 118,16 | ML001 (0,219) | non (d90 < 124) | LH200 75 % + LH220 25 % (0,076) ; ML006 25 % + LH200 75 % (0,080) | **LH200 + ~25 % de fines** ; alternative : ML001 hors spec en d90 (peu probable pour un lot libéré) |
| 9 | 12,95 / 79,01 / 159,97 | LH200 (0,182) | non | **SV010 40 % + LH200 60 % (0,030)** ; LH200 50 % + LH206 50 % (0,053) | **Porteur grossier ajouté à LH200** — « two grades of lactose » au sens grossier + fin ; LH200 seul est trop fin en d90 |
| 2 | 4,23 / 34,98 / 99,65 | ML001 (0,328) | non (d90 < 124) | SV003 50 % + LH220 50 % (0,096) — seul candidat ≤ 0,10 | **Aucune combinaison de la bibliothèque n'explique bien** cette ligne ; d90 ≈ 100 avec d10 ≈ 4 évoque un tamisé fin (SV003) fortement chargé en fines, ou un **grade personnalisé** |
| 5 | 3,66 / 19,76 / 84,32 | LH201 (0,306) / ML006 (0,398) | non | SV003 30 % + LH220 70 % (0,091) — seul candidat ≤ 0,10 | **Grade fin non catalogué ou mélange riche en fines** ; ni LH201 (d90 55) ni ML006 (d90 46) n'ont un d90 de 84 |

### Synthèse
- **Identifications fermes (2)** : ligne 1 = Respitose ML001 ; ligne 4 = Lactohale 200. Les deux sont confirmées par les mesures indépendantes de Karabulut 2022 à < 10 %.
- **Identifications probables avec ambiguïté ML001 / LH200+fines (2)** : lignes 6 et 10 — dans la spécification de ML001, mais tout aussi bien expliquées par LH200 + 15–20 % de fines. **Non séparables sur trois percentiles.**
- **Mélanges (4)** : ligne 3 (ML001 + ~10 % fines micronisées), lignes 7–8 (LH200 + 25–40 % fines broyées type LH220/ML006), ligne 9 (LH200 + ~40 % SV010).
- **Non identifiables avec la bibliothèque (2)** : lignes 2 et 5 — probablement des grades personnalisés ou des mélanges ternaires.

Conclusion générale : l'article a très vraisemblablement utilisé **deux porteurs de base broyés — Respitose ML001 et Lactohale 200 —** enrichis en fines (LH220/LH230/LH300 ou ML006) ou en porteur grossier (SV010) pour balayer le d10 (3,3–13 µm) et le d50 (20–79 µm). C'est cohérent avec la conclusion SHAP de l'article (d10 du lactose = variable dominante pour IND) : le plan a été construit pour faire varier les fines. La bibliothèque explique 8 lignes sur 10 à ≤ 10 %.

## 3. Comment trancher les ambiguïtés (au laboratoire ou par la donnée)

| Levier | Ce qu'il apporte | Coût |
|---|---|---|
| Demander aux auteurs (corresp. : A. Rzewińska, E. Juszczyk) le tableau des grades ou les données brutes | Réponse directe ; l'article n'a pas de supplément | Un courriel |
| Mesurer SV003, ML001, LH200, LH201, LH206, LH220, LH230, LH300, SV010 sur **Sympatec RODOS/HELOS à 2 et 3 bar**, même appareil que l'article | Bibliothèque dans la même métrologie ; supprime le biais Malvern/Sympatec | 9 échantillons gratuits (DFE fournit des échantillons), 1 journée |
| Exploiter la courbe complète, pas 3 percentiles : **x16, x84, x99 et surtout la fraction < 4,5 et < 15 µm** | Un mélange binaire a une cumulée bimodale reconnaissable ; un grade seul ne l'a pas | Inclus dans la mesure ci-dessus |
| SEM : tomahawk lisse (tamisé) vs fragments irréguliers (broyé) vs mélange des deux morphologies | Distingue ML001 seul (une morphologie) de LH200 + fines (deux populations) et détecte SV010 (tomahawk grossier) dans la ligne 9 | 1 h par échantillon |
| Densité vrac / tassée : SV003 0,69 ; ML001 0,63 ; LH200 0,67 ; LH230 0,31 ; LH300 0,27 (fiches DFE) | Une ligne à 10 % de LH230 a une densité vrac ~0,58 ; ML001 seul ~0,63 | Trivial si la poudre est disponible |
| Fixer un **a priori de plan** : les auteurs ont cherché à varier d10 à d50 constant | Réduit l'espace des mélanges plausibles à porteur constant + fines variables | Raisonnement |

## 4. Ce que cela change pour notre plan
- Le couple **ML001 / SV003** retenu dans `RESULTATS.md` reste pertinent : ML001 est l'un des deux porteurs de base identifiés ; SV003 apporte le contraste tamisé absent de l'article (les auteurs ont surtout varié les fines, pas la morphologie du porteur).
- Les lignes 6–8 montrent que Celon a exploré **jusqu'à 25–40 % de fines broyées** — bien au-delà de nos 8 % de LH300. Ce n'est pas contradictoire : fines broyées (x50 13–17) et fines micronisées (x50 3) n'ont pas le même effet (Kinnunen 2014). Si la phase 0 suggère que le princeps est riche en fines, prévoir un bras exploratoire à 20 % de LH220 plutôt que d'augmenter LH300.
- Pour comparer nos lots aux 67 formulations de l'article, mesurer nos lactoses sur Sympatec RODOS et rapporter d10/d50/d90 **et** la fraction < 10 µm, afin de placer chaque lot dans l'espace exploré par l'article.

## 5. Sources
- Rzewińska A. et al., AAPS PharmSciTech 2025;26:230 — texte et tableau I (lecture directe).
- Karabulut M., Kekec A., Acar C., RDD 2022, « The Effect of Lactose Quality Attributes on Predicted Inhaled Drug Deposition in Tiotropium Bromide DPI Formulations », tableau 1.
- DFE Pharma, pages produit Respitose SV003/SV010/ML001, Lactohale 100/200/201/206/210/300 ; estore Lactohale 230 ; brochure « Inhalation lactose for design » (#15, 02/2022) ; spécification Respitose ML001 PD-0063 (10/04/2020).
