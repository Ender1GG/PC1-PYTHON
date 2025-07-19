def contar_loc(ruta):
    if not ruta.endswith(".py"):
        return

    try:
        with open(ruta, "r") as f:
            lineas = f.readlines()

        loc = 0
        for linea in lineas:
            linea_strip = linea.strip()
            if linea_strip and not linea_strip.startswith("#"):
                loc += 1

        print(f"Número de líneas de código: {loc}")
    except FileNotFoundError:
        print("Ruta no válida o archivo no existe.")

ruta = input("Ingrese la ruta del archivo .py: ")
contar_loc(ruta)
