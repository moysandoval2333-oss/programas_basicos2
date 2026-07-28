try:
    # 1. Solicitar el monto en pesos mexicanos y validar
    pesos = float(input("Introduce la cantidad en pesos mexicanos (MXN): "))
    if pesos <= 0:
        print("Error: El monto debe ser una cantidad mayor a cero.")
    else:
        # Mostrar el menú de opciones
        print("\nDivisas disponibles para conversión:")
        print("USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS")
        destino = input("Elige la moneda de destino: ").strip().upper()

        # 2. Estructura match-case para las tasas de cambio (Valores de referencia)
        match destino:
            case "USD":
                resultado = pesos * 0.050    # Dólar estadounidense
            case "EUR":
                resultado = pesos * 0.046    # Euro
            case "THB":
                resultado = pesos * 1.68     # Baht tailandés
            case "JPY":
                resultado = pesos * 7.72     # Yen japonés
            case "KRW":
                resultado = pesos * 71.50    # Won surcoreano
            case "AUD":
                resultado = pesos * 0.078    # Dólar australiano
            case "PEN":
                resultado = pesos * 0.19     # Sol peruano
            case "CAD":
                resultado = pesos * 0.070    # Dólar canadiense
            case "VES":
                resultado = pesos * 1.82     # Bolívar venezolano
            case "ARS":
                resultado = pesos * 43.10    # Peso argentino
            case _:
                resultado = None
                # Manejar opción inválida si la moneda no está en la lista
                print(f"Error: La moneda '{destino}' no está soportada.")

        # 3. Mostrar el resultado si la conversión fue exitosa
        if resultado is not None:
            print(f"\n{pesos:.2f} MXN equivalen a: {resultado:.2f} {destino}")

except ValueError:
    # Validar si el usuario introduce texto en el monto numérico
    print("Error: Por favor, introduce un número válido para el monto.")
