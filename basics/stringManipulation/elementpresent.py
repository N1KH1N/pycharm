# s="luminar technolab"
# e=input("enter the element to check:")
# flag=0
#
# for i in s:
#     if e==i:
#         flag=1
#         break
#
#
# if flag==1:
#     print("present")
# else:
#     print("absent")
# .........................................................



# for break else concept
# break inside for loop is necessary for the else to work
# either break or the else statement get executed

# for i in range(5):
#     if i==7:
#         print(i)
#         break
# else:
#     print('inside else')


# checking the element present using the (for break else) concept
# s="luminar technolab"
# e=input("enter the element to check:")
#
# for i in s:
#     if e==i:
#         print("present")
#         break
#
# else:
#     print("not present")

s="luminar technolab"
e=input("enter the element to check:")
# e should be single element
# to check the presence of a single element in an iterable object
if e in s:
    print("present")
else:
    print("not present")

# if e not in s:
#     print("not present")
# else:
#     print("present")