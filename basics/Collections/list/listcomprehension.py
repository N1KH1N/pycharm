# l=[1,4,7,8,9,3,2]
# square=[]
# for i in l:
#     square.append(i**2)
# print(square)

# l=[1,4,7,8,9,3,2]
# square=[i**2 for i in l]
# print(square)


# l=[1,4,7,8,9,3,2]
# even=[i for i in l if i%2==0]
# print(even)

# odd=[i for i in range(1,20+1) if i%2!=0]
# print(odd)

name=["anu","amal","vinay","ebin","rahul","nivya","megha"]
namewithvowel=[i for i in name if i[0] in "aeiou"]
print(namewithvowel)