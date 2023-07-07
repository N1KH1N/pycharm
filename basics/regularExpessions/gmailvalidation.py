import re
rule='[\d\w]+[@][g][m][a][i][l][.][c][o][m]'
s=input("enter mail id:")
match=re.fullmatch(rule,s)
if match is not None:
    print("valid")
else:
    print("Invalid")