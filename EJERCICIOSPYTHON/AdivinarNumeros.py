
import random

numeroSecreto = random.randint(1, 100)
numeroUsuario = 0

while numeroUsuario != numeroSecreto :
    numeroUsuario = int(input("Ingrese un numero:"))

    if numeroUsuario < numeroSecreto:
        print ("El numero es mayor")
    elif numeroUsuario > numeroSecreto:
        print ("El numero es menor")
    elif numeroUsuario == numeroSecreto:
        print ("**HAS ADIVINADO EL NUMERO**")
    else:
        print ("No has ingresado un numero")

print ("El numero secreto era: ",numeroSecreto)








