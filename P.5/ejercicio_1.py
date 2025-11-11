# Ejercicio 1
# Modifica la calculadora (Ejercicio 1 de colecciones) para evitar que se interrumpa su ejecución tras
# un uso erróneo. Captura las siguientes excepciones:
# - ValueError: Cuando se introduce un operando no numérico
# - ZeroDivisionError: Cuando se intenta dividir entre cero
# - IndexError: Si la operación no tiene suficientes operandos o tiene demasiados (sqrt)
# - KeyboardInterrupt: Si el usuario interrumpe con Ctrl + C mostrar un mensaje “amigable”
# Además, crea una excepción personalizada que se lance cuando la operación no esté definida en la
# calculadora:
# - OperaciónNoValida(Excepción)


#!/usr/bin/env python3
from math import sqrt

# Excepción personalizada
class OperacionNoValida(Exception):
    pass

# Diccionario de operaciones
ops = {
    'ADD': lambda nums: sum(nums),
    'MUL': lambda nums: nums[0] if len(nums) == 1 else nums[0] * ops['MUL'](nums[1:]),
    'SUB': lambda nums: nums[0] if len(nums) == 1 else nums[0] - sum(nums[1:]),
    'DIV': lambda nums: nums[0] if len(nums) == 1 else nums[0] / ops['MUL'](nums[1:]),
    'SQRT': lambda nums: sqrt(nums[0])
}

ans = 0
print("Calculadora robusta con operaciones: ADD, SUB, MUL, DIV, SQRT")
print("Ejemplos: ADD 2 3 4, MUL 2 3, SQRT 16")
print("Usa ANS para el último resultado y EXIT para salir")

while True:
    try:
        entrada = input("> ").strip()
        if entrada.upper() == "EXIT":
            print("¡Hasta luego!")
            break

        partes = entrada.split()
        if len(partes) == 0:
            raise IndexError("No se ingresó ninguna operación")

        op = partes[0].upper()
        if op not in ops:
            raise OperacionNoValida(f"Operación no definida: {op}")

        # Convertir operandos a números, usando ANS si corresponde
        nums = []
        for n in partes[1:]:
            if n.upper() == "ANS":
                nums.append(ans)
            else:
                try:
                    nums.append(float(n))
                except ValueError:
                    raise ValueError(f"Operando no numérico: {n}")

        # Validaciones especiales
        if op == "SQRT":
            if len(nums) != 1:
                raise IndexError("SQRT necesita exactamente un número")
            if nums[0] < 0:
                raise ValueError("No se puede calcular la raíz de un número negativo")
        if op == "DIV" and 0 in nums[1:]:
            raise ZeroDivisionError("No puedo dividir por 0")
        if len(nums) == 0:
            raise IndexError("Se necesitan operandos para la operación")

        # Calcular resultado
        ans = ops[op](nums)
        print("=", ans)

    except ValueError as ve:
        print("Error de valor:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)
    except IndexError as ie:
        print("Error de índice:", ie)
    except OperacionNoValida as onv:
        print("Error:", onv)
    except KeyboardInterrupt:
        print("\nInterrupción detectada. ¡Hasta luego!")
        break
    except Exception as e:
        print("Error inesperado:", e)
