# Number 1
class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        return ((2*self.length) + (2*self.width))
    
class Square():
    def __init__(self,length):
        self.length = length

    def perimeter(self):
        return (4*self.length)
    
rec_1 = Rectangle(3,4)
sqr_1 = Square(6)

print(rec_1.perimeter())
print(sqr_1.perimeter())

# Number 2
class Square():
    def __init__(self,length):
        self.length = length

    def perimeter(self):
        return (4*self.length)
    
    def change_size(self, change):
        self.length += change

sqr_1 = Square(6)
print(sqr_1.perimeter())
sqr_1.change_size(4)
print(sqr_1.perimeter())

# Number 3
class Shape():
    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        return ((2*self.length) + (2*self.width))

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def perimeter(self):
        return (4*self.length)
    
    def change_size(self, change):
        self.length += change

rec_1 = Rectangle(3,4)
sqr_1 = Square(6)

rec_1.what_am_i()
sqr_1.what_am_i()

# Number 4
class Rider():
    def __init__(self,name):
        self.name = name

class Horse():
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

Thiago = Rider('Thiago')
Min = Horse('Min',Thiago)