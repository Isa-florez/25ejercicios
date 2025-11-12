# Simulación de ahorro durante 6 meses
total_ahorro = 0

for mes in range(1, 7):
    ahorro = float(input(f"Ingrese el ahorro del mes {mes}: $"))
    total_ahorro += ahorro

    if total_ahorro > 1000000:
        print("¡Meta alcanzada!")

print(f"Total acumulado en 6 meses: ${total_ahorro:,.2f}")
