space=5
for row in range(5):
    for k in range(space):
        print(end=" ")
    space-=1
    for col in range(row):
            print("*",end=" ")
    print()

# for row in range(5):
#     for k in range(row):
#         print(end=" ")
#     for col in range(row):
#             print("*",end=" ")
#     print()