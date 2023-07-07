def factorial(s):
    flag=1
    for i in range(1,s+1):
        flag=flag*i
    return flag
s=int(input("enter the digit:"))
print(factorial(s))
