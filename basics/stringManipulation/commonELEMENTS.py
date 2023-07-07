s1="abcd"
# s1=input("enter the string:")
# s2=input("enter second string:")
s2="cdef"
flag=""
for i in s1:
    if i in s2:
        flag=flag+i
print(flag)