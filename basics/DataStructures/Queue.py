# queue
# uses first in first out (FIFO) principle

# Operations
# 1.enqueue(add element)
# 2.dequeue(remove element)

queue=[]
size=int(input("enter queue size:"))
flag=0

def enqueue():
    global  flag
    if flag>=size:
        print("queue full")
    else:
        e=int(input("enter element to enqueue:"))
        queue.append(e)
        print(queue)
        flag+=1

def dequeue():
    global flag
    if flag==0:
        print("queue is empty !!!")
    else:
        queue.remove(queue[0])
        print(queue)
        flag-=1

while True:
    option = int(input("\nOperation \n1.enqueue \n2.dequeue \nSelect the operation:"))
    if option == 1:
        enqueue()
    elif option == 2:
        dequeue()
    else:
        print("invalid operation")