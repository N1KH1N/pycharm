class Person:
    def per(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
        print("inside 1")
class Student(Person):
    def std(self,roll,dep,col):
        self.roll=roll
        self.dep=dep
        self.col=col
    def printall(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.roll)
        print(self.dep,self.col)
p1=Student()
p1.per("nikhin","palakkad",21)
p1.Std(5,"bca","sngc")
p1.printall()



