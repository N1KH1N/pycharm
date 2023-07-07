# Create a child class Bus that will inherit all of the variables and methods of Vehicle class?

class Vehicle:
    def data(self,name,speed,capacity):
        self.name=name
        self.speed=speed
        self.capacity=capacity
    def printd(self):
        print(self.name)
        print(self.speed)
        print(self.capacity)
class Bus(Vehicle):
    def data2(self,milege):
        self.milege=milege
    def printfinal(self):
        print(self.name)
        print(self.speed,self.milege)
        print(self.capacity)
obj=Bus()
obj.data("volvo",80,34)
obj.data2(21)
obj.printfinal()

