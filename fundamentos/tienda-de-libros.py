import math

print("Propocione los siguientes datos del libro:")
nombre = input("Proporciona el nombre:")
id = int(input("Propociona el ID:"))

precio = float(input("Proporcione el precio:"))
envioGratuito = input("Indica si el envio es gratuito (True/False):")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"

print("Nombre: ", nombre)
print("Id", id)
print("Precio:", precio)
print("Envio gratuito?:", envioGratuito)

print(type(envioGratuito))