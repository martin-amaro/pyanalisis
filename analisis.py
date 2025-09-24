import pandas as pd
from utils.data_utils import (
    load_data,
    handle_nulls,
    normalize,
    clean_dollar_sign
)

# --- Cargar datos ---
productos = load_data("data/productos.csv")
envios = load_data("data/envios.json")

# --- Preprocesamiento ---
productos = handle_nulls(productos, method="fill", fill_value="desconocido")
envios = handle_nulls(envios, method="drop")

productos = normalize(productos, ["nombre", "categoria"])
envios = normalize(envios, ["estado"])

productos = clean_dollar_sign(productos, "precio")

# Unión de tablas
df = envios.merge(productos, on="producto_id")

# Análisis de frecuencia
frecuencia = df["nombre"].value_counts().idxmax()
print("Producto con más transacciones:", frecuencia)

# Análisis de agregación
unidades_por_bodega = df.groupby("bodega")["cantidad"].sum()
print("\nUnidades totales por bodega:\n", unidades_por_bodega)

# Análisis con filtrado y conteo
retrasados = df[df["estado"] == "retrasado"].shape[0]
print("\nCantidad de envíos retrasados:", retrasados)
