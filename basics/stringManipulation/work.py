for i in range(5):
    for j in range(3):
        if j==2 and i==3:
            break
        else:
            print(j)
    else:
        print(i)
        break