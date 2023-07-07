s="arun,aji,athul,megha,nikhin,lekshmi"
n=s.split(",")
c=[i for i in n if i[0] not in "aeiou"]
print(c)