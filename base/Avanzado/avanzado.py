class Jugador:
    def __init__(self, id_jugador, nombre, edad):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.edad = edad
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.puntos_a_favor = 0

    def registro_victoria(self):
        self.partidos_jugados += 1
        self.partidos_ganados += 1
        self.puntos_a_favor += 2

    def registro_derrota(self):
        self.partidos_jugados += 1
        self.partidos_perdidos += 1

    def calcular_puntos_a_favor(self, puntos_realizados, puntos_recibidos):
        self.puntos_a_favor += puntos_realizados - puntos_recibidos

    def __str__(self):
        return f"{self.id_jugador} {self.nombre} {self.partidos_jugados} {self.partidos_ganados} {self.partidos_perdidos} {self.puntos_a_favor}"


class TorneoMesaDeTenis:
    def __init__(self):
        self.jugadores_novatos = []
        self.jugadores_intermedios = []
        self.jugadores_avanzados = []

    def registrar_jugador(self, categoria, id_jugador, nombre, edad):
        if categoria == "Novato" and 15 <= edad <= 16:
            self.jugadores_novatos.append(Jugador(id_jugador, nombre, edad))
        elif categoria == "Intermedio" and 17 <= edad <= 20:
            self.jugadores_intermedios.append(Jugador(id_jugador, nombre, edad))
        elif categoria == "Avanzado" and edad > 20:
            self.jugadores_avanzados.append(Jugador(id_jugador, nombre, edad))
        else:
            print("El jugador no cumple con los requisitos de edad para la categoría especificada.")

    def iniciar_juegos(self, categoria):
        if categoria == "Novato" and len(self.jugadores_novatos) >= 5:
            print("Iniciando juegos en la categoría Novato.")
        elif categoria == "Intermedio" and len(self.jugadores_intermedios) >= 5:
            print("Iniciando juegos en la categoría Intermedio.")
        elif categoria == "Avanzado" and len(self.jugadores_avanzados) >= 5:
            print("Iniciando juegos en la categoría Avanzado.")
        else:
            print("No hay suficientes jugadores inscritos en esta categoría para iniciar los juegos.")

    def obtener_ganador_categoria(self, categoria):
        jugadores = getattr(self, f"jugadores_{categoria.lower()}s")

        if len(jugadores) >= 2:
            ganador = max(jugadores, key=lambda jugador: jugador.puntos_a_favor)
            print(f"Ganador de la categoría {categoria}: {ganador.nombre} con {ganador.puntos_a_favor} puntos a favor.")
        else:
            print("No hay suficientes jugadores para determinar un ganador en esta categoría.")


def main():
    torneo = TorneoMesaDeTenis()

    while True:
        categoria = input("Ingrese la categoría del jugador (Novato/Intermedio/Avanzado): ").capitalize()
        id_jugador = int(input("Ingrese el ID del jugador: "))
        nombre = input("Ingrese el nombre del jugador: ")
        edad = int(input("Ingrese la edad del jugador: "))
        
        torneo.registrar_jugador(categoria, id_jugador, nombre, edad)

        continuar = input("¿Desea registrar otro jugador? (S/N): ").upper()
        if continuar != 'S':
            break

    categoria_juegos = input("Ingrese la categoría en la que desea iniciar los juegos: ").capitalize()
    torneo.iniciar_juegos(categoria_juegos)

    categoria_ganador = input("Ingrese la categoría de la que desea obtener el ganador: ").capitalize()
    torneo.obtener_ganador_categoria(categoria_ganador)


if __name__ == "__main__":
    main()
