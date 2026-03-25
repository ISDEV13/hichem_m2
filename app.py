
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

from utils import remove_outliers_iqr



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
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True)
    plt.title("Matrice de corrélation")
    plt.show()


def analyse_boxplots(df):
    plt.figure(figsize=(10, 5))
    df.boxplot()
    plt.title("Boxplot global")
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


def run_pipeline(path):
    df = load_data(path)

    print("Shape initiale :", df.shape)


    analyse_missing_values(df)
    analyse_distributions(df)
    analyse_correlations(df)
    analyse_boxplots(df)

    # Nettoyage
    df_clean = clean_data(df)

    print("Shape après nettoyage :", df_clean.shape)
    analyse_missing_values(df_clean)
    analyse_distributions(df_clean)
    analyse_correlations(df_clean)
    analyse_boxplots(df_clean)
    return df_clean


# ==============================
# 6. EXECUTION
# ==============================
if __name__ == "__main__":
    df_clean = run_pipeline("./dataset.csv")