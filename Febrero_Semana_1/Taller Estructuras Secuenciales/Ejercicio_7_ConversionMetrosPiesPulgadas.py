import math

METRO_PULGADA = 39.27

Metros = int(input("¿Cuantos metros desea convertir a pies y pulgadas?: "))
Pulgadas = Metros * METRO_PULGADA
Pies = math.trunc(Pulgadas / 12)
PulgadasRestantes = Pulgadas - (Pies * 12)

print("La cantidad en metros equivale a: ", Pies, " pies y ", Pulgadas, " pulgadas.")