s="hello hi hello"
count={}
data=s.split(" ")
for i in data:
    if i not in count:
        count.update({i:1})
    else:
        val=count[i]
        val+=1
        count.update({i:val})
print(count)

