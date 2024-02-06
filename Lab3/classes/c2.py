class Shape:
    def __init__(self):
        self.A = 0
    def area(self):
        print(self.A)

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
        self.A = length ** 2

b = Square(6)
b.area()