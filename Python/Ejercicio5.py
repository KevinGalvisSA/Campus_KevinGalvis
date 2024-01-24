"""1. Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.

print ("*******Bienvenido*******")

edad = int(input("Querido usuario, ingrese su edad"))

if edad > 18 :
    print ("Usted es mayor de 18 años y puede votar")
else : 
    print("Usted es menor de 18 años y no puede votar")"""


"""2. Pide una calificación numérica y utiliza condicionales elif para asignar una calificación en letras, como A, B, C o D.

print ("*******Bienvenido*******")

calificacion = int(input("Hola usuario, ingrese una calificación (10 a 100):"))

if calificacion >= 10 and calificacion <=30 :
    print ("Su calificacion en el trabajo es:","D")
elif calificacion > 30 and calificacion <= 60 :      
    print ("Su calificacion en el trabajo es:","C")
elif calificacion > 60 and calificacion <= 80 :
    print ("Su calificacion en el trabajo es:","B")
elif calificacion > 80 and calificacion <= 100 :
    print ("Su calificacion en el trabajo es:","A")
else :
    print ("No ha ingresado un numero de calificacion permitido")"""

"""#3. Permítele a alguien elegir un tipo de comida y utiliza condicionales if para recomendar un restaurante según la elección (por ejemplo, comida italiana, mexicana o china).

tipoComida = str(input("Bienvenido estimado cliente, puedo saber que tipo de comida desea? (Italiana - Japonesa - China - Mexicana - Colombiana):"))


if tipoComida == "Italiana" :
    print ("Ya veo, en ese caso le recomiendo ir al restaurante italiano. Tiene la mejor pasta y pizza.")
elif tipoComida == "Japonesa" :
    print ("Ya veo, en este caso le recomiendo ir al restuaurante japones. Es uno de los más famosos.")
elif tipoComida == "China" :
    print ("Ya veo, en este caso le recomiendo ir al restuaurante chino. Tiene una gran diversidad.")
elif tipoComida == "Mexicana" :
    print ("Ya veo, en ese caso le recomiendo ir al restuaurante mexicano. Ahi venden los mejores tacos.")
elif tipoComida == "Colombiana" :
    print ("Ya veo, en este caso le recomiendo ir al restuaurante colombiano. Hacen una comida de tu gusto.")
else :
    print ("Uy... Disculpame, no se que restaurante recomendarte para ese tipo de comida (no es uno de los que se puso entre parentesis)")"""

#4. Solicita una contraseña y utiliza una declaración if para verificar si coincide con una contraseña predefinida antes de permitir el acceso.

Contraseña = "CampusLand"

contraseña = str(input("Ingrese la contraseña de este sistema","(Recuerde que es un caracter/string)"))


while contraseña != Contraseña :
    if contraseña == Contraseña :
        print ("Has ingresado correctamente la contraseña. La contraseña era:",Contraseña)
        print ("Ahora puede acceder al sistema")
    else :
        print ("No has ingresado la contraseña correcta.")


























