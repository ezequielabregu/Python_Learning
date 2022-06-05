lucky_numbers = [4, 8, 15, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Oscar']
friends.append("Creed")                         #agrega un elemento a la lista
friends.insert(1,'Kelly')                       #inserta elemento en el index
friends.remove('Kevin')                         #remueve elemento
# friends.clear()
lucky_numbers.sort()                            #ordena de menor a mayor
#lucky_numbers.reverse()                        #ordena de mayor a menor
print(friends.index('Oscar'))                   #si Oscar está en la lista, sino error
print(friends.count('Oscar'))                   #cuenta las veces que está en la lista
print(lucky_numbers)
