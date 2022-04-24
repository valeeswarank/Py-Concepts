import time
import threading


def calculate_square(numbers):
    print("calculate square numbers")
    for num in numbers:
        time.sleep(0.2)
        print("square", num*num)


def calculate_cube(numbers):
    print("calculating cubes")
    for num in numbers:
        time.sleep(0.2)
        print("cube", num*num*num)


arr = [2,3,8,9]

# The following method as normal
t = time.time()
calculate_square(arr)
calculate_cube(arr)

print("done in : ", time.time()-t)
print("process completed")

# The following method with multitheading
t = time.time()
t1 = threading.Thread(target=calculate_square, args=(arr,))
t2 = threading.Thread(target=calculate_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print("done in : ", time.time()-t)
print("process completed")