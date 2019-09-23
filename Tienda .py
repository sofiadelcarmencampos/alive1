#Inputs

print("Bienvenido ")
cantidad=int(input("Dame el precio del producto: "))

#proceso

porcentaje=float(cantidad * 0.15 )
resultado=float(cantidad - porcentaje)

#output
print("Tu precio a pagar es de :" )
print (resultado)
