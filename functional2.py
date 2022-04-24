import math

def double(x):
    return x * 2

def minus_one(x):
    return x - 1

def squared(x):
    return x * x

function_list = [
    double,
    minus_one,
    squared,
    math.sqrt
]
my_number = 3

# Mechanical way of doing the calculation
my_number = double(my_number)
my_number = minus_one(my_number)
my_number = squared(my_number)
print(my_number)

my_number = 3

# Funcational way of doing the calculation
for func in function_list:
    my_number = func(my_number)

print(my_number)