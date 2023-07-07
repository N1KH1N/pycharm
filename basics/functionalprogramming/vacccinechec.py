def agecheck(f):
    def wrapper(a,b):
        if b>=18:
            return f(a,b)
        else:
            raise Exception("not eligible")
    return wrapper

@agecheck
def vaccine(name,age):
    return "vaccination successfull"
print(vaccine("lekshmi",22))