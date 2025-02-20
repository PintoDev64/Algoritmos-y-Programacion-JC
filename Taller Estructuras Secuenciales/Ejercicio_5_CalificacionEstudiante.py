print("Estudiante: Juan Pedro Paizanes")

print("Por favor, digite las calificaciones del estudiante:")
PrimeraNota = int(input("Primera Nota: "))
SegundaNota = int(input("Segunda Nota: "))
TerceraNota = int(input("Tercera Nota: "))

print("Por favor digite la calificacion del examen final")
ExamenNota = int(input())

print("Por favor digite la calificacion del trabajo final")
TrabajoFinalNota = int(input())

TotalNotas = PrimeraNota + SegundaNota + TerceraNota
PromedioNotas = TotalNotas * 0.55
PromedioExamen = ExamenNota * 0.30
PromedioTrabajoFinal = TrabajoFinalNota * 0.15
PromedioTotal = PromedioNotas + PromedioExamen + PromedioTrabajoFinal

print("El promedio del estudiante es de: ", PromedioTotal)