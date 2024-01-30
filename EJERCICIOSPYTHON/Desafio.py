#Eres el desarrollador de software encargado de implementar un sistema de facturación simplificado para una tienda. 
#Este sistema debe calcular el total a pagar por un cliente después de aplicar descuentos específicos a tres productos diferentes.
#Luego sumar los impuestos correspondientes a cada uno. 
#Aunque el ejercicio se simplifica al no utilizar colecciones, deberás aplicar principios de descomposición de problemas para manejar cada cálculo con su propia función.

#### Requerimientos

#Cálculo de Precio con Descuento: Implementa una función que reciba dos parámetros: el precio original de un producto y el porcentaje de descuento aplicable a ese producto. 
#La función debe calcular y retornar el precio del producto después de aplicar el descuento.

#Cálculo de Precio con Impuesto: Implementa una función que reciba dos parámetros:
#el precio de un producto después de aplicar el descuento y el porcentaje de impuesto aplicable a ese producto. 
#La función debe calcular y retornar el precio del producto después de sumar el impuesto.

#Cálculo del Total de la Compra: 
#Implementa una función principal que llame a las funciones anteriores para cada uno de los tres productos, con sus respectivos precios originales, descuentos y tasas de impuesto. 
#Luego, suma los resultados de los tres productos para obtener el total final a pagar. 
#Esta función no recibirá ningún parámetro directamente. 
#pero utilizará valores predefinidos dentro de su implementación para representar los precios, descuentos, y tasas de impuesto de cada producto.

#### Ejemplo de Datos

#Producto 1: precio original $100, descuento 10%, impuesto 15%
#Producto 2: precio original $200, descuento 5%, impuesto 10%
#Producto 3: precio original $50, descuento 0%, impuesto 5%

#### Salida Esperada

def calculoPrecioConDescuento(precioOriginal, porcentajeDescuento):
    descuento = precioOriginal*porcentajeDescuento
    return precioOriginal - descuento

def calculoPrecioConImpuesto(precioConDescuento, porcentajeImpuesto):
    IVA = precioConDescuento*porcentajeImpuesto 
    return precioConDescuento + IVA

def total():
    precioTotal = float(input("Precio producto:"))
    descuento = float(input("descuento:"))
    impuesto = float(input("IVA:"))

    PrecioConDescuento = calculoPrecioConDescuento(precioTotal, descuento)
    PrecioConDescuentoConImpuesto = calculoPrecioConImpuesto(PrecioConDescuento, impuesto)

    print("Bienevenido! Su precio inicial fue: ",precioTotal)
    print("El precio del producto con descuento es: ",PrecioConDescuento)
    print("El precio del producto con impuesto es: ",PrecioConDescuentoConImpuesto)


#Algoritmo
total()


























