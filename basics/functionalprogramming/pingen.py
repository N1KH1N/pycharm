def adm(fn):
    def wrapper(a,b):
        if a=="admin":
        else:
            raise Exception ("No Admin Acess")
    return wrapper

@adm
def changepin(username, newpin):
    pin = newpin
    return "pin changed"
# print(changepin("nikhin",8374))
print(changepin("admin",678551))

