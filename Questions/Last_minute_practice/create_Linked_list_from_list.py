
from LinkedList import LinkedList, Node

def create_LinkedList(values):
    # Creating the LinkedList object
    l1 = LinkedList()
    head = l1.create_linked_list(values)
    return head

def show(head):
    temp = head
    while temp:
        print(temp.value, end="->")
        temp = temp.next
    print("None")


values = [2, 0, 2, 1]
head = create_LinkedList(values)
show(head)