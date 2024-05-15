n1 = int(input("Ingresa un número para la tabla de multiplicar: "))

if n1 < 0:
    for i in range(1, 10):
        print(i, "x", n1, "=", i*n1)
else:
    print("El numero debe ser mayor a 0")
        