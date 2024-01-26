#Algoritmo que pregunte nombre, numero de horas trabajadas, costo por hora y debe mostrar el total de la hora

nombre = str((input("-Bienvenido Usuario- ingrese su nombre")))

numeroHoras = int((input("Ahora,ingresa el numero de horas que has trabajado")))

costoHora = int((input("Por ultimo. ingresa el costo de la hora")))

print ("Listo. A continuacion te presentamos el calculo del total de la hora")

totalHora = numeroHoras * costoHora

print ("El total de la hora es:",totalHora)