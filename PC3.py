#1
def porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                print("E")
                break
            elif porcentaje > 99:
                print("F")
                break
            else:
                print(f"{round(porcentaje)}%")
                break
        except ValueError:
            print("Error: Por favor ingrese solo numeros enteros.")
        except ZeroDivisionError as e:
            print(e)

porcentaje_combustible()
#2
def calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por coma: ")
            calificaciones = [int(cal) for cal in entrada.split(',')]
            print("Las calificaciones son:", calificaciones)
            break
        except ValueError:
            print("Error: Algunos valores no son numeros enteros, intente de nuevo.")

calificaciones()
#3
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio**2
circulo1 = Circulo(5)
circulo2 = Circulo(7)
print(f"Area del primer circulo: {circulo1.calcular_area():.2f}")
print(f"Area del segundo circulo: {circulo2.calcular_area():.2f}")
#4
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
rectangulo = Rectangulo(4, 6)
cuadrado = Cuadrado(5)
print(f"Area del rectangulo: {rectangulo.calcular_area()}")
print(f"Area del cuadrado: {cuadrado.calcular_area()}")
#5
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Numero de registro: {self.registro}")
    
    def set_age(self, edad):
        self.edad = edad
    
    def set_nota(self, nota):
        self.nota = nota
alumno = Alumno("Juan Perez", 12345)
alumno.set_age(20)
alumno.set_nota(8.5)
alumno.display()
print(f"Edad: {alumno.edad}")
print(f"Nota: {alumno.nota}")
