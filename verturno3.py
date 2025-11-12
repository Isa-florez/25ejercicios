# Definición de la función
def verificarTurno(hora):
    if hora < 12:
        return "Turno de mañana"
    elif 12 <= hora <= 18:
        return "Turno de tarde"
    else:
        return "Turno de noche"

# Programa principal
hora_actual = int(input("Ingresa la hora (en formato 24h): "))
turno = verificarTurno(hora_actual)
print(turno)
