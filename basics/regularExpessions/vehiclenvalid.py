import re
rule='[Kk][lL][0-9]{2}[a-zA-Z]{2}[0-9]{4}'
n=input("enter vehicle number:")
match=re.fullmatch(rule,n)
if match is not None:
    print("valid vehicle number")
else:
    print("invalid")