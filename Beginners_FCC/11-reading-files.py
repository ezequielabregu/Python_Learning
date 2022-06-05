names_file = open("names.txt", "r") # r = read

#print(names_file.readline())    # para leer solo una línea
#print(names_file.readlines())    # para leer TODAS las líneas
#print(names_file.readlines()[1])    # para leer la primera línea

for index in names_file.readlines():
    print(index)

names_file.close()