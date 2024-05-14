"""Para tributar un determinado impuesto se debe ser mayor de 16 años y
tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no."""

print("¿Eres tributario?\nLo veremos en seguida")

age = int(input("¿Cuál es tu edad? "))

if age > 16:
    print("¿Cuál es tu salario mensual?")
    salary = int(input("Introduce tu salario: "))
    if salary >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")
        
else:
    print("No tienes que tributar")