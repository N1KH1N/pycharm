import re
rule='^0\d{3}0$'
s=input("enter string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")

