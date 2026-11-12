# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None: 
            return head
        dummy = ListNode(-1,head)
        prev_to_prev = dummy
        curr = head.next
        prev = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev.next = nxt
            prev_to_prev.next = curr

            #now move the pointer ahead
            prev_to_prev = prev
            prev = nxt
            curr = nxt.next if nxt is not None else None
        
        return dummy.next


        