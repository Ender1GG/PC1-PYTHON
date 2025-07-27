import requests
import time
URL ="https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year={year}"
from pymongo import MongoClient 
cadena_conexion_mongo = "mongodb+srv://gon2794:WGA2LLADVph52DYf@mongodbcluster.polzshz.mongodb.net/?retryWrites=true&w=majority&appName=mongodbCluster"
def obtener_tipo_cambio(month:int,year:int)->list:
    try:
        response = requests.get(URL.format(month=month, year=year))
        #assert response.status_code=200,"Error codigo"
        return response.json()
        pass
    except requests.RequestException:
        return []
        pass
        
def main():
    for codmes in range(1,13):
        print(f"tipo cambio mes{codmes} ...")
        dicxt_sunat= obtener_tipo_cambio(month=codmes, year=2023)
        print(dicxt_sunat)
        pass
        time.sleep(2)
if __name__ == "__main__":
    main()
    pass