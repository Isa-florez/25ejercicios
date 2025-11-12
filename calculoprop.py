# funcion
def calcular_propina(total_cuenta):
    if total_cuenta > 100000:
        propina = total_cuenta * 0.15
    else:
        propina = total_cuenta * 0.10
    total_final = total_cuenta + propina
    print(f"Propina:${propina:..2f}")
    print(f"total a pagar: ${total_final:..2f}")
    
    