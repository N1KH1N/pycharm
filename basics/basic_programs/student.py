chemistry=float(input("Enter the Mark of chemistry:"))
maths=float(input("Enter the Mark of Maths:"))
physics=float(input("Enter the Mark of Physics:"))
total=chemistry+maths+physics
average=total/3
print("The Total Marks Obtained is",total)
print("Your Average Mark is",average)
if (chemistry>=50 and maths>=50 and physics>=50):
    print("yaay,You have Passed")
# if chemistry<50:
#     print("sorry,you have failed")
# elif maths<50:
#     print("sorry,you have failed")
# elif physics<50:
#     print("sorry,you have failed")
else:
    print("yaay,You have Passed")
