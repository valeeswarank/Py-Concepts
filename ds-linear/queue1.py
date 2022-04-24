from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    pq = Queue()
    pq.enqueue({
        'company': 'tata steel',
        'time': '30 Jan, 09:13 PM',
        'price': 789
    })
    pq.enqueue({
        'company': 'tata steel',
        'time': '30 Jan, 09:14 PM',
        'price': 792
    })
    pq.enqueue({
        'company': 'tata steel',
        'time': '30 Jan, 09:14 PM',
        'price': 795
    })

    print(pq.buffer)