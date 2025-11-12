# Control de repeticiones con mensaje especial cada 3
repeticiones = int(input("Ingrese el número de repeticiones: "))

for x in range(1, repeticiones + 1):
    print(f"Repetición {x} completada")
    if x % 3 == 0:
        print("¡Excelente ritmo!")
