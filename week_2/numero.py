n1 = int(input("Ingresa un número hasta el que deseas contar: "))


if n1 < 0:
        print("Por favor, introduce un número entero positivo.")
else:
    cuenta_atras = [str(i) for i in range(n1, -1, -1)]
    print(", ".join(cuenta_atras))
    