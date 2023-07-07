def evensum(start,end):
    sum=0
    for i in range(start,end):
        if i%2==0:
            sum=sum+i
    print("the sum is:",sum)
# start = int(input("enter stating range:"))
# end = int(input("enter ending range:"))

evensum(1,10)
