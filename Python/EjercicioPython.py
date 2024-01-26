
print ("*******Bienvenido*******")

descuento0 = 0
descuento = 0.10
descuento2 = 0.15
PrecioProducto = 5000 * descuento
PrecioTotal = 5000 - PrecioProducto 
PrecioProducto2 = 5000 * descuento2
PrecioTotal2 = 5000 - PrecioProducto2
PrecioSinDescuento = 5000

Producto = int(input("Ingrese cuantos productos desea comprar:"))

cantidad = 0
adicionales = Producto // 12
cantidad = adicionales - 3



if Producto == 0 or Producto < 0:
    print ("No desea comprar nada.")
elif Producto < 6 :
    print ("El numero de productos comprados es de: ",Producto)
    print ("El precio de su compra sin el descuento es:",PrecioSinDescuento)
    print ("El descuento que recibes es de: ",descuento0)
    print ("El precio de su compra es de:",PrecioTotal)
    print ("No se le obsequia unidades extra")
elif Producto > 6 and Producto <= 18 :
    print ("El numero de productos comprados es de: ",Producto)
    print ("El precio de su compra sin el descuento es:",PrecioSinDescuento)
    print ("El descuento que recibes es de: ",descuento)
    print ("El precio de su compra es de:",PrecioTotal)
    print ("No se le obsequia unidades extra")
elif Producto > 18 :
    print ("El numero de productos comprados es de: ",Producto)
    print ("El precio de su compra sin el descuento es:",PrecioSinDescuento)
    print ("El descuento que recibes es de: ",descuento2)
    print ("El precio de su compra es de:",PrecioTotal2)
    print ("El numero de unidades de obsequio que te damos es de: ",cantidad)
else :
    print ("Como llegaste hasta aqui lol")

















