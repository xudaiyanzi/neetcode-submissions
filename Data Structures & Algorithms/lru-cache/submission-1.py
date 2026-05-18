class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
    
    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.delete(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.add(node)
            node.val = value
        else:
            if len(self.dic) >= self.capacity:
                old = self.tail.pre
                self.delete(old)
                del self.dic[old.key]
            new = Node(value, key)
            self.add(new)
            self.dic[key] = new
        
