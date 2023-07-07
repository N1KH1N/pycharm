def palindrome(s):
    rev=(s[::-1])
    if s==rev:
        return "yes,the given string is a palindrome"
    else:
        return "no,it is not a palindrome"
s=input("enter the string:")
print(palindrome(s))