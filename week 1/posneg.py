W = 'Hola Bienvenido a la semana 1. Reto 3: POSITIVO / NEGATIVO / CERO '
print(W)

n1 = int(input('Ingresa un número: '))

if n1 > 0: 
    print(f'{n1} es positivo')
elif n1 < 0:
    print(f'{n1} es negativo')
else:
    print(f'{n1} es cero')