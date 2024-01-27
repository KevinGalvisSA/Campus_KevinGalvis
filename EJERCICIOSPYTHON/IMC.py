#Calculadora de Índice de Masa Corporal (IMC)

peso = int(input("Ingrese el peso a medir: "))

altura = float(input("Ingrese la altura a medir: "))


IMC = peso / (altura**2)


if IMC < 18.5:
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Insuficiencia ponderal¨")
elif IMC >= 18.5 and IMC <= 24.9:
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Intervalo normal¨")
elif IMC == 25:
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Sobrepeso¨")
elif IMC > 25 and IMC <= 29.9:
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Pre-Obesidad¨")
elif IMC >= 30 :
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Obesidad¨")
else:
    print ("Su indice de masa corporal es de: ",IMC)
    print ("Su categoria es: ¨Obesidad tipo 1 2 o 3 (Obesidad aun más grave)¨")






