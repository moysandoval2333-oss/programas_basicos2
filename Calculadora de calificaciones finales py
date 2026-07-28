try:
    # 1. Solicitar las calificaciones (Escala 0-100)
    tareas = float(input("Introduce nota de Tareas (0-100): "))
    examen = float(input("Introduce nota de Examen (0-100): "))
    proyecto = float(input("Introduce nota de Proyecto (0-100): "))

    # 2. Validar que las notas estén en el rango correcto
    if (tareas < 0 or tareas > 100) or (examen < 0 or examen > 100) or (proyecto < 0 or proyecto > 100):
        print("Error: Las calificaciones deben estar entre 0 y 100.")
    else:
        # 3. Calcular el promedio ponderado (Ejemplo: Tareas 30%, Examen 40%, Proyecto 30%)
        nota_final = (tareas * 0.30) + (examen * 0.40) + (proyecto * 0.30)
        
        print(f"\nTu calificación final es: {nota_final:.2f}")

except ValueError:
    # Manejar si el usuario introduce texto en lugar de números
    print("Error: Por favor, introduce solo números válidos.")
