# Candidat recommandé — exécution du prompt de sélection (11/09/2026)

Exécution de `PROMPT.md`. Notes et poids fixés avant agrégation ; agrégation et sensibilité par `tools/select_candidate.py` (`outputs/selection_mcda.csv`). **[H]** = jugement d'expert sans preuve directe.

---

## 1. Candidats et élagage

Espace complet : 3 porteurs × 2 niveaux de fines × 2 architectures MgSt × 2 mélangeurs = 24 combinaisons. Sept sont conservées ; les autres sont dominées :

| Éliminé | Pourquoi (preuve) |
|---|---|
| Toute combinaison **Turbula + MgSt externe seul** | À faible cisaillement, le MgSt n'est pas étalé : Thalberg 2023 montre qu'il faut des temps très longs pour atteindre la même FPF ; Bungert 2021 montre que le coating à fort cisaillement abaisse plus l'énergie de surface. Le princeps utilise un PI (EPAR) : sans cisaillement ni PI, on n'a aucune des deux voies de fonctionnalisation du MgSt. |
| **SV003 + 4 % LH300 + MgSt externe** | Cumule un porteur sans fines intrinsèques (S2 = 0 dans `lactose/RESULTATS.md`) et l'absence de PI : GLY, actif le plus cohésif et agglomérant (EPAR Seebri, brevet US10314784), n'a alors aucune protection. |
| **50/50 + fines + externe seul**, **50/50 + fines + PI** | Points intermédiaires du DSD, utiles au plan mais pas comme point de départ : ils ne testent aucune hypothèse tranchée. |
| Tout **PI + Turbula** hors C7 | C7 conservé comme témoin « sans cisaillement » ; les variantes avec fines n'apportent rien de plus. |

Sept candidats retenus : C1–C7 (voir tableau § 3).

---

## 2. Justification des notes (1 = défavorable, 5 = favorable)

### K1 — Similarité attendue pour l'indacatérol (poids 20)
- **Fait clé** : la FPF d'IND est **plus élevée** dans Ultibro que dans Onbrez (EPAR Ultibro p. 13, ajustement de dose 150 → 110 µg). La cible IND est donc celle d'une plateforme *avec* MgSt et fines, pas d'un simple mélange lactose.
- Rzewińska 2025 : « *indacaterol performance is more influenced by the PSD of lactose — particularly the d10* » ; un d10 plus bas augmente la masse IND sur S1–S3.5 (donc déplace la distribution). Le d10 est donc le levier IND → **ML001 (x10 5) = 4 ; 50/50 (x10 ≈ 8–10) = 3 ; SV003 (x10 35) = 2**.
- Fines ajoutées (C5) : gain incertain, effet non monotone (Grasmeijer 2014) → pas de bonus au-delà du porteur broyé **[H]**.
- Turbula (C7) : moins de dispersion des agglomérats d'IND ; l'EPAR signale que le mélange IND/GLY interagit → 3 **[H]**.

### K2 — Similarité attendue pour le glycopyrronium (poids 20)
- **Fait clé** : le princeps transforme GLY en **PI** (EPAR Ultibro/Seebri) ; le brevet Novartis US10314784 documente que la co-micronisation GLY + 3–5 % MgSt réduit l'agglomération et conserve la FPF au stockage (tableau 1 du brevet : −10 % FPF(ED) à 6 semaines 30/65 pour le témoin). GLY est un ammonium quaternaire micronisé connu pour s'agglomérer (Ticehurst 2000, cité par le brevet).
- Rzewińska 2025 : GLY gouverné par sa **propre PSD** (d90) et l'énergie de mélange, peu par le lactose → le levier GLY est le **PI + le cisaillement**, pas le porteur.
- → **PI + fort cisaillement (C2, C3, C4) = 4 ; externe seul (C1, C5) = 3 ; SV003 externe (C6) = 2 ; PI + Turbula (C7) = 3**.

### K3 — Stabilité physique (poids 15)
- Le produit fini est sensible à l'humidité, ce qui affecte la FPM (EPAR Ultibro p. 15) ; le PI protège GLY (brevet) → **PI = 4**.
- Fines intrinsèques d'un porteur broyé : perte de mobilité au vieillissement (Bungert 2022) → C1 = 3 ; fines micronisées ajoutées à 4 % : population la plus réactive à l'humidité (surface, amorphe) → **C5 = 2**, C4 = 3 **[H]**.

### K4 — Homogénéité et fabricabilité (poids 12)
- SV003 : Carr 19, écoulement libre (fiche DFE) → 5 ; ML001 : Carr > 25, cohésif → 4 ; le 50/50 combine écoulement et fines → **5** ; fines ajoutées dégradent l'écoulement (Kinnunen 2014 : fluidisation plus énergétique) → 3.
- Turbula : homogénéité plus lente à atteindre pour des agglomérats de GLY (§ 4.2 du DOSSIER : le CV est gouverné par la désagglomération) → 3.
- Vectura US10729647 rappelle que les fines améliorent la reproductibilité de dosage au Dosator : pas de pénalité au-delà de 3 pour C4/C5.

### K5 — Fidélité à l'architecture du princeps (poids 10)
- EPAR : PI de GLY, puis IND + lactose + **MgSt additionnel** ; un seul lactose cité ; équilibrage. → **PI + externe = 5 (C2, C3), PI sans externe n'existe pas ici ; externe seul = 3 ; fines ajoutées = 2 (aucune source ne les documente) ; C4 = 4 ; C7 = 4**.

### K6 — Simplicité / coût / transposabilité (poids 8)
- Externe seul : une étape de moins, pas de microniseur → 5 ; PI : campagne de co-micronisation ≥ 20 g, qualification → 3 ; fines : une matière et un prémélange de plus → 4 (C5), 2 (C4 : trois lactoses de fait) ; Turbula : matériel banal → 4.

### K7 — Risque PI (observations techniques) (poids 8)
- EP2037879 (co-micronisation GLY/MgSt) : **révoqué** en Europe ; famille US10314784 **active jusqu'en 2028**, revendiquant 3–5 % MgSt et un ratio porteur/PI 200:1–20:1 — notre ratio ≈ 377:1 est hors fourchette (observation). → **PI = 3** (à vérifier par conseil) ; **externe seul = 5**.
- Vectura US10729647 (active) vise > 10 % de fines + MgSt : nos candidats à 0–4 % de LH300 sur ML001 (~5–8 % de fines intrinsèques **[H]**) sont proches de la borne ; C5 pourrait la franchir → pas de pénalité supplémentaire car le brevet est un brevet de *procédé de remplissage*, mais à vérifier.

### K8 — Robustesse à faible débit (poids 7)
- Grasmeijer 2014 : à faible débit, les fines ultrafines **réduisent** le détachement à faible dose ; des fines plus grossières le maintiennent. Les fines intrinsèques de ML001 (x10 5) sont du type « grossier » → 3–4 ; LH300 (x50 3) est du type « fin » → C5 = 4 seulement grâce au MgSt **[H]** ; C4 = 3.
- PI : GLY moins aggloméré se détache mieux à faible énergie → +1 pour C2 (4).
- SV003 lisse sans fines : dépendance au débit la plus forte (Pinto 2021, gélule à faible dose) → C6 = 2.

---

## 3. Agrégation

| Candidat | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | Score /5 | P(1er) sur 10 000 tirages de poids ±50 % |
|---|---|---|---|---|---|---|---|---|---|---|
| **C2 — ML001, 0 % LH300, PI 5 % + MgSt externe, fort cisaillement** | 4 | 4 | 4 | 4 | 5 | 3 | 3 | 4 | **3,94** | **0,99** |
| C3 — 50/50 SV003-ML001, 0 %, PI + externe, fort cisaillement | 3 | 4 | 4 | 5 | 5 | 3 | 3 | 3 | 3,79 | 0,01 |
| C1 — ML001, 0 %, MgSt externe seul, fort cisaillement | 4 | 3 | 3 | 4 | 3 | 5 | 5 | 3 | 3,64 | 0,00 |
| C7 — ML001, 0 %, PI + externe, Turbula | 3 | 3 | 4 | 3 | 4 | 4 | 3 | 3 | 3,33 | 0,00 |
| C5 — ML001, 4 % LH300, externe seul | 4 | 3 | 2 | 3 | 2 | 4 | 5 | 4 | 3,26 | 0,00 |
| C4 — SV003, 4 % LH300, PI + externe | 3 | 4 | 3 | 3 | 4 | 2 | 3 | 3 | 3,22 | 0,00 |
| C6 — SV003, 0 %, externe seul | 2 | 2 | 3 | 5 | 3 | 5 | 5 | 2 | 3,09 | 0,00 |

C2 est premier dans 99 % des tirages : la recommandation est **robuste au choix des poids**. Le seul critère où C2 n'est pas au moins à égalité avec C1 est K6/K7 (coût et PI) ; il faudrait donner à ces deux critères plus de 45 % du poids total pour renverser l'ordre.

---

## 4. Le candidat : FB-2 (= C2)

### 4.1 Composition (calcul `tools/formulation.py`, titres 100 %, à corriger par CoA)

| Composant | µg / gélule | g / lot 300 g |
|---|---|---|
| Maléate d'indacatérol micronisé (110 µg base) | 142,530 | 1,71036 |
| **PI** = bromure de glycopyrronium (50 µg base) co-micronisé avec 5 % m/m de MgSt | 65,674 (dont GLY-Br 62,546 + MgSt 3,127) | 0,78808 |
| MgSt externe (prétraitement du porteur) | 31,873 | 0,38247 |
| Respitose ML001 (porteur, q.s.) | 24 759,92 | 297,11909 |
| **Total** (MgSt total 35 µg = 0,14 %) | **25 000** | **300,000** |

Si la pesée du princeps (J1) donne 23,75 mg au lieu de 25,0 mg, le porteur seul est ajusté (FB-2b).

### 4.2 Spécifications d'entrée
| Matière | Fenêtre | Contrôles décisifs |
|---|---|---|
| GLY-Br micronisé (avant PI) | d50 1,5–2,5 ; d90 3,6–5,0 µm ; forme A | PSD à 2/3/4 bar (agglomération), XRPD, eau, SSA |
| PI (GLY + 5 % MgSt) | d50 1,5–3,0 ; d90 ≤ 6 µm ; titre GLY-Br 94–96 % ; Mg par ICP conforme à 5 ± 0,5 % | Homogénéité du MgSt (Raman/EDX), eau, impuretés, rendement |
| IND maléate micronisé | d50 1,4–2,4 ; d90 2,7–5,0 µm ; forme A | PSD, chiralité, amorphe (DSC/DVS) |
| Respitose ML001 | spec DFE (d10 3–7 / d50 37–61 / d90 124–194) **et** % < 4,5 µm et % < 15 µm documentés, SSA, SEM | Un lot pour tout le programme initial |
| MgSt LIGAMED MF-2-V-BI (ou équivalent inhalation, végétal) | d50 5–10 µm | SSA, stéarate/palmitate, hydratation |
| Gélule HPMC taille 3 inhalation | eau 4–6 % **[H]** | Perforation sur le dispositif cible |

### 4.3 Procédé (grandeurs transposables ; point central du DSD)
1. **PI** : prémélange GLY-Br + 5 % MgSt au Turbula 2 h **[H]** (brevet : 5 h), puis broyeur à jets d'air, gaz sec, alimentation régulière ; campagne ≥ 20 g de GLY + 1 g MgSt ; conditionnement 24 h en sachet antistatique (Rzewińska 2025 pour la pratique). Contrôles § 4.2.
2. **Prétraitement du porteur** : ML001 297,1 g + MgSt externe 0,382 g, chargés en 2 couches (MgSt entre) dans une cuve 1 L, remplissage 30–40 % ; **vitesse périphérique 11 m/s (2500 tr/min sur turbine 85 mm), 2 min**, hacheur arrêté, 20–25 °C / 30–45 % HR ; enregistrer couple/température.
3. **Ajout des actifs** : arrêt ; PI (0,788 g) et IND (1,710 g) déposés en sandwich entre deux portions de porteur prétraité ; réconciliation des pertes de transfert (> 99 %).
4. **Mélange final** : **vitesse périphérique 6,7 m/s (1500 tr/min sur 85 mm), 3 min** ; température du lit < 30 °C.
5. **Repos** 30 min en récipient antistatique fermé ; tamisage doux 250 µm **uniquement si** des agglomérats > 250 µm sont observés et sans rejet non dosé.
6. **Remplissage** 25,00 mg nets, doseur à faible compaction, 100 % pesée ; 200 gélules minimum par lot pour la caractérisation.
7. **Équilibrage** : trois bras — scellage immédiat, 24 h et 72 h à 22 °C / 40 % HR — puis blister PA/Alu/PVC-Alu.

Transposition 1 L → 5 L : conserver la vitesse périphérique du prétraitement (≈ 1 420 tr/min pour une turbine de 150 mm) et le produit révolutions × taux de remplissage du mélange final (`outputs/transposition_melangeur.csv`).

### 4.4 Contrôles en cours et critères d'acceptation du lot
| Contrôle | Critère (interne, exploratoire) |
|---|---|
| Homogénéité du mélange (10 × 25 mg, LC deux actifs) | Moyenne 95–105 %, RSD ≤ 3 %, aucun individuel hors 90–110 % |
| Masse nette des gélules (n = 30) | 25,0 mg ± 3 %, RSD ≤ 3 % |
| Teneur gélules début/milieu/fin | Écart ≤ 3 % entre positions |
| DD (DUSA, n = 10) à 60 L/min | Rapport T/R des moyennes 0,90–1,10 pour **chaque** actif ; RSD ≤ 8 % |
| APSD (NGI, n = 3) à 30 et 90 L/min | FPD < 5 µm T/R 0,90–1,10 pour chaque actif ; profil sans écart systématique ; bilan massique 85–115 % |
| Rétention gélule + dispositif | ≤ 20 % de la dose nominale, chaque actif |
| Stabilité 4 semaines 40/75 ouvert (alerte) | Dérive FPD ≤ 10 % et ≤ dérive de la référence |

### 4.5 Challenger : FB-2-C (= C3)
Même composition et procédé, porteur **50/50 ML001–SV003**. Il teste la seule hypothèse ouverte à fort enjeu : *la performance IND dépend-elle du d10 du porteur autant que Rzewińska 2025 le suggère ?* Si FB-2-C égale FB-2 sur IND, on gagne l'écoulement du tamisé (Carr 19) sans perdre la similarité ; si FB-2 est meilleur, le d10 est confirmé comme levier et le facteur F du DSD se resserre vers 50–100 %.

### 4.6 Plan de confirmation (phase 0, révisée)
- 2 lots FB-2 + 2 lots FB-2-C (4 × 300 g), même lot de PI, même lot de matières.
- Mesures § 4.4 sur chaque lot ; référence : 3 lots d'Ultibro aux mêmes débits, mêmes jours.
- Décision : **retenir la formule dont le pire écart |ln(T/R)| parmi {DD, FPD} × {IND, GLY} × {30, 90 L/min} est le plus faible**, à condition d'homogénéité conforme. Puis DSD centré sur la formule retenue (facteur F recentré si FB-2-C gagne).

---

## 5. Ce qui ferait changer d'avis
| Observation en phase 0 | Conséquence |
|---|---|
| La rétro-caractérisation du princeps montre un lactose **tamisé** (tomahawk lisse, SSA basse, < 2 % < 10 µm) | Le candidat devient C3 puis C4 ; le facteur F du DSD explore 0–50 % |
| Le princeps contient > 8 % de particules < 10 µm | Ajouter un bras à 20 % de LH220 (fines broyées, cf. lignes 6–8 de Rzewińska) plutôt qu'augmenter LH300 |
| Le PI ne peut pas être qualifié (rendement, MgSt hétérogène) ou l'avis PI est négatif sur US10314784 | Basculer sur C1 (externe seul) et compenser par l'énergie du prétraitement (facteur C) ; accepter un risque de stabilité GLY plus élevé et allonger la stabilité précoce |
| FB-2 excellent sur GLY mais IND trop fin (FPD IND T/R > 1,10) | Cohérent avec l'EPAR (FPF IND ↑ en présence de MgSt) : réduire l'énergie du mélange final ou le d10 (aller vers C3), **pas** la dose |
| Homogénéité RSD > 3 % sur ML001 | Passer au 50/50 (C3) ; vérifier l'état d'agglomération du PI |

---

## 6. Ce que cette recommandation n'est pas
- Ce n'est pas une preuve d'équivalence : c'est le point de départ qui maximise la probabilité a priori sous les preuves lues, avec une sensibilité aux poids vérifiée.
- Les notes K1–K3 s'appuient sur des mécanismes démontrés sur d'autres actifs (budesonide, salbutamol, tiotropium) et sur une seule étude IND/GLY ; elles sont marquées comme telles.
- La question de propriété intellectuelle n'est traitée que par des observations techniques ; un avis de liberté d'exploitation est requis avant la phase 1.
