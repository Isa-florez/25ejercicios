# Definición de la función
def calcularEnergia(repeticiones):
    if repeticiones < 5:
        return "Necesitas más esfuerzo"
    else:
        return "¡Buen trabajo!"

# Programa principal
reps = int(input("Ingresa el número de repeticiones: "))
mensaje = calcularEnergia(reps)
print(mensaje)
