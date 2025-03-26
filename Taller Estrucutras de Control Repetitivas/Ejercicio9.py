estudiantes = []

N = int(input("Ingrese el número de estudiantes: "))

max_puntaje = float('-inf')
min_puntaje = float('inf')
nombre_max = ""
nombre_min = ""
suma_puntajes = 0

for _ in range(N):
    nombre = input("\nIngrese el nombre del estudiante: ")
    puntaje = float(input("Ingrese el puntaje obtenido: "))

    estudiantes.append((nombre, puntaje))
    suma_puntajes += puntaje

    if puntaje > max_puntaje:
        max_puntaje = puntaje
        nombre_max = nombre

    if puntaje < min_puntaje:
        min_puntaje = puntaje
        nombre_min = nombre

promedio = suma_puntajes / N

inferiores_al_promedio = sum(1 for _, puntaje in estudiantes if puntaje < promedio)
superiores_al_promedio = sum(1 for _, puntaje in estudiantes if puntaje > promedio)

porcentaje_inferiores = (inferiores_al_promedio / N) * 100
porcentaje_superiores = (superiores_al_promedio / N) * 100

print("\nResultados de la prueba de admisión:")
print(f"Estudiante con el puntaje más alto: {nombre_max} ({max_puntaje})")
print(f"Estudiante con el puntaje más bajo: {nombre_min} ({min_puntaje})")
print(f"Puntaje máximo obtenido: {max_puntaje}")
print(f"Puntaje mínimo obtenido: {min_puntaje}")
print(f"Promedio de todos los puntajes: {promedio:.2f}")
print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {porcentaje_inferiores:.2f}%")
print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {porcentaje_superiores:.2f}%")