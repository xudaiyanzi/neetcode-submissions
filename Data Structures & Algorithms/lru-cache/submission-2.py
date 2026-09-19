class ListNode:
    def __init__(self, key=-1, value=-1, next=None, pre=None):
        self.key = key
        self.value = value
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        curr = self.dic[key]
        self.delNode(curr)
        self.addNode(curr)
        return curr.value

    def put(self, key: int, value: int) -> None:
        new = ListNode(key, value)
        if key not in self.dic:
            if self.size >= self.capacity:
                self.delNode(self.head.next)        
            self.addNode(new)
        else:
            old = self.dic[key]
            self.dic[key] = new
            self.delNode(old)
            self.addNode(new)
    
    def addNode(self, new):

            pre = self.tail.pre

            pre.next = new
            new.pre = pre

            new.next = self.tail
            self.tail.pre = new

            self.dic[new.key] = new
            self.size += 1
    
    def delNode(self, old):

            old_pre = old.pre
            old_next = old.next
            old_pre.next = old_next
            old_next.pre = old_pre

            old_key = old.key
            del self.dic[old_key]
            self.size -= 1
