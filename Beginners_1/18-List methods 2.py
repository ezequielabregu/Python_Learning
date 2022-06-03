numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = [] # inicializo una lista vacía
for number in numbers:
    if number not in uniques: # si number no está en la lista uniques agrega los valores a uniques
        uniques.append(number)
print(uniques)