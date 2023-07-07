# def vaccine(name,age):
#
#     if age<18:
#         print("not vacccinated")
#     else:
#         print("vaccinated")
# print(vaccine("nikhin",21))

def vaccine(**kwargs):

    if kwargs["age"]<=18:
        return kwargs["name"]+(",not eligible for vacccination")
    else:
        return kwargs["name"]+(",eligible for vaccination")

print(vaccine(name="nikhin",age=17))
print(vaccine(name="lekshmi",age=22))

