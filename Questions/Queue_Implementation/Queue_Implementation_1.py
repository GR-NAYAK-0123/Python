
class Queue:
    def __init__(self):
        self.queue = []
    
    # Push
    def push(self, value):
        self.queue.append(value)
    
    # Pop
    def pop(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            self.queue.pop(0)
    
    # Peek
    def peek(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            return self.queue[-1]
        
    # For checking empty or not
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    # For printing the queue
    def show(self):
        print(self.queue)
    

q1 = Queue()
q1.push(2)
q1.push(4)
q1.push(6)
q1.push(8)
q1.show()

print(q1.peek())

q1.pop()

q1.show()

print(q1.peek())
