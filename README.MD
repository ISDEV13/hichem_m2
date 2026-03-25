# Analyse et Prétraitement de Données pour Modèle de Prêt

## Description

Ce projet vise à analyser et prétraiter un jeu de données pour construire un modèle prédictif d'estimation de montants de prêt, tout en respectant les principes du RGPD et en intégrant des considérations éthiques pour éviter les biais discriminants.

L'analyse RGPD des variables est détaillée dans le fichier `analyse.MD`.

## Fonctionnalités

- **Analyse exploratoire des données** : Visualisation des valeurs manquantes, distributions, corrélations, boxplots
- **Nettoyage des données** : Suppression des doublons, traitement des outliers, imputation
- **Prétraitement technique** : Suppression des colonnes problématiques, scaling, encodage
- **Prétraitement éthique** : Transformation des variables sensibles (âge en tranches, IMC), suppression des identifiants directs
- **Respect RGPD** : Analyse de sensibilité des données, justification d'usage

## Structure du Projet

```
├── analyse.MD              # Analyse RGPD des variables
├── app.py                  # Pipeline principal d'analyse et prétraitement
├── pretraitement.py        # Fonctions de prétraitement technique et éthique
├── utils.py                # Fonctions utilitaires (outliers, etc.)
├── datasetmixte.csv        # Jeu de données d'entrée
├── data/                   # Dossier de sortie des données traitées
│   ├── dataset_ethique.csv
│   └── dataset_technique_final.csv
└── README.MD               # Ce fichier
```

## Installation

1. Cloner le repository
2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   ```
3. Activer l'environnement :
   ```bash
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Dépendances

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- missingno

## Utilisation

### Exécution complète du pipeline

```bash
python app.py
```

Cette commande :
1. Charge le jeu de données `datasetmixte.csv`
2. Effectue l'analyse exploratoire (visualisations)
3. Applique le prétraitement éthique
4. Applique le prétraitement technique
5. Sauvegarde les datasets traités dans le dossier `data/`

