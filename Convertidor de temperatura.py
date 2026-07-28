def convertidor_temperatura():
    print("=== CONVERTIDOR DE TEMPERATURA ===")
    
    try:
        # 1. Solicitar la temperatura base en Celsius
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        
        # 2. Mostrar el menú de opciones de conversión
        print("\n¿A qué unidad deseas convertir?")
        print("F -> Fahrenheit")
        print("K -> Kelvin")
        opcion = input("Elige una opción (F / K): ").strip().upper()
        
        # 3. Aplicar match-case según la elección del usuario
        match opcion:
            case "F":
                fahrenheit = (celsius * 9/5) + 32
                print(f"\nResultado: {celsius}°C es igual a {fahrenheit:.2f}°F")
                
            case "K":
                kelvin = celsius + 273.15
                print(f"\nResultado: {celsius}°C es igual a {kelvin:.2f} K")
                
            case _:
                print("\nError: Opción no válida. Debes elegir 'F' o 'K'.")
                
    except ValueError:
        print("\nError: Por favor, introduce un número válido para la temperatura.")

# Llamar a la función para ejecutar el programa
convertidor_temperatura()
              
