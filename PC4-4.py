import requests
import time
from pymongo import MongoClient


URL = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year={year}"


cadena_conexion_mongo = "mongodb+srv://carlosabelgrande:Cs1xyqN4kFBBvADv@datuxcurso.jomz9vs.mongodb.net/?retryWrites=true&w=majority&appName=datuxcurso"


def obtener_tipo_cambio(month: int, year: int) -> list:
    try:
        response = requests.get(URL.format(month=month, year=year))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error código {response.status_code} al obtener mes {month}")
            return []
    except requests.RequestException as e:
        print(f"Error de red al obtener mes {month}: {e}")
        return []


def guardar_en_mongo(datos: list):
    cliente = MongoClient(cadena_conexion_mongo)
    db = cliente["cursodb"]
    coleccion = db["ventas"]

    
    coleccion.delete_many({"origen": "sunat"})

    if datos:
        for doc in datos:
            doc["origen"] = "sunat"  
        coleccion.insert_many(datos)
        print("✅ Datos insertados en MongoDB correctamente en cursodb.ventas.")
    else:
        print("⚠️ No hay datos para insertar.")
    cliente.close()


def mostrar_datos_mongo():
    cliente = MongoClient(cadena_conexion_mongo)
    db = cliente["cursodb"]
    coleccion = db["ventas"]

    print("\n📋 Mostrando datos desde MongoDB (solo 'sunat'):\n")
    for doc in coleccion.find({"origen": "sunat"}):
        print(doc)
    cliente.close()


def main():
    todos_los_datos = []
    for codmes in range(1, 13):
        print(f"🔄 Obteniendo tipo de cambio del mes {codmes}...")
        datos_mes = obtener_tipo_cambio(month=codmes, year=2023)
        todos_los_datos.extend(datos_mes)
        time.sleep(2)  

    guardar_en_mongo(todos_los_datos)
    mostrar_datos_mongo()


if __name__ == "__main__":
    main()
