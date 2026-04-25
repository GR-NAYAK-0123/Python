
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

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    # For adding the node
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    # For removing a node
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # For getting the value
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.value
    
    # Putting new Value
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value, self.tail)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
    
    # Showing the value or printing the value
    def show(self):
        for i in self.cache:
            print(self.cache[i].key,":", self.cache[i].value, end=" -> ")


obj = LRUCache(2)
obj.put(1, 10)
obj.put(2, 20)

print(obj.get(2))
print(obj.get(1))

obj.put(3, 30)

obj.show()


        