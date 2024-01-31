"""Escribe una función que recomiende qué tipo de ropa vestir basado en la temperatura exterior actual. 
Por ejemplo, por encima de 25°C recomienda ropa ligera, entre 15°C y 25°C sugiere una camiseta y pantalón, etc."""


def RecomendarRopa(tempExterior):
    tempExterior = float(input("Ingrese la temperatura del exterior (se trabaja con celcius):"))
    
    if tempExterior < 15 :
        print ("La temperatura esta baja, te recomiendo llevar sacos o en general ropa para el frio")
    elif tempExterior >= 15 and tempExterior <= 25 :
        print ("La temperatura es adecuada, te recomimiendo llevar camiseta y pantalón, ropa casual.")
    elif tempExterior > 25 :
        print ("La temperatura esta alta, te recomimiendo llevar ropa ligera")
    else :
        print("No has ingresado un valor de temperatura o lo ingresaste mal")

def llamaFuncion():
    temperatura = 0
    RecomendarRopa(temperatura)

llamaFuncion()





