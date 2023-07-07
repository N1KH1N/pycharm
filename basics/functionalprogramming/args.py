# * args  (arguments)

# def printn(n1,n2):
#     print(n1,n2)
# print()


# def printn(*args):
#     return args
# print(printn(8,58))
#  *args tuple

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(5,2,8))

