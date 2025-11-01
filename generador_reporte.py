def generar_reporte_html(graficos, tabla_datos):
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte de Análisis de Consumo</title>
        <link rel="stylesheet" href="estilos.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.css">
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.js"></script>
    </head>
    <body>
        <div class="container">
            <h1>Reporte de Análisis de Consumo Eléctrico</h1>
            
            <div class="chart-container">
                <h2>Consumo Mensual</h2>
                <img src="data:image/png;base64,{graficos['consumo_mensual']}" />
            </div>
            
            <div class="chart-container">
                <h2>Distribución del Consumo</h2>
                <img src="data:image/png;base64,{graficos['distribucion']}" />
            </div>
            
            <div class="table-container">
                <h2>Datos Detallados</h2>
                {tabla_datos}
            </div>
        </div>
        
        <script>
            $(document).ready(function() {{
                $('.dataTable').DataTable();
            }});
        </script>
    </body>
    </html>
    """
    
    with open('reporte.html', 'w', encoding='utf-8') as f:
        f.write(template)
