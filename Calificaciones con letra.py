try:
    # Solicita la nota al usuario
    nota = float(input("Introduce la calificación (0 a 100): "))

    # 1. Validar entradas (Rango correcto de notas)
    if nota < 0 or nota > 100:
        print("Error: La calificación debe estar entre 0 y 100.")
    
    # 2. Asignación de letras según el puntaje
    elif nota >= 90:
        print("Tu calificación es: A")
    elif nota >= 80:
        print("Tu calificación es: B")
    elif nota >= 70:
        print("Tu calificación es: C")
    elif nota >= 60:
        print("Tu calificación es: D")
    else:
        print("Tu calificación es: F")

except ValueError:
    # Manejar opciones inválidas (si ingresan texto o símbolos)
    print("Error: Por favor, introduce un número válido.")
