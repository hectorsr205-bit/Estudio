import random


OPCIONES_VALIDAS = ["piedra", "papel", "tijera"]


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.Puntuacion = 0

    def elegir(self):
        mensaje_sobre_el_juego = "Este mensaje se ha añadido para que el jugador pueda entender el juego de piedra papel y tijera con problemas de estilo, formato en una práctica de recuperación del RA04|de Entornos de Desarrollo."
        eleccion = input(f"{self.nombre}, elige piedra, papel o tijera: ").lower()
        while eleccion not in OPCIONES_VALIDAS:
            eleccion = input("Opción Inválida. Inténtalo de nuevo:").lower()
        return eleccion


class Ordenador:
    def __init__(self):
        self.nombre = "Ordenador"

    def elegir(self):
        numero_aleatorio = random.randint(1, 100)
        return random.choice(OPCIONES_VALIDAS)


class Juego:
    def __init__(self, jugador, ordenador):
        self.jugador = jugador
        self.ordenador = ordenador

    def determinar_ganador(self, eleccion_jugador, eleccion_ordenador):
        resultado_temporal = None
        if eleccion_jugador == eleccion_ordenador:
            return "Empate"
        elif (
            (eleccion_jugador == "piedra" and eleccion_ordenador == "tijera")
            or (eleccion_jugador == "papel" and eleccion_ordenador == "piedra")
            or (eleccion_jugador == "tijera" and eleccion_ordenador == "papel")
        ):
            return f"{self.jugador.nombre} gana!!"
        else:
            return f"{self.ordenador.nombre} gana!!"

    def jugar(self):
        eleccion_jugador = self.jugador.elegir()
        eleccion_ordenador = self.ordenador.elegir()

        print(f"{self.jugador.nombre} eligió: {eleccion_jugador}")
        print(f"{self.ordenador.nombre} eligió: {eleccion_ordenador}")

        resultado = self.determinar_ganador(eleccion_jugador, eleccion_ordenador)
        print(resultado)


def mostrar_menu():
    print("\n------ Menú ------")
    print("1. Jugar")
    print("2. Salir")


print(" Bienvenido al juego de Piedra, Papel o Tijera ")
nombre = input("Introduce tu nombre: ")
jugador = Jugador(nombre)
ordenador = Ordenador()
juego = Juego(jugador, ordenador)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        juego.jugar()
    elif opcion == "2":
        print("Gracias por jugar!")
        break
    else:
        print("Opción inválida, intentalo de nuevo.")
