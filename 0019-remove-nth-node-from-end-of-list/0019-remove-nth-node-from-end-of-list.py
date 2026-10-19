# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        pi = dummy
        pj = dummy
        #move pj by n steps
        for _ in range(n): pj = pj.next if pj is not None else None
        #now move both till the time we do not reach end 
        while pj.next is not None:
            pj = pj.next
            pi = pi.next
        pi.next = pi.next.next if pi.next is not None else None
        return dummy.next

        