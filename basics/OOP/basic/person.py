class person:
    def setvalue(self,name,place,age):
        # to use the arguments of one function in another function we use "self"
        # here we can use name ,place,age in another function
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.location)
        print(self.age)
p1=person()
p1.setvalue("anu","kottayam",24)
p1.printdata()

p2=person()
p2.setvalue("nikhin","palakkad",21)
p2.printdata()