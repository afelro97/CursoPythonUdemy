condicion = True

print("Condicion verdadera") if condicion else print("Condicion falsa")

if condicion:
    print("La condicion es verdadera")
elif condicion:
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")

numero = int(input("Propociona un número entre 1 y 3:"))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de rango"

print("Numero propocionado:" + numeroTexto)
