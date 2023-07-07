space=5
for row in range(5):
    for col in range(space):
        print(end=" ")
    space-=1
    for col in range(row):
        print(col*row,end=" ")
    print()
