# Defining a Class

class Orange:
    def __init__(self, c, w):
        self.colour = c
        self.weight = w

    def rot(self, hours, temp):
        days = hours / 24
        self.mold =  round(days * temp,2)

# Instantiating an Object

navel_orange = Orange('Orange', 0.8)
blood_orange_2 = Orange('Red',0.6)
tangerine = Orange('Yellow-Org',0.4)
tangerine.rot(22,21)
print(tangerine.mold)