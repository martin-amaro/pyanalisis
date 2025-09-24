import pandas as pd

def load_data(path: str):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    else:
        raise ValueError("Formato no soportado.")
    
