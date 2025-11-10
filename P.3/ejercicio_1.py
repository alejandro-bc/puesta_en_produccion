# Ejercicio 1
# Copia y modifica la calculadora (Ejercicio 1 de los tipos de texto) para que admita
# operaciones con un número variable de operandos (Ej. ADD 2 3 5 8). Añade una operación
# unaria, como SQRT (raíz cuadrada). Además, utiliza diccionarios para almacenar las
# operaciones.

from math import sqrt

# Diccionario de operaciones
ops = {
    'ADD': sum,                     # suma todos los números
    'MUL': lambda nums: nums[0] if len(nums) == 1 else nums[0] * ops['MUL'](nums[1:]),  # multiplicación
    'SUB': lambda nums: nums[0] if len(nums) == 1 else nums[0] - sum(nums[1:]),  # resta todo del primero
    'DIV': lambda nums: nums[0] if len(nums) == 1 else nums[0] / ops['MUL'](nums[1:]),  # divide el primero entre el resto
    'SQRT': lambda nums: sqrt(nums[0])  # raíz cuadrada (solo primer número)
}

ans = 0
print("Operaciones: ADD, SUB, MUL, DIV, SQRT")
print("Ejemplos: ADD 2 3 4, MUL 2 3, SQRT 16")

while True:
    try:
        texto = input("> ")
        if texto.upper() == "EXIT":
            break
            
        # Separar operación y números
        partes = texto.split()
        op = partes[0].upper()
        
        # Convertir números (usar ANS si aparece)
        nums = []
        for n in partes[1:]:
            if n.upper() == "ANS":
                nums.append(ans)
            else:
                nums.append(float(n))
        
        # Verificar operación
        if op not in ops:
            print("Operación no válida")
            continue
            
        # SQRT necesita exactamente 1 número
        if op == "SQRT" and len(nums) != 1:
            print("SQRT necesita solo un número")
            continue
            
        # Calcular
        if len(nums) == 0:
            print("Necesito al menos un número")
            continue
            
        ans = ops[op](nums)
        print("=", ans)
        
    except ValueError:
        print("Error en los números")
    except ZeroDivisionError:
        print("No puedo dividir por 0")
    except:
        print("Error en la operación")