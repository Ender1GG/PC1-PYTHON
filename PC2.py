# Problema 1
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)

# Problema 2
for i in range(1, 6):
    print('* ' * i)
for i in range(4, 0, -1):
    print('* ' * i)

# Problema 3
numeros = []
while True:
    respuesta = input("Desea ingresar un numero? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el numero: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break

pares = sum(1 for num in numeros if num % 2 == 0)
impares = len(numeros) - pares
print(f"Numeros ingresados: {numeros}")
print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")

# Problema 4
alumnos = []
n = int(input("Ingrese el numero de alumnos: "))
for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    alumnos.append({"Alumno": nombre, "Notas": notas})

print("Listado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(alumno)

# Problema 5
def contar_digitos(numero, digito):
    return str(numero).count(str(digito))

numero = int(input("Ingrese el numero: "))
digito = int(input("Ingrese el digito: "))
print(f"Cantidad de veces {digito} en el numero {numero}: {contar_digitos(numero, digito)}")

# Problema 6
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
print()

# Problema 7
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")

# Problema 8
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

numero = int(input("Ingrese un numero: "))
print(f"El factorial de {numero} es {factorial(numero)}")

# Problema 9
def eliminar_vocales(cadena):
    return ''.join([letra for letra in cadena if letra.lower() not in 'aeiou'])

texto = input("Ingrese una cadena de texto: ")
print(f"Texto sin vocales: {eliminar_vocales(texto)}")

# Problema 10
def convertir_fecha(fecha):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
        return f"{anio}-{mes.zfill(2)}-{dia.zfill(2)}"
    else:
        mes, dia, anio = fecha.split()
        mes_num = meses.index(mes) + 1
        return f"{anio}-{str(mes_num).zfill(2)}-{dia.split(',')[0].zfill(2)}"

fecha = input("Ingrese la fecha en formato MM/DD/AAAA o Mes dia, año: ")
print(f"Fecha en formato AAAA-MM-DD: {convertir_fecha(fecha)}")
