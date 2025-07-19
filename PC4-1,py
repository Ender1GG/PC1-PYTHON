import requests

def procesar_temperaturas():
    url = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202506/main/Modulo4/src/temperaturas.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        lineas = response.text.strip().split('\n')

        temperaturas = []
        for linea in lineas:
            try:
                fecha, temp = linea.strip().split(',')
                temperaturas.append(float(temp))
            except ValueError:
                print(f"Linea invalida: {linea.strip()}")

        promedio = sum(temperaturas) / len(temperaturas)
        maxima = max(temperaturas)
        minima = min(temperaturas)

        with open("resumen_temperaturas.txt", "w") as resumen:
            resumen.write(f"Promedio: {promedio:.2f}\n")
            resumen.write(f"Maxima: {maxima:.2f}\n")
            resumen.write(f"Minima: {minima:.2f}\n")

    except requests.exceptions.RequestException as e:
        print("Error al descargar el archivo:", e)

procesar_temperaturas()
