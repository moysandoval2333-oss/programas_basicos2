print("--- Calculadora de Precios con Descuento ---")

# Solicitar el precio original
precio_original = float(input("Ingresa el precio total de la compra: "))

# Determinar el porcentaje de descuento según el rango
if precio_original <= 100:
    porcentaje = 5    # 5% de descuento hasta 100
elif precio_original <= 200:
    porcentaje = 10   # 10% de descuento entre 101 y 200
elif precio_original <= 500:
    porcentaje = 15   # 15% de descuento entre 201 y 500
else:
    porcentaje = 20   # 20% de descuento para más de 500

# Calcular el monto descontado y el precio final
descuento = precio_original * (porcentaje / 100)
precio_final = precio_original - descuento

# Mostrar los resultados
print(f"Descuento aplicado: {porcentaje}% (-${descuento:.2f})")
print(f"Total a pagar: ${precio_final:.2f}")
