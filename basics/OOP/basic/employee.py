class Employee:
    def setvalue(self,empid,empname,age,designation,salary):
        self.id=empid
        self.name=empname
        self.age=age
        self.position=designation
        self.salary=salary
    def printvalue(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.salary)
p1=Employee()
p1.setvalue(88,"nikhin",21,"devops",20000)
p1.printvalue()

p2=Employee()
p2.setvalue(55,"dinoop",21,"javadev",18000)
p2.printvalue()