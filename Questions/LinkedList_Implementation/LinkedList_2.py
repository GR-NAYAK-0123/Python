
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at begin
    def insert_at_begin(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    # Insert at end
    def insert_at_end(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node
    
    # Insert at nth position
    def insert_at_nth_position(self, value, position):
        node = Node(value)
        if position == 1:
            self.head = node
            return
        temp = self.head
        while (position - 1) != 1:
            temp = temp.next
            position -= 1
        node.next = temp.next
        temp.next = node
    
    # Print the LinkdeList
    def show(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print("None")
    

l1 = LinkedList()
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l1.insert_at_end(3)
l1.insert_at_nth_position(4, 4)
l1.insert_at_begin(0)

l1.show()


