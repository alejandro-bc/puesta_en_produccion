#Ejercicio 2
#Una calculadora que pida operaciones al usuario: ADD, SUB, MUL, DIV, EXIT. Si el usuario no ha
#introducido el comando QUIT, solicita 2 números a los que aplica la operación (en el caso de DIV,
#el primer número es el numerador y el segundo el denominador). Mejora opcional, usar ‘ANS’ para
#referirse a cualquiera de los 2 operandos para reutilizar el resultado de la operación anterior

resultado_anterior = 0
while True:
    operacion = input("Introduce la operación (ADD, SUB, MUL, DIV) o EXIT para salir: ").upper()
    if operacion == "EXIT":
        print("Saliendo de la calculadora.")
        break
    num1_input = input("Introduce el primer número (o 'ANS' para usar el resultado anterior): ")
    num2_input = input("Introduce el segundo número (o 'ANS' para usar el resultado anterior): ")
    
    if num1_input.strip().upper() == 'ANS':
        num1 = resultado_anterior
    else:
        # Verificar si es un número válido
        num1 = float(num1_input.strip())

    if num2_input.strip().upper() == 'ANS':
        num2 = resultado_anterior
    else:
        # Verificar si es un número válido
        num2_input = num2_input.strip()
        if num2_input.replace(".", "").replace("-", "").isdigit():
            num2 = float(num2_input)
        else:
            print("Número 2 no válido.")
            continue

    if operacion == "ADD":
        resultado_anterior = num1 + num2
    elif operacion == "SUB":
        resultado_anterior = num1 - num2
    elif operacion == "MUL":
        resultado_anterior = num1 * num2
    elif operacion == "DIV":
        if num2 != 0:
            resultado_anterior = num1 / num2
        else:
            print("Error: División por cero.")
            continue
    else:
        print("Operación no válida.")
        continue
    
    print("Resultado: ", resultado_anterior)