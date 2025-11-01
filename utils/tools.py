from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64

def generate_graph_1(df):
    plt.figure(figsize=(8, 4))
    sns.barplot(x=df['date'].dt.date, y=df['quantity'], color='skyblue')
    plt.title("Cantidad de productos vendidos por día")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad vendida")
    plt.xticks(rotation=45)
    buffer1 = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    return base64.b64encode(buffer1.read()).decode('utf-8')

def generate_graph_2(df):
    avg_price = df.groupby(df['date'].dt.date)['price'].mean().reset_index()
    plt.figure(figsize=(8, 4))
    sns.lineplot(x=avg_price['date'], y=avg_price['price'], marker='o', color='orange')
    plt.title("Precio promedio de venta por día")
    plt.xlabel("Fecha")
    plt.ylabel("Precio promedio ($)")
    plt.xticks(rotation=45)
    buffer2 = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer2, format='png')
    plt.close()
    buffer2.seek(0)
    return base64.b64encode(buffer2.read()).decode('utf-8')

def generate_graph_3(df):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='quantity', y='price', data=df, hue=df['date'].dt.date, palette='cool')
    plt.title("Relación entre cantidad y precio")
    plt.xlabel("Cantidad")
    plt.ylabel("Precio ($)")
    plt.legend(title="Fecha", bbox_to_anchor=(1.05, 1), loc='upper left')
    buffer3 = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer3, format='png')
    plt.close()
    buffer3.seek(0)
    return base64.b64encode(buffer3.read()).decode('utf-8')
# def generate_html():
#     html = f"""
# <!DOCTYPE html>
# <html lang="es">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Reporte de Ventas</title>
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
# </head>
# <body class="bg-light">
#     <div class="container py-5">
#         <h1 class="text-center mb-4">Reporte de Ventas</h1>
#         <p class="text-center text-muted">Generado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

#         <div class="card mb-4 shadow-sm">
#             <div class="card-body">
#                 <h5 class="card-title">Cantidad de productos vendidos por día</h5>
#                 <img src="data:image/png;base64,{img1}" class="img-fluid rounded">
#             </div>
#         </div>

#         <div class="card mb-4 shadow-sm">
#             <div class="card-body">
#                 <h5 class="card-title">Precio promedio de venta por día</h5>
#                 <img src="data:image/png;base64,{img2}" class="img-fluid rounded">
#             </div>
#         </div>

#         <div class="card mb-4 shadow-sm">
#             <div class="card-body">
#                 <h5 class="card-title">Relación entre cantidad y precio</h5>
#                 <img src="data:image/png;base64,{img3}" class="img-fluid rounded">
#             </div>
#         </div>

#         <footer class="text-center mt-5 text-muted">
#             <small>© {datetime.now().year} Insignia Analytics</small>
#         </footer>
#     </div>
# </body>
# </html>
# """
