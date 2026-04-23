
# Here I am gonna implement LRU (Least recently used) Cache

class Node:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        
        self.tail = Node(0, 0)
        self.head = Node(0, 0, self.tail)
        self.tail.prev = self.head

    # Adding a node at the end  
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    # Removing a node from the first
    def remove(self, node):
        prev = node.prev
        front = node.next
        prev.next = front
        front.prev = prev
    
    # Getting the value of a node
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        
        return node.value
    
    # Putting a node
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
    
    
    # Printing the entire Cache
    def show(self):
        temp = self.head.next
        while temp.next != None:
            print(temp.key, ":", temp.value, end = " -> ")
            temp = temp.next
        print()
    
    

obj = LRUCache(2)
obj.put(1, 10)
obj.put(2, 20)
obj.put(3, 30)

print(obj.get(2))

obj.put(4, 40)

obj.show()

print(obj.get(2))

obj.show()

            
        