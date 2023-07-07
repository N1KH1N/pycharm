space=1
for row in range(6,0,-1):
    for k in range(space):
        print(end=" ")
    space+=1
    for col in range(row):
            print("*",end=" ")
    print()