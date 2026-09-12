# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:     
        if not head or not head.next:
            return
        
        ## find middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## reverse second half
        curr = slow.next
        slow.next = None
        pre = None

        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        ## waving:
        curr = head

        while pre and curr:
            c_next = curr.next
            p_next = pre.next

            curr.next = pre
            pre.next = c_next

            curr = c_next
            pre = p_next
        
        return None


        
