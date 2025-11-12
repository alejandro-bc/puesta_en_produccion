# Ejercicio 2
# Modifica el ejercicio 3 de funciones para practicar el manejo de interrupciones.
# Se evita la interrupción del programa ante errores de entrada y Ctrl+C.

def validar_dni(dni, lista_dnis):
    """Valida un DNI español"""
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni = dni.strip().upper()

    if len(dni) < 9:
        print("❌ Longitud insuficiente.")
        return False

    numeros = dni[:-1]
    letra = dni[-1]

    if not numeros.isdigit():
        print("❌ Letras en la parte numérica.")
        return False

    if not letra.isalpha():
        print("❌ Falta la letra del DNI.")
        return False

    num = int(numeros)
    if letra != letras[num % 23]:
        print("❌ Letra incorrecta.")
        return False

    if dni in lista_dnis:
        print("❌ DNI duplicado.")
        return False

    return True


def crear_identificador(nombre, dni, lista_ids):
    """Crea un identificador a partir del nombre y DNI"""
    palabras = nombre.lower().split()
    if len(palabras[0]) < 3:
        print("❌ Nombre demasiado corto para generar un identificador.")
        return None

    id_nombre = "".join(p[:2] for p in palabras)
    id_numero = dni[-4:-1]
    identificador = id_nombre + id_numero

    if identificador in lista_ids:
        print("❌ Identificador duplicado.")
        return None

    return identificador


def main():
    socios = []
    dnis = []
    ids = []

    while True:
        try:
            nombre = input("\nIntroduce el nombre completo (o 'fin' para terminar): ").strip()

            if nombre.lower() == 'fin':
                break

            # Validaciones del nombre
            if not nombre:
                raise ValueError("❌ El nombre no puede estar vacío.")
            if len(nombre.split()) < 2:
                raise ValueError("❌ Faltan apellidos.")
            if any(not (c.isalpha() or c.isspace()) for c in nombre):
                raise ValueError("❌ El nombre no puede contener símbolos o números.")

            # Validación del DNI
            dni = input("Introduce el DNI: ").strip().upper()
            if not validar_dni(dni, dnis):
                continue

            # Crear identificador
            id_socio = crear_identificador(nombre, dni, ids)
            if not id_socio:
                continue

            socios.append((id_socio, nombre, dni))
            dnis.append(dni)
            ids.append(id_socio)

            print(f"✅ Socio añadido: {nombre} ({dni}) -> ID: {id_socio}")

        except ValueError as e:
            print(e)
            continue
        except KeyboardInterrupt:
            print("\n🚫 Interrupción por teclado detectada. No se detiene el programa.")
            continue

    if socios:
        print("\nLista de socios:")
        print("ID            Nombre                           DNI")
        print("-" * 55)
        for id_socio, nombre, dni in sorted(socios):
            print(f"{id_socio:<13} {nombre:<32} {dni}")
    else:
        print("\nNo hay socios registrados.")


if __name__ == "__main__":
    main()
