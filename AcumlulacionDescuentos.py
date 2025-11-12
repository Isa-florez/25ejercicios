def aplicar_descuentos():
    total = 0
    while true:
        precios = float(input("ingrese el precio (0 para terminar): "))
        if precio == 0:
            break
        if precio > 50000:
            precio *= 0.9
        total += precio
        print(f"total con descuento: $ {total:..2f}")
