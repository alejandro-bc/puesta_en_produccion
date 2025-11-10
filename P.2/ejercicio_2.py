# Ejercicio 2 
#Crea un contador de palabras. Pasado un texto debe contar el número de palabras que contiene.
#A continuación, se deber añadir una palabra clave para ver el número de ocurrencias de dicha
#palabra en el texto.

# Pedir el texto
texto = input("Escribe un texto: ")
palabras = texto.split()
total = len(palabras)
print(f"Total de palabras: {total}")

# Buscar una palabra (opcional)
palabra = input("¿Qué palabra quieres buscar? (Enter para terminar): ")
if palabra:
    veces = palabras.count(palabra)
    print(f"La palabra '{palabra}' aparece {veces} veces")