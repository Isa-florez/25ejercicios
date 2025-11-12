# Definición de la función
def calcularInteres(monto, tasa):
    interes = monto * (tasa / 100)
    total = monto + interes
    return total

# Programa principal
monto = float(input("Ingresa el monto inicial: "))
tasa = float(input("Ingresa la tasa de interés (%): "))

resultado = calcularInteres(monto, tasa)
print("El valor final con interés es:", resultado)
