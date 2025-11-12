# Mostrar cuántas tazas se han servido del 1 al 10
for taza in range(1, 11):
    if taza == 5:
        print("¡Mitad del turno completada!")
    else:
        print(f"Taza servida número {taza}")
