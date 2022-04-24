# Nomal method

numbers = [1, 2, 3, 4]
double_numbers = []

for number in numbers:
    doubled = number * 2
    double_numbers.append(doubled)
print(double_numbers)


# Using map in build function
def double(x):
    return x * 2

doubled_list_functional = list(map(double, numbers))
print(doubled_list_functional)