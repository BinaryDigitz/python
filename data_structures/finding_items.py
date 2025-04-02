
numbers = [ 1, 2, 3, 4]

# using the index, method we can get the index
index_1 = numbers.index(3)

# You will get an error if the given item is not in the list
# so we check for it availabilty first
if  2 in numbers:
    print(numbers.index(2))

# then number of occurances of a given item, use count()
numbers.count(3)
