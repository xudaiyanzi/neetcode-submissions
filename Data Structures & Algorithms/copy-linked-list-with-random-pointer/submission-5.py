"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        ## create the node with val and connect to original link list
        while curr:
            new_curr = Node(curr.val)
            nxt = curr.next 
            new_curr.next = nxt
            curr.next = new_curr
            curr = nxt
        ## copy random
        res = head.next if head else None

        curr = head
        while curr:
            new_curr = curr.next
            random = curr.random
            new_curr.random = random.next if random else None
            curr = curr.next.next if curr.next else None
        
        ## break the new and original node
        curr = head
        while curr:
            new_curr = curr.next
            curr.next = new_curr.next
            new_curr.next = curr.next.next if curr.next else None
            curr = curr.next
        
        return res
        


            