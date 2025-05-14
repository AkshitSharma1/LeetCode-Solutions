# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #M1 - Using Recursion
    
        if head is None or head.next is None: return head
        #Reverse the remaining part
        newHead = self.reverseList(head.next)
        curr = head
        nxt = curr.next
        nxt.next = curr
        curr.next = None
        return newHead

        #M2 Using loop
        prev = None
        curr = head
        nxt = curr.next
        while curr is not None:
            curr.next = prev
            nxtToNext = nxt.next if nxt is not None else None
            nxt.next = curr
            prev = curr
            curr = nxt
            nxt = nxtToNext
            


        