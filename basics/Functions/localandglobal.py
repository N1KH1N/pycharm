# local and global variable
# num=10
def printnumber():
    global num,x
    x=9
    num=8
    print(num,x)
printnumber()

print(num)