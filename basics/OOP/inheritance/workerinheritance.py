class Person:
    def setvalue(self,name,place,age):
        self.name1=name
        self.location=place
        self.age=age
    def printdata(self):
        print(self.name1)
        print(self.age)
        print(self.location)
class Parent:
    def setparent(self,address,phone):
        self.address=address
        self.phone=phone
class Employee(Person,Parent):
    def setemp(self,designation,salary):
        self.desig=designation
        self.salary=salary
    def printemp(self):
        print(self.name1,self.desig,self.age,self.salary,self.location,self.phone)
emp=Employee()
emp.setvalue("nikhin","kochi",22)
emp.setparent("kochi",9497632541)
emp.setemp("devloper",54000)
emp.printemp()

