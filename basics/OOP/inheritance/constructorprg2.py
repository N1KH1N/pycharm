class Person:
    def __init__(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
class Parent:
    def __init__(self,address,phone):
        self.address=address
        self.phone=phone
class Employee(Person,Parent):
    def __init__(self,designation,salary,name,place,age,address,phone):
        Person.__init__(self,name,place,age)
        Parent.__init__(self,address,phone)
        self.desig=designation
        self.salary=salary
    def printemp(self):
        print(self.name1,self.desig,self.age,self.salary,self.location,self.phone)
emp=Employee("dev",59000,"nikhin","palakkad",21,"kallingal",9497632541)
emp.printemp()