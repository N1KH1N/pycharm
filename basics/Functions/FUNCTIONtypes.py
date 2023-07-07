# 1.function without argument

# def factorial():
#     s=int(input('enter the digit:'))
#     flag=1
#     for i in range(1,s+1):
#         flag=flag*i
#     print(flag)
#
# factorial()



# 2.function with arguments

# def add(num1,num2):
#     sum=num1+num2
#     print(sum)
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
#
# add(a,b)
# add(22,73)

# def factorial(s):
#     flag=1
#     for i in range(1,s+1):
#         flag=flag*i
#     print(flag)
#
# factorial(8)




# 3.function with arguments and return
def add(num1,num2):
    sum=num1+num2
    return sum
# print(add(12,46))
res=add(23,75)
print(res)

# rules
# no code can be given after the return statements
# multiple values cannot be returned using return statements
# (only single value can be given. it can be arithmatic operations)
# only one return statement is allowed in one block
# but there can be multiple return statements in the single function
# when the return statement works the rest of the code in that block stops working
# (-just like break statement)
# iterative elements cannot be printed using return statement


def posnegcheck(n):
    if n>0:
        return "positive"
    elif n==0:
        return "zero"
    else:
        return "negative"
print(posnegcheck(-5))



def printnum(a,b):
    for i in range(1,b+1):
        return i
print(printnum(1,10))                #output=1 (loop stops)


