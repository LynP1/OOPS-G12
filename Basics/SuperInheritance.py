class Rectangle():

    type = 'Type: Rectangle'

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

    type = 'Type: Square'

    def __init__(self,length):
        super().__init__(length,length)

sqr_1 = Square(2)
print(sqr_1.type)
print(sqr_1.area())

class Cube(Square):

    type = 'Type: Cube'

    def volume(self):
        return self.length**3

    def surface_area(self):
        return (self.area()*6)

    def family_tree(self):
        return (self.type + '| Child of ' + super().type)

cube_1 = Cube(4)
print(cube_1.family_tree())
print(cube_1.volume())
print(cube_1.surface_area())