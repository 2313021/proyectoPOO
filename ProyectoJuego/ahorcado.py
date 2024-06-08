import random
from jugador import Jugador

class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.progreso_palabra = "_" * len(palabra)
        self.adivinada = False
        self.letras_adivinadas = []
        self.palabras_adivinadas = []
        self.intentos = 6

    def mostrar_ahorcado(self):
        etapas = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      
               |      
               |    
               |      
               |     
               -
            """
        ]
        return etapas[self.intentos]

    def adivinar(self, adivinanza):
        if len(adivinanza) == 1 and adivinanza.isalpha():
            if adivinanza in self.letras_adivinadas:
                print("Ya adivinaste la letra", adivinanza)
            elif adivinanza not in self.palabra:
                print(adivinanza, "no está en la palabra.")
                self.intentos -= 1
                self.letras_adivinadas.append(adivinanza)
            else:
                print("¡Buen trabajo,", adivinanza, "está en la palabra!")
                self.letras_adivinadas.append(adivinanza)
                lista_palabra = list(self.progreso_palabra)
                indices = [i for i, letra in enumerate(self.palabra) if letra == adivinanza]
                for indice in indices:
                    lista_palabra[indice] = adivinanza
                self.progreso_palabra = ''.join(lista_palabra)
                if "_" not in self.progreso_palabra:
                    self.adivinada = True
        elif len(adivinanza) == len(self.palabra) and adivinanza.isalpha():
            if adivinanza in self.palabras_adivinadas:
                print("Ya adivinaste la palabra", adivinanza)
            elif adivinanza != self.palabra:
                print(adivinanza, "no es la palabra.")
                self.intentos -= 1
                self.palabras_adivinadas.append(adivinanza)
            else:
                self.adivinada = True
                self.progreso_palabra = self.palabra
        else:
            print("Adivinanza no válida.")

    def jugar(self, jugador):
        print("¡Vamos a jugar al Ahorcado!")
        print(self.mostrar_ahorcado())
        print(self.progreso_palabra)
        print("\n")

        while not self.adivinada and self.intentos > 0:
            adivinanza = input("Adivina una letra o palabra: ").lower()
            self.adivinar(adivinanza)
            print(self.mostrar_ahorcado())
            print(self.progreso_palabra)
            print("\n")

        if self.adivinada:
            print("¡Felicidades, adivinaste la palabra! ¡Ganaste!")
            jugador.agregar_puntos(10)
        else:
            print(f"Lo siento, te quedaste sin intentos. La palabra era {self.palabra}. ¡Quizás la próxima vez!")
