def add(num1,num2):
    return int(num1) + int(num2)
def subtract(num1,num2):
    return int(num1) - int(num2)

num1 = input('Enter a number: ')
operation = input('Enter operation sign: ')
num2 = input('Enter another number: ')

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
print (result)
