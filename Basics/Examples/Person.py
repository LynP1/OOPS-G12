from random import choice

food = ['apple','pizza','burger','carrot','bacon','cheese','tomato','potato','chips']
action = ['jumps','runs','falls','sprints','flies','teleports','disapears']

class Person():
    description = 'Normal person'

    def __init__(self,name,age):
        self.name, self.age = name, age

    def speak(self):
        print('%s says: My name is %s and I am %d years old.' %(self.name,self.name,self.age))

    def eat(self):
        print('%s eats %s' %(self.name,choice(food)))

    def action(self):
        print('%s %s' %(self.name,choice(action)))

class Baby(Person):
    def speak(self):
        print('%s says: Goo goo ga ga' %(self.name))

    def nap(self):
        print('%s takes a nap' %(self.name))

Silva = Person('Silva',39)
Silva.speak()
Silva.eat()
Silva.action()

Son = Person('Son', 31)
Son.speak()
Son.eat()
Son.action()

Giovanni = Person('Giovanni Giorgio', 83)
Giovanni.speak()

Bob = Baby('Bob',2)
Bob.speak()
Bob.nap()