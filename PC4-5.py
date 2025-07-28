import csv
import sqlite3
from collections import defaultdict
from pymongo import MongoClient

def obtener_tipo_cambio(fecha, cursor):
    cursor.execute("SELECT cambio FROM tipo_cambio WHERE fecha = ?", (fecha,))
    fila = cursor.fetchone()
    if fila:
        return fila[0]
    else:
        return 3.8

def procesar_ventas(archivo_csv, cursor):
    ventas_soles = defaultdict(float)
    ventas_cantidad = defaultdict(int)
    nombres_columnas = ['fecha', 'producto', 'cantidad', 'precio_dolares']

    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, fieldnames=nombres_columnas)
        for fila in lector:
            fecha = fila['fecha']
            producto = fila['producto']
            cantidad = int(fila['cantidad'])
            precio_dolares = float(fila['precio_dolares'])
            tipo_cambio = obtener_tipo_cambio(fecha, cursor)
            precio_soles = precio_dolares * tipo_cambio
            total_soles = precio_soles * cantidad
            ventas_soles[producto] += total_soles
            ventas_cantidad[producto] += cantidad

    return ventas_soles, ventas_cantidad

def imprimir_reporte(ventas_soles, ventas_cantidad):
    print("\nReporte total vendido (S/):")
    for producto, total in ventas_soles.items():
        print(f"- Producto: {producto}, Total vendido: S/{total:.2f}, Cantidad: {ventas_cantidad[producto]}")

def guardar_en_mongodb(ventas_soles, ventas_cantidad):
    cliente = MongoClient("mongodb+srv://carlosabelgrande:Cs1xyqN4kFBBvADv@datuxcurso.jomz9vs.mongodb.net/?retryWrites=true&w=majority&appName=datuxcurso")
    db = cliente["cursodb"]
    coleccion = db["ventas_solarizadas"]
    coleccion.delete_many({})
    documentos = []
    for producto in ventas_soles:
        doc = {
            "producto": producto,
            "total_soles": round(ventas_soles[producto], 2),
            "cantidad": ventas_cantidad[producto]
        }
        documentos.append(doc)
    coleccion.insert_many(documentos)
    print("\nReporte almacenado en MongoDB (cursodb.ventas_solarizadas).")
    cliente.close()

def main():
    con = sqlite3.connect('tipos_cambio.db')
    cur = con.cursor()
    archivo_csv = 'ventas.csv'
    ventas_soles, ventas_cantidad = procesar_ventas(archivo_csv, cur)
    imprimir_reporte(ventas_soles, ventas_cantidad)
    guardar_en_mongodb(ventas_soles, ventas_cantidad)
    con.close()

if __name__ == '__main__':
    main()
