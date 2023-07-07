# select an operation
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.stop


# if 1 num1,num2,res
# if other than 1 to 5 invalid operation
# 5= process finish

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

while True:
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.stop")
    # print(("Select Operation:"))
    op=int(input("select operation:"))
    num1 = float(input("enter number 1:"))
    num2 = float(input("enter number 2:"))
    if op==5:
        break
    elif op==1:
        num1 = float(input("enter number 1:"))
        num2 = float(input("enter number 2:"))
        print(add(num1,num2))
    elif op==2:
        print(sub(num1,num2))
    elif op==3:
        print(mul(num1,num2))
    elif op==4:
        print(div(num1,num2))
    # elif op==5:
    #     break
    else:
        print("input invalid")




