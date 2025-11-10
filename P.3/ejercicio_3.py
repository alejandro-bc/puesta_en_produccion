# Ejercicio 3 - Contador de frecuencia de palabras

# Pedir texto
texto = input("Escribe un texto: ")
palabras = texto.split()

# Diccionario para contar
cuenta = {}
for p in palabras:
    if p in cuenta:
        cuenta[p] += 1
    else:
        cuenta[p] = 1

# Mostrar resultados
print(f"\nTotal palabras: {len(palabras)}")
print("\nFrecuencia de cada palabra:")
for palabra in cuenta:
    print(f"{palabra}: {cuenta[palabra]}")