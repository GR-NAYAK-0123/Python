
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # Creating a linkedList
    def create_linked_list(self, nums):
        temp = self.head
        for i in nums:
            node = Node(i)
            if self.head == None:
                self.head = node
                temp = self.head
            else:
                temp.next = node
                temp = node
        return self.head
    

    #Deleting from end
    def delete_end(self):
        if self.head == None or self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    
    
    # Deleting from begin
    def delete_begin(self):
        if self.head == None or self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
    
    #Inserting at end
    def inserting_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
        


    #Inserting at begin
    def inserting_begin(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)

    
    # printing the LinkedList
    def show(self):
        temp = self.head
        while temp != None:
            print(temp.data, "-> ", end="")
            temp = temp.next
        print("None")

    
nums = [1, 5, 8, 3, 9, 10]

list1 = LinkedList()
head = list1.create_linked_list(nums)

list1.show()
list1.inserting_begin(100)
list1.show()
list1.inserting_end(200)
list1.show()
list1.delete_begin()
list1.show()
list1.delete_end()
list1.show()