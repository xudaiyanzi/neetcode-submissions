# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        move = 0
        dummy = ListNode(0)
        pre = dummy
        curr = head
        pre.next = curr

        while move < count - n:
            print('count: ', count, ', n: ', n)
            pre = pre.next
            curr = curr.next
            move += 1
        
        nxt = curr.next
        pre.next = nxt

        return dummy.next
        

            
                

