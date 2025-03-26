suma = 0
k = 1
terminos = 0
limite = 1000

while suma + (k**2 + 1) / k <= limite:
    suma += (k**2 + 1) / k
    terminos += 1
    k += 1

print("Número de términos necesarios:", terminos)