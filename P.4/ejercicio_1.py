def agregar_moneda(tasas, moneda, factor):
    """
    Crea una nueva moneda con su factor de conversión
    """
    if moneda in tasas:
        return False
    tasas[moneda] = factor
    return True

def modificar_factor(tasas, moneda, nuevo_factor):
    """
    Modifica el factor de conversión de una moneda existente
    """
    if moneda not in tasas:
        return False
    tasas[moneda] = nuevo_factor
    return True

def eliminar_moneda(tasas, moneda):
    """
    Elimina una moneda y su tasa de conversión
    """
    if moneda not in tasas:
        return False
    del tasas[moneda]
    return True

def mostrar_factores(tasas):
    """
    Muestra todos los factores de conversión de forma ordenada
    """
    print("\nFactores de conversión disponibles:")
    print("-" * 35)
    print(f"{'Moneda':<15}Factor de conversión")
    print("-" * 35)
    for moneda in sorted(tasas.keys()):
        print(f"{moneda:<15}{tasas[moneda]:.4f}")

def convertir_cantidad(cantidad, moneda_origen, moneda_destino, tasas):
    """
    Convierte una cantidad de una moneda a otra
    """
    if moneda_origen not in tasas or moneda_destino not in tasas:
        return None
    
    # Convertir a EUR primero (si no es EUR)
    if moneda_origen != "EUR":
        cantidad_eur = cantidad / tasas[moneda_origen]
    else:
        cantidad_eur = cantidad
    
    # Convertir de EUR a la moneda destino
    if moneda_destino != "EUR":
        cantidad_final = cantidad_eur * tasas[moneda_destino]
    else:
        cantidad_final = cantidad_eur
    
    return cantidad_final

def main():
    # Diccionario con los factores de conversión (1 EUR = X unidades de otra moneda)
    tasas_conversion = {
        "EUR": 1.0,
        "USD": 1.18,
        "GBP": 0.86,
        "JPY": 130.0,
        "CHF": 1.08
    }
    
    while True:
        print("\n=== Conversor de Divisas ===")
        print("1. Convertir cantidad")
        print("2. Agregar nueva moneda")
        print("3. Modificar factor de conversión")
        print("4. Eliminar moneda")
        print("5. Mostrar factores de conversión")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == "1":
            cantidad = float(input("Introduce la cantidad: "))
            moneda_origen = input("Introduce la moneda de origen: ").upper()
            moneda_destino = input("Introduce la moneda de destino: ").upper()
            
            resultado = convertir_cantidad(cantidad, moneda_origen, moneda_destino, tasas_conversion)
            if resultado is not None:
                print(f"\n{cantidad:.2f} {moneda_origen} = {resultado:.2f} {moneda_destino}")
            else:
                print("\nError: Una o ambas monedas no existen en el sistema.")
        
        elif opcion == "2":
            moneda = input("Introduce el código de la nueva moneda: ").upper()
            try:
                factor = float(input("Introduce el factor de conversión respecto al EUR: "))
                if agregar_moneda(tasas_conversion, moneda, factor):
                    print(f"\nMoneda {moneda} agregada exitosamente.")
                else:
                    print(f"\nError: La moneda {moneda} ya existe.")
            except ValueError:
                print("\nError: El factor debe ser un número válido.")
        
        elif opcion == "3":
            moneda = input("Introduce el código de la moneda a modificar: ").upper()
            try:
                nuevo_factor = float(input("Introduce el nuevo factor de conversión: "))
                if modificar_factor(tasas_conversion, moneda, nuevo_factor):
                    print(f"\nFactor de conversión de {moneda} modificado exitosamente.")
                else:
                    print(f"\nError: La moneda {moneda} no existe.")
            except ValueError:
                print("\nError: El factor debe ser un número válido.")
        
        elif opcion == "4":
            moneda = input("Introduce el código de la moneda a eliminar: ").upper()
            if moneda == "EUR":
                print("\nError: No se puede eliminar el EUR del sistema.")
            elif eliminar_moneda(tasas_conversion, moneda):
                print(f"\nMoneda {moneda} eliminada exitosamente.")
            else:
                print(f"\nError: La moneda {moneda} no existe.")
        
        elif opcion == "5":
            mostrar_factores(tasas_conversion)
        
        elif opcion == "6":
            print("\n¡Gracias por usar el conversor de divisas!")
            break
        
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()

