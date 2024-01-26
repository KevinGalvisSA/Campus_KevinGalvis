print ("*******Bienvenido*******")

calificacion = int(input("Hola usuario, ingrese una calificación (1 a 100):"))

if calificacion >= 1 and calificacion <=30:
    print ("Su calificacion en el trabajo es:","D")
elif calificacion > 30 and calificacion <= 60:      
    print ("Su calificacion en el trabajo es:","C")
elif calificacion > 60 and calificacion <= 80:
    print ("Su calificacion en el trabajo es:","B")
elif calificacion > 80 and calificacion <= 100:
    print ("Su calificacion en el trabajo es:","A")
else:
    print ("No ha ingresado un numero de calificacion permitido")