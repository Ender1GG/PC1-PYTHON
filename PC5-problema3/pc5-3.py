import os
import zipfile
import pandas as pd
from pymongo import MongoClient
import requests
import csv


ZIP_URL = "https://netsg.cs.sfu.ca/youtubedata/0302.zip"
ZIP_NAME = "0302.zip"
FOLDER_NAME = "youtube_data"
MONGO_URI = "mongodb+srv://carlosabelgrande:Cs1xyqN4kFBBvADv@datuxcurso.jomz9vs.mongodb.net/?retryWrites=true&w=majority&appName=datuxcurso"
DB_NAME = "cursodb"
COLLECTION_NAME = "youtube_videos"

COLUMNAS = [
    "video_id",       # Columna 1: Video ID
    "uploader",       # Columna 2: Nombre del cargador
    "age",            # Columna 3: Edad en días
    "category",       # Columna 4: Categoría
    "length",         # Columna 5: Duración en minutos
    "views",          # Columna 6: Visualizaciones
    "rate",           # Columna 7: Calificación
    "ratings",        # Columna 8: Número de calificaciones
    "comments",       # Columna 9: Comentarios
    "related_ids"     # Columna 10: IDs relacionados
]


COLUMNAS_REQUERIDAS = ["video_id", "age", "category", "views", "rate"]

def descargar_zip(url, nombre_zip):
    if not os.path.exists(nombre_zip):
        print(f"Descargando {nombre_zip}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(nombre_zip, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Descarga completada")

def descomprimir_zip(nombre_zip, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    print("Descomprimiendo archivos...")
    with zipfile.ZipFile(nombre_zip, 'r') as zip_ref:
        zip_ref.extractall(carpeta_destino)
    print(f"Archivos descomprimidos en: {carpeta_destino}")

def leer_y_procesar_archivo(ruta_archivo):
    try:
        
        lineas = []
        with open(ruta_archivo, 'r', encoding='latin1') as f:
            lector = csv.reader(f, delimiter='\t')
            for fila in lector:
                if len(fila) >= 10: 
                    lineas.append(fila[:10])  
        
        
        df = pd.DataFrame(lineas, columns=COLUMNAS)
        
        print(f"\nDatos originales: {len(df)} registros")
        
        
        df = df[COLUMNAS_REQUERIDAS]
        
        
        for col in ['age', 'views', 'rate']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        
        df = df.dropna(subset=['video_id', 'category'])
        df = df[df['video_id'].str.len() == 11]  
        
        print(f"Datos válidos después de procesar: {len(df)} registros")
        return df
        
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return pd.DataFrame()

def guardar_en_mongodb(df):
    if df.empty:
        print("\n⚠️ ¡Advertencia: No hay datos para insertar!")
        return
    
    try:
        print("\nConectando a MongoDB Atlas...")
        cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
        cliente.server_info()
        print("✔ Conexión exitosa a MongoDB Atlas")
        
        db = cliente[DB_NAME]
        coleccion = db[COLLECTION_NAME]
        
       
        datos = df.to_dict(orient="records")
        resultado = coleccion.insert_many(datos)
        
        print(f"\n✅ Datos insertados en MongoDB Atlas")
        print(f"Base de datos: {DB_NAME}")
        print(f"Colección: {COLLECTION_NAME}")
        print(f"Registros insertados: {len(resultado.inserted_ids)}")
        
        
        ejemplo = coleccion.find_one()
        print("\nDocumento de ejemplo en MongoDB:")
        for campo, valor in ejemplo.items():
            print(f"{campo}: {valor}")
        
    except Exception as e:
        print(f"\n❌ Error de conexión: {e}")

def main():
    print("="*50)
    print("SOLUCIÓN DEFINITIVA: ANÁLISIS DE DATOS DE YOUTUBE")
    print("="*50)
    
    
    if not os.path.exists(ZIP_NAME):
        descargar_zip(ZIP_URL, ZIP_NAME)
    descomprimir_zip(ZIP_NAME, FOLDER_NAME)
    
    
    archivos_datos = []
    for root, _, files in os.walk(FOLDER_NAME):
        for file in files:
            if file.endswith((".txt", ".video")):
                archivo_path = os.path.join(root, file)
                if os.path.getsize(archivo_path) > 1024:  # >1KB
                    archivos_datos.append(archivo_path)
    
    if not archivos_datos:
        print("\n❌ Error: No se encontraron archivos de datos válidos")
        return
    
    print(f"\nEncontrados {len(archivos_datos)} archivos de datos válidos")
    
    
    todos_datos = pd.DataFrame()
    for archivo in archivos_datos:
        nombre_archivo = os.path.basename(archivo)
        print(f"\n📂 Procesando: {nombre_archivo} ({os.path.getsize(archivo)/1024:.1f} KB)")
        df = leer_y_procesar_archivo(archivo)
        if not df.empty:
            todos_datos = pd.concat([todos_datos, df], ignore_index=True)
    
    if not todos_datos.empty:
        print(f"\n📊 Total de registros válidos: {len(todos_datos)}")
        print("\nEjemplo de datos antes de insertar:")
        print(todos_datos.head(3).to_string(index=False))
        guardar_en_mongodb(todos_datos)
    else:
        print("\n⚠️ No se encontraron datos válidos en ningún archivo")

if __name__ == "__main__":
    main()