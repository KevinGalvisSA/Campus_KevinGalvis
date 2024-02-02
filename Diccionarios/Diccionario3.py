Diccionario = {
    
    'Persona1': "Kevin",
    
    'Persona2': "Santiago",
    
    'Persona3': "Galvis",
}

print(f"Aqui hay un diccionario: {Diccionario}")

print("")

NuevoDiccionario = Diccionario.setdefault('Persona4',"Arias")

print(f"Este es el nuevo diccionario: {Diccionario}")
