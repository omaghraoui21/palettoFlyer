# Prompt pour l'agent générateur de la présentation

Tu génères une présentation de 16 diapositives (PowerPoint ou HTML/reveal, 16:9) à partir du script `SCRIPT.md` situé dans le même dossier. Ne modifie pas le contenu technique ; ne rajoute aucun chiffre qui n'y figure pas.

## Public et ton
Supérieur hiérarchique technique (directeur R&D / développement galénique). Ton factuel, précis, sans superlatif. Français. Pas de « vision », pas de slogans.

## Règles visuelles
- Une idée par diapositive ; titre = la conclusion de la diapositive (phrase complète), pas un intitulé.
- Texte ≤ 60 mots par diapositive hors tableaux ; le reste passe en notes de présentateur (fournies dans SCRIPT.md sous « Notes »).
- Chaque diapositive contient **un visuel principal** décrit dans SCRIPT.md sous « Visuel » : flowchart (Mermaid ou équivalent), tableau, schéma, timeline, ou capture. Génère les flowcharts à partir des blocs Mermaid fournis.
- Palette sobre : 1 couleur d'accent + gris ; police sans-serif ; chiffres alignés à droite dans les tableaux.
- Distinguer visuellement trois statuts d'information avec une pastille : **Établi** (source publique lue), **Calculé** (reproductible par les scripts du projet), **Hypothèse** (marqué [H]). Ne jamais présenter une hypothèse comme un fait.

## Captures et images
- Pour les captures d'articles : n'utilise que les URL listées dans SCRIPT.md § Sources ; capture la première page ou le tableau cité, avec la légende « Source : auteur, revue, année, DOI ». Si la capture n'est pas possible (accès), remplace par une carte de citation (titre, auteurs, revue, DOI) — pas d'image inventée.
- Pour les équipements : schémas simplifiés (icônes/blocs), pas de photos de marques ; si une photo est utilisée, elle doit être libre de droits et légendée.
- Aucun logo Novartis / Ultibro / Breezhaler ; ces noms apparaissent en texte uniquement.

## Contraintes
- Bandeau discret sur chaque diapositive : « Dossier R&D — aucun lot fabriqué — usage in vitro uniquement ».
- Dernière diapositive = décision demandée + ressources, rien d'autre.
- Livrer aussi les notes de présentateur et une version PDF.
