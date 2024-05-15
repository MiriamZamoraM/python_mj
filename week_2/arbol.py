def imprimir_triangulo_rectangulo_altura(altura):
    for i in range(1, altura + 1):
        print('*' * i)

# Pedir al usuario que introduzca un número entero
try:
    altura = int(input("Introduce la altura del triángulo (número entero): "))
    if altura <= 0:
        print("Por favor, introduce un número entero positivo mayor que cero.")
    else:
        imprimir_triangulo_rectangulo_altura(altura)
except ValueError:
    print("Error: Debes introducir un número entero válido.")
