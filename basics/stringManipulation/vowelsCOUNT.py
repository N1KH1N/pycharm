s="aeiou"
v=input("enter the word:")
flag=0

for i in v:
    if i in s:
    # if i==s:  ......................
        flag=flag+1
print(flag)