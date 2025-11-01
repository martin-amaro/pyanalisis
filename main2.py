import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import requests
import sys
from utils.backend import backend_request
from dotenv import load_dotenv
from visualizacion import grafico_consumo_por_mes, grafico_distribucion_consumo
from generador_reporte import generar_reporte_html

load_dotenv()

# users = response.json()


# df = pd.DataFrame(users)
# print(df)

def main():
    # Access in backend
    auth:dict = backend_request('POST', '/auth/login', data={
        'email': 'admin@insignia.com',
        'password': 'ADMIN2025'
    })

    if auth == None:
        raise RuntimeError("Abortando...")


    token = auth.get('token')

    response = backend_request('GET', '/sales', token=token)

    print(response)
    # Cargar y procesar datos
    df = pd.read_json(response)
    
    # Generar gráficos
    graficos = {
        'consumo_mensual': grafico_consumo_por_mes(df),
        'distribucion': grafico_distribucion_consumo(df)
    }
    
    # Generar tabla HTML
    tabla_html = df.to_html(classes='dataTable')
    
    # Generar reporte
    generar_reporte_html(graficos, tabla_html)

if __name__ == "__main__":
    main()

