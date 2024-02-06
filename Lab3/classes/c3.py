from c2 import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__(self)
        self.length  = length
        self.width = width
        
    def area(self):
        self.A = self.length * self.width
        return self.A
