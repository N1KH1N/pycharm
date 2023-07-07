# inheritance
# to use properties (methods and variables) of a class in another class

# single inheritance
class A: #  --  parent class/base class/super class
    def printa(self,num):
        self.num=num
        print("inside A class")

class B(A):
    def printb(self):
        print("inside B class",self.num)

obj=B()
obj.printa(8)
obj.printb()