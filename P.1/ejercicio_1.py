#Ejercicio 1 
#Adivinar número aleatorio. Usando el módulo ‘random’, método ‘randint’. Se calcula un número
#aleatorio entre 0 y n y se solicita al usuario que introduzca números hasta que acierte el elegido,
#dando pistas sobre si el número elegido es mayor o menor que el introducido

import random

n = int(input("Introduce el valor máximo para el número aleatorio: "))
numero_aleatorio = random.randint(0, n)
adivinado = False

while not adivinado:
    intento = int(input(f"Adivina el número aleatorio entre 0 y {n}: "))
    
    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True

