class Node:

    def __init__(self, key, val):
        self.val = val if val else 0
        self.key = key if key else 0
        self.left = None
        self.right = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.first = Node(0,0)
        self.last = Node(0,0)
        self.first.right = self.last
        self.last.left = self.first
    
    def add(self, key, value):
        newNode = Node(key, value)
        newNode.right, newNode.left = self.first.right, self.first
        self.first.right = newNode
        newNode.right.left = newNode
        self.cache[key] = newNode
    
    def remove(self, key):
        node = self.cache[key]
        node.right.left = node.left
        node.left.right = node.right
        del self.cache[key]

    def get(self, key: int) -> int:
        if(key in self.cache):
            value = self.cache[key].val
            self.remove(key)
            self.add(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.remove(key)
            self.add(key, value)
        else:
            if(len(self.cache) >= self.cap):
                self.remove(self.last.left.key)
            self.add(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)