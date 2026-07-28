try:
    # Solicita la edad y la convierte a número entero
    edad = int(input("Introduce tu edad: "))

    # Validación de entradas: comprueba que no sea una edad imposible o negativa
    if edad < 0 or edad > 120:
        print("Error: La edad introducida no es válida.")
    # Verifica la mayoría de edad
    elif edad >= 18:
        print("Tienes edad legal para votar.")
    else:
        print("No tienes la edad mínima para votar.")

except ValueError:
    # Manejo de opciones inválidas si el usuario introduce texto en vez de números
    print("Error: Por favor, introduce un número entero válido.")
