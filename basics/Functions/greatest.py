def great(a,b):
    if a>b:
        return "first number is greatest"
    elif a==b:
        return "fist number is equal to second"
    else:
        return "second number is greatest"
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(great(a,b))