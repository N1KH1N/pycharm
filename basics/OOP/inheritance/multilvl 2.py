# class Person:
#     def setperson(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def printperson(self):
#         print(self.name)
#         print(self.age)
#         print(self.place)
# class Child(Person):
#     def setchild(self,adress,phone):
#         self.add=adress
#         self.phone=phone
#     def printchild(self):
#         print(self.add)
#         print(self.phone)
# class Student(Child):
#     def setstudent(self,roll,dep):
#         self.roll=roll
#         self.dep=dep
#     def printstudent(self):
#         print(self.name,self.age,self.place,self.add,self.phone,self.roll,self.dep)
#
# st=Student()
# st.setperson("aji",21,"palakkad")
# st.setchild("kallingal house","9372524382")
# st.setstudent(10,"MicroBio")
# st.printstudent()
#


# using constructor

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name)
        print(self.age)
        print(self.place)
class Child(Person):
    def __init__(self,adress,phone,name,age,place):
        super().__init__(name,age,place)
        self.add=adress
        self.phone=phone
    def printchild(self):
        print(self.add)
        print(self.phone)
class Student(Child):
    def __init__(self,adress,phone,roll,dep,name,age,place):
        super().__init__(adress,phone,name, age, place)
        self.roll=roll
        self.dep=dep
    def printstudent(self):
        print(self.name,self.age,self.place,self.add,self.phone,self.roll,self.dep)

st=Student("abc",9536575467,21,"bca","nikhin",22,"pkd")
st.printstudent()
