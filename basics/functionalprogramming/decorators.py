# decorators
# to provide extra rule or conditon to the created function
def changev(fn):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return fn(a,b)
        else:
            return fn(a,b)
    return wrapper

@changev
def substract(a,b):
    print(a-b)
substract(3,9)
substract(10,5)

@changev
def div(n1,n2):
    print(n1/n2)
div(3,9)