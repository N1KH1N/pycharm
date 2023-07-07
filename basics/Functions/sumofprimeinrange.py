start=int(input("enter starting range:"))
end=int(input("enter ending range:"))
sum=0
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)



