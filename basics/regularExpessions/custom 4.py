import re
rule='[a][\d\w\W]{3,8}[b]'
s=input("enter string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")