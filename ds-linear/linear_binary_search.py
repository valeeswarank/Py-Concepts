from utilities import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for idx, number in enumerate(numbers_list):
        if number == number_to_find:
            return idx
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            left_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        left_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == "__main__":
    numbers_list = [4, 9, 11, 17, 21, 25, 29, 32, 38]
    number_to_find = 32

    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000

    index = linear_search(numbers_list, number_to_find)
    print (f"Number found in linear search at {index}.")

    index = binary_search(numbers_list, number_to_find)
    print (f"Number found in binary search at {index}.")

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print (f"Number found in binary search at {index}.")