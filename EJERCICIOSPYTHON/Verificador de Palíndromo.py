#Verificar si una palabra es un palíndromo (se lee igual al reves)

print ("**Bienvenido Usuario**")

palabra = input("Ingresa una palabra:")

palabra = palabra.lower()

if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")