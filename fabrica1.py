# si el número es par, mostrar “Producto verificado”
#Si es impar, mostrar “Producto pendiente”

numP = int(input("Ingresa la cantidad de productos fabricados"))

for i in range(1, numP + 1):
    if i % 2 == 0:
        print(f"producto {i}:producto verificado")
    else:
        print(f"producto {i}: producto pendiente")
