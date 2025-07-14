import requests
import zipfile
import os

def descargar_imagen():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    imagen = requests.get(url)
    with open("imagen.jpg", "wb") as f:
        f.write(imagen.content)
    with zipfile.ZipFile('imagen.zip', 'w') as zipf:
        zipf.write("imagen.jpg")
    with zipfile.ZipFile('imagen.zip', 'r') as zipf:
        zipf.extractall("descomprimida")  
    print("Imagen descargada, comprimida y descomprimida correctamente.")
descargar_imagen()
