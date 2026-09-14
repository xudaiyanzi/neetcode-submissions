# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            value = l1_val + l2_val + carry

            digit = value % 10
            carry = value // 10

            new = ListNode(digit)
            curr.next = new

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
            
        return dummy.next