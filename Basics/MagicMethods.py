#__init__ is dundr method (double underscore) alsoo magic method

# MODIFYING __repr__

class Person():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        #Originally returns object type and position in memory <Meesa dont like>. Changes to return variable name
        return self.name

Son = Person('Son')

print(Son)

#Car class containing make model colour and mileage. Also modified __repr__ which prints out variables
class Car():
    def __init__(self, make, model, colour, mileage):
        self.make = make
        self.model = model
        self.colour = colour
        self.mileage = mileage

    def __repr__(self):
        return ('Class: %s\nMake: %s\nModel: %s\nColour: %s\nMileage: %d'%(self.__class__.__name__,self.make,self.model,self.colour,self.mileage))

Altima = Car('Nissan','Altima','Red',123000)

print(Altima)

# MODIFYING __add__

class Proton():
    def __init__(self,number):
        self.n = number

    def __add__(self,other):
        return abs(self.n+other.n)

x = Proton(-38)
y = Proton(15)

print(x+y)

class Basket():
    def __init__(self, contents):
        self.contents = contents

    def __add__(self,other):
        return self.contents + other.contents
    
    def __repr__(self):
        list_str = 'Items in Basket:\n'
        for i in range(len(self.contents)-1):
            list_str += str(i+1)+') '+self.contents[i]+'\n'
        list_str += str(len(self.contents))+') '+self.contents[len(self.contents)-1]
        return list_str

my_cart = Basket(input('Enter Basket Items Seperated By Commas (not spaces): ').split(','))
other_cart = Basket(input('Enter Basket Items Seperated By Commas (not spaces): ').split(','))
print(my_cart+other_cart)
print(my_cart)

# MODIFIYING __  __