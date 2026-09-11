# Prompt d'exécution — Sélection des lactoses pour le plan d'expériences (générique Ultibro)

*Rédigé par Fable le 11/09/2026 avant toute recherche, pour éviter d'ajuster la méthode aux résultats. Ce fichier est figé ; les résultats vont dans `RESULTATS.md` et `candidats_lactose.csv`.*

## Rôle
Tu es formulateur DPI senior chargé de choisir les grades de lactose (porteur et fines) qui entreront dans le plan de criblage d'un générique d'indacatérol 110 µg / glycopyrronium 50 µg en gélule HPMC, plateforme lactose + MgSt à fort cisaillement. Tu dois aboutir à une **liste courte justifiée**, pas à une revue.

## Questions auxquelles répondre, dans l'ordre
- **Q1 — Contrainte du princeps.** Que disent les brevets du titulaire (Novartis) et l'EPAR sur le lactose d'Onbrez/Seebri/Ultibro : type (tamisé, broyé, mélange), fenêtres de PSD, teneur en fines, surface, forme (α-monohydrate) ? Un brevet décrit un domaine revendiqué, pas nécessairement le produit commercial : distinguer les deux.
- **Q2 — Ce que font les génériqueurs.** Que revendiquent les brevets/demandes de tiers (Celon, Polpharma, Zentiva, Cipla, Glenmark, Lupin, Chiesi, Teva, Hovione, Nanopharm…) sur les mélanges IND/GLY ou GLY seul : grades nommés, PSD, ratio porteur/fines, MgSt ? Repérer les convergences.
- **Q3 — Mécanismes publiés.** Dans la littérature primaire (revues à comité de lecture), quels attributs du lactose gouvernent la FPF d'un mélange adhésif à faible dose (< 1 % d'actif) avec un actif cohésif (GLY) et un actif moins cohésif (IND) : d10/fines intrinsèques, d50, span, rugosité, énergie de surface, lactose amorphe, teneur en eau ; interaction fines × MgSt ; effet du procédé (tamisé vs broyé) ?
- **Q4 — Offre commerciale.** Quels grades inhalation (DFE Pharma, Meggle, Kerry/Sheffield si applicable) ont des PSD publiées compatibles avec Q1–Q3 ? Extraire d10/d50/d90 typiques et le type (tamisé/broyé/micronisé).
- **Q5 — Décision.** Construire une grille de score explicite et retenir : 2 porteurs contrastés + 1 grade de fines, avec justification traçable.

## Stratégie de recherche (à exécuter, à journaliser)
1. **Google Patents** : requêtes `indacaterol glycopyrronium lactose inhalation powder`, `glycopyrronium lactose fines d10 inhalation`, `indacaterol maleate lactose carrier particle size`, cessionnaires Novartis puis tiers. Lire les revendications et exemples, extraire toute fenêtre chiffrée de PSD/fines.
2. **Littérature** : Exa/PubMed avec `lactose carrier fines fine particle fraction adhesive mixture`, `magnesium stearate lactose fines interaction DPI`, `glycopyrronium lactose carrier`, `indacaterol dry powder lactose`, `sieved vs milled lactose DPI`, `lactose intrinsic fines d10 FPF`. Privilégier 2010–2026, articles avec données quantitatives.
3. **Fiches fournisseurs** : PSD typiques des grades inhalation (documents publics des fabricants).
4. **Ancrage** : Rzewińska 2025 (tableau I) donne les PSD de lactoses réellement utilisés pour cette association — servir de borne empirique.

## Critères d'inclusion / exclusion
- Inclure : brevets avec exemples chiffrés ; articles avec PSD et FPF/FPD mesurées ; fiches fournisseurs avec d10/d50/d90.
- Exclure : revues sans données primaires ; brevets sans exemple pertinent ; toute source dont le contenu n'a pas pu être lu (ne pas citer d'après un résumé de tiers).
- Chaque affirmation chiffrée porte une référence lisible (URL ou DOI) et le passage vérifié.

## Grille de score (fixée a priori)
Pour chaque grade candidat, note 0–2 sur :
- **S1 Compatibilité princeps** : PSD dans les fenêtres des brevets Novartis / mesure du princeps (2 = au cœur, 1 = en bordure, 0 = hors).
- **S2 Fines intrinsèques** : d10 et % < 10 µm documentés et dans la plage où la littérature montre un gain de FPF sans perte d'uniformité.
- **S3 Aptitude au dry-coating MgSt** : surface rugueuse/broyée documentée comme favorable à l'étalement du MgSt au cisaillement.
- **S4 Contraste utile pour le plan** : le grade apporte un axe de variation distinct (d50, fines, process) par rapport à l'autre porteur retenu.
- **S5 Disponibilité et documentation** : grade inhalation commercial, DMF/fiche, historique d'usage dans des produits approuvés.
Pondération : S1 ×2, S2 ×2, S3 ×1, S4 ×1, S5 ×1 (max 14). Aucune modification de la grille après lecture des résultats.

## Livrables
- `RESULTATS.md` : journal de recherche (requêtes, hits retenus/écartés), extraction Q1–Q4, grille de score, décision Q5, mise à jour des facteurs du plan, limites.
- `candidats_lactose.csv` : un grade par ligne, PSD, type, sources, scores.
- Mise à jour de `tools/doe.py` si les niveaux du facteur « fines » ou la définition du porteur changent.

## Garde-fous
- Ne pas inférer la composition commerciale d'Ultibro à partir d'un brevet ; dire « revendiqué » vs « mesuré ».
- Ne pas recommander un fournisseur ; recommander des attributs, illustrés par des grades nommés.
- Signaler tout conflit entre sources plutôt que le lisser.
