# question= https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

n = int(input("enter number:"))

if n % 2 != 0:
    print("Weird")

elif n % 2 == 0:
    if n > 2 and n <= 5:
        print("Not Weird")
    elif n > 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")