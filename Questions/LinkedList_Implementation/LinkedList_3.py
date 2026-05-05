
# LinkedList Implementation

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert at begin
    def insert_at_begin(self, value):
        node = Node(value, self.head)
        if self.head is None:
            self.head = node
            return
        self.head = node
    
    # insert at end
    def insert_at_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node

    # insert at nth position
    def insert_at_nth_position(self, value, pos):
        node = Node(value)
        if pos == 1:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        while (pos - 1) != 1:
            temp = temp.next
            pos -= 1
        node.next = temp.next
        temp.next = node
    
    # deleting from begin
    def delete_from_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    # deleting from end
    def delete_from_end(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def show(self):
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print("None")


l1 = LinkedList()
l1.show()

l1.insert_at_end(2)
l1.insert_at_begin(1)
l1.insert_at_begin(0)

l1.show()

l1.delete_from_begin()
l1.delete_from_end()

l1.show()