from personajes import Jugador
from monstruos import generar_monstruo
import random

def combatir(personajes):
    # Elegir número de monstruos en la horda
    while True:
        try:
            n_monstruos = int(input("¿Cuántos monstruos quieres enfrentar en la horda? (1-5): "))
            if 1 <= n_monstruos <= 5:
                break
            else:
                print("Elige un número entre 1 y 5.")
        except ValueError:
            print("Introduce un número válido.")

    monstruos = [generar_monstruo() for _ in range(n_monstruos)]
    monstruos = [m for m in monstruos if m is not None]
    if not monstruos:
        print("No hay monstruos disponibles para combatir.")
        return

    print(f"\n¡Aparecen {len(monstruos)} monstruos!")
    for i, m in enumerate(monstruos):
        print(f"{i+1}. {m.nombre} (Vida: {m.vida}, Ataque: {m.ataque}, Defensa: {m.defensa})")

    vivos = [pj for pj in personajes if pj.vida > 0]
    while any(m.vida > 0 for m in monstruos) and any(pj.vida > 0 for pj in personajes):
        # Turno por velocidad
        turno = sorted([*vivos, *monstruos], key=lambda x: getattr(x, 'velocidad', 0), reverse=True)
        for ente in turno:
            if isinstance(ente, Jugador) and ente.vida > 0 and any(m.vida > 0 for m in monstruos):
                print(f"\nTurno de {ente.nombre} ({ente.tipo})")
                print("Monstruos vivos:")
                for idx, m in enumerate(monstruos):
                    if m.vida > 0:
                        print(f"{idx+1}. {m.nombre} (Vida: {m.vida})")
                print("1. Atacar")
                print("2. Pasar turno")
                opcion = input("Elige una acción: ")
                if opcion == "1":
                    while True:
                        objetivo = input("¿A qué monstruo quieres atacar? (número): ")
                        if objetivo.isdigit():
                            objetivo_idx = int(objetivo) - 1
                            if 0 <= objetivo_idx < len(monstruos) and monstruos[objetivo_idx].vida > 0:
                                m = monstruos[objetivo_idx]
                                daño = max(ente.ataque - m.defensa, 1)
                                m.vida -= daño
                                print(f"{ente.nombre} hace {daño} de daño a {m.nombre}. Vida: {max(m.vida,0)}")
                                if m.vida <= 0:
                                    print(f"¡El monstruo {m.nombre} ha sido derrotado!")
                                    ente.ganar_experiencia(m.experiencia)
                                break
                            else:
                                print("Elige un monstruo válido.")
                        else:
                            print("Introduce un número.")
                elif opcion == "2":
                    print(f"{ente.nombre} pasa el turno.")
            elif hasattr(ente, "nombre") and not isinstance(ente, Jugador) and ente.vida > 0:
                # Monstruo ataca a un personaje aleatorio vivo
                objetivo = random.choice([pj for pj in personajes if pj.vida > 0])
                daño = max(ente.ataque - objetivo.defensa, 1)
                objetivo.vida -= daño
                print(f"{ente.nombre} ataca a {objetivo.nombre} y le hace {daño} de daño. Vida: {max(objetivo.vida,0)}")
                if objetivo.vida <= 0:
                    print(f"{objetivo.nombre} ha sido derrotado.")
        vivos = [pj for pj in personajes if pj.vida > 0]

    if all(pj.vida <= 0 for pj in personajes):
        print("\n💀 Todos los personajes han sido derrotados...")
    elif all(m.vida <= 0 for m in monstruos):
        print("\n¡La horda ha sido derrotada!")