# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
      
        while curr and curr.next:
            nxt = curr.next
            second_nxt = curr.next.next if curr.next else None

            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt

            prev = curr
            curr = second_nxt
        
        return dummy.next
        

        