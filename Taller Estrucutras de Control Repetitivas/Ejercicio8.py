total_encuestados = 0
consumen_licor = 0
mujeres_menores = 0
hombres_sin_aguardiente_20_25 = 0
suma_edades_cerveza = 0
contador_cerveza = 0
consumen_whisky = 0

while True:
    print("\nEncuesta sobre consumo de licor")

    consume = input("¿Consume licor? (Sí/No): ").strip().lower()
    
    if consume == "sí" or consume == "si":
        consumen_licor += 1

        print("1 - Aguardiente, 2 - Ron, 3 - Cerveza, 4 - Tequila, 5 - Whisky, 6 - Otro")
        licor_preferido = int(input("Seleccione su licor preferido (1-6): "))

    else:
        licor_preferido = 0

    edad = int(input("Ingrese su edad: "))

    sexo = input("Ingrese su sexo (M/F): ").strip().upper()

    if sexo == "F" and edad < 18:
        mujeres_menores += 1

    if sexo == "M" and 20 <= edad <= 25 and licor_preferido != 1:
        hombres_sin_aguardiente_20_25 += 1
    
    if licor_preferido == 3:
        suma_edades_cerveza += edad
        contador_cerveza += 1

    if licor_preferido == 5:
        consumen_whisky += 1

    total_encuestados += 1

    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
    if continuar != "sí" and continuar != "si":
        break

if contador_cerveza > 0:
    promedio_edad_cerveza = suma_edades_cerveza / contador_cerveza
else:
    promedio_edad_cerveza = 0

if total_encuestados > 0:
    porcentaje_whisky = (consumen_whisky / total_encuestados) * 100
else:
    porcentaje_whisky = 0

print("\nResultados de la encuesta:")
print(f"Total de personas encuestadas que consumen licor: {consumen_licor}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {hombres_sin_aguardiente_20_25}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky:.2f}%")
