numbers = [ 2, 43, 45, 5, 1, 30, 7 ]

# Sort numbers ascendingly, we use the sort method
#  numbers.sort()

# sort numbers in descending other
numbers.sort(reverse=True)

# Create a new list and sort without touching the original list
asc = sorted(numbers)

# Create a new list and sort in reverse without touching the original list
desc = sorted( numbers, reverse=True)



# SORTING TUPPLE
items = [
    ('prod1', 10),
    ('prod2', 6),
    ('prod3', 12)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# also written as
# items.sort(key=lamda item:item[1])

# Create a list or Prices
prices = []
for item in items:
    prices.append(item[1])


# MAP FUNCTION
# prices = list(map(lambda item: item[1], items))

# Shorter syntax also known as LIST COMPREHENTION
prices = [item[1] for item in items]

# FILTER FUNCTION
# filtered = list(filter(lambda item: item[1] >= 10, items))

# LIST COMPREHENTION
filtered = [ item for item in items if item[1] > 10 ]
