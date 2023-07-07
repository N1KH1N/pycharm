# object oriented programming

# class  --  blueprint/design pattern
# also known as collection of objects

# objects  --  real world entity

# reference  --  to perform operations on object and to store each objects

# self  --  instance keyword


class Person:
    def read(self):
        print("person is reading")
    def walk(self):
        print("person is walking")

# reference=object_creation
obj=Person()
# call methods
obj.walk()
obj.read()

obj2=Person()
obj2.read()
