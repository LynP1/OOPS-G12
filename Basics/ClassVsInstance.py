class Rectangle():

    recs = [] #class variable

    def __init__(self, width, length):
        #instance variables
        self.width = width
        self.length = length

        self.recs.append((self.length,self.width))

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (2*self.width) + (2*self.length)

    def size(self):
        return str(self.width)+' by '+str(self.length)
    
rec_1 = Rectangle(6,3)
print(rec_1.area())
print(rec_1.perimeter())
print(rec_1.size())
rec_2 = Rectangle(4,4)
print(rec_2.area())
print(rec_2.perimeter())
print(rec_2.size())
print(Rectangle.recs)

class Dog():

    species = 'mammal'

    def __init__(self,age,name):
        self.age = age
        self.name = name

Max = Dog(3,'Max')
print(Max.species)