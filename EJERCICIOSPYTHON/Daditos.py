#Simulador de Dados

import random 

Dado = 0

while Dado != 6:
    Dado = random.randint(1, 6)
    print (Dado)
    if Dado == 6:
        print ("El dado arrojó un: ",Dado)
        print ("Fin de los lanzamientos")











