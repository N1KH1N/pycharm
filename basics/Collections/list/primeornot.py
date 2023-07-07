l=[1,2,3,4,5,6,7,8,9,10]
np=[]
p=[]
for i in l:
    for j in range(2,i):
        if i%j==0:
            np.append(i)
            break
    else:
        p.append(i)

print(p)
print(np)
