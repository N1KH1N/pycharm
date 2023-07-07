# regular expression
# pattern matching
# re   (package)


# methods used
# 1.finditer
# 2.fullmatch


import re
s="aaaabbbbaaab"
var=re.finditer('ab',s)
c=0
for i in var:
    c+=1
    print("match start at",i.start())
    print("match group",i.group())
print(c)