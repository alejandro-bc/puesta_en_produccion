# Ejercicio 4 
# Crea un programa que compruebe si una frase es palíndromo. Intenta normalizar lo máximo que
# puedas el texto, eliminando todo carácter no alfanumérico. Por ejemplo:
# • “Ateo por Arabia, iba raro poeta” debería quedar así: “ateoporarabiaibararopoeta”

from unidecode import unidecode

texto = input("Escribe una frase: ")

limpio = ""
for c in unidecode(texto.lower()):
    if c.isalpha():  # solo letras
        limpio += c

es_palindromo = limpio == limpio[::-1]

print(f"\nTexto original: {texto}")
print(f"Texto limpio: {limpio}")
print()
if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
