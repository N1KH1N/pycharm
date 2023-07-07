space=5
for i in range(5):
    for x in range(space):
        print(end=" ")
    space=space-1
    for j in range(i):
        if i==3 and j==1:
            print(end="  ")
        else:
            print("*",end=" ")
    print()