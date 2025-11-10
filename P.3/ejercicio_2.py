#!/usr/bin/env python3

tasas = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0,
    'CAD': 1.25
}

print("Conversor de divisas")
print("Monedas disponibles:", ", ".join(tasas.keys()))
print("Escribe EXIT para salir")

while True:
    origen = input("De (moneda origen): ").strip().upper()
    if origen == "EXIT":
        break
    if origen not in tasas:
        print("Moneda no válida")
        continue

    destino = input("A (moneda destino): ").strip().upper()
    if destino == "EXIT":
        break
    if destino not in tasas:
        print("Moneda no válida")
        continue

    cantidad_str = input("Cantidad: ").strip()
    # Validar que sea un número
    if cantidad_str.replace('.', '', 1).isdigit() or (cantidad_str.startswith('-') and cantidad_str[1:].replace('.', '', 1).isdigit()):
        cantidad = float(cantidad_str)
    else:
        print("Cantidad no válida")
        continue

    # Conversión
    usd = cantidad / tasas[origen]
    resultado = usd * tasas[destino]

    print(f"{cantidad} {origen} = {resultado} {destino}")
