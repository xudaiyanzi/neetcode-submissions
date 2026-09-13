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
        dic = {}

        curr = head

        while curr:
            new = Node(curr.val)
            dic[curr] = new
            curr = curr.next
        
        curr = head
        dummy = Node(0)
        new_curr = dic[curr] if curr else None
        dummy.next = new_curr

        while curr:
            new_next = dic[curr.next] if curr.next else None
            new_random = dic[curr.random] if curr.random else None
            new_curr.next = new_next
            new_curr.random = new_random
            curr = curr.next
            new_curr = new_curr.next
        
        return dummy.next