# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        nxt = curr.next
        nxtToNext = nxt.next if nxt is not None else None

        nxt.next = curr
        curr.next = self.swapPairs(nxtToNext)

        return nxt


        return prev
        