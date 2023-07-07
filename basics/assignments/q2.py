import re
rule='[a-zA-Z][\w\W]{8}[0-9]'
s=input("enter the string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("Valid")
else:
    print("Not Valid")