# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        prev = None
        curr = head

        for _ in range(2):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.swapPairs(curr)

        return prev
        