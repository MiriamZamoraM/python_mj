"""Escribir un programa que pregunte al usuario las dimensiones de un
rectángulo (largo y ancho) y calcule tanto el área como el perímetro del
rectángulo, mostrando ambos valores por pantalla."""

h = int(input("Altura del rectangulo: "))
w = int(input("Anchura del rectangulo: "))

area = w * h

print(f'La base del rectángulo es {w} y su altura es {h}, por lo que su área es {area}')