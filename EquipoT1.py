import random

class Equipo: 
    def __init__(self, nombre = "", partidosGanados = 0, partidosPerdidos = 0, setGanados = 0):
        self._nombre = nombre
        self._partidosGanados = partidosGanados
        self._partidosPerdidos = partidosPerdidos
        self._setGanados = setGanados #/

def RegistraSet(equipo):
    global equipo1, equipo2

    if equipo == 1: 
        equipo1._setGanados += 1 
        if equipo1._setGanados == 3:
            equipo1._partidosGanados += 1
            equipo2._partidosPerdidos += 1
            equipo1._setGanados = 0
            equipo2._setGanados = 0
    elif equipo == 2:
        equipo2._setGanados += 1
        if equipo2._setGanados == 3:
            equipo2._partidosGanados += 1
            equipo1._partidosPerdidos += 1
            equipo1._setGanados = 0
            equipo2._setGanados = 0

def Puntos(): 
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    global equipo1, equipo2
    while equipo1._setGanados < 2 and equipo2._setGanados < 2: #  números mayor a 3 no para 
        puntos1 = Puntos()
        puntos2 = Puntos()

        while (puntos1 < 25 and puntos2 < 25) or puntos1 == puntos2:
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()

        print(f"Set - {equipo1._nombre}: {puntos1} | {equipo2._nombre}: {puntos2}")

        if puntos1 >= 25 and puntos1 > puntos2:
            RegistraSet(1)
        elif puntos2 >= 25 and puntos2 > puntos1:
            RegistraSet(2)

def ResultadoTorneo():
    global equipo1, equipo2
    print("\nResultado del Torneo:")
    print(equipo1._nombre, "- Ganados:", equipo1._partidosGanados, "Perdidos:", equipo1._partidosPerdidos)
    print(equipo2._nombre, "- Ganados:", equipo2._partidosGanados, "Perdidos:", equipo2._partidosPerdidos)

print("¿Cuántos partidos deben jugar los equipos?")
n = int(input())
a = input("Nombre del 1er equipo: ")
b = input("Nombre del 2do equipo: ")

equipo1 = Equipo(a)
equipo2 = Equipo(b)

for i in range(n):
    print("\nPartido", i + 1)
    JugarPartido()

ResultadoTorneo()
