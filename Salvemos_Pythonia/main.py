from personajes import Guerrero, Mago, Asesino, Clerigo
from db import init_db, guardar_partida, cargar_partida, listar_jugadores, obtener_monstruo_aleatorio
from combate import combatir

def elegir_tipo_personaje():
    print("\nElige el tipo de héroe:")
    print("1. Guerrero (vida alta, ataque medio, defensa alta)")
    print("2. Mago (vida baja, ataque alto, defensa baja)")
    print("3. Asesino (vida media, ataque alto, defensa baja)")
    print("4. Clérigo (vida media, ataque medio, defensa media)")

    while True:
        opcion = input("Selecciona un número: ")
        if opcion == "1":
            return Guerrero
        elif opcion == "2":
            return Mago
        elif opcion == "3":
            return Asesino
        elif opcion == "4":
            return Clerigo
        else:
            print("Opción inválida, intenta de nuevo.")

def crear_personajes_minimos():
    personajes = []
    print("Debes crear al menos 3 personajes para comenzar:")
    while len(personajes) < 3:
        nombre = input(f"Nombre del personaje {len(personajes)+1}: ")
        tipo_clase = elegir_tipo_personaje()
        personaje = tipo_clase(nombre)
        personaje.tipo = tipo_clase.__name__  # Guardamos el tipo como string
        personajes.append(personaje)
    return personajes

def elegir_personaje(personajes):
    print("\nElige el personaje con el que quieres jugar:")
    for i, pj in enumerate(personajes):
        print(f"{i+1}. {pj.nombre} ({pj.tipo}) Nivel {pj.nivel}")
    while True:
        opcion = input("Selecciona un número: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(personajes):
            return personajes[int(opcion)-1]
        else:
            print("Opción inválida.")

def seleccionar_jugador():
    jugadores = listar_jugadores()
    print("\nPartidas disponibles:")
    for i, nombre in enumerate(jugadores):
        print(f"{i+1}. {nombre}")
    print(f"{len(jugadores)+1}. Crear nueva partida")
    while True:
        opcion = input("Selecciona un número: ")
        if opcion.isdigit():
            idx = int(opcion)
            if 1 <= idx <= len(jugadores):
                return jugadores[idx-1]
            elif idx == len(jugadores)+1:
                nombre = input("Introduce el nombre para la nueva partida: ")
                return nombre
        print("Opción inválida.")

def main():
    init_db()
    jugador_nombre = seleccionar_jugador()
    personajes = cargar_partida(jugador_nombre)
    if personajes:
        print(f"¡Bienvenido de nuevo, {jugador_nombre}! Hay {len(personajes)} personajes guardados.")
    else:
        personajes = crear_personajes_minimos()
        guardar_partida(jugador_nombre, personajes)
        print(f"\n¡Bienvenido, {jugador_nombre}! Partida creada.")
    while True:
        print(f"\nJugador actual: {jugador_nombre}")
        for pj in personajes:
            pj.mostrar_stats()
        print("1. Buscar combate")
        print("2. Guardar partida")
        print("3. Cambiar de jugador")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            monstruo = obtener_monstruo_aleatorio()
            if monstruo:
                combatir(personajes)
            else:
                print("No hay monstruos disponibles en la base de datos.")
        elif opcion == "2":
            guardar_partida(jugador_nombre, personajes)
            print("Partida guardada.")
        elif opcion == "3":
            jugador_nombre = seleccionar_jugador()
            personajes = cargar_partida(jugador_nombre)
            if not personajes:
                personajes = crear_personajes_minimos()
                guardar_partida(jugador_nombre, personajes)
        elif opcion == "4":
            print("Saliendo del juego...")
            break
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    main()
