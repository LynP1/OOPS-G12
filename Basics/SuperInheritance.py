import setuptools


class Rectangle():

    type = 'Type of: Rectangle'

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return ((2*self.length)+(2*self.width))
    
rec_1 = Rectangle(5,23)

print(rec_1.type)

class Square(Rectangle):

    type = 'Type of: Square'

    def __init__(self,length):
        super().__init__(length,length)

sqr_1 = Square(2)
print(sqr_1.type)
print(sqr_1.area())