W = 'Hola Bienvenido a la semana 1. Reto 5: CALIFICACIONES'
print(W)

n1 = float(input('Ingresa tu calificación entre 0 y 100: '))

if n1 < 60:
    print('Tu calificación es F')

elif n1 < 69:
    print('Tu calificación es D')

elif n1 < 79:
    print('Tu calificación es C')

elif n1 < 89:
    print('Tu calificación es B')

elif n1 <= 100:
    print('Tu calificación es A')