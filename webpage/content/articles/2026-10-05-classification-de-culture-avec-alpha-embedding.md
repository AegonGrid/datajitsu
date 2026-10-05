Title: Classification de cultures à partir d'embeddings satellites
Date: 2026-10-05
Slug: classification-culture-a-partir-d-embeddings-satellite
Summary: Comment classifier 
Language: FR
Category: project
Status: draft

## Le contexte

La cartographie des cultures est possible grâce à la disponibilité des données satellites (Landsat, Sentinel, ...) et la recherche ménée autour de la télédetection. Le champ applicatif de cette technologie est large: modélisation de rendement, suivi de surface cultivée, etc.

Pour classifier les types de culture, on peut exploiter leurs signaux spectraux, qui reflètent leur cycle de développement. Pour simplifier, lorsque la culture se développe, un signal dans le vert augmente jusqu'à un pic de saison pour ensuite redescendre lors du déssechement de la plante et de sa récolte. La multitude de spectres et d'indices dont on peut en décliner (autre que le sacro-saint NDVI), leur temporalité, ainsi que leur dynamique sont autant de paramètres qui permettent de différencier une type de culture à un autre. Par exemple, le colza d'hiver se développant sur une longue période, avec des couleurs marquée de part sa floraison, aura un signal distinct d'une culture de printemps tel que le maïs.

La difficulté de l'exercice réside dans le pré-traitement des données, et la disponibilité de données d'observation permettant l'entrainement d'algorithme de Machine-Learning (ML) tel que des modèles de classification.

La technologie récente des modèles géospatiaux fondationnels, tel que les [AlphaEarth Foundations](https://arxiv.org/pdf/2507.22291) ou [TESSERA](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_TESSERA_Temporal_Embeddings_of_Surface_Spectra_for_Earth_Representation_and_CVPR_2026_paper.pdf) permettent de palier à cela. Elle condense pour chaque année un très grand nombre de données dans des embeddings qui conservent, voir améliorent, le pouvoir prédictif des signaux satellitaires.

Celle-ci a déjà été utilisée pour classifier les types de culture: [Britt W. Smith, Jessica J. Walker, Christopher E. Soulard,
Satellite embeddings for crop type classification: a comparative examination](https://doi.org/10.1016/j.jag.2026.105531).

Mais cette étude a utilisée des classes de cultures généraliste: pâturage, champ, cultures maraîchères, agrumes et cultures subtropicales, feuillus, céréales, vignes, rizières et jachère.

## Qu'en est-il d'espèces culturales comme le colza ou le maïs ?

Si les embeddings condensent l'information annuel en un unique point temporel, sont-ils capables de détecter des cultures au cycle de développement court, tel que le lin et ces 100 jours de développement ?



