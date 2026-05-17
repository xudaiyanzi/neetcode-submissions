# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## find the mid
        fast = head.next
        slow = head
        while fast:
            fast = fast.next.next if fast.next else None
            slow = slow.next
        curr = slow.next ## slow is the mid
        slow.next = None ## break the first half

        ## reverse the second half
        pre = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        ##### pre is the beginning of second half

        ## link the first half and second half
        l1 = head
        l2 = pre
        while l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2
        
        
