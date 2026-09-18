class ListNode:
    def __init__(self, val, next = None, pre = None):
        self.val = val
        self.next = next
        self.pre = pre

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.head.pre = self.tail

        self.tail.next = self.head
        self.tail.pre = self.head
        self.curr_size = 0
        self.size = k


    def enQueue(self, value: int) -> bool:
        if self.curr_size < self.size:
            new = ListNode(value)
            last = self.tail.pre
            last.next = new
            new.pre = last
            new.next = self.tail
            self.tail.pre = new
            self.curr_size += 1
            return True
        
        else:
            return False

    def deQueue(self) -> bool:
        if self.curr_size > 0:

            delete_node = self.head.next
            nxt = delete_node.next

            self.head.next = nxt
            nxt.pre = self.head
            self.curr_size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.curr_size == 0:
            return -1
        return self.tail.pre.val

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()