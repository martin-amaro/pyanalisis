import pandas as pd


def load_data(path: str):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    else:
        raise ValueError("Formato no soportado.")


def handle_nulls(df: pd.DataFrame, method: str = "drop", fill_value=None):
    if method == "drop":
        return df.dropna()
    elif method == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError("Método no soportado.")


def normalize(df: pd.DataFrame, columns: list):
    for col in columns:
        df[col] = df[col].str.lower().str.strip()
    return df


def clean_dollar_sign(df: pd.DataFrame, column: str):
    df[column] = df[column].replace(r"[\$,]", "", regex=True).astype(float)
    return df