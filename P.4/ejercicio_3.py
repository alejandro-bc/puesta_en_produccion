def validar_dni(dni):
    """Valida un DNI español"""
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Limpiar el DNI
    dni = dni.strip().upper()
    
    # Comprobar longitud y formato básico
    if len(dni) < 8 or len(dni) > 9:
        return False
    
    # Separar números y letra
    numeros = dni[:-1]
    letra = dni[-1]
    # Comprobar que los números son válidos y la letra es correcta
    if not numeros.isdigit():
        return False

    num = int(numeros)
    return letra == letras[num % 23]

def crear_identificador(nombre, dni):
    """Crea un identificador a partir del nombre y DNI"""
    # Convertir nombre a minúsculas y dividir en palabras
    palabras = nombre.lower().split()
    # Tomar las dos primeras letras de cada palabra
    id_nombre = ""
    for palabra in palabras:
        id_nombre += palabra[:2]
    
    # Añadir los últimos 3 dígitos del DNI
    id_numero = dni[-4:-1]
    
    return id_nombre + id_numero

def main():
    socios = []  # Lista para almacenar los socios
    
    while True:
        nombre = input("\nIntroduce el nombre completo (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
            
        dni = input("Introduce el DNI: ")
        if not validar_dni(dni):
            print("DNI no válido. Inténtalo de nuevo.")
            continue
            
        # Crear y guardar el identificador
        id_socio = crear_identificador(nombre, dni)
        socios.append((id_socio, nombre, dni.upper()))
    
    # Mostrar todos los socios ordenados
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

