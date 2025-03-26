NStudents = int(input("Ingrese el número de estudiantes: "))

Max_Altura = 0

for StudentID in range(NStudents):
    Altura = float(input(f"Ingrese la altura del estudiante {StudentID+1}: "))
    if (Altura > Max_Altura):
        Max_Altura = Altura

print(f"La mayor altura es: {Max_Altura}")
