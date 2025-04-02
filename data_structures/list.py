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