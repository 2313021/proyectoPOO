from gestor_de_juego import GestorDeJuego

if __name__ == "__main__":
    gestor_de_juego = GestorDeJuego()
    while True:
        print("\n--- Menú ---")
        print("1. Jugar una partida")
        print("2. Ver lista de jugadores y puntajes")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_jugador = input("Introduce el nombre del jugador: ")
            gestor_de_juego.jugar_partida(nombre_jugador)
        elif opcion == "2":
            gestor_de_juego.mostrar_puntajes()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del menú.")
