start=int(input("enter starting range:"))
end=int(input("enter ending range:"))
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
