Algoritmo Ejercicio_6_PorcentajePersonas
	Escribir "Cuantos hombres hay en el grupo"
	Leer CantidadHombres
	Escribir "Cuantos mujeres hay en el grupo"
	Leer CantidadMujeres
	TotalPersonas<-CantidadHombres+CantidadMujeres
	PorcentajeHombres<-CantidadHombres*100/TotalPersonas
	PorcentajeMujeres<-CantidadMujeres*100/TotalPersonas
	Escribir "El Porcentaje de hombres en el grupo es: ", PorcentajeHombres, "%"
	Escribir "El Porcentaje de mujeres en el grupo es: ", PorcentajeMujeres, "%"
FinAlgoritmo
