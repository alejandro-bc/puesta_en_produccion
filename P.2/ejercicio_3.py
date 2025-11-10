# Ejercicio 3 
#Crea un programa que calcule el factorial de un número dado y el número de 0s que quedan a la
#derecha del número. 

try:
    n = int(input("Número para calcular factorial: "))
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
        for d in num_str[::-1]:
            if d != '0':
                break
            ceros += 1
            
        # Mostrar resultado
        print(f"factorial({n}) = {f}")
        if ceros == 1:
            print("Tiene 1 cero al final")
        else:
            print(f"Tiene {ceros} ceros al final")
except ValueError:
    print("Entrada no válida - usa un número entero")
