import re
x='+[9][1]\d{10}'
f=open('q77.txt','r')
f1=open('q88.txt','w')
for i in f:
    d=i.rstrip("\n")
    print(i)
    match=re.fullmatch(x,i)
if match is not None:
    f1.write(i)