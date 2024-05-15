print("¿A qué grupo perteneces?\n")

g1 = "A"
g2 = "B"

letter = int(input("¿Tienes letra asignada? (1 = Sí, 0 = No): "))
name = input("¿Cuál es tu nombre? ")
sex = input("¿Cuál es tu sexo? (M = Mujer, H = Hombre): ")
letter = str(letter)
name = str(name)
sex = str(sex)

if letter == "1":
    if sex =="M":
        print(name," M, por lo que perteneces al grupo ", g1)
    else:
        print("N ",name," por lo que perteneces al grupo ", g1)

        
else:
    print("Perteneces al grupo", g2)