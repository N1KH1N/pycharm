cost=int(input("enter the cost:"))
if cost>100000:
    print("15% tax")
elif cost>50000<=100000:
    print("10% tax")
else:
    print("5% tax")
