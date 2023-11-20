class Dog():
    def __init__(self,name,age,breed,owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

Son = Person('Son',31)
Min = Dog('Min',12,'Huskie',Son)

print(Min.owner.name)