def aplicar_descuentos():
    total = 0
    while True:
        precio = float(input("ingrese el precio (0 para terminar): "))
        if precio == 0:
            break
        if precio > 50000:
            descuento = precio * 0.10
            precio -= descuento
        total += precio
        print(f"total con descuento: $ {total:2f}")
aplicar_descuentos()
