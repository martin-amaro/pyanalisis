# Proyecto de Análisis de Datos

Este proyecto construye un pipeline simple de análisis de datos usando **Python y Pandas**.  
Se parte de dos archivos de datos relacionados (`productos.csv` y `envios.json`) con problemas de calidad (nulos, símbolos de moneda, texto inconsistente).

## Funcionalidades

- Cargar datos desde CSV o JSON
- Manejar valores nulos
- Estandarizar texto (minúsculas, quitar espacios)
- Limpieza de columnas con moneda
- Operaciones de `merge`, `groupby`, filtrado

## Preguntas respondidas

1. Producto con más transacciones.
2. Número total de unidades por bodega.
3. Cantidad de envíos retrasados.

## Requisitos

- Python 3.9+
- pandas

Instalar dependencias:
```bash
pip install -r requirements.txt
