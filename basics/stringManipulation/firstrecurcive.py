s=input("enter the string:")
flag=""
for i in s:
    if i not in flag:
        flag=flag+i
    else:
        print(i)
        break

        