# Protocole expérimental complet — Candidat FB-2 et challenger FB-2-C

**Générique d'indacatérol 110 µg / glycopyrronium 50 µg, poudre pour inhalation en gélule HPMC taille 3.**
Version 1.0 — 11/09/2026 — exécution du prompt `protocole/PROMPT.md`.

> **Aucune gélule issue de ce protocole ne doit être administrée à une personne ou à un animal.** Usage R&D in vitro exclusivement. Les valeurs marquées **[H]** sont des choix de jugement ; celles marquées **[Q]** doivent être remplacées par les valeurs de qualification locale (balance, mélangeur, débitmètres, hygrométrie).

---

## 0. Organisation, sécurité, traçabilité

### 0.1 Sécurité (avant toute manipulation)
- Indacatérol maleate et glycopyrronium bromide : actifs très puissants (doses cliniques en µg). Bande d'exposition professionnelle à fixer par l'hygiéniste ; par défaut **OEB 4 [H]** : pesées et transferts en isolateur ou sous hotte à flux laminaire à pression négative avec sas ; EPI : combinaison, double gants nitrile, masque FFP3 ou APR à adduction d'air pour les opérations ouvertes ; aspiration à la source sur le mélangeur et le microniseur.
- Poussière de lactose : risque ATEX faible mais réel dans le microniseur (broyeur à jets d'air sous azote sec).
- Nettoyage : validation d'un test de rinçage (LC, LOQ ≤ 0,1 µg/cm² **[H]**) entre lots pour les surfaces en contact ; écouvillonnage de 5 points par équipement.
- Déchets : poudres actives et solvants LC en filière déchets cytotoxiques/chimiques selon la réglementation locale.

### 0.2 Traçabilité
- Numérotation : `FB2-L01`, `FB2-L02`, `FB2C-L01`, `FB2C-L02` (lots de mélange) ; `PI-01` (intermédiaire) ; `REF-A/B/C` (lots Ultibro).
- Chaque lot : fiche de pesée (`tools/batch_record.py`), feuille de fabrication (paramètres, heures, T/HR, couple), feuille de remplissage, journal analytique, fiche de prélèvement d'échantillothèque (≥ 30 gélules par bras de conditionnement).
- Balances : analytique 0,01 mg (actifs, PI, MgSt) et de précision 1 mg (lactose) ; poids minimal qualifié et incertitude U **[Q]** consignés sur la fiche.

### 0.3 Matériel minimal
Mélangeur à fort cisaillement, cuve 1 L, turbine de diamètre mesuré (référence de calcul : **85 mm [H]**), vitesse réglable 300–3000 tr/min, hacheur débrayable, sonde de température produit, enregistrement couple/puissance ; broyeur à jets d'air en spirale (chambre 50–100 mm) sous azote sec, alimentation vibrante ; Turbula 2 L ; tamis 250 µm inox ; voleur d'échantillons 25 mg ; doseur de gélules à faible compaction ou doseur manuel qualifié ; DUSA + débitmètre + minuterie ; NGI avec préséparateur, gorge USP, revêtement (Brij 35 / glycérol 1 % **[H]**) ; LC-UV (gradient) ; Karl Fischer ; diffraction laser dispersion sèche (Sympatec RODOS ou Malvern Aero) ; balance 0,01 mg ; enceinte climatique 40 °C / 75 % HR ; blistereuse de laboratoire PA/Alu/PVC-Alu ou sachets Alu thermoscellés avec dessiccant témoin.

---

## 1. Réception et libération des matières (semaine 1)

### EXP-01 — Réception et libération
**Objectif** : disposer de matières caractérisées et d'un seul lot par matière pour tout le programme.

| Matière | Quantité à commander | Contrôles à la réception (au-delà du CoA) | Critère de libération interne |
|---|---|---|---|
| Glycopyrronium bromide micronisé (2 fournisseurs si possible) | 30 g | PSD à 2, 3, 4 bar (3 × 30 mg), XRPD (forme A), KF, SSA (BET), SEM | d50 1,5–2,5 µm, d90 3,6–5,0 µm à 3 bar ; **ratio d90(2 bar)/d90(4 bar) ≤ 1,3** (agglomération acceptable) **[H]** |
| Indacatérol maleate micronisé | 10 g | PSD à 2, 3, 4 bar, XRPD, DSC, KF, pureté chirale (CoA) | d50 1,4–2,4 ; d90 2,7–5,0 µm ; pas de signal amorphe > 2 % (DVS) **[H]** |
| Respitose ML001 | 2 kg | PSD Sympatec 2 bar (6 × 1 g), % < 4,5 et < 15 µm, SSA, KF, SEM, densités vrac/tassée | Dans la spec DFE (d10 3–7 / d50 37–61 / d90 124–194) ; **enregistrer** % < 4,5 µm et % < 15 µm (attendu ~2–4 % et ~10–14 % **[H]**) |
| Respitose SV003 | 1 kg | Idem | d10 ≥ 28, d50 50–70, d90 85–110 ; % < 15 µm ≤ 3 % **[H]** |
| MgSt LIGAMED MF-2-V-BI (végétal) | 100 g | PSD 1 bar, SSA, KF, stéarate/palmitate (CoA) | d50 5–10 µm ; SSA ≥ 5 m²/g **[H]** |
| Gélules HPMC taille 3 inhalation, transparentes | 5 000 | Masse (n = 50), KF (n = 3), perforation sur dispositif cible (n = 20) | Masse RSD ≤ 3 % ; eau 4–6 % ; 20/20 perforations sans fragment > 0,5 mm |
| Ultibro Breezhaler | 3 lots × 90 gélules (10 boîtes de 30) | Numéro de lot, péremption ≥ 12 mois, aspect blister | Traçabilité complète ; stockage 25 °C / 40 % HR |
| Dispositif candidat basse résistance (RS01 ou équivalent) | 60 unités | Résistance R = √ΔP/Q (n = 10) | R dans ±15 % de celle du Breezhaler mesurée (n = 10) |

**Enregistrements** : CoA, résultats internes, décision de libération signée. **Échec** : matière hors fenêtre → autre lot ou autre fournisseur ; **ne pas** compenser une PSD hors fenêtre par le procédé.

---

## 2. Qualification des méthodes (semaines 1–4, en parallèle de EXP-01)

### EXP-02 — Méthode LC pour IND et GLY
**Point de départ** (Rzewińska 2025, à valider) : colonne C18 150 × 4,6 mm 3 µm (Gemini NX ou équivalent) ; A = KH₂PO₄ 20 mM pH 3,5 (H₃PO₄) ; B = ACN/MeOH 9:1 ; gradient 25 % B → 33 % à 16 min → 70 % à 17–19 min → 25 % à 20–25 min ; 1,0 mL/min ; 210 nm (IND aussi à 258 nm en confirmation **[H]**) ; injection 50–100 µL ; extraction eau/MeOH/ACN 3:1:1.
**Étapes** : (1) spécificité vs lactose, MgSt, HPMC, revêtement NGI ; (2) linéarité 5 niveaux de 0,02 à 6 µg/mL (GLY) et 0,05 à 15 µg/mL (IND) ; (3) LOQ par S/N = 10 et fidélité ≤ 10 % ; (4) récupération sur chaque surface du NGI et du DUSA (dépôt de 1 µg puis rinçage) ≥ 95 % ; (5) stabilité des extraits 48 h à 5 °C ; (6) fidélité intermédiaire 2 jours × 2 analystes.
**Critère de passage** : LOQ ≤ 0,02 µg/mL pour GLY (≈ 2 % de la dose sur un étage rincé dans 10 mL), ≤ 0,05 µg/mL pour IND ; récupération 95–105 % ; RSD ≤ 2 % à 100 %.
**Échec** : LOQ GLY insuffisante → volume de rinçage 5 mL, injection 100 µL, ou détecteur MS.

### EXP-03 — Dose délivrée (DUSA)
Ph. Eur. 2.9.18 (préparations pour inhalation, poudres) pour le montage ; débits **30, 60, 90 L/min**, volume 4 L → durées **8,0 / 4,0 / 2,67 s** ; filtre + rinçage 20 mL ; dispositif rincé séparément ; gélule vide rincée séparément (rétention). Vérification : débitmètre calibré ±2 % **[Q]** ; fuite < 0,5 L/min à 4 kPa ; 6 déterminations sur REF-A pour estimer le RSD.
**Critère** : RSD DD ≤ 8 % sur la référence ; bilan (DD + rétention gélule + rétention dispositif) = 85–115 % du nominal.

### EXP-04 — APSD (NGI)
Gorge USP, préséparateur (15 mL de solvant), plaques revêtues ; débits 30, 60, 90 L/min, 4 L ; cut-off recalculés au débit réel (Ph. Eur. 2.9.18, formule d = d₆₀ (60/Q)^½ pour chaque étage) ; FPD < 5 µm par interpolation log-probit de la cumulée ; 1 gélule par essai à 60/90 L/min, **2 gélules** à 30 L/min si LOQ insuffisante **[H]** (à préspécifier et à appliquer identiquement à T et R).
**Critère** : bilan massique 85–115 % ; 3 déterminations sur REF-A avec RSD FPD ≤ 10 %.

### EXP-05 — PSD laser, KF, résistance du dispositif
- PSD lactose : Sympatec RODOS/HELOS, R5, 2 bar, 6 répétitions ; PSD actifs : 3 bar (et 2/4 bar pour l'agglomération) **[Q]**.
- KF : 0,5 g de poudre, méthode volumétrique ; gélules : 5 gélules broyées.
- Résistance : R = √ΔP/Q sur 10 dispositifs, ΔP à 30/60/90 L/min ; comparer Breezhaler et candidat.

---

## 3. Caractérisation de la référence (semaines 3–6)

### EXP-06 — Pesée du contenu et rétro-caractérisation
1. 30 gélules par lot REF (A, B, C) : pesée pleine, vidange par tapotement + brosse, pesée vide → masse nette ; **tranche le scénario 25,0 vs 23,75 mg** (§ 2.1 du DOSSIER). Critère : moyenne à ±0,3 mg de l'un des deux scénarios.
2. Réunir 20 contenus (~0,5 g) : KF ; dosage IND/GLY (teneur) ; **Mg par ICP-OES** après minéralisation → % MgSt (÷ 0,041 fraction de Mg dans MgSt).
3. 3 × 0,5 g : dissolution sélective des actifs dans 20 mL de MeOH/ACN 1:1 **[H]** (vérifier < 0,5 % de dissolution du lactose par pesée d'un témoin lactose seul), filtration, séchage doux sous azote, PSD Sympatec 2 bar du lactose récupéré ; SEM (morphologie tamisée vs broyée, présence de fines).
4. Raman/SEM-EDX sur 3 contenus : localisation du Mg.
**Enregistrements** : masse nette (n = 90), % MgSt, d10/d50/d90 et % < 10 µm du lactose du princeps, morphologie.
**Décision** : alimente le § 5 de `selection/CANDIDAT.md` (changement de porteur si tamisé ; 25,0 vs 23,75 mg).

### EXP-07 — Performance de la référence
Pour chaque lot REF-A/B/C, avec le Breezhaler fourni **et** avec le dispositif candidat :
- DD : 10 gélules × 3 débits (30 gélules).
- NGI : 3 × 3 débits (9 gélules).
- Rétention gélule et dispositif à chaque essai.
Total ≈ 39 gélules/lot/dispositif ; avec les 30 pesées et 20 de réserve : **≈ 90 gélules par lot** (3 boîtes de 30). Si un seul dispositif est testé par manque de gélules, privilégier le **dispositif candidat** (c'est lui qui sera dans l'étude pivot) et faire le Breezhaler à 60 L/min seulement.
**Sorties** : moyennes et CV intra-lot et inter-lot de DD et FPD par actif et débit → entrées de `tools/equivalence_power.py` ; pente FPD vs √ΔP.
**Critère de fin de phase** : CV inter-lot connu à ±2 points ; profils complets à 3 débits.

---

## 4. Fabrication de l'intermédiaire PI-01 (semaine 5)

### EXP-08 — Co-micronisation GLY-Br + 5 % MgSt
**Objectif** : 20 g de PI à titre GLY-Br ≈ 95 %, d50 1,5–3,0 µm, d90 ≤ 6 µm, MgSt réparti.
**Matières** : GLY-Br micronisé (ou cristallin si l'on veut reproduire le brevet ; ici **micronisé [H]** pour découpler l'effet du coating de celui de la taille) 20,000 g ± 0,020 g ; MgSt 1,000 g ± 0,002 g (= 5,00 % de la masse de GLY-Br ; le brevet exprime 3–5 % « du total GLY + MgSt » : 1,000/21,000 = 4,76 % — choisir et **documenter** la convention ; ici 5 % de GLY-Br).
**Étapes** :
1. Prémélange au Turbula, flacon 250 mL, 46 tr/min, **2 h [H]** (brevet : 5 h) ; contrôle visuel de l'absence de grumeaux.
2. Broyeur à jets d'air sous azote sec (point de rosée < −40 °C) : pression de broyage **3,5 bar [H]**, pression d'injection 5–6 bar, alimentation 3–5 g/min ; enregistrer pression, débit, température, durée. Passer **une aliquote de 2 g de lactose LH300 avant** pour saturer les surfaces puis rejeter (perte évitée sur le GLY).
3. Récupération au cyclone + filtre ; conditionnement 24 h en sachet PE antistatique à 22 °C / 40 % HR (Rzewińska 2025, pratique) ; pesée du rendement.
**Contrôles** : rendement (≥ 85 % **[H]**) ; PSD 2/3/4 bar ; titre GLY-Br (LC) ; **Mg par ICP** → % MgSt ; homogénéité du MgSt : 5 prélèvements de 100 mg, RSD Mg ≤ 10 % **[H]** ; KF ; XRPD (forme A conservée) ; SEM/EDX qualitatif ; impuretés (LC).
**Critère de passage** : d50 1,5–3,0 µm, d90 ≤ 6,0 µm ; GLY-Br 93–97 % ; MgSt 4,5–5,5 % du PI ; RSD Mg ≤ 10 % ; forme A ; impuretés ≤ CoA + 0,1 %.
**Échec** : rendement bas ou MgSt hétérogène → allonger le prémélange à 5 h et réduire l'alimentation ; PSD trop fine (d50 < 1,5) → baisser la pression à 2,5 bar. **Ne jamais** microniser l'aliquote de 0,79 g seule.

---

## 5. Fabrication des lots de mélange (semaines 6–8 : 4 lots, 1 par jour, ordre L01 FB2 → L01 FB2C → L02 FB2C → L02 FB2, pour équilibrer la dérive de jour)

### EXP-09 — Fiche de pesée (exemple avec IND 98,6 %, PI 94,9 % GLY-Br et 4,9 % MgSt ; **régénérer avec les CoA réels** : `python3 tools/batch_record.py`)

| Composant | FB-2 (g) | FB-2-C (g) | Tolérance |
|---|---|---|---|
| Maléate d'indacatérol | 1,73464 | 1,73464 | ± 0,5 % (± 8,7 mg) |
| PI-01 | 0,79089 | 0,79089 | ± 0,5 % (± 4,0 mg) |
| MgSt externe | 0,38125 | 0,38125 | ± 1 % (± 3,8 mg) |
| Respitose ML001 | 297,09322 | 148,54661 | ± 1 % |
| Respitose SV003 | — | 148,54661 | ± 1 % |
| **Total** | **300,000** | **300,000** | |

Contrôles de la fiche : 110,000 µg IND base et 50,000 µg GLY base par gélule ; MgSt total 0,1400 % ; 12 000 unités théoriques. Pesées des actifs et du PI dans des nacelles antistatiques tarées, **par différence**, avec pesée de la nacelle vide après transfert (perte de transfert consignée ; ≤ 0,5 %).

### EXP-10 — Prétraitement du porteur
**Conditions d'ambiance** : 20–25 °C, 30–45 % HR, enregistrées en continu ; matières équilibrées 12 h en emballage fermé dans la salle.
1. Désagglomération du lactose : passage doux au tamis 250 µm ; consigner le refus (attendu < 0,1 % **[H]**) ; **ne pas forcer**.
2. Charger la cuve 1 L : moitié du porteur, puis MgSt externe (0,381 g) réparti en surface, puis seconde moitié. Taux de remplissage visé 30–40 % du volume utile (300 g à densité vrac 0,63 ≈ 0,48 L → 48 % d'une cuve 1 L nominale ; **vérifier le volume utile réel [Q]** ; si > 50 %, passer à une cuve 2 L en conservant la vitesse périphérique).
3. Mélanger **2,0 min à vitesse périphérique 11,1 m/s** — soit **2 500 tr/min pour une turbine de 85 mm** ; formule : N (tr/min) = v × 60 / (π × D). Hacheur **arrêté**. Enregistrer couple/puissance chaque 10 s et température produit avant/après (ΔT ≤ 3 °C **[H]**).
4. Prélever 3 × 1 g (haut, milieu, bas) pour PSD 2 bar (contrôle d'attrition : d10 et d50 dans ±10 % du lactose initial) et Mg par ICP (couverture ; attendu 0,127 % MgSt externe ± 15 % **[H]**).

### EXP-11 — Incorporation des actifs et mélange final
1. Arrêter ; retirer ~1/3 du porteur prétraité dans un récipient antistatique.
2. Déposer le PI-01 (0,791 g) et l'IND (1,735 g) en surface du lit restant, chacun sur une zone distincte ; recouvrir avec le tiers prélevé (sandwich). Peser les nacelles vides ; réconcilier (transfert ≥ 99,5 %).
3. Mélanger **3,0 min à vitesse périphérique 6,7 m/s = 1 500 tr/min sur 85 mm**, hacheur arrêté ; enregistrer couple et température (ΔT ≤ 3 °C).
4. Décharger dans un récipient antistatique fermé ; **repos 30 min**.
5. Tamisage 250 µm **uniquement si** des agglomérats visibles > 250 µm sont présents ; le refus est pesé, dosé et **réintroduit** après désagglomération douce (jamais rejeté sans dosage).
**Enregistrements** : heures, tr/min réels, couple, T, HR, pertes de transfert, refus de tamis.

### EXP-12 — Homogénéité du mélange
Voleur d'échantillons 25 mg (ou spatule à cavité calibrée) : **10 positions** (schéma fixe : 3 hauteurs × 3 positions + centre) → 10 × 25 mg dans 10 mL d'extractant → LC.
**Critère** : moyenne 95–105 % de la cible pour chaque actif ; RSD ≤ 3 % ; aucun individuel hors 90–110 %.
**Échec** : RSD 3–5 % → 2 min supplémentaires à 6,7 m/s et re-test (une seule fois) ; RSD > 5 % ou biais → investiguer PI (agglomération) et voleur (biais par comparaison avec 5 gélules remplies) avant tout nouveau lot.

---

## 6. Remplissage, équilibrage, conditionnement (jour de fabrication + 3 jours)

### EXP-13 — Remplissage
- Doseur à faible compaction (tambour/vide) ou remplissage manuel qualifié ; **25,00 mg nets**, contrôle de masse 100 % (balance 0,01 mg) ; cible **≥ 300 gélules par lot** (caractérisation ≈ 150, stabilité ≈ 90, réserve 60).
- Consigner la masse nette de chaque gélule ; **critère** : moyenne 24,25–25,75 mg, RSD ≤ 3 % ; rejeter les gélules hors ±7,5 %.
- Prélever 5 gélules début / 5 milieu / 5 fin pour teneur (LC) : écart entre positions ≤ 3 %.
- Temps ouvert total du lot ≤ 4 h **[H]** ; HR 30–45 %.

### EXP-14 — Équilibrage (facteur exploratoire, identique pour les 4 lots)
Trois bras par lot, ~100 gélules chacun :
- **E0** : scellage dans les 30 min ;
- **E24** : 24 h en couche mince, plateau ouvert, 22 °C / 40 % HR **[H]** ;
- **E72** : 72 h idem.
Puis blister PA/Alu/PVC-Alu (ou sachet Alu thermoscellé, sans dessiccant, avec témoin d'humidité). KF sur 5 gélules par bras à la fin de l'équilibrage.
**Sortie** : effet de l'équilibrage sur KF, DD et FPD (§ 7) ; choix du délai pour la suite. L'EPAR mentionne un équilibrage sans en donner les conditions ; celles-ci sont **nôtres**.

---

## 7. Caractérisation in vitro (semaines 7–9)

### EXP-15 — Plan de mesure par lot (bras E24 comme bras principal **[H]** ; E0 et E72 à 60 L/min seulement)
| Mesure | Débits | n | Gélules |
|---|---|---|---|
| DD (DUSA), chaque actif | 30 / 60 / 90 L/min | 10 par débit | 30 |
| APSD (NGI), chaque actif | 30 / 60 / 90 L/min | 3 par débit | 9 (18 si 2 gélules à 30 L/min) |
| DD + NGI bras E0 et E72 | 60 L/min | 6 DD + 3 NGI | 18 |
| Rétention gélule/dispositif | à chaque essai | — | — |
| KF poudre (gélules ouvertes) | — | 3 × 5 gélules | 15 |
| Teneur gélules (LC) | — | 15 (déjà EXP-13) | — |
| **Total par lot** | | | **≈ 80–90** |

Ordre des essais **randomisé par bloc jour**, en alternant T et R chaque demi-journée ; même analyste et même NGI pour T et R d'un même bloc ; un lot REF re-testé à 60 L/min chaque semaine (dérive analytique, ±5 % toléré).

### EXP-16 — Stabilité précoce (alerte)
Bras E24 blistérisé : **1, 2 et 4 semaines à 40 °C / 75 % HR** et 4 semaines à 25 °C / 60 % HR ; à chaque temps : KF (5), DD 60 L/min (6), NGI 60 L/min (3), impuretés LC (3), aspect gélule. REF-A en parallèle (même enceinte).
**Signal d'alerte** : dérive de FPD ou DD > 10 % vs T0, ou > dérive de la référence + 5 points.

---

## 8. Analyse statistique préspécifiée et décision (semaine 10)

### 8.1 Unité expérimentale et réponses
- Unité expérimentale = **le lot de mélange** (n = 2 par formule). Les gélules et étages sont des répétitions techniques.
- Réponses primaires, par actif et par débit : ln(DD_T/DD_R), ln(FPD_T/FPD_R), où R = moyenne des 3 lots de référence au même débit avec le même dispositif.
- **Réponse composite** (préspécifiée) : W = max |ln(T/R)| sur {DD, FPD} × {IND, GLY} × {30, 90 L/min} — le pire écart.
- Réponses secondaires : MMAD, profil par étage (graphique T vs R), pente FPD vs √ΔP, rétention, RSD DD, KF, dérive à 4 semaines.

### 8.2 Règle de décision
1. **Prérequis** : homogénéité (EXP-12) et remplissage (EXP-13) conformes pour les deux lots de la formule ; sinon la formule n'est pas éligible.
2. **Choix** : la formule dont la moyenne de W sur ses 2 lots est la plus faible **et** dont W ≤ 0,15 (T/R entre 0,86 et 1,16) pour les deux lots est retenue.
3. Si les deux formules satisfont W ≤ 0,15 et que |ΔW| < 0,03 : retenir **FB-2-C** (meilleur écoulement, Carr 19 du SV003) et recentrer le facteur F du DSD sur 25–75 %.
4. Si aucune ne satisfait W ≤ 0,15 : ne pas lancer le DSD ; identifier l'actif et la fraction en échec et appliquer le tableau § 5 de `selection/CANDIDAT.md`.
5. Le bras d'équilibrage (E0/E24/E72) qui minimise |ln(T/R)| à 60 L/min **et** la dérive à 4 semaines devient la condition standard.

### 8.3 Présentation
Tableau des W par lot, graphiques T vs R par étage et débit pour chaque actif, FPD vs √ΔP (absolue et normalisée), profils de stabilité ; toutes les données brutes en annexe (CSV).

---

## 9. Ressources et calendrier

| Poste | Quantité |
|---|---|
| Lots de mélange | 4 × 300 g (1,2 kg de poudre ; ≈ 7 g d'IND et 3,2 g de PI) |
| PI | 1 campagne de 20 g de GLY-Br + 1 g MgSt |
| Gélules HPMC | ≈ 1 400 remplies (300/lot + rebuts) |
| Référence | 3 lots × 90 gélules |
| Essais NGI | ≈ 4 lots × (9 + 6) + référence 3 × 9 (× 2 dispositifs) + stabilité 4 × 3 × 4 ≈ **180 NGI** |
| Essais DD | ≈ 4 × (30 + 12) + 3 × 30 × 2 + stabilité ≈ **450 DD** |
| Analyses LC | ≈ 2 500 injections (NGI 12 fractions × 2 actifs) |
| Durée | 10 semaines, 2 techniciens + 1 analyste |

---

## 10. Annexes
- A. `outputs/fiche_pesee_FB2.csv`, `outputs/fiche_pesee_FB2C.csv` (exemple de titres ; à régénérer).
- B. Conversions tr/min ↔ vitesse périphérique : N = 60 v / (π D). Turbine 85 mm : 6,7 m/s → 1 500 ; 11,1 m/s → 2 500 ; 15 m/s → 3 370 tr/min. Turbine 150 mm : 6,7 → 850 ; 11,1 → 1 415 ; 15 → 1 910 tr/min.
- C. Temps d'inhalation à 4 L : 30 L/min 8,0 s ; 60 L/min 4,0 s ; 90 L/min 2,67 s.
- D. Références : Ph. Eur. 2.9.18 (édition applicable) ; EMA CPMP/EWP/4151/00 Rev. 2 ; EMEA/CHMP/QWP/49313/2005 Rev. 1 ; sources listées dans `DOSSIER.md` § 13 et `lactose/RESULTATS.md` § 8.
