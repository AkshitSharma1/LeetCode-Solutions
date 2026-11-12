# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None: return head
        dummy = ListNode(-1,head)
        prev_to_prev = dummy
        prev = head
        curr = head.next

        while curr:
            nxt = curr.next
            nxt_to_nxt = curr.next.next if curr.next else None
            curr.next = prev
            prev_to_prev.next = curr
            prev.next = nxt

            prev_to_prev = prev
            prev = nxt
            curr = nxt_to_nxt
        
        return dummy.next
