f=open('copy.txt','r')
for i in f:
    d=i.rstrip('\n')
f = open('new.txt', 'w')
f.write(i)

f1=open('copy.txt','r')
f2=open('new.txt','w')
for i in f:
    f2.write(i)


