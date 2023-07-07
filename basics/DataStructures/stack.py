# stack
# uses last in first out (LIFO) principle

# operations in stack
# 1.push  -  add element  ...stack full
# (can only add if not full)
# (need to check if stack is full or not)

# 2.pop  -  remove element
# (need to check if the stack is empty)

# 3.display

# list
stack=[]
size=int(input("enter stack size:"))
top=0

def push():
    global top
    if top>=size:
        print("stack full")
    else:
        e=int(input("enter element to push:"))
        stack.append(e)
        print(stack)
        top+=1

def pop():
    global top
    if top==0:
        print("stack empty")
    else:
        stack.pop()
        print(stack)
        top-=1

while True:
    option=int(input("\nOperation \n1.push \n2.pop \nSelect the operation:"))
    if option==1:
        push()
    elif option==2:
        pop()
    else:
        print("invalid operation")