# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        for _ in range(n):
            p2 = p2.next
        
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next if p1.next else None
        return dummy.next

