# Conteo de vehículos hasta 20
contador = 0

while contador < 20:
    contador += 1
    print(f"Vehículo {contador} registrado")
    if contador % 2 == 0:
        print("Vehículo par registrado")

if contador == 20:
    print("Capacidad completa")
