# Contador de ejercicios completados con mensaje cada 5
num_ejercicios = int(input("Ingrese el número total de ejercicios completados: "))

for i in range(1, num_ejercicios + 1):
    if i % 5 == 0:
        print(f"Ejercicio {i} completado - ¡Gran avance!")
    else:
        print(f"Ejercicio {i} completado")
