import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import sys
from utils.backend import backend_request
from dotenv import load_dotenv
import io, base64
from datetime import datetime
from utils.tools import generate_graph_1, generate_graph_2, generate_graph_3

load_dotenv()

# Access in backend
auth: dict = backend_request('POST', '/auth/login', data={
    'email': 'admin@insignia.com',
    'password': 'ADMIN2025'
})

if auth is None:
    raise RuntimeError("Abortando...")

token = auth.get('token')

response = backend_request('GET', '/sales', token=token)

if not response:
    raise RuntimeError("Sin datos de ventas")

# Convertimos los datos a DataFrame
df = pd.DataFrame(response)

# Aseguramos que la columna de fecha sea tipo datetime
df['date'] = pd.to_datetime(df['date'])


img1 = generate_graph_1(df)
img2 = generate_graph_2(df)
img3 = generate_graph_3(df)


# --- Generar HTML ---
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Ventas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="text-center mb-4">Reporte de Ventas</h1>
        <p class="text-center text-muted">Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Cantidad de productos vendidos por día</h5>
                <img src="data:image/png;base64,{img1}" class="img-fluid rounded">
            </div>
        </div>

        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Precio promedio de venta por día</h5>
                <img src="data:image/png;base64,{img2}" class="img-fluid rounded">
            </div>
        </div>

        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Relación entre cantidad y precio</h5>
                <img src="data:image/png;base64,{img3}" class="img-fluid rounded">
            </div>
        </div>

        <footer class="text-center mt-5 text-muted">
            <small>© {datetime.now().year} Insignia Analytics</small>
        </footer>
    </div>
</body>
</html>
"""

# Guardar en archivo
with open("reporte_ventas.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML generado: reporte_ventas.html")
