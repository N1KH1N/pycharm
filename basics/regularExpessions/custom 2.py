import re
rule='[a][\w\W]*[b]'
s=input("enter string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")