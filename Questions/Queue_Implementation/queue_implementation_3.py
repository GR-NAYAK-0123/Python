
# Queue Implementation

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, value):
        self.queue = self.queue + [value]

    # Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        element = self.queue[0]
        self.queue = self.queue[1:len(self.queue):]
        return element
    
    # is_empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # Print
    def show(self):
        print(self.queue)


q1 = Queue()
print(q1.dequeue())

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q1.show()

print(q1.dequeue())

q1.show()