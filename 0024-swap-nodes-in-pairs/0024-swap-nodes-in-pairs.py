# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1,head)
        if head is None or head.next is None: return head
        prev = dummy
        curr = head
        nxt = curr.next

        curr.next = self.swapPairs(nxt.next)
        nxt.next = curr
        prev.next = nxt
      
       
        return dummy.next
        

        