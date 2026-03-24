# Documentation du traitement et Analyse statistique des données

## Analyse des distributions

On commence par afficher les distributions de chaque variable.
Pour chaque variable :

- Âge : distribution équilibrée selon les tranches d’âge entre 18 et 70 ans.
- Poids : distribution proche d’une courbe gaussienne.
- Taille : distribution proche d’une courbe gaussienne.
- Revenu estimé par mois : la distribution semble globalement gaussienne, mais on observe de nombreuses valeurs en dehors de la distribution centrale, principalement sur les faibles revenus.
- Historique de crédit : distribution équilibrée entre les différentes valeurs.
- Risque personnel : distribution équilibrée entre les différentes valeurs.
- Score de crédit : distribution équilibrée entre les différentes valeurs.
- Loyer mensuel : distribution regroupée autour de trois valeurs principales (1000, 5000, 10000).
- Montant du prêt : forte concentration autour de 1000 €, avec une distribution décroissante à mesure que le montant augmente.

## Analyse des valeurs manquantes et des outliers
Ensuite, on met en évidence, grâce à la bibliothèque missingno :

- Une matrice des valeurs manquantes
- Le nombre de valeurs manquantes par variable
- La présence d’outliers selon les variables

On observe :

De nombreuses valeurs manquantes dans les colonnes historique de crédit, score de crédit et loyer mensuel
Aucune corrélation significative entre les variables, à l’exception d’une légère corrélation entre le revenu estimé et le montant du prêt
La présence d’outliers dans les colonnes taille, poids, revenu estimé par mois et montant du prêt

## Traitement des données
Nous commençons par traiter les valeurs aberrantes (outliers) sur les variables les plus pertinentes, à savoir la taille et le poids, en utilisant la méthode IQR (Interquartile Range)
Le choix de la méthode IQR repose sur le fait qu’elle s’appuie sur la médiane et les quartiles, qui sont des indicateurs robustes aux valeurs extrêmes, contrairement à la moyenne. En effet :

- Si la distribution suit une loi gaussienne, la médiane est égale (ou très proche) de la moyenne
- Si la distribution n’est pas gaussienne ou contient des valeurs extrêmes, la médiane reste plus représentative que la moyenne

En revanche, nous faisons le choix de conserver les outliers pour certaines variables spécifiques :

- Montant du prêt : étant la variable cible, il est essentiel de préserver l’ensemble de sa variabilité afin de ne pas biaiser l’apprentissage du modèle
- Revenu estimé par mois : malgré la présence de valeurs extrêmes, celles-ci apportent une information importante et contribuent à enrichir la diversité des profils, ce qui peut améliorer la capacité de généralisation du modèle

On décide de supprimer les colonnes contenant plus de 50 % de valeurs manquantes, à savoir :

- Historique de crédit
- Score de crédit

Ces colonnes sont supprimées car :

Elles contiennent trop de valeurs manquantes
L’imputation sur des variables de type score (souvent sensibles et non linéaires) avec une proportion aussi élevée de données manquantes risquerait de biaiser fortement l’analyse

Concernant la colonne loyer mensuel, on choisit d’imputer les valeurs manquantes avec la médiane.

Ce choix est plus pertinent que la moyenne, car la distribution des loyers n’est pas normale (présence de regroupements et de valeurs extrêmes), ce qui rend la médiane plus robuste aux outliers

