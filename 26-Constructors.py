class Point:
    def __init__(self, x, y):   #CONSTRUCTOR crea el objeto
        self.x = x              #Son valores de inicializacón
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)