# Ejercicio 5
# Calculadora de anagramas. Para un texto determinado, detecta todos los anagramas
# (palabras que tienen las mismas letras, pero en distinto orden). Por ejemplo: “acontecido” es
# anagrama de “anecdótico”, y “anecdótico” es anagrama de “acontecido”. Para eliminar los
# acentos se puede utilizar la librería no estándar “unidecode”

from unidecode import unidecode

# Pedir texto
texto = input("Escribe varias palabras: ")

# Separar palabras y quitar acentos
palabras = texto.lower().split()
palabras = [unidecode(p) for p in palabras]

# Agrupar por letras ordenadas
grupos = {}
for p in palabras:
    # Ordenar letras de la palabra
    letras = ''.join(sorted(p))
    
    # Guardar palabra en su grupo
    if letras in grupos:
        grupos[letras].append(p)
    else:
        grupos[letras] = [p]

# Mostrar anagramas
print("\nAnagramas encontrados:")
for letras in grupos:
    if len(grupos[letras]) > 1:
        print(", ".join(grupos[letras]))