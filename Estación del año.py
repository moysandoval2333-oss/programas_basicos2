# Solicita #solicita el nombre del mes
mes = input("Introduce el nombre del mes: ").strip().lower()

# Estructura match-case para agrupar los meses por estación
match mes:
    case "diciembre" | "enero" | "febrero":
        estacion = "Invierno"
    case "marzo" | "abril" | "mayo":
        estacion = "Primavera"
    case "junio" | "julio" | "agosto":
        estacion = "Verano"
    case "septiembre" | "octubre" | "noviembre":
        estacion = "Otoño"
    case _:
        estacion = "Desconocida (Mes no válido)"

print(f"La estación correspondiente es: {estacion}")
