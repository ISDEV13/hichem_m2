#  En utilisant les bibliothèques standard (Pandas, missingno, pyplot, seaborn, altair, plotly) Inspecter le dataset pour repérer :
import seaborn as sns
from utils import remove_outliers_iqr




# Importer le dataset
import pandas as pd
df = pd.read_csv(".\dataset.csv")

# Importer les bibliothèques de prétraitement
import missingno as msno
import matplotlib.pyplot as plt

#Matrice de valeurs manquantes
fig2, ax2 = plt.subplots(figsize=(10,5))
msno.matrix(df, ax=ax2)

# # Nombre de valeurs manquantes
fig1, ax1 = plt.subplots(figsize=(10,5))
msno.bar(df, ax=ax1)


# Correlation entre valeurs manquantes
fig3, ax3 = plt.subplots(figsize=(10,5))
msno.heatmap(df, ax=ax3)

fig4, ax4 = plt.subplots(figsize=(10,5))
df.boxplot()
plt.show()


colonnes = df.select_dtypes(include='number').columns

# Créer une figure avec autant de sous-graphes que de colonnes
fig, axes = plt.subplots(len(colonnes), 1, figsize=(8, 4*len(colonnes)))

# Si une seule colonne, axes n'est pas un tableau, on le transforme en liste
if len(colonnes) == 1:
    axes = [axes]

# Tracer chaque histogramme
for ax, col in zip(axes, colonnes):
    sns.histplot(df[col], kde=True, ax=ax, color='skyblue')
    ax.set_title(f"Distribution de {col}")

plt.tight_layout()
plt.show()


ax = sns.heatmap(df.corr(), annot=True)
plt.show()


# Supprimer les doublons
df = df.drop_duplicates()

# Traiter les outliers
df = remove_outliers_iqr(df, columns=["taille", "poids"])

# Suppression des collonne avec plus de 50% de valeurs manquantes
taux_nan = df.isnull().mean()  # renvoie 0.0 à 1.0
# Choix d’un seuil : ici on supprime les colonnes avec > 50% de NaN
seuil = 0.5
colonnes_a_supprimer = taux_nan[taux_nan > seuil].index

df = df.drop(columns=colonnes_a_supprimer)

# On impute les valeurs manquantes du loyer mensuel avec la médiane de la colonne
df['loyer_mensuel'] = df['loyer_mensuel'].fillna(df['loyer_mensuel'].median())
