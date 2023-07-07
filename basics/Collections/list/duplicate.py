s=[1,3,5,6,7,8,2,3,1,2,3]
print(len(s))
l=[]
for i in s:
    if i not in l:
        l.append(i)
    else:
        print(i)

# first recursive
# second recursive
# last recursive

s = [1, 3, 5, 6, 7, 8, 2, 3, 1, 2, 3]
print(len(s))
l = []
rep = []
for i in s:
    if i not in l:
        l.append(i)
    else:
        if i not in rep:
            rep.append(i)

print(rep)