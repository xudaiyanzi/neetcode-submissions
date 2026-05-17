# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr1 = head

        ## count the length
        count = 0
        while curr1:
            curr1 = curr1.next
            count += 1

        ## find the previous one of the nth from the end of the list
        curr2 = dummy
        while (count - n) > 0 and curr2:
            curr2 = curr2.next
            count -= 1

        pre = curr2
        nxt = curr2.next
        pre.next = nxt.next

        return dummy.next