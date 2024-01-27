# Celsius a Fahrenheit (0 °C × 9/5) + 32 = 32 °F
# Fahrenheit to Celsius (32 °F − 32) × 5/9 = 0 °C
#Convertir Celsius y Fahrenheit

print ("----Bienvenido Usuario----")

C = int(input("Ingrese la temperatura Celcius:"))

Fahrenheit = (C * 9/5) + 32

print ("Los grados celcius convertidos a grados Fahrenheit equivalen a: ",Fahrenheit,"°F")

F = int(input("Ingrese la temperatura Fahrenheit:"))

Celcius = (F - 32) * 5/9


print ("Los grados Fahrenheit convertidos a grados Celcius equivalen a: ",Celcius,"°C")