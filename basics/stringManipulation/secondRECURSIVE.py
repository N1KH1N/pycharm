s=input("enter the string:")
a=""
rep=""
for i in s:
    if i not in a:
        a=a+i
    else:
        if i not in rep:
            rep=rep+i
print("first recursive:",rep[0])
print("second recursive:",rep[1])
print("last recursive:",rep[-1])
