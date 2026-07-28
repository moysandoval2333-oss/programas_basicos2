# 1. Calificaciones finales
print("--- Calculadora de Calificaciones ---")

# Solicitar las notas al usuario
parciales = float(input("Ingresa la calificación de parciales (0-100): "))
proyecto = float(input("Ingresa la calificación del proyecto (0-100): "))
examen = float(input("Ingresa la calificación del examen (0-100): "))

# Calcular el porcentaje de cada elemento
nota_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)

# Mostrar el resultado
print("Tu calificación final es:", nota_final)
