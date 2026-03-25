from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from utils import remove_outliers_iqr
import pandas as pd


def split(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)



def preprocessingTechnique(df):

    #  Suppression colonnes 
    to_drop = ["nationalité_francaise",'score_credit', "historique_credits"]
    df = df.drop(columns=to_drop, errors="ignore")


    #  Colonnes
    num_cols = [
        "revenu_estime_mois",
        "loyer_mensuel",
        "risque_personnel"
    ]

    categorical_cols = [
        "sexe",
        "sport_licence",
        "niveau_etude",
        "region",
        "smoker",
        "situation_familiale",
        "imc_cat",
        "age_bucket",
    ]


    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", MinMaxScaler())
    ])

    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, categorical_cols)
    ])

    X = df.drop(columns=["montant_pret"])
    y = df["montant_pret"]

    X_processed = preprocessor.fit_transform(X)
    feature_names = preprocessor.get_feature_names_out()
    X_processed = pd.DataFrame(X_processed, columns=feature_names)
    df_final = pd.concat([X_processed, y.reset_index(drop=True)], axis=1)
    return X_processed, y, preprocessor,df_final

def preprocessingEthique(df):

    to_drop = ["nom", "prenom"]
    df = df.drop(columns=to_drop, errors="ignore")
    df["age_bucket"] = pd.cut(
        df["age"],
        bins=[18, 30, 45, 60, 100],
        labels=["jeune", "adulte", "senior", "retraite"]
    )
    df = df.drop(columns=["age"])

    df["imc"] = df["poids"] / ((df["taille"] / 100) ** 2)

    df["imc_cat"] = pd.cut(
        df["imc"],
        bins=[0, 18.5, 25, 30, 100],
        labels=["insuffisant", "normal", "surpoids", "obese"]
    )

    df = df.drop(columns=["taille", "poids", "imc"])

    return df

