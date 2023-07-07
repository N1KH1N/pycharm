import re
x='[+][9][1][0-9]{10}'
n=input("enter number:")
match=re.fullmatch(x,n)
if match is not None:
    print("valid number")
else:
    print("invalid number")


