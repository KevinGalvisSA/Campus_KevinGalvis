#Calculadora de Impuestos 


ingresos = float(input("Ingrese el valor de sus ingresos en dolares: "))

Impuesto1 = 0.05
Impuesto2 = 0.10
Impuesto3 = 0.15
Impuesto4 = 0.20
Impuesto5 = 0.30
Impuesto6 = 0.40


if ingresos < 100:
    Impuesto = ingresos * Impuesto1
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: \Ingresos bajos/")
elif ingresos > 100 and ingresos <= 200:
    Impuesto = ingresos * Impuesto2
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: -Ingresos medio bajos-")
elif ingresos > 200 and ingresos <= 300:
    Impuesto = ingresos * Impuesto3
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: --Ingresos medio--")
elif ingresos > 300 and ingresos <= 400:
    Impuesto = ingresos * Impuesto4
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: ¨Ingresos medio altos¨")
elif ingresos > 400 and ingresos <=500:
    Impuesto = ingresos * Impuesto5
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: ¨¨Ingresos altos¨¨")
elif ingresos > 500:
    Impuesto = ingresos * Impuesto6
    print ("El impuesto a pagar es de: ",Impuesto)
    print ("Usted se encuentra en la categoria: **Ingresos super altos**")










