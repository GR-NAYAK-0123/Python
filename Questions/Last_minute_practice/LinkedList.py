
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Create a linkedList from a list of values
    def create_linked_list(self, values):
        temp = self.head
        for i in values:
            node = Node(i)
            if self.head is None:
                self.head = node
                temp = self.head
            else:
                temp.next = node
                temp = temp.next
        return self.head
    
    
