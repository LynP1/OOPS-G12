class Item():
    def __init__(self):
        pass

class Food(Item):
    pass

class Weapon(Item):
    pass

class Material(Item):
    pass

class Being():
    def __init__(self):
        self.health = 100
        self.damage = 5

class Player(Being):
    def __init__(self,name):
        self.name = name
        self.exp = 0
        self.level = 1
        self.health = 100
        self.damage = 5
        self.inventory = []

class Enemy(Being):
    def __init__(self):
        self.level = 1
        self.health = 100
        self.damage = 5
        self.drop_table = []