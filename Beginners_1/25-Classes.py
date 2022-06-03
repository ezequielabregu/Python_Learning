class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point() # OBJETO point1 - llamo a la class Point
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw() # llamo a la function Draw dentro de la class Point

point2 = Point() # OBJETO point2 (es una instancia diferente de la anterior)
point2.x= 1
print(point2.x)

'''
CLASSES 

Numbers
Strings
Booleans
-----
List
Doctionaries
'''
