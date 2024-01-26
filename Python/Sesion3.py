
print ("*******Bienvenido*******")

horasTrabajo = int(input("Ingrese el numero de horas:"))

if horasTrabajo < 10:
    print ("La hora vale 5$:")
    print ("El valor de su sueldo es: ",horasTrabajo * 5)
elif horasTrabajo >= 10 and horasTrabajo <= 20:
    print ("La hora vale 10$:")
    print ("El valor de su sueldo es: ",horasTrabajo * 10)
elif horasTrabajo > 20:
    print ("La hora vale 15$:")
    print ("El valor de su sueldo es: ",horasTrabajo * 15)
else:
    print ("No ha ingresado un valor de hora")







