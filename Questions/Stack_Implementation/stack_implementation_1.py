
# Here I am going to implement the stack with the help of list in python

class Stack:
    def __init__(self):
        self.stack = []
    
    #Push
    def push(self, value):
        self.stack.append(value)
    
    #Pop
    def pop(self):
        if len(self.stack) == 0:
            return "Stsck is empty"
        return self.stack.pop()
    
    #Peek
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]
    
    #Check empty or not
    def is_empty(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return "Stack is not empty"
    
    #Deleting all the element from the stack
    def deleteAll(self):
        if len(self.stack) == 0:
            return "Stack is already Empty"
        return self.stack.clear()
    
    # print
    def show(self):
        print(self.stack)
    
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.show()
s1.pop()
s1.show()
print(s1.peek())
s1.deleteAll()
s1.show()
print(s1.is_empty())
