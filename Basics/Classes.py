# Defining a Class3
class Orange:
    def __init__(self, c, w):
        self.colour = c
        self.weight = w

    def rot(self, hours, temp):
        days = hours / 24
        self.mold = round(days * temp,2)

# Instantiating an Object

navel_orange = Orange('Orange', 0.8)
blood_orange_2 = Orange('Red',0.6)
tangerine = Orange('Yellow-Org',0.4)
tangerine.rot(22,21)
print(tangerine.mold)

#Another Example

class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return (self.length*2) + (self.width*2)

    def change_size(self,l,w):
        self.length = l
        self.width = w

    def identify(self):
        print('Type of: Rectangle')

rec_1 = Rectangle(4,3)
rec_2 = Rectangle(9,4)
rec_3 = Rectangle(3,9)

print(rec_2.area())
rec_2.change_size(5,12)
print(rec_2.area())

print(rec_1.perimeter())
rec_3.identify()

#Another Example

class Door:
    def __init__(self, h, c, is_locked):
        self.height = h
        self.colour = c
        self.is_locked = is_locked

    def open(self):
        self.is_locked = False

    def close(self):
        self.is_locked = True

    def toggle_lock(self):
        if self.is_locked:
            self.is_locked = False
        elif not self.is_locked:
            self.is_locked = True

door_1 = Door(85,'Red',False)
door_2 = Door(95,'Purple',True)