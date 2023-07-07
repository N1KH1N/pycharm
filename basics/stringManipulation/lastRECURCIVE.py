# last recursive element
s=input("enter the string:")
a=""
rep=""
for i in s:
    if i not in a:
        a=a+i
    else:
        rep=rep+i
print(rep[-1])


