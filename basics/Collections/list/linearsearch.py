l=[2,4,5,6,8,9,13,21,35,55,88]
# e=8

def linear(e):
    count=0
    for i in l:
        count=count+1
        if i==e:
            print("present")
            break
    else:
        print("not present")
    print(count)



linear(48)