s=int(input("enter the number:"))
flag=0
for i in range(2,s):
    if s%i==0:
        flag=flag+1
if flag<2:
    print("the number is prime")
else:
    print("the number is not prime")

# for i in range(2,s):
#     if s%i==0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")