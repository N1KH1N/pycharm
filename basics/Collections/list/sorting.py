l=[4,2,3,6,7,8,9,1,5]
n=[]
# l.sort()
# print(l)

# without sort
while l: #only false when l is empty
    min=l[0]
    for i in l:
        if i<min:
            min=i
    n.append(min)
    l.remove(min)
print(n)
print(l)
