
# Set is a list of items which are unique denoted with { }

numbers = [1,2,2,3,4,5]
#to convert to a set

unique = set(numbers)

numbers2 = { 1, 4 }
# items are added using the add method
numbers2.add(5)

# items are removed using the removed method
# numbers2.remove(2)
# to create a set with to sets 
two_sets = (numbers2 | unique)

# create a new set with items found in both sets
all_items_in_sets = ( unique & numbers2)

