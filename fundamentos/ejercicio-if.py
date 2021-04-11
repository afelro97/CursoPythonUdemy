mes = int(input("Proporciona el mes del año (1-12):"))

estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else:
    estacion = "Mes incorrecto"

print("Estación:", estacion, " Para el mes: ", mes)


valor = int(input("Proporcione un valor"))

if valor == 0 or valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5:
    valorFinal = "F"
    print(valorFinal)
elif valor == 7 :
    valorFinal = "C"
    print(valorFinal)
elif valor == 6 :
    valorFinal = "D"
    print(valorFinal)
elif valor == 9 or valor == 10  :
    valorFinal = "A"
    print(valorFinal)
else:
    valorFinal = "Valor desconocido"
    print(valorFinal)
