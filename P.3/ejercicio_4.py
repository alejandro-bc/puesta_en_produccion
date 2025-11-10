# Ejercicio 4
# Registro de alumnos. Crea un registro que permita almacenar distinta información de
# alumnos, tal como:
# • NRE (Número Regional de Estudiante)
# • Nombre
# • Apellidos
# • Número de teléfono
# • Lista de asistencia (fecha, asiste o no)
# Crea un par de alumnos “a mano” e imprime el diccionario
# Opcional: Modifica el programa para que el usuario pueda introducir nuevos alumnos y
# registrar asistencias a través del teclado (input())

alumnos = {}

# Pedir datos
while True:
    print("\nRegistro de alumno (Enter en NRE para terminar)")
    
    nre = input("NRE: ")
    if nre == "":
        break
        
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    
    # Lista de asistencia
    asistencia = []
    fecha = input("Fecha (Enter para terminar): ")
    while fecha != "":
        presente = input("¿Asistió? (s/n): ").lower() == "s"
        asistencia.append((fecha, presente))
        fecha = input("Fecha (Enter para terminar): ")
    
    # Guardar alumno
    alumnos[nre] = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "asistencia": asistencia
    }

# Mostrar alumnos
print("\nLista de alumnos:")
for nre, datos in alumnos.items():
    print(f"\nNRE: {nre}")
    print(f"Nombre: {datos['nombre']} {datos['apellidos']}")
    print(f"Teléfono: {datos['telefono']}")
    print("Asistencia:")
    for fecha, presente in datos['asistencia']:
        asiste = "Sí"
        if not presente:
            asiste = "No"
        print(f"  {fecha}: {asiste}")