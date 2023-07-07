d=dict()
print(d)
print(type(d))

# d1={}
# print(d1)
# print(type(d1))

# add element
# method 1
# can add single and multiple element
d.update({1:8,2:5})
print(d)
print(d.keys())
print(d.values())

# method 2
d[4]=100
print(d)

# update
d[1]=10
print(d)
