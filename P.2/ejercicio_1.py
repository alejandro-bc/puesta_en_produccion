#!/usr/bin/env python3

ans = 0
print("Calculadora con operaciones: ADD, SUB, MUL, DIV")
print("Ejemplos: ADD 26 16   o   MUL ANS 2")
print("Escribe EXIT para salir")

while True:
    texto = input("> ").strip()
    if texto.upper() == "EXIT":
        break

    partes = texto.split()

    # Validar que haya 3 partes
    if len(partes) != 3:
        print("Error: formato inválido. Usa OPERACIÓN NUMERO NUMERO")
        continue

    op, a_str, b_str = partes

    # Validar que los operandos sean números o ANS
    if a_str.upper() == "ANS":
        x = ans
    elif a_str.replace('.', '', 1).isdigit() or (a_str.startswith('-') and a_str[1:].replace('.', '', 1).isdigit()):
        x = float(a_str)
    else:
        print("Error: primer operando inválido")
        continue

    if b_str.upper() == "ANS":
        y = ans
    elif b_str.replace('.', '', 1).isdigit() or (b_str.startswith('-') and b_str[1:].replace('.', '', 1).isdigit()):
        y = float(b_str)
    else:
        print("Error: segundo operando inválido")
        continue

    # Realizar operación
    op_upper = op.upper()
    if op_upper == "ADD":
        ans = x + y
    elif op_upper == "SUB":
        ans = x - y
    elif op_upper == "MUL":
        ans = x * y
    elif op_upper == "DIV":
        if y == 0:
            print("No puedo dividir por 0")
            continue
        ans = x / y
    else:
        print("Operación no válida. Usa ADD, SUB, MUL o DIV")
        continue

    print("=", ans)
