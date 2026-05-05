
# Stack Implementation

class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, value):
        self.stack = self.stack + [value]

    def pop(self):
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-1:]
        return element
    
    # is_empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Size
    def size(self):
        return len(self.stack)
    
s1 = Stack()
print(s1.pop())

s1.push(1)
s1.push(2)
s1.push(3)

print(s1.stack)

print(s1.pop())

print(s1.stack)
