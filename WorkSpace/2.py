# write a python program to print the frequency of each element in a given list   (count of nums)

ex=[1,2,7,7,7,8,2,2,1,1,1,4,3]
count={}

for i in ex:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

# for i,count in  count.items():
#     print(f"{i}:{count}")

