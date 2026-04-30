
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # enqueue
    def enqueue(self, value):
        self.queue.append(value)

    # dequeue
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()
    
    # front
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    # is_empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # size
    def size(self):
        return len(self.queue)
    

q1 = Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

print(q1.queue)

print(q1.dequeue())

print(q1.queue)

print(q1.is_empty())