# sum of natural nums
# 5= 5+4+3+2+1



def sumofn(n):
    if n==0:
        return n
    else:
        return n+sumofn(n-1)           #n+sum(n-1)      #5+sumofn(4)=5+10=15
                                                          #4+sumofn(3)=4+6=10
                                                            #3+sumofn(2)=3+3=6
                                                              #2+sumofn(1)=2+1=3
                                                                #1+sumofn(0)=1+0=1
                                                                  #0

print(sumofn(5))

