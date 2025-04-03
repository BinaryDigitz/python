from sys import getsizeof
# A collection of key value pairs
point = {}

point2 = dict(x=1, y=3)
print(point2['x'])

# Deleting an item 
del point2['x']

# looping in dict

for key in point2:
    print(point2[key])

    values = []
    for x in range(5):
        values.append( x * 2)

# it is same as

values2 = ( x * 2 for x in range(100000))


values = [*range(5)]
print(values)