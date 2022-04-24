import time
import threading
import queue


my_queue = queue.Queue()

def storeInQueue(f):
    def wrapper(*args):
        my_queue.put(f(*args))
    return wrapper

@storeInQueue
def calculate_square(numbers):
    numbers = sum(numbers)
    return numbers


arr = [2, 3, 8, 9]
t1 = threading.Thread(target=calculate_square, args=(arr, ))
t1.start()

mydata = my_queue.get()
print(mydata)

