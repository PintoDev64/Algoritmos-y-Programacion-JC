ExamenMatematicas = float(input("Ingrese la nota del examen de Matemática: "))
TareaMatematicas1 = float(input("Ingrese la nota de la primera tarea de Matemática: "))
TareaMatematicas2 = float(input("Ingrese la nota de la segunda tarea de Matemática: "))
TareaMatematicas3 = float(input("Ingrese la nota de la tercera tarea de Matemática: "))

PromedioMatematicas = (ExamenMatematicas * 0.9) + (((TareaMatematicas1 + TareaMatematicas2 + TareaMatematicas3) / 3) * 0.1)

ExamenFisica = float(input("Ingrese la nota del examen de Física: "))
TareaFisica1 = float(input("Ingrese la nota de la primera tarea de Física: "))
TareaFisica2 = float(input("Ingrese la nota de la segunda tarea de Física: "))

PromedioFisica = (ExamenFisica * 0.8) + (((TareaFisica1 + TareaFisica2) / 2) * 0.2)

ExamenQuimica = float(input("Ingrese la nota del examen de Química: "))
TareaQuimica1 = float(input("Ingrese la nota de la primera tarea de Química: "))
TareaQuimica2 = float(input("Ingrese la nota de la segunda tarea de Química: "))
TareaQuimica3 = float(input("Ingrese la nota de la tercera tarea de Química: "))

PromedioQuimica = (ExamenQuimica * 0.85) + (((TareaQuimica1 + TareaQuimica2 + TareaQuimica3) / 3) * 0.15)

PromedioTotal = (PromedioMatematicas + PromedioFisica + PromedioQuimica) / 3

print("\nResultados:")
print(f"Promedio Matemática: {PromedioMatematicas:.2f}")
print(f"Promedio Física: {PromedioFisica:.2f}")
print(f"Promedio Química: {PromedioQuimica:.2f}")
print(f"Promedio General: {PromedioTotal:.2f}")
