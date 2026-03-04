cat1 = {
    "name": "Chaos",
    "color": "Grey",
    "age": 3,
    "preference": "biscuits",
}

cat2 = {
    "name": "Willow",
    "color": "Black",
    "age": 5,
    "preference": "tuna",
}

cat3 = {
    "name": "Dude",
    "color": "Orangee",
    "preference": "salmon",
    "age": 3,
}

cathouse = []
cathouse.append(cat1)
cathouse.append(cat2)
cathouse.append(cat3)

print(cat1)
print(cat1["name"])

print(cathouse)

print(cathouse[1]["age"])

for cats in cathouse:
    print(cats["name"])
    print(cats["preference"])