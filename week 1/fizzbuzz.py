W = 'Hola Bienvenido a la semana 1. Reto 4: FIZZBUZZ SIMPLE'
print(W)

n1 = int(input('Ingresa un número: '))

if n1 % 5 == 0 and n1 % 3 == 0:
    print(f'{n1} es divisible entre 3 y 5' )

elif n1%5==0:
    print(f'{n1} es divisible entre 5')

elif n1%3==0:

    print(f'{n1} es divisible entre 3')

else:
    print(f'{n1} no es divisible entre 3 ni 5')