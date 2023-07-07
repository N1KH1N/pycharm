class A:
    def printa(self):
        print("inside a")

class B(A):
    def printb(self):
        print("inside b")

class C(B):
    def printc(self):
        print("inside c")

obj=C()
obj.printc()
obj.printb()
obj.printa()
