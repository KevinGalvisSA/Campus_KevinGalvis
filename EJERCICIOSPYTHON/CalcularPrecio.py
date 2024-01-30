
print ("*----Bienvenido----*")

print ("Te encuentras en tu tienda de confianza")

calculoDePrecios = 0
def Calculo_Precio(nombre = "Kevin",cantidad = 2, precio = 5000):
    nombre = input("Antes de nada, ingresa tu nombre")
    cantidad = int(input("Cuantos objetos deseas llevar?"))
    Calculo = precio * cantidad
    return print (f"Hola {nombre}, tienes que pagar ${Calculo} por la cantidad de productos {cantidad}")
Calculo_Precio(calculoDePrecios)


def Calculando_Precios(nombre, cantidadProductos = 5, precio = 5000):
    Total = precio * cantidadProductos
    print (f"Hola {nombre}, el total a pagar por la compra de {cantidadProductos} productos es de: ${Total}.")
Calculando_Precios("Kev")










