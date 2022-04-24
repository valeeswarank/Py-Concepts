numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

add = lambda x, y: x + y

print(add(5, 5))

# Using the doubled number program with lamda

doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)