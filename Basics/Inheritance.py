#creating child classes
class Shape():
    def __init__(self,l,w):
        self.length,self.width = l,w

    def print_size(self):
        print('Length: %d | Width: %d' %(self.length,self.width))

class Square(Shape):
    def __init__(self, l):
        self.length,self.width = l,l

shape_1 = Shape(30,40)
shape_1.print_size()

square_1 = Square(5)
square_1.print_size()