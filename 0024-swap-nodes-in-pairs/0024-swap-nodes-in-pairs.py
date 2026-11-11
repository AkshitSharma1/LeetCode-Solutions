# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1,head)
        curr = head
        prev = dummy
        while curr and curr.next:
            nxt = curr.next
            nxt_to_nxt = curr.next.next
            nxt.next = curr
            curr.next = nxt_to_nxt
            prev.next = nxt

            #move the pointers ahead
            prev = curr
            curr = nxt_to_nxt
        return dummy.next


            #prev point