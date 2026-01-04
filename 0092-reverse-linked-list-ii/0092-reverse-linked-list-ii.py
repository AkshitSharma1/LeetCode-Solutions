# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1)
        dummy.next = head
        p1 = dummy #just before left node
        p2 = dummy #just after right node
        for _ in range(left-1):

            p1 = p1.next
        for _ in range(right+1):
            p2 = p2.next
        
        #reverse this part
        prev = None
        curr = p1.next
        while curr!=p2:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        p1.next.next = p2
        p1.next = prev

        return dummy.next
        


