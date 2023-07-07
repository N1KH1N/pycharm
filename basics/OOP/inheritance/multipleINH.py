# multiple inheritance

class A:
    def printa(self):
        print("inside A class")
class B:
    def printb(self):
        print("inside B class")
class C(A,B):
    def printc(self):
        print("inside C ")
obj=C()
obj.printc()
obj.printa()
obj.printb()