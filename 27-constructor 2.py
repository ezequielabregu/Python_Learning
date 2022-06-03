class Person:
    def __init__(self, name):           # CONSTRUCTOR
        self.name = name                # defino el parámetro de la class Person
    def talk(self):                     # defino la function
        print(f"Hi, I am {self.name}")

john = Person("John Smith")             # OBJETO john, de la class Person
print(john.name)                        # imprimo el parámetro name del objeto john
john.talk()                             # imprimo del OBJETO john, la función talk de la CLASS Person

bob = Person("Bob Mills")               # cada OBJETO es una instancia distinta de la CLASS Person
bob.talk()