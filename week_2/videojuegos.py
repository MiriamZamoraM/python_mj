print("Bienvenido a nuestro mundo de videojuegos")

age = int(input("¿Cuál es tu edad? "))

if age <= 4:
    print("Puedes entrar gratis")
elif age <= 18 and age >= 4:
    print("El precio de la entrada es de 5€")
else:
    print("El precio de la entrada es de 10€")