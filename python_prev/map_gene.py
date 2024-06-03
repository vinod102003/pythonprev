# Define the list of values using range
a = list(range(1, 11))

# (i) List of squares of the values
squares = list(map(lambda x: x**2, a))
print("List of squares:", squares)

# (ii) List of cubes of the values
cubes = list(map(lambda x: x**3, a))
print("List of cubes:", cubes)

# (iii) List where each element is larger by one than the corresponding element in the original list
larger_by_one = list(map(lambda x: x + 1, a))
print("List where each element is larger by one:", larger_by_one)
