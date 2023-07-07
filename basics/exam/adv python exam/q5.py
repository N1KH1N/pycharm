class Books:
    def bookdetail(self,name):
        self.name = name
        print(self.name,"is an top selling book of all time")
class Child(Books):
    def bookdetail(self,name):
        self.name=name
        print(self.name, "is an popular book")
obj=Child()
obj.bookdetail("Chainsaw man")

