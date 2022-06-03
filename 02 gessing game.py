secret_numb = 9
count = 0
guess_limit = 3

while count <= guess_limit:
   guess = int(input('Guess: '))
   count += 1
   if guess == secret_numb:
      print ('You won!')
      break
else:    # -> se ejecuta solo si el while termina
   print('You losse!')


