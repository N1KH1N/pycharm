for i in range(5):
    for j in range(i):
        if i==3 and j==1:
            print(end="  ")
        else:
            print("*",end=" ")
    print()