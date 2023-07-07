#write a program to calculate electricity bill

n=int(input("enter the unit consumed:"))

if n<=100:
    s=0
    print("no cost")
elif n<=200:
    s=0+(n-100)*5
    print("5 per unit:")
else:
    s=500+(n-200)*10
    print("10 per unit:")
print(s)