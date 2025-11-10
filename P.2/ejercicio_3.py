#!/usr/bin/env python3

entrada = input("Número para calcular factorial: ").strip()

# Validar que sea un número entero
if not (entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit())):
    print("Entrada no válida - usa un número entero")
else:
    n = int(entrada)
    if n < 0:
        print("El número debe ser positivo")
    else:
        # Calcular factorial
        f = 1
        for i in range(1, n + 1):
            f *= i

        # Contar ceros al final
        ceros = 0
        num_str = str(f)
        for d in reversed(num_str):
            if d != '0':
                break
            ceros += 1

        # Mostrar resultado
        print(f"factorial({n}) = {f}")
        if ceros == 1:
            print("Tiene 1 cero al final")
        else:
            print(f"Tiene {ceros} ceros al final")
