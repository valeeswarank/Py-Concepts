from functools import reduce
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_sum(acc, x):
    print(f"acc is {acc}, x is {x}")
    return acc + x

sum = reduce(get_sum, numbers)
print(sum)