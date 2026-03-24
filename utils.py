def remove_outliers_iqr(df, columns, factor=1.5):
    """Fonction pour détecter et supprimer les outliers en utilisant la méthode de l'IQR (Interquartile Range).
    Args:        df (pd.DataFrame): Le DataFrame à traiter.
        columns (list): Liste des colonnes à vérifier pour les outliers.
        factor (float): Le facteur pour déterminer les limites des outliers (par défaut 1.5).
    Returns:        pd.DataFrame: Le DataFrame filtré sans les outliers.    
    """
    df_filtered = df.copy()

    for col in columns:
        Q1 = df_filtered[col].quantile(0.25)
        Q3 = df_filtered[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR

        df_filtered = df_filtered[
            (df_filtered[col] >= lower_bound) &
            (df_filtered[col] <= upper_bound)
        ]

    return df_filtered