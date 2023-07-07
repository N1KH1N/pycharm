# map()   (no. of input set value should be equal to output set values)
# filter()      (no. of input value may not be equal to no. of output value)

l=[1,2,3,4,5,6,8,9]

# square list       -map
# map(function,iterable data)
def square(n):
    return n**2
new=list(map(square,l))
print(new)
# newl=list(map(lambda n:n**2,l))
# print(newl)


# odd and even sets     -filter
s=[1,4,5,3,55,77,44,65,35,65]
even=set(filter(lambda n:n%2==0,s))
print(even)

odd=set(filter(lambda n:n%2!=0,s))
print(odd)


