# try / except evitan que python crashee cuando hay un ingreso válido

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except  ZeroDivisionError: # hay diferentes tipos de errores
    print('age cannot be 0.')
except ValueError:          # evita el crash
    print('invalid value')