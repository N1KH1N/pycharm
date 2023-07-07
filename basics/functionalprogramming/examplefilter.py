products=[
    [1,"oreo",30],
    [2,"parley",20],
    [3,"good day",15],
    [4,"dark fantasy",35],
    [5,"brittania",25]
]
print(products)

# create a new list with all product names
pname=list(map(lambda n:n[1],products))
print(pname)


# 30 below product price
prod=list(filter(lambda n:n[2]<30,products))
print(list(map(lambda n:n[1],prod)))
