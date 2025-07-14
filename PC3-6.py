import requests

def obtener_tipo_cambio():
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2025")
        response.raise_for_status()
        data = response.json()
        min_compra = float('inf')
        max_venta = float('-inf')
        max_diferencia = float('-inf')
        fecha_min_compra = ""
        fecha_max_venta = ""
        fecha_max_diferencia = ""
        for registro in data:
            fecha = registro['fecha']
            compra = float(registro['compra'])
            venta = float(registro['venta'])
            diferencia = venta - compra
            if compra < min_compra:
                min_compra = compra
                fecha_min_compra = fecha
            if venta > max_venta:
                max_venta = venta
                fecha_max_venta = fecha
            if diferencia > max_diferencia:
                max_diferencia = diferencia
                fecha_max_diferencia = fecha
        print(f"La fecha con el valor de compra minimo es: {fecha_min_compra} con un valor de compra de {min_compra}")
        print(f"La fecha con el valor de venta maximo es: {fecha_max_venta} con un valor de venta de {max_venta}")
        print(f"La fecha con la diferencia maxima entre compra y venta es: {fecha_max_diferencia} con una diferencia de {max_diferencia}")
    
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}")
    except ValueError as e:
        print(f"Error al procesar los datos: {e}")
obtener_tipo_cambio()
