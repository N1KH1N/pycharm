l=[10,20,20,30,10,40,20,10,30,50]
count={}
for i in l:
    if i not in count:
        count[i]=1
    else:
        val=count[i]
        val+=1
        count[i]=val
print(count)


