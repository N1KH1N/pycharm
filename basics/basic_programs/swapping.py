num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))

print("before swapping the value of num1 =",num1)
print("before swapping the value of num2 =",num2)

# swapping
# method 1
# a=num1
# num1=num2
# num2=a

# method 2
# tuple unpacking concept
# num1,num2=num2,num1

# method 3
#  num1=5 num2=10
num1=num1+num2 #num1=15
num2=num1-num2 #num2=5
num1=num1-num2 #num1=10

print("after swapping the value of num1 =",num1)
print("after swapping the value of num2 =",num2)