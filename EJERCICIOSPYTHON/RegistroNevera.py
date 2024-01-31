"""Desarrolla una función que simule un sistema de monitoreo para un refrigerador. 
Esta función debe recibir la temperatura actual del refrigerador y retornar un mensaje de alerta si la temperatura es menor a 2°C (riesgo de congelación) o mayor a 4°C (riesgo de descomposición)."""

def monitoreoRefri(tempActual):
    tempActual = float(input("Ingrese el numero de la temperatua actual del refrigerador (en celsicus):"))
    
    if tempActual < 2 :
        print (f"La temperatura que ingresaste ¨{tempActual} °C¨ puede implicar un riesgo de congelación.")
    elif tempActual > 4 :
        print (f"La temperatura que ingresaste ¨{tempActual} °C¨ puede implicar un riesgo de descomposición.")
    elif tempActual > 2 and tempActual < 4 :
        print (f"La temperatura que ingresaste ¨{tempActual} °C¨ es una temperatura adecuada.")
    else :
        print ("No ingresaste un valor de temperatura permitido/adecuado")

def llamaFuncion():
    temperatura = 3.5
    monitoreoRefri(temperatura)

llamaFuncion()
