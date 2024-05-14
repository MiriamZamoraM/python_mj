"""Escribir un programa que pida al usuario que ingrese las calificaciones
de varios exámenes y luego calcule y muestre por pantalla el promedio
de esas calificaciones."""

calificaciones = []

while True:
    grade = float(input("Ingresa tu calificación (o -1 para parar): "))
    if grade == -1:
        break
    calificaciones.append(grade)

average = sum(calificaciones) / len(calificaciones)

print("El promedio de tus examenes es: ", average)