"""Calculadora de Propina
Crea una función que calcule cuánto de propina dejar en un restaurante basado en la calidad del servicio. 
La función debe aceptar el monto de la cuenta y la calidad del servicio (buena, aceptable, mala) y retornar el monto de la propina."""

def calculoCuenta(montoCuenta):
    TotalCuenta = montoCuenta 
    return TotalCuenta

def CalidadServicio(TotalCuenta):
    Calidad = input("Por favor, califica nuestro servicio. (Buena - buena, Aceptable - aceptable, Mala - mala)")
    if Calidad == "Buena" or Calidad == "buena":
        MontoPropina = 2000
        TotalCuenta = TotalCuenta + MontoPropina
        print ("El total de la cuenta es de: ",TotalCuenta)
    elif Calidad == "Aceptable" or Calidad == "aceptable":
        MontoPropina = 1000
        TotalCuenta = TotalCuenta + MontoPropina
        print ("El total de la cuenta es de: ",TotalCuenta)
    elif Calidad == "Mala" or Calidad == "mala":
        MontoPropina = 500
        TotalCuenta = TotalCuenta + MontoPropina
        print ("El total de la cuenta es de: ",TotalCuenta)
    else:
        print("No ha ingresado una calificacion aceptada.")

def FuncionTraeFunciones():
    PagoCuenta = int(input("Valor de la cuenta: "))

    TotalDeLaCuenta = calculoCuenta(PagoCuenta)
    ValorCuentaMasPropina = CalidadServicio(TotalDeLaCuenta)


FuncionTraeFunciones()

















