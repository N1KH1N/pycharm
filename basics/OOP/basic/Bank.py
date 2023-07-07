class Bank:
    def account(self,name,accno):
        self.name=name
        self.acc=accno
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("your account has been credited with",self.amount)
        print("your available balance is",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if(self.amount<=self.balance):
            self.balance=self.balance-self.amount
            print("your account has been debited with amount",self.amount)
            print("available balance is",self.balance)
        else:
            print("insufficient balance available")



s1=Bank()
s1.account("nikhin",8973636262)
s1.deposit(5585)
s1.withdraw(1200)







