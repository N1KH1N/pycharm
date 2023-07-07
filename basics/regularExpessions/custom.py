# starting and ending a number
# uppercase and lowercase

import re
rule='\d[a-zA-Z]{1,}\d'       #'\d[a-zA-Z]+\d'
s=input("enter string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")