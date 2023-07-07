# tostring method
# __str__()

class Person:
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
    def printdata(self):
        print(self.name)
        print(self.place)
        print(self.age)
    def __str__(self):
        return self.name  #to print 2 value (self.name+self.place)

p=Person("anu","kochi",21)
p.printdata()
print(p)