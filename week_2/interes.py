def calcular_capital_inversion(inversion, interes_anual, num_anios):
    capital = inversion
    for i in range(1, num_anios + 1):
        capital *= (1 + interes_anual / 100)
        print(f"Año {i}: Capital obtenido = {capital:.2f}")

try:
    inversion = float(input("Ingrese la cantidad a invertir: "))
    interes_anual = float(input("Ingrese el interés anual (%): "))
    num_anios = int(input("Ingrese el número de años de la inversión: "))
    
    if inversion <= 0 or interes_anual < 0 or num_anios <= 0:
        print("Por favor, asegúrese de ingresar valores positivos para la inversión, el interés y el número de años.")
    else:
        calcular_capital_inversion(inversion, interes_anual, num_anios)
except ValueError:
    print("Error: Debe ingresar valores numéricos válidos para la inversión, el interés y el número de años.")
