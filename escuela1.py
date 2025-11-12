# Sumar tareas entregadas hasta llegar a 10
tareas = 0
while tareas < 10:
    tareas += 1
    if tareas == 10:
        print("¡Todas las tareas recibidas!")
    else:
        print(f"Faltan {10 - tareas} tareas por entregar.")
