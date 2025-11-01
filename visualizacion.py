import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def grafico_consumo_por_mes(df):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='Mes', y='Consumo')
    plt.title('Consumo Mensual')
    plt.xlabel('Mes')
    plt.ylabel('Consumo (kWh)')
    return get_graph_as_base64()

def grafico_distribucion_consumo(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Consumo', bins=30)
    plt.title('Distribución del Consumo')
    plt.xlabel('Consumo (kWh)')
    plt.ylabel('Frecuencia')
    return get_graph_as_base64()

def get_graph_as_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()
    return base64.b64encode(image_png).decode('utf-8')
