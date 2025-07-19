import os

def crear_tabla(n):
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")

def leer_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("El archivo no existe.")

def leer_linea(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print("Linea fuera de rango.")
    except FileNotFoundError:
        print("El archivo no existe.")

def menu():
    while True:
        print("\n1. Crear tabla\n2. Leer tabla\n3. Leer linea de tabla\n4. Salir")
        op = input("Seleccione una opcion: ")
        if op == "1":
            n = int(input("Numero (1-10): "))
            if 1 <= n <= 10:
                crear_tabla(n)
        elif op == "2":
            n = int(input("Numero (1-10): "))
            leer_tabla(n)
        elif op == "3":
            n = int(input("Numero (1-10): "))
            m = int(input("Linea (1-10): "))
            leer_linea(n, m)
        elif op == "4":
            break
        else:
            print("Opcion no valida")

menu()
