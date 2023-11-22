#__init__ is dundr method (double underscore) alsoo magic method
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