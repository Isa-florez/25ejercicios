# Caja registradora que suma ventas hasta ingresar 0
total = 0

while True:
    venta = float(input("Ingrese el monto de la venta (0 para terminar): $"))
    if venta == 0:
        break
    if venta > 100000:
        print("Venta destacada")
    total += venta

print(f"Total vendido: ${total:,.2f}")
