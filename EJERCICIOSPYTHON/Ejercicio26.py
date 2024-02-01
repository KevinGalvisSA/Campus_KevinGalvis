
import time

print("----Bienvenido----")

time.sleep(1)

ListaMateo = [9, 7, "Genesis", "Wanda", "Teo", "Manuela"]

ListaCepeda = [6, 1, "Sara", "Carmen", "Rodrigo", "Manolo", "Negro", "Guiso"]

ListaMarruquin = [4, 8, "Rocio", "Yahira", "Pedro", 69, 666, 10, 64, 256, 77]


def mostrarLista():
    print("La listaMarruquin contiene el mayor numero de caracteres.")
    print("")
    print(f"ListaMarruquin: {ListaMarruquin}")
    print("")
    print(f"Las otras listas eran: \nListaMateo: {ListaMateo} \nListaCepeda: {ListaCepeda}")
    print("")

print("En este algoritmo hay tres listas establecidas.")
print("")
print("Las listas son: \n 1. ListaMateo \n 2. ListaCepeda \n 3. ListaMarruquin")
print("")
print("Cada una de ellas tiene cierta cantidad de elementos.")
print("¿Quieres saber cual lista contiene la mayor cantidad de elementos/caracteres?")
respuesta = input("¨s¨ / ¨n¨: ")

if respuesta == "s":
    mostrarLista()
elif respuesta == "n":
    print ("Entendido, no vamos a presentar la lista con mayor caracteres")
else:
    print("No has ingresado una respuesta permitida")

print ("Ahora, vamos a dejar que tu decidas que lista es la mayor")

time.sleep(5)

print ("En este algoritmo hay dos listas NO establecidas.")

time.sleep(2)
print("")

print ("Las listas son: \n 1. ListaDesconocida1 \n 2. ListaDesconocida2")

print("")

ListaDesconocida2 = []
def mostrarlista1():
    global ListaDesconocida2
    print("Iniciemos con la lista")
    palabra = "inicio"
    print("")
    while palabra!="fin":
        palabra=input("Por favor ingrese una palabra y termine con "'¨fin¨'": ")
        if(palabra!="fin"):
            ListaDesconocida2.append(palabra)
    print(ListaDesconocida2)
    print("")

ListaDesconocida1 = []
def mostrarlista2(): 
    global ListaDesconocida1
    print("Iniciemos con la lista")
    palabra2 = "inicio"
    print("")
    while palabra2!="fin":
        palabra2=input("Por favor ingrese una palabra y termine con "'¨fin¨'": ")
        if(palabra2!="fin"):
            ListaDesconocida1.append(palabra2)
    print(ListaDesconocida1)
    print("")

mostrarlista1()

mostrarlista2()

if len(ListaDesconocida1) < len(ListaDesconocida2) :
    print("LA LISTA CON MAYOR NUMERO DE CARACTERES ES:")
    print("")
    print(f"ListaDesconocida2: {ListaDesconocida2}")
elif len(ListaDesconocida1) > len(ListaDesconocida2) :
    print("LA LISTA CON MAYOR NUMERO DE CARACTERES ES:")
    print("")
    print(f"ListaDesconocida1: {ListaDesconocida1}")
elif len(ListaDesconocida1) == len(ListaDesconocida2) :
    print("Las listas contienen el mismo numero de caracteres")

print("")
time.sleep(10)

print("Si no te diste cuenta, la primera lista ingresada corresponde a la ListaDesconocida2. Mientras que la segunda lista ingresada corresponde a la ListaDesconocida1 >:)")

