Diccionario = {
    
    'Persona1': "Kevin",
    
    'Persona2': "Santiago",
    
    'Persona3': "Galvis",
    
    'Edad1': 20,
    
    'Edad2': 15,
    
    'Rasgos1': "Blanco"
}

Clave = input("Ingrese una clave: (Persona'i', Edad'i', Rasgos'i'): ")

if Clave in Diccionario:
    print(f"La clave '{Clave}' existe en el diccionario y tiene el valor ¨{Diccionario[Clave]}¨.")
else:
    print(f"La clave '{Clave}' no existe en el diccionario.")



