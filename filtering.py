# Normal typical/procedural way to check the even number

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []

for x in numbers:
    if (x % 2 == 0):
        even_numbers.append(x)

print(even_numbers)

# Writing the same function in functional way with build-in function

def is_even(x):
    return x % 2 == 0

even_numbers_functional = list(filter(is_even, numbers))
print(even_numbers_functional)