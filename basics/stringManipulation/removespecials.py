# s=input("enter the string:")
# b="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPAASDFGHJKLZXCVBNM"
# flag=""
# for i in s:
#     if i in b:
#         flag=flag+i
# print(flag)

s=input("enter the string:")
b='''~`!@#$%^&*()_+=-][{}":';/?.><,'''
flag=""
for i in s:
    if i not in b:
        flag=flag+i
print(flag)