# file operation methods in python

# read 'r'
# write 'w'
# append 'a'

# read
f=open('data.txt','r')
# print(f)
for i in f:
    d=i.rstrip('\n')
    print(d)