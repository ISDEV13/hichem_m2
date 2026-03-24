# Module M2 : Nettoyage et traitement éthique de données structurées

### Objectif principal
**Analyser, nettoyer et transformer les données numériques pour produire un dataset fiable, propre, cohérent et directement exploitable**, en appliquant des techniques rigoureuses de traitement et en garantissant intégrité et traçabilité.

---

## 📊 Contenu du projet

### Fichiers sources
- **`dataset.csv`** : données brutes initiales (1000 lignes, 9 colonnes numériques)
- **`app.py`** : script principal de nettoyage et visualisation
- **`utils.py`** : fonction `remove_outliers_iqr()` pour détection/suppression outliers

### Données traitées
Colonnes numériques présentes :
- **age** : âge du client (18-75 ans)
- **taille** : taille en cm
- **poids** : poids en kg
- **revenu_estime_mois** : revenu mensuel estimé
- **historique_credits** : nombre de crédits antérieurs
- **risque_personnel** : score risque (0-1)
- **score_credit** : score crédit (0-850+)
- **loyer_mensuel** : loyer ou charge mensuelle
- **montant_pret** : variable cible (montant du prêt)

---

## 🚀 Utilisation

### Installation des dépendances
```bash
pip install pandas numpy matplotlib seaborn missingno scikit-learn
```

### Exécution du pipeline complet
```bash
python app.py
```
Produit :
- Visualisations PNG (valeurs manquantes, distributions, corrélations)
- CSV des statistiques avant/après
- Dataset nettoyé


Consulter :
- **`documentation.md`** : analyse exploratoire complète




