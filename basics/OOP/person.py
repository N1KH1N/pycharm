class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printdata(self):
        print(self.name)
        print(self.age)
        print(self.place)

f=open('dat.txt','r')
l=[]
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    place=data[2]
    p=Person(name,age,place)
    l.append(p.name)
    p.printdata()
print(l)