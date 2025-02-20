import math

print("Medir area de un triangulo: ")

LadoA = int(input("Ingrese el area A del trinagulo"))
LadoB = int(input("Ingrese el area B del trinagulo"))
LadoC = int(input("Ingrese el area C del trinagulo"))

Operacion = (LadoA + LadoB + LadoC) / 2

Area = math.sqrt(Operacion * (Operacion - LadoA) * (Operacion - LadoB) * (Operacion - LadoC))

print("El area dle triangulo es de: ", Area)