def element(s):
    a=s[-2:]+s[:-2]
    return a
# return s[-2:]+s[:-2]             to avoids variable "a"
s=input("enter the string:")
print(element(s))