# Ejercicio 1
#Copia y modifica la calculadora (Ejercicio 2 de los tipos numéricos) para que acepte las
#operaciones de la siguiente forma:
#“ADD 26 16”,
#“MUL ANS 2”

ans = 0
print("Escribe operaciones como: ADD 26 16 o MUL ANS 2")
print("Operaciones: ADD, SUB, MUL, DIV")

while True:
    try:
        texto = input("> ")
        if texto.upper() == "EXIT":
            break
            
        partes = texto.split()
        op = partes[0]
        
        # Ver si usar ANS o el número
        if partes[1].upper() == "ANS":
            x = ans
        else:
            x = float(partes[1])
            
        if partes[2].upper() == "ANS":
            y = ans
        else:
            y = float(partes[2])
        
        if op.upper() == "ADD": ans = x + y
        elif op.upper() == "SUB": ans = x - y
        elif op.upper() == "MUL": ans = x * y
        elif op.upper() == "DIV": 
            if y == 0:
                print("No puedo dividir por 0")
                continue
            ans = x / y
        else:
            print("Operación no válida")
            continue
            
        print("=", ans)
        
    except ValueError:
        print("Error: usa OPERACIÓN NÚMERO NÚMERO")
    except:
        print("Error en la operación")