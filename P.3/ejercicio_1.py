#!/usr/bin/env python3
from math import sqrt

# Diccionario de operaciones
ops = {
    'ADD': lambda nums: sum(nums),
    'MUL': lambda nums: nums[0] if len(nums) == 1 else nums[0] * ops['MUL'](nums[1:]),
    'SUB': lambda nums: nums[0] if len(nums) == 1 else nums[0] - sum(nums[1:]),
    'DIV': lambda nums: nums[0] if len(nums) == 1 else nums[0] / ops['MUL'](nums[1:]),
    'SQRT': lambda nums: sqrt(nums[0])
}

ans = 0
print("Operaciones: ADD, SUB, MUL, DIV, SQRT")
print("Ejemplos: ADD 2 3 4, MUL 2 3, SQRT 16")
print("Escribe EXIT para salir")

while True:
    texto = input("> ").strip()
    if texto.upper() == "EXIT":
        break

    partes = texto.split()
    if len(partes) == 0:
        print("No se ingresó nada")
        continue

    op = partes[0].upper()
    if op not in ops:
        print("Operación no válida")
        continue

    # Convertir números (usar ANS si aparece)
    nums = []
    error_num = False
    for n in partes[1:]:
        if n.upper() == "ANS":
            nums.append(ans)
        else:
            # Validar si es número
            if n.replace('.', '', 1).isdigit() or (n.startswith('-') and n[1:].replace('.', '', 1).isdigit()):
                nums.append(float(n))
            else:
                print(f"Operando inválido: {n}")
                error_num = True
                break
    if error_num:
        continue

    # Validaciones especiales
    if op == "SQRT":
        if len(nums) != 1:
            print("SQRT necesita exactamente un número")
            continue
        if nums[0] < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo")
            continue
    if op == "DIV" and 0 in nums[1:]:
        print("No puedo dividir por 0")
        continue
    if len(nums) == 0:
        print("Necesito al menos un número")
        continue

    # Calcular resultado
    ans = ops[op](nums)
    print("=", ans)
