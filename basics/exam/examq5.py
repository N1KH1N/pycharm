f1=open('text.txt','r')
for i in f1:
    count={}
    l=i.split(" ")
    for i in l:
        if i not in count:
            count.update({i:1})
        else:
            val=count[i]
            val=val+1
            count.update({i:val})
    print(count)


# logic 2
# f=open('text.txt','r')
# all=[]
# count={}
# for i in f:
#     d=i.rstrip("\n").split(" ")
#     all.extend(d)
#     print(all)
#         if i not in count:
#             count.update({i:1})
#         else:
#             val=count[i]
#             val=val+1
#             count.update({i:val})
# print(count)