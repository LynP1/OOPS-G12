#creating child classes
class Shape():
    def __init__(self,l,w):
        self.length,self.width = l,w

    def print_size(self):
        print('Length: %d | Width: %d' %(self.length,self.width))

class Square(Shape):
    def __init__(self, l):
        self.length,self.width = l,l