# Definición de la función
def promedioNotas(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    if promedio >= 3.0:
        print("Aprobado con promedio de", round(promedio, 2))
    else:
        print("Reprobado con promedio de", round(promedio, 2))

# Programa principal
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedioNotas(nota1, nota2, nota3)
