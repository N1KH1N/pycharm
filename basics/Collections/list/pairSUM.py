l=[1,2,3,4,5,6]
sum=int(input("enter the sum:"))
count=0
for i in l:
    for j in l:
        if i+j==sum:
            print(i,j)