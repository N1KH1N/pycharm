a=int(input("enter first number:"))
b=int(input("enter second number:"))
try:
    print("in try")
    print(a/b)
except Exception as e:
    print(e)

