# Mostrar clientes atendidos del 1 al 8
for cliente in range(1, 9):
    if cliente == 8:
        print("Último cliente del día.")
    else:
        print(f"Atendiendo cliente número {cliente}")
