for pet in ['Dog', ['Cat'], ['Fish']]:
    print(pet)

x = ''
for pet in ['Dog'], ['Cat'], ['Fish']:
    x = x + pet
print(x)

x = ''
for pet in ['Dog'], ['Cat'], ['Fish']:
    x = pet + x
print(x)