import random
from jugador import Jugador
from ahorcado import Ahorcado

class GestorDeJuego:
    def __init__(self):
        self.jugadores = {}

    def jugar_partida(self, nombre_jugador):
        if nombre_jugador not in self.jugadores:
            self.jugadores[nombre_jugador] = Jugador(nombre_jugador)
        jugador = self.jugadores[nombre_jugador]
        palabra = self.elegir_palabra()
        juego = Ahorcado(palabra)
        juego.jugar(jugador)
        self.mostrar_puntajes()

    def mostrar_puntajes(self):
        print("\nPuntajes de los jugadores:")
        for nombre, jugador in self.jugadores.items():
            print(f"{nombre}: {jugador.puntos} puntos")

    def elegir_palabra(self):
        palabras = ['python', 'programacion', 'desarrollador', 'ahorcado', 'computadora']
        return random.choice(palabras)
