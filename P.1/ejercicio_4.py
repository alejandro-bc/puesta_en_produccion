# Ejercicio 4 - Conversor de divisas sencillo
# Monedas soportadas: USD, EUR, GBP, CAD, JPY

divisas = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'CAD': 1.25, 'JPY': 110.0}

origen = input('Divisa origen (USD, EUR, GBP, CAD, JPY): ').strip().upper()
if origen not in divisas:
    print('Divisa de origen no soportada:', origen)
else:
    destino = input('Divisa destino (USD, EUR, GBP, CAD, JPY): ').strip().upper()
    if destino not in divisas:
        print('Divisa de destino no soportada:', destino)
    else:
        cantidad_text = input('Cantidad a convertir: ').strip()
        try:
            cantidad = float(cantidad_text)
        except Exception:
            print('Cantidad no válida:', cantidad_text)
        else:
            # Convertimos pasando por USD como referencia
            cantidad_en_usd = cantidad / divisas[origen]
            resultado = cantidad_en_usd * divisas[destino]
            print(f'{cantidad} {origen} = {resultado} {destino}')
