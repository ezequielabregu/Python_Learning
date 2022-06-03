def find_max(numbers):
    maximum = numbers[0]            # defino como max al primer elemento de la lista (arbitrario)
    for number in numbers:      # recorro la lista numbers con el indice number
        if number > maximum:        # si el valor de number es mayor que max entonces...
            maximum = number        # redefino max con el nuevo valor más alto
    return maximum
