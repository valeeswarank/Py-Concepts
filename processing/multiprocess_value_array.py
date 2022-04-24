import time
import multiprocessing

# Sharing memory via Value and Array
# this programe will help to understand the memory/variable sharing in between multi processing
def calc_square(numbers, result, v):
    v.value = 3.3
    for idx, num in enumerate(numbers):
        result[idx] = num*num


# Note if you are not using the following line then you will get an error message since the functions are not
# initialised.
if __name__ == "__main__":
    arr = [2, 3, 5]
    result = multiprocessing.Array("i", 3)
    v = multiprocessing.Value("d", 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))
    p1.start()
    p1.join()
    print(result[:], v.value)
