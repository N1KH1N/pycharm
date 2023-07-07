# import re
# s='aaa abbb aaaaa aa @ 123'
# x='a+'   #'[abc]+'
# matcher=re.finditer(x,s)
# # print(matcher)
# count=0
# for i in matcher:
#     count+=1
#     print("match starts at",i.start())
#     print("match group",i.group())
# print(count)

# import re
# s='aaa abbb aaaaa aa @ 123'
# x='a*'   #'a?'-match each element(a? match each element not as group)
# matcher=re.finditer(x,s)
# # print(matcher)
# count=0
# for i in matcher:
#     count+=1
#     print("match starts at",i.start())
#     print("match group",i.group())
# print(count)



# import re
# s='aaa abbb aaaaa aa @ 123'
# x='a{3}'    here 3 is the count of a
# matcher=re.finditer(x,s)
# # print(matcher)
# count=0
# for i in matcher:
#     count+=1
#     print("match starts at",i.start())
#     print("match group",i.group())
# print(count)


# import re
# s='aaa abbb aaaaa aa @ 123'
# x='^a'   #here ^ doesn't mean except instead it mean the starting of a word
# matcher=re.finditer(x,s)
# # print(matcher)
# count=0
# for i in matcher:
#     count+=1
#     print("match starts at",i.start())
#     print("match group",i.group())
# print(count)

import re
s='aaa abbb aaaaa aa @ 123'
x='a$'    #here $ check for ending letter
matcher=re.finditer(x,s)
# print(matcher)
count=0
for i in matcher:
    count+=1
    print("match starts at",i.start())
    print("match group",i.group())
print(count)