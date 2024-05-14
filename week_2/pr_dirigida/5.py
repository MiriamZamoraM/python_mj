"""Escribir un programa que pregunte al usuario por una temperatura en
grados Celsius y luego convierta esa temperatura a grados Fahrenheit y
Kelvin, mostrando los resultados por pantalla."""


"""Función para convertir grados Celsius a grados Fahrenheit."""
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


"""Función para convertir grados Celsius a Kelvin."""
def celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


tcelsius = float(input("Ingrese la temperatura en grados Celsius: "))


temperatura_fahrenheit = celsius_a_fahrenheit(tcelsius)
temperatura_kelvin = celsius_a_kelvin(tcelsius)

print(f"Temperatura en grados Fahrenheit: {temperatura_fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {temperatura_kelvin:.2f} K")

# .2f para redondear los valores a 2 decimales