capitals = {
    'France' : 'Paris',
    'Chile' : 'Santiago',
    'Canada' : 'Ottawa'
}


grade = {
    'midterm' : '75',
    'final' : '95',
    'homework1' : '75',
    'midterm' : '95'
}
print(grade)

print(capitals ['Canada'])
#OR
print(capitals.get('Canada'))
#difference bw these two is that if you put china in the brackets while its not in the dictionary, the first one returns error and the second returns none

#only prints keys not values:
for x in grade:
    print(x)
list(grade)

#prints keys and values:
for x in grade:
    print(x, grade)
list(grade.items())

#only values:
for event, grade in grade.items():
    print(grade)

print('China' in capitals)
#boolean

#ways to make dictionary:

'''ages = {}
ages['Mom'] = 50
ages['Grandma'] = 87

lengths = {w : len(w) for w in 'Sam I am'.split()}'''

