W = 'Hola Bienvenido a la semana 1. Reto 6: ORDENADO'
print(W)
n1 = int(input('Ingresa un número: '))
n2 = int(input('Ingresa otro numero: '))
n3 = int(input('Ingresa otro numero: '))

numeros = [n1, n2, n3]

numeros.sort(reverse=True)
print(numeros)
