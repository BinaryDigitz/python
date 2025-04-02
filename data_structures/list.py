# LIST

letters = [ 'a', 'b','c','d','e', 'f','i','j','k']

# create a list of numbers ranging from 0 to 19
numbers = list(range(20))

# print a list of 100 0 (zeros)
zeros = [0] * 100

# slice from the first item to the second
slice1 = letters[0:1] 

# slice all letters
sliceAll = letters[:]

# select every third element in a list // also we get all even numbers 
slice_third = numbers[::2]

# get all numbers in reverse order
reverse_number = numbers[::-1]

numbers = list(range(20 + 1))
lettters = list('hello world')


# UNPARKING LIST // distructuring
numbers2 = [ 1, 2, 3]
# the number of item in the left side should be == to the number of items in the list
first, second, third = numbers2
# if we care only for the first 2 items 
first, second, *rest = numbers2

# We need the first and the last items
first, *rest, last = numbers2

# It is thesame as 
# first = numbers2[0]
# second = numbers2[1]
# third = numbers2[2]


# LOOPING IN LIST
for number in numbers2:
    print(number)

# get indexes? we use the enumerate operator
for index, number in enumerate(numbers2):
    print(index, number )

# ADDING ITEMS TO LIST
letters2 = [ 'a', 'b', 'c']

# Adding at the end, we use the apend method
letters2.append('d')

# Adding at the begining, we use the insert method
letters2.insert(0, '-')

# Removing item at the end, use pop
letters2.pop()

# Removing a specific item, we pass the index
letters2.pop(0)

# Removing an item without the index, we use the remove method
letters2.remove('b')

# Deleting a range of items, we us the del method
del numbers[ 0 : 3]

# Remove all items in list, we use the clear method
clear_items = [ 1, 2, 3, 4]
clear_items.clear()
