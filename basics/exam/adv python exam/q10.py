# Write a Python program to find the sequences of one upper case letter followed by lower case letters/special characters?

import re
def validation(n):
    rule = '[A-Z]+[a-z\W]'
    if re.search(rule,n):
        print("match found")
    else:
        return("no match found")

print(validation("hsdghbjdhbj"))
print(validation("sdaA5%$$S&"))
print(validation("SDFGHJ@#$%^&"))
print(validation("asdfg$"))
print(validation("ASDF2345"))
print(validation("Aasdfghj"))







