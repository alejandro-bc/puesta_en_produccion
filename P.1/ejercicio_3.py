#Ejercicio 3
#Calculadora de edad. Usando el módulo ‘datetime’. El usuario introduce su fecha de nacimiento y el
#método calcula su edad. A tener en cuenta:
#• Año actual – Año de nacimiento = edad
#• Si Mes actual < Mes nacimiento: edad – 1
#• Sino, si Mes actual = mes nacimiento
#◦ Si Día actual < Día nacimiento: edad – 1

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year

    if (hoy.month < fecha_nacimiento.month) or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
        edad -= 1

    return edad

fecha_str = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
edad = calcular_edad(fecha_nacimiento)
print(f"Tienes {edad} años.")
