def add(n1,n2):
    print(n1+n2)

def sub(n1,n2):
    print(n1-n2)

def mul(n1,n2):
    print(n1*n2)

def div(n1,n2):
    print(n1/n2)

while True:
    option=int(input("select an operation\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Cancel"))
    if option==5:
        break
    elif option>0 and option<5:
        n1=float(input("enter num 1:"))
        n2=float(input("enter num 2:"))

        if option==1:
            add(n1,n2)

        elif option==2:
            sub(n1,n2)

        elif option==3:
            mul(n1,n2)

        else:
            div(n1,n2)

    else:
        print("invalid option")


