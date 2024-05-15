def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        n1 = int(input("Ingrese un número entero: "))

        if n1 <=2:
            print("Ingrese otro número ")
            continue

        if n1 > 2 and es_primo(n1):
            print(f'El número {n1} es primo')
        else:
            print(f'El número {n1} no es primo')
        break
    except ValueError:
        print("El valor ingresado no es un número entero")
