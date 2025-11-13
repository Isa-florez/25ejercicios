def promedio_notas():
    
    while True:

        nota1 = float(input("ingrese la primera nota: "))
        nota2 = float(input("ingrese la segunda nota:"))
        nota3 = float(input("ingrese la tercera nota:"))
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 3:
                print(f"{promedio:2f} aprobado")
        else:
                print(f"{promedio:2f} reprobado")
        
        continuar = input("desea ingresar a otro estudiante (s/n)").lower()
        if continuar != 's':
              print("fin del programa")
              break
promedio_notas()
