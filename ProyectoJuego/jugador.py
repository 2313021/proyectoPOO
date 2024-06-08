class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def agregar_puntos(self, puntos):
        self.puntos += puntos
