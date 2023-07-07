d={1:100,2:200,3:300,4:400,5:500}
key=int(input("enter the key to search:"))

for i in d.keys():
    if i==key:
# if key in d:  direct check   (should avoid break)
        print("present")
        break
else:
    print("not present")


