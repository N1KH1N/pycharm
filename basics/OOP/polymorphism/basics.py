# method overloading
# method overriding

# pverloading
# methods name are same but different number of argumets

# class A:
#     def printa(self):
#         print("inside a")
#
# class B(A):
#     def printa(self,num):
#         self.num=num
#         print("inside b")
#
# obj=B()
# obj.printa()
# obj.printa(8)

# overriding
# both method name and number of arguments will be the same
# child class method  overrides parent class method


class Parent:
    def cart(self):
        print("control premium edition")

class Child(Parent):
    def cart(self):
        print("Legion Standard Edition")

s=Child()
s.cart()


# class
# object
# reference
# variable type- static,instance
# constructor- to initialise object at the same time of creation
# inheritance-to access the properties of one in another class
#
#                                     (methods and variables)
# polymorphism  --  overriding,overloading
# abstraction
# encapsulation