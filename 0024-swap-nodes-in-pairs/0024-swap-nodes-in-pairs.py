# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        temp = head.next
        temp2 = head.next.next
        head.next.next = head
        head.next = self.swapPairs(temp2)
        return temp

