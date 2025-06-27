#PROBLEMA 1
print("PROBLEMA 1")
nombre=input("Ingrese su nombre de usuario: ")
print(f"! Hola {nombre} !")
#PROBLEMA 2
print("PROBLEMA 2")
consumo=float(input("Consumo : "))
porc_propina=int(input("Porcentaje de propina a dejar: "))
propina=consumo*porc_propina/100
print(f"Cantidad de dinero a dejar como propina: {propina} ")
#PROBLEMA 3
print("PROBLEMA 3")
payaso_peso=112
muneca_peso=75
payasos_vend=int(input("Payasos vendidos ultimo paquete= "))
munecas_vend=int(input("Munecas vendidas ultimo paquete: "))
peso_paquete=payasos_vend*payaso_peso+munecas_vend*muneca_peso
print(f"Peso total del ultimo paquete a enviar: {peso_paquete} gr")
#PROBLEMA 4
print("PROBLEMA 4")
N=int(input("Ingrese el entero positivo : "))
suma=(N*(N+1))/2
print(f"Suma de los N enteros positivos: {suma}")
#PROBLEMA 5
print("PROBLEMA 5")
shows_ultimoa=int(input("Shows vistos : "))
print(shows_ultimoa>3)
#PROBLEMA 6
print("PROBLEMA 6")
edad=int(input("Ingrese su edad: "))
if edad < 4 :
    print("Ingrese gratis")
elif 4 <= edad <= 18 :
    print("El costo es $5")
elif edad>18 :
    print("El costo es $10")
#PROBLEMA 7
print("PROBLEMA 7")
num_1=float(input("Ingrese numero 1: "))
num_2=float(input("Ingrese numero 2: "))
print("Elegir una opcion del menu: ")
print("1.Mostrar suma de los dos numeros")
print("2.Mostrar resta de los dos numeros")
print("3.Mostrar multiplicacion")
opcion=int(input("Ingrese numero de opcion "))
if opcion == 1 :
    print(f"La suma es {num_1 + num_2}")
elif opcion == 2 :
    print(f"La resta es : {num_1 - num_2}")
elif opcion == 3 :
    print(f"La multiplicacion es {num_1 * num_2}")
#PROBLEMA 8
print("PROBLEMA 8")
time=input("Ingrese la hora: ")
hours,minutes=time.split(":")
hours=int(hours)
minutes=int(minutes)
horas_minutos= hours + minutes/60
if 7 <= horas_minutos <= 8:
    print("Hora de desayunar")
elif 12 <= horas_minutos <= 13:
    print("Hora de almorzar")
elif 18 <= horas_minutos <= 19:
    print("Hora de cenar")
else:
    pass
#PROBLEMA 9
print("PROBLEMA 9")
lista= ["Di", "buen","dia","a", "papa"]
lista.reverse()
print(lista)
#PROBLEMA 10
print("PROBLEMA 10")
lista_muestra=["Rojo","Verde","Blanco","Negro","Rosa","Amarillo"]
del lista_muestra[5]
del lista_muestra[4]
del lista_muestra[0]
#del lista_muestra[int(input("posicion a eliminar: "))]
#del lista_muestra[int(input("posicion a eliminar: "))]
#del lista_muestra[int(input("posicion a eliminar: "))]
print(lista_muestra)
#PROBLEMA 11
print("PROBLEMA 11")
lista_orig=[1,1,2,3,4,4,5,1]
conjunto=set(lista_orig)
lista_procesada=list(conjunto)
print(lista_procesada)
#PROBLEMA 12
print("PROBLEMA 12")
nombre_archivo=input("ingrese nombre del archivo: ").lower()
nombre,extension=nombre_archivo.split(".")
if extension == "gif":
    print("image/gif")
elif extension == "jpg" or extension == "jpeg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")