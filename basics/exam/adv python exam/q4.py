# Create an Animal class using constructor and build a child class  Dog?

class Animal():
    def __init__(self,name,food):
        self.name=name
        self.food= food
    def intro(self):
        print("I am", self.name, "and I love ",self.food)
class Dog(Animal):
    def _init__(self, name, food):
        self.name = name
        self.food = food
        self.type ="dog"

jacky = Dog("jacky", "meat")
jacky.intro()