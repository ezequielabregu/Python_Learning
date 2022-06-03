class Mammal:               # creo Class Mammal
    def walk(self):         # creo la función
        print("walk")

class Dog(Mammal):          # creo Class y uso la Class mammals como argumento
    def bark(self):
        print("bark")

class Cat(Mammal):
    def annoy(self):
        print("annoying")

class Animal(Mammal):
    pass                    #pass para que el interpreter no se queje

dog1 = Dog()                # creo objeto dog1 llamando la clase Dog
dog1.bark()

cat1 = Cat()
cat1.annoy()
