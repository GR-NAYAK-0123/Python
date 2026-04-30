
# Stack Implementation

class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, value):
        self.stack.append(value)
    
    # Pop
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    # Peek
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    # isEmpty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Size
    def size(self):
        return len(self.stack)
    
    # Print
    def show(self):
        print(self.stack)
    
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)

s1.show()

print(s1.pop())
print(s1.pop())

s1.show()

print(s1.peek())

print(s1.size())


