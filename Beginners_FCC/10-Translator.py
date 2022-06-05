def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter in "aeiou":
            if letter.isupper():                # si es UPPER
                translation = translation + "I" #
            else:
                translation = translation + "i"
        else:
            translation = translation + letter
    return translation

print(translate(input("Mensaje:> ")))