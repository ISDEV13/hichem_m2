
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

from utils import remove_outliers_iqr
from pretraitement import preprocessingEthique, preprocessingTechnique



def load_data(path):
    df = pd.read_csv(path)
    return df



def analyse_missing_values(df):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    msno.matrix(df, ax=axes[0])
    axes[0].set_title("Matrice des valeurs manquantes")

    msno.bar(df, ax=axes[1])
    axes[1].set_title("Nombre de valeurs manquantes")

    msno.heatmap(df, ax=axes[2])
    axes[2].set_title("Corrélation des valeurs manquantes")

    plt.tight_layout()
    plt.show()


def analyse_distributions(df):
    colonnes = df.select_dtypes(include='number').columns

    fig, axes = plt.subplots(len(colonnes), 1, figsize=(8, 4 * len(colonnes)))

    if len(colonnes) == 1:
        axes = [axes]

    for ax, col in zip(axes, colonnes):
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution de {col}")

    plt.tight_layout()
    plt.show()


def analyse_correlations(df):
    
  # Séparer types
    df_num = df.select_dtypes(include='number')
  
    df_corr = df_num

    # Calcul corrélation
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_corr.corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation (numériques)")
    plt.show()


def analyse_boxplots(df):
      # Sélection des colonnes numériques
    df_num = df.select_dtypes(include='number')

    # Boxplot
    plt.figure(figsize=(12, 6))
    df_num.boxplot()

    plt.title("Boxplots des variables numériques")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def analyse_categorical_distributions(df, to_drop=None):
    df = df.copy()
    if to_drop is not None:
            df = df.drop(columns=to_drop, errors="ignore")
    # Sélection des colonnes catégorielles
    df_cat = df.select_dtypes(include=['object', 'category', 'bool'])

    n_cols = 3  # nombre de graphes par ligne
    n_rows = (len(df_cat.columns) + n_cols - 1) // n_cols

    plt.figure(figsize=(15, 5 * n_rows))

    for i, col in enumerate(df_cat.columns, 1):
        plt.subplot(n_rows, n_cols, i)
        sns.countplot(data=df, x=col)
        plt.title(f"Distribution de {col}")
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()



def clean_data(df):

    # Supprimer les doublons
    df = df.drop_duplicates()

    # Supprimer les colonnes avec trop de NaN (>50%)
    seuil = 0.5
    taux_nan = df.isnull().mean()
    colonnes_a_supprimer = taux_nan[taux_nan > seuil].index
    df = df.drop(columns=colonnes_a_supprimer)

    # Traiter les outliers (IQR)
    df = remove_outliers_iqr(df, columns=["taille", "poids"])

    # Imputation
    if 'loyer_mensuel' in df.columns:
        df['loyer_mensuel'] = df['loyer_mensuel'].fillna(df['loyer_mensuel'].median())

    return df

def run_preprocess(df):

    df = df.copy()
    
    df = df.drop_duplicates()
    df_ethique = preprocessingEthique(df)
    
    X_processed, y, preprocessor,df_final = preprocessingTechnique(df_ethique)
    
    os.makedirs("data", exist_ok=True)
    df_ethique.to_csv("data/dataset_ethique.csv", index=False)
    df_final.to_csv("data/dataset_technique_final.csv", index=False)
    



    return df_final, df_ethique



def run_pipeline(path):
    df = load_data(path)

    print("Shape initiale :", df.shape)

    analyse_missing_values(df)
    analyse_distributions(df)
    analyse_correlations(df)
    analyse_boxplots(df)
    analyse_categorical_distributions(df, to_drop=["nom", "prenom"])
    df_final, df_ethique = run_preprocess(df)

 

    return df_final


# ==============================
# 6. EXECUTION
# ==============================
if __name__ == "__main__":
    df_final = run_pipeline("./datasetmixte.csv")