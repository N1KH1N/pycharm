# s=input("enter the word:")
# v="aeiou"
# flag=""
# for i in s:
#     if i in v:
#         flag=flag+i
# print(flag)


s=input("enter the word:")
v="aeiou"
for i in s:
    if i in v:
        print(i,end='')
