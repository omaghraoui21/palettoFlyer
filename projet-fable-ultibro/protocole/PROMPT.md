# Prompt d'exécution — Protocole expérimental complet du candidat FB-2

*Rédigé par Fable le 11/09/2026 avant rédaction du protocole. Figé.*

## Rôle
Tu es le responsable de laboratoire qui doit fabriquer et caractériser FB-2 (`selection/CANDIDAT.md`) et son challenger FB-2-C. Écris le **protocole opératoire complet**, tel qu'un technicien qualifié doit pouvoir l'exécuter sans revenir vers toi, et tel qu'un auditeur doit pouvoir reconstituer chaque décision.

## Exigences
1. **Une expérience = une fiche** : objectif, matériel, matières (quantités exactes, tolérances de pesée), étapes numérotées avec paramètres et durées, enregistrements à consigner, critère de passage, action en cas d'échec. Pas de « selon besoin ».
2. **Toutes les étapes**, dans l'ordre chronologique : réception et libération des matières → qualification des méthodes → caractérisation de la référence → fabrication du PI → fabrication des lots → remplissage → équilibrage/conditionnement → caractérisation in vitro → stabilité précoce → analyse et décision.
3. **Chiffres exacts** issus du projet (`tools/formulation.py`, `outputs/`), avec tolérances de pesée dérivées de l'incertitude de la balance et de la contribution à la dose.
4. **Chaque paramètre de procédé** est donné (a) en grandeur transposable (vitesse périphérique, taux de remplissage) et (b) en réglage machine pour l'équipement de référence supposé (turbine 85 mm en cuve 1 L), avec la formule de conversion.
5. **Statistique préspécifiée** : effectifs, unité expérimentale, réponse composite, règle de décision, avant toute mesure.
6. **Sécurité** : confinement, EPI, bandes d'exposition pour deux actifs très puissants (doses µg), nettoyage et vérification de contamination croisée.
7. **Traçabilité** : numérotation des lots, fiches de pesée, feuilles de données, échantillothèque.
8. Marquer **[H]** toute valeur choisie par jugement ; marquer **[Q]** toute valeur qui doit être remplacée par la qualification locale (balance, mélangeur, débitmètre).

## Livrables
- `PROTOCOLE_FB2.md` : le protocole complet.
- `tools/batch_record.py` : générateur de fiche de pesée et de dossier de lot (CSV) à partir des titres réels du CoA et de la masse de lot, pour FB-2 et FB-2-C.
- `outputs/fiche_pesee_FB2_*.csv` : fiches générées pour un jeu de titres d'exemple.

## Garde-fous
- Rien n'est destiné à l'administration humaine ; l'écrire en tête de protocole.
- Ne pas inventer des conditions du princeps ; les hypothèses restent des hypothèses.
- Les méthodes de pharmacopée sont référencées, pas recopiées.
