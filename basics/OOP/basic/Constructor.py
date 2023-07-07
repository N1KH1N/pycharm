# constructor
# to initialise the object at the same time as it is created
class person:
    def __init__(self,name,place,age):
        self.name=name
        self.location=place
        self.age=age
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.location)
p1=person("anu","kakkanad",22)
p1.printvalue()