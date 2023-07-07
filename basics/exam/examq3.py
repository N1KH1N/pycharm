# code to find the name of Student who scored maximum mark? Students=[('anu',67),('amal',69),('arun',65)]

student=[('anu',67),('amal',69),('arun',65)]
for i in student:
    a,b,c=student
if a[1]>b[1]:
    if a[1]>c[1]:
        print(a[0])
elif b[1]>a[1]:
    if b[1]>c[1]:
        print(b[0])
else:
    print(c[0])


# second logic
# student=[('anu',67),('amal',69),('arun',65)]
# marks=[]
# for i in student:
#     marks.append(i[1])
# high=max(marks)
# for j in student:
#     if j[1]==high:
#         print(j[0])