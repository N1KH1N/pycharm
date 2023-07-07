# Find out a pair of elements which form a particular value as sum from a given array?
# For eg: arr=[2,3,4,5,6] print elements having sum=9
# o/p :   pairs which give sum=9  is (3,6),(4,5)

arr=[2,3,4,5,6]
sett=set()
sum=9
for i in arr:
    for j in arr:
        if i+j==sum:
            sett.add(i)
            sett.add(j)
print(sett)

