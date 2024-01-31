#arreglo
lista = []

palabra = "inicio"
while palabra!="final":

    palabra=input("Por favor ingrese una palabra y termine con "'final'" ")
    if(palabra!="final"):
        lista.append(palabra)

print(lista)

for pala in lista:
    print(pala)

print(type(lista))
