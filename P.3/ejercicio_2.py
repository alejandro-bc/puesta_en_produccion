# Ejercicio 2 - Conversor de divisas con diccionarios

tasas = {
    'USD': 1.0,    
    'EUR': 0.85,   
    'GBP': 0.75,   
    'JPY': 110.0,  
    'CAD': 1.25    
}

print("Conversor de divisas")
print("Monedas:", ", ".join(tasas.keys()))

while True:

    origen = input("De (moneda origen): ").upper()
    if origen == "EXIT":
        break
        
    if origen not in tasas:
        print("Moneda no válida")
        continue
        
    destino = input("A (moneda destino): ").upper()
    if destino not in tasas:
        print("Moneda no válida")
        continue
        
    try:
        cantidad = float(input("Cantidad: "))
    except:
        print("Cantidad no válida")
        continue
        

    usd = cantidad / tasas[origen]
    resultado = usd * tasas[destino]
    
    print(f"{cantidad} {origen} = {resultado} {destino}")

