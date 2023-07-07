# l1=[1,2,3,4]
# l2=[5,6,7,8]
# for i in l1:
#     l2.append(i)
# print(l2)


l1=[1,2,3,4]
l2=[5,6,7,8]
l2.extend(l1)
print(l2)