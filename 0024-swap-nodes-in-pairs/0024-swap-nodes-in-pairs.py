# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        rest= self.swapPairs(head.next.next)
        temp = head.next
        head.next = rest
        temp.next = head

        return temp

