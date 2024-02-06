from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self,p):
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

p1 = Point(3,4)
p1.show()
p1.move(4, -5)
p1.show()
p1.move(-4, 5)

O = Point(0,0)
print(p1.dist(O))
p1.show()