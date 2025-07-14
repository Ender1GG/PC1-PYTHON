import random
from pyfiglet import Figlet

def generar_figlet():
    figlet = Figlet()
    fuentes = figlet.getFonts()
    fuente = input(f"Elija una fuente (de lo contrario se seleccionará aleatoriamente): ")
    if not fuente:
        fuente = random.choice(fuentes)
    
    figlet.setFont(font=fuente)
    texto = input("Ingrese el texto a mostrar: ")
    print(figlet.renderText(texto))

generar_figlet()
