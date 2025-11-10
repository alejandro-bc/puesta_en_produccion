#!/usr/bin/env python3

def es_primo(n):
    """Comprueba si un número es primo"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def posicion_primo(n):
    """Encuentra la posición del número primo n dentro de la secuencia de primos"""
    if not es_primo(n):
        return -1
    
    posicion = 1
    for i in range(2, n):
        if es_primo(i):
            posicion += 1
    return posicion

def descomponer_en_primos(n):
    """Descompone un número en sus factores primos"""
    factores = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factores.append(n)
            break
    return factores

def main():
    while True:
        entrada = input("\nIntroduce un número (o 'EXIT' para salir): ").strip()
        if entrada.upper() == "EXIT":
            print("\n¡Hasta luego!")
            break

        # Validar que sea un número entero
        if not (entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit())):
            print("Error: Por favor, introduce un número válido o 'EXIT' para salir.")
            continue

        numero = int(entrada)

        if numero < 1:
            print("Por favor, introduce un número positivo mayor que 0.")
            continue

        if es_primo(numero):
            pos = posicion_primo(numero)
            print(f"\n{numero} ES un número primo.")
            print(f"Es el {pos}º número primo.")
        else:
            factores = descomponer_en_primos(numero)
            print(f"\n{numero} NO es un número primo.")
            print("Su descomposición en factores primos es:", end=" ")
            print(" × ".join(map(str, factores)), end=" ")
            print(f"= {numero}")

if __name__ == "__main__":
    main()
