# Write a Python program that matches a string that has an 'a' followed by 5 numbers, ending in 'b'?

import re
rule='[a]\d{5}[b]'
s=input("enter string:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")