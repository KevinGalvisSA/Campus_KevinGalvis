Tupla = (1,2,3,4,5,6,7,8,9,10)

MaxDupla = max(Tupla)

MinDupla = min(Tupla)

print(f"A continuanción, se le presenta una tupla: {Tupla}")

print("")

print("Que desea hacer con la tupla? \n 1. Imprimir numero minimo. \n 2. Imprimir numero maximo")

print("")

Deseo = int(input("Ingrese una opcion: "))

print("")

if Deseo == 1:
    print(f"El numero minimo de la tupla es: {MinDupla}")
elif Deseo == 2:
    print(f"El numero maximo de la tupla es: {MaxDupla}")
else:
    print("No has ingresado una de las opciones")







