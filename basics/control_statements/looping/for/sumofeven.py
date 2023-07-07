start=int(input('enter starting range:'))
end=int(input('enter ending range:'))
sum=0

for i in range(start,end):
    if i%2==0:
        # sum=sum+i
        sum+=i
print('the sum of even numbers b/w',start,"and",end,"is",sum,end='')
