s=input("enter the string:")
flag=""
for i in s:
    if i not in "aeiou":
        flag=flag+i
print(flag)