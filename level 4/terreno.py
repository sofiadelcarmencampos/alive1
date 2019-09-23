#Inputs
print("Dame las medidas :")
A = float(input("dame la medida de A: "))
B = float(input("Dame la medida de B: "))
C = float(input("Dame la medida de C: "))

#Proceso

arearectangulo = ( C * B)
areat = (A - C)
areatriangulo = (areat * B)
areatriangulototal = (areatriangulo / 2)
areatotal = (areatriangulototal + arearectangulo)

#Outputs
print ( f" El area total de tu terreno es de: {areatotal}")
