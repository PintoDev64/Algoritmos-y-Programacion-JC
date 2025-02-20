SalarioEmpleado = int(input("¿Cual es su salario base? "))
PrimeraVenta = int(input("Ingrese el valor de su primera venta "))
SegundaVenta = int(input("Ingrese el valor de su segunda venta "))
TerceraVenta = int(input("Ingrese el valor de su tercera venta "))

VentasTotales = PrimeraVenta + SegundaVenta + TerceraVenta
ComisionTotal = (VentasTotales * 10) / 100
PagoTotal = SalarioEmpleado + ComisionTotal

print("El sueldo del empleado con comisiones es de: ", PagoTotal)