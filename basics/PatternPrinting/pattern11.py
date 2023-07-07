space=6
for i in range(6):
    for x in range(space):
        print(end=" ")
    space=space-1
    for j in range(i):
        print("@",end=" ")
    print()

space=0
for i in range(6,0,-1):
    for x in range(space):
        print(end=" ")
    space+=1
    for j in range(i):
        print("@",end=" ")
    print()