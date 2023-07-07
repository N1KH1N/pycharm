import re
x='[p][y]\d{4}'
f=open('reg.txt','r')
f1=open('pyreg.txt','w')
for i in f:
    d=i.rstrip("\n")
    print(d)
    match=re.fullmatch(x,d)
    if match is not None:
        f1.write(i)



