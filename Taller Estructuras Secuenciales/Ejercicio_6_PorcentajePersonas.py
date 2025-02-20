print("Aplicacion para calcular el porcentaje de personas")
CantidadHombres = int(input("Cantidad de hombres en el grupo: "))
CantidadMujeres = int(input("Cantidad de mujeres en el grupo: "))

CantidadEncuestados = CantidadMujeres + CantidadHombres
Promedio_Hombres = (CantidadHombres / CantidadEncuestados)*100
Promedio_Mujeres = (CantidadMujeres / CantidadEncuestados)*100

print("El porcentaje de hombres: ", Promedio_Hombres, "%")
print("El porcentaje de mujeres: ", Promedio_Mujeres, "%")