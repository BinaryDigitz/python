from collections import deque

# FIFO First In First Out

# Create an empty queue
numbers = deque([])

# Add items to queue
numbers.append(1)
numbers.append(2)
numbers.append(3)

# Remove an item from the queue
numbers.popleft()

print(numbers)

# check if queue is empty
if not numbers:
    print('Empty')