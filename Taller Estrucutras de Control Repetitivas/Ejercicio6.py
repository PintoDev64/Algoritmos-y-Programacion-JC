dividiendo = int(input("Escriba el dividiendo: "))
divisor = int(input("Escriba el divisor: "))

counter = 0

while (dividiendo >= divisor):
    dividiendo -= divisor
    counter += 1;

print(f"numero de restas: {counter}")
print(f"residuo: {dividiendo}")