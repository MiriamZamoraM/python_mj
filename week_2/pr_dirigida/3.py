"""Escribir un programa que pida al usuario dos números enteros y luego
muestre por pantalla todos los números primos que se encuentren en el
rango comprendido entre esos dos números."""

"""Función que verifica si un número es primo."""
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


"""Función que encuentra todos los números primos entre a y b (inclusive)."""
def encontrar_primos_entre(a, b):
    primos = []
    for num in range(a, b + 1):
        if es_primo(num):
            primos.append(num)
    return primos


n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))


inicio = min(n1, n2)
fin = max(n1, n2)


primos_en_rango = encontrar_primos_entre(inicio, fin)

print(f"Los números primos entre {inicio} y {fin} son:")
print(primos_en_rango)


