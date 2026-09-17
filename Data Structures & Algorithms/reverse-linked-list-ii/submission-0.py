# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy

        for _ in range(left - 1):
            before_left = before_left.next
        
        left_node = before_left.next
        pre = None
        curr = left_node

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        before_left.next = pre
        left_node.next = curr

        return dummy.next