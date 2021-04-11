#a = int(input("Proporciona un valor: "))
a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)

if(dentroRango):
    print("dentro de Rango")
else:
    print("Fuera de Rango")

vacaciones = False
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")

print(not (vacaciones))


alto = int(input("alto: "))
ancho = int(input("ancho: "))

print("El area es ", alto*ancho)
print("El perimetro es ", (alto+ancho)*2)

numero1 = int(input("Proporciona el numero1: "))

numero2 = int(input("Proporciona el numero2: "))

if(numero1 > numero2):
    numeroMayor = numero1
    print("El numero mayor es " + str(numeroMayor))
else:
    numeroMayor = numero2
    print("El numero mayor es " + str(numeroMayor))

# Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):

