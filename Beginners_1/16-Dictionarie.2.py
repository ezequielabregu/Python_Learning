
phone = input("Phone: ")                            # usuario introduce su phone number
digits_mapping = {                                  # defino mi diccionario
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eigth",
    "9": "nine"
}
output = ""                                         # inicializo un string vacío
for ch in phone:                                    # analizará cada dígito de la lista phone (input del usuario)
    output += digits_mapping.get(ch,"!") + " "      # output = cada uno de las keys con su valor

print(output)