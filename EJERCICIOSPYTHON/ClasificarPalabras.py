#Clasificador de Palabras - Escribe un programa que clasifique una palabra ingresada como 'corta' (menos de 5 caracteres), 'media' (entre 5 y 10 caracteres) o 'larga' (más de 10 caracteres).

contador = 0
palabra = input("Ingrese una palabra:")

for i in palabra:
    contador += 1

if contador > 0 and contador < 5:
    print (f"La palabra: {palabra} clasifica como una palabra corta.")
elif contador >= 5 and contador <= 10:
    print (f"La palabra: {palabra} clasifica como una palabra mediana.")
elif contador > 10:
    print (f"La palabra: {palabra} clasifica como una palabra larga.")








