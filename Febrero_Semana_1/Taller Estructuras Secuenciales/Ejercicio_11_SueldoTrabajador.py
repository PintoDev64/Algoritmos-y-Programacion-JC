Nombre = input("Ingrese el nombre del trabajador: ")
HorasNormales = float(input("Ingrese el número de horas normales trabajadas: "))
PagoHora = float(input("Ingrese el pago por hora normal: "))
HorasExtras = float(input("Ingrese el número de horas extras trabajadas: "))
NumeroHijos = int(input("Ingrese el número de hijos: "))

SueldoBase = HorasNormales * PagoHora
PagoExtras = HorasExtras * (PagoHora * 1.25)

Asignaciones = PagoExtras + 250000 + (173000 * NumeroHijos) + 180000

Deduccion = (SueldoBase * 0.05) + (SueldoBase * 0.02) + (SueldoBase * 0.07)

SalarioNeto = SueldoBase + Asignaciones - Deduccion

print("\nResumen del sueldo del trabajador:")
print(f"Nombre: {Nombre}")
print(f"Asignaciones: {Asignaciones}")
print(f"Deducciones: {Deduccion}")
print(f"Sueldo neto: {SalarioNeto}")
