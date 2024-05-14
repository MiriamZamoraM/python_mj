"""Escribir un programa que pida al usuario que ingrese un texto y luego
cuente y muestre por pantalla la cantidad de palabras que contiene ese
texto."""

"""Función que cuenta la cantidad de palabras en un texto."""
def contar_palabras(texto):
    texto = texto.strip()
    palabras = texto.split()

    return len(palabras)

texto_usuario = input("Ingrese un texto: ")

cantidad_palabras = contar_palabras(texto_usuario)

print(f"La cantidad de palabras en el texto ingresado es: {cantidad_palabras}")
