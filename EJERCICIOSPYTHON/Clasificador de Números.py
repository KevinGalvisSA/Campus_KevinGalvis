#Clasificar numeros en positivos y negativos

print ("----Bienvenido Usuario----")


numero = int(input("Ingrese un numero"))

if numero == 0: 
    print ("El numero ingresado es 0")
elif numero > 0:
    print ("El numero ingresado es positivo")
elif numero < 0:
    print ("El numero ingresado es negativo")
else:
    print ("Como llegaste a tener un error?")